from scholarly import scholarly, ProxyGenerator
import json
from datetime import datetime
import os
import sys, time, random

# ---------- 代理（注意：FreeProxies 在 CI 上很不稳定，仅作兜底） ----------
pg = ProxyGenerator()
pg.FreeProxies()  # 建议改为付费稳定代理或自托管出口
scholarly.use_proxy(pg)

def retry_search_author_id(scholar_id, retries=3, backoff=(3, 6)):
    """对 search_author_id 也做重试，并禁止自动填充"""
    for i in range(retries):
        try:
            # 关键：filled=False，避免在这里就去 fill()
            return scholarly.search_author_id(scholar_id, filled=False)
        except Exception as e:
            print(f"[warn] search_author_id failed: {e}", file=sys.stderr)
            if i < retries - 1:
                time.sleep(random.uniform(*backoff))
    return None

def safe_fill(author, sections):
    """只负责 fill 的重试"""
    for i in range(3):
        try:
            return scholarly.fill(author, sections=sections)
        except AttributeError as e:
            # 多半是风控页；等待后重试
            time.sleep(3 + random.random()*3)
        except Exception as e:
            print(f"[warn] scholarly.fill failed: {e}", file=sys.stderr)
            time.sleep(2)
    print("[warn] Give up filling author due to repeated failures.", file=sys.stderr)
    return None

scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID')
if not scholar_id:
    print("[error] Missing env GOOGLE_SCHOLAR_ID", file=sys.stderr)
    sys.exit(0)  # 或者直接 return，让 CI 不红

# 先拿到“未填充”的作者对象
author = retry_search_author_id(scholar_id)
if author is None:
    print("[warn] Cannot fetch author stub; outputting minimal placeholder.", file=sys.stderr)
    author = {"scholar_id": scholar_id}

# 再尝试填充
filled = safe_fill(author, sections=['basics', 'indices', 'counts', 'publications'])

# 根据是否填充成功，稳妥构造输出
obj = filled if filled is not None else author
obj['updated'] = datetime.now().isoformat(timespec='seconds')

# publications 可能不存在或是列表；都要小心处理
pubs = obj.get('publications', [])
if isinstance(pubs, list):
    try:
        obj['publications'] = {v['author_pub_id']: v for v in pubs if 'author_pub_id' in v}
    except Exception:
        # 出现异常就回退成空字典
        obj['publications'] = {}
elif not isinstance(pubs, dict):
    obj['publications'] = {}

# 指标字段稳妥读取
citedby = -1
if isinstance(obj.get('citedby'), int):
    citedby = obj['citedby']
elif 'citedby' in obj:
    try:
        citedby = int(obj['citedby'])
    except Exception:
        citedby = -1

results_dir = 'results'
os.makedirs(results_dir, exist_ok=True)

# 输出与保存
if citedby != -1:
    print(json.dumps(obj, ensure_ascii=False, indent=2))
    
    data_path = os.path.join(results_dir, 'gs_data.json')
    badge_path = os.path.join(results_dir, 'gs_data_shieldsio.json')
    
    # 读取已有的 message（如文件不存在或损坏，则视为需要更新）
    prev_message = None
    if os.path.exists(badge_path):
        try:
            with open(badge_path, 'r', encoding='utf-8') as f:
                prev = json.load(f)
                prev_message = str(prev.get('message'))
        except Exception:
            prev_message = None
    
    current_message = str(citedby)
    
    if prev_message == current_message:
        # 不更新
        print("No changes: citedby unchanged, skip writing.")
    else:
        # 更新两个文件
        with open(data_path, 'w', encoding='utf-8') as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)
    
        shieldio_data = {
            "schemaVersion": 1,
            "label": "citations",
            "message": current_message,
        }
        with open(badge_path, 'w', encoding='utf-8') as f:
            json.dump(shieldio_data, f, ensure_ascii=False, indent=2)
    
        print("Updated: wrote gs_data.json and gs_data_shieldsio.json.")
else:
    # 通知 GitHub Actions：本次是否有变化
    gh_out = os.environ.get('GITHUB_OUTPUT')
    if gh_out:
        with open(gh_out, 'a', encoding='utf-8') as f:
            f.write(f"changed=false\n")
