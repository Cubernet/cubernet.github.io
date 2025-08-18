from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import sys, time, random

# Setup proxy
pg = ProxyGenerator()
pg.FreeProxies()  # Use free rotating proxies
scholarly.use_proxy(pg)

def safe_fill(author, sections):
    for i in range(3):
        try:
            return scholarly.fill(author, sections=sections)
        except AttributeError as e:
            # 多半是风控页，等待后重试
            time.sleep(3 + random.random()*3)
        except Exception as e:
            # 其他错误也别让CI直接挂
            print(f"[warn] scholarly.fill failed: {e}", file=sys.stderr)
            time.sleep(2)
    print("[warn] Give up filling author due to repeated failures.", file=sys.stderr)
    return None  # 返回原对象，后续逻辑自行判空

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
if not safe_fill(author, sections=['basics', 'indices', 'counts', 'publications']):
    name = author['name']
    author['updated'] = str(datetime.now())
    author['publications'] = {v['author_pub_id']:v for v in author['publications']}
    print(json.dumps(author, indent=2))
    os.makedirs('results', exist_ok=True)
    with open(f'results/gs_data.json', 'w') as outfile:
        json.dump(author, outfile, ensure_ascii=False)
    
    shieldio_data = {
      "schemaVersion": 1,
      "label": "citations",
      "message": f"{author['citedby']}",
    }
    with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)
