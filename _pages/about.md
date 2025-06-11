---
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

**Research**: I am currently an associate research fellow in Chinese Academy of Engineering Physics (CAEP). My goal is to build trustworthy AI models and software in strong adversarial environments. My current work broadly involves research on attack and defense for AI algorithms, explainable AI (XAI), LLM security, data-driven software security, etc.

**Previously**: I got my Ph.D degree from University of Electronic Science and Technology of China ([UESTC](https://www.uestc.edu.cn/)) advised by Prof. [Xiaosong Zhang](https://sise.uestc.edu.cn/info/1035/13033.htm) and Prof. Qingxin Zhu. I was a visiting scholar at UC Santa Barbara, where I worked with [Yufei Ding](https://scholar.google.com/citations?user=MiPxo9UAAAAJ).

**Openings**: My research team has multiple openings for <span style="color:blue">Research Assistants, Software Engineers, Research Interns, Postdoc and Ph.D./Master</span>, please drop me an email or visit the website of [CAEP graduate school](https://zsxx.gscaep.ac.cn/list/13) for more information.

> 📌 **非常欢迎考虑报考我的研究生**！在给我写邮件之前，请您先仔细阅读下面的文字，并确认我们在科研观念、兴趣上一致:
> 
> 💡 **研究兴趣**：我的研究聚焦于可信人工智能技术，包括算法安全、隐私保护、软件脆弱性挖掘等，并将相关方法应用于关键基础设施与高安全场景。 
> ✨ **招生期望**：希望能够招收算法基础好、编程能力强、英语功底扎实、擅于口头及书面表达的学生。有学术竞赛、论文发表、课外学术活动等科研经历者加分。   
> 🎯 **培养目标**：经过精心组织的科研训练，使学生具备扎实的专业知识、缜密的科研思维、较强的动手能力、广阔的学术视野，及独立发现问题、思考问题、解决问题的重要科学素养；在校期间在世界顶级期刊或会议上发表高水平、有影响力的论文，并有志于毕业后继续从事科研工作。   
> 🤝 **我的承诺**：作为一线科研工作者，我将为你的成长提供全方位支持，包括但不限于：1）亲自指导算法设计、代码实现、实验设计、论文撰写、专利申请、成果展示等全过程；2）提供积极向上的科研氛围、舒适的工作环境、稳定的科研经费与高性能计算资源；3）几乎不会让你处理报账、递送材料、拿快递等与科研无关的事务性工作，让你专注科研；4）对于在顶会上发表论文的学生，会提供经费积极资助你参会（只要没出地球）； 5）对表现优秀的同学，我会积极推荐工作或深造机会，助你拓展未来发展路径。
> 
> ⚠️ **特别提醒**：<span style="color:red">课题组欢迎真正热爱科研、喜欢探索、乐于挑战、想学知识的同学加入。如果你只是单纯想通过读研获得学位上的提升，建议谨慎考虑，否则在这个过程中我们双方都会很难受。</span>

# 🔥 News
- <span style="color:red">[2025.06]</span> &nbsp;🎉 One paper is accepted by **USENIX Security 2025**!
- <span style="color:red">[2025.02]</span> &nbsp;🎉 One paper is accepted by **计算机研究与发展**!
- <span style="color:red">[2024.12]</span> &nbsp;🎉 One paper is accepted by **CCS 2024**!
- <span style="color:red">[2024.12]</span> &nbsp;🎉 One paper is accepted by **IEEE TIFS**!
- <span style="color:red">[2024.11]</span> &nbsp;🎉 One survey of backdoor attack and defense on deep learning is accepted by **IEEE TCSS**! 
- <span style="color:red">[2024.08]</span> &nbsp;🎉 One paper is accepted by **ASE 2024**!
- <span style="color:red">[2024.03]</span> &nbsp;🎉 One paper is accepted by **IEEE TIFS**! 

# 📝 Selected Publications 

Top-tier Conferences and Journal articles <a href='https://scholar.google.com/citations?user=2ahbtVoAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>

## Conference
- `USENIX Sec'25` **MalGuard: Towards Real-Time, Accurate, and Actionable Detection of Malicious Packages in PyPI Ecosystem**.  
  Xingan Gao, Xiaobing Sun, Sicong Cao, Kaifeng Huang, Du Wu, <span style="color:blue">Xiaolei Liu</span>, Xingwei Lin, and Yang Xiang.   
  In *Proceedings of the 34th USENIX Security Symposium (USENIX Sec)*, August, 2025.  (<span style="color:red">CCF-A</span>)   
  [[Paper]()]
  [[DOI]()]
- `CCS'24` **SUB-PLAY: Adversarial Policies against Partially Observed Multi-Agent Reinforcement Learning Systems**.   
  Oubo Ma, Yuwen Pu, Linkang Du, Yang Dai, Ruo Wang, <span style="color:blue">Xiaolei Liu</span>, Yingcai Wu, and Shouling Ji.   
  In *Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security (CCS)*, December, 2024. (<span style="color:red">CCF-A</span>)   
  [[Paper](https://cubernet.github.io/publications/CCS24/CCS24-Paper.pdf)]
  [[Slides](https://cubernet.github.io/publications/CCS24/CCS24-Slides.pdf)]
  [[DOI](https://doi.org/10.1145/3658644.3670293)]
- `ASE'24` **Snopy: Bridging Sample Denoising with Causal Graph Learning for Effective Vulnerability Detection**.  
  Sicong Cao, Xiaobing Sun, Xiaoxue Wu, David Lo, Lili Bo, Bin Li, <span style="color:blue">Xiaolei Liu</span>, Xingwei Lin, and Wei Liu.  
  In *Proceedings of the 39th ACM/IEEE International Conference on Automated Software Engineering (ASE)*, October, 2024.  (<span style="color:red">CCF-A</span>)   
  [[Paper](https://cubernet.github.io/publications/ASE24/ASE24-Papera.pdf)]
  [[Video](https://youtu.be/d8clWq9JC0Y)]
  [[Code](https://github.com/SnopyArtifact/Snopy)]
  [[DOI](https://dl.acm.org/doi/10.1145/3691620.3695057)]
- `ICASSP'23` **Sparse Black-Box Inversion Attack with Limited Information**.  
  Yixiao Xu, <span style="color:blue">Xiaolei Liu</span>, Teng Hu, Bangzhou Xin, and Run Yang.  
  In *Proceedings 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, June, 2023.  (<span style="color:red">CCF-B</span>)   
  [[Paper](https://cubernet.github.io/publications/ICASSP23/ICASSP23-Paper.pdf)]
  [[DOI](https://doi.org/10.1109/ICASSP49357.2023.10095514)]
- `ICME'22` **Targeted Anonymization: A Face Image Anonymization Method for Unauthorized Models**.  
  Kangyi Ding, Teng Hu, <span style="color:blue">Xiaolei Liu</span>, Weina Niu, Yanping Wang, and Xiaosong Zhang.  
  In *Proceedings 2022 IEEE International Conference on Multimedia and Expo (ICME)*, August, 2022.  (<span style="color:red">CCF-B</span>)   
  [[Paper](https://cubernet.github.io/publications/ICME22/ICME22-Paper.pdf)]
  [[DOI](https://doi.org/10.1109/ICME52920.2022.9859898)] 
- `ICASSP'22` **Sparse Adversarial Attack For Video Via Gradient-Based Keyframe Selection**.  
  Yixiao Xu, <span style="color:blue">Xiaolei Liu</span>, Mingyong Yin, Teng Hu, and Kangyi Ding.  
  In *Proceedings 2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, May, 2022.  (<span style="color:red">CCF-B</span>)   
  [[Paper](https://cubernet.github.io/publications/ICASSP22/ICASSP22-Paper.pdf)]
  [[DOI](https://doi.org/10.1109/ICASSP43922.2022.9747698)]     
- `AAAI'20` **Weighted-sampling audio adversarial example attack**.  
  <span style="color:blue">Xiaolei Liu</span>, Kun Wan, Yufei Ding, Xiaosong Zhang, and Qingxin Zhu.  
  In *Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)*, February, 2020.  (<span style="color:red">CCF-A</span>)   
  [[Paper](https://cubernet.github.io/publications/AAAI20/AAAI20-Paper.pdf)]
  [[Website](https://sites.google.com/view/audio-adversarial-examples/)]
  [[DOI](https://doi.org/10.1609/aaai.v34i04.5928)]

## Journal
- `计算机研究与发展'25` **大语言模型安全与隐私风险综述**.   
  姜毅, 杨勇, 印佳丽, <span style="color:blue">刘小垒</span>, 李吉亮, 王伟, 田有亮, 巫英才, 纪守领.   
  In *计算机研究与发展*, 2025. (<span style="color:red">中文CCF-A</span>)   
  [[Paper](https://cubernet.github.io/publications/CARD25/CARD25-Paper.pdf)]
  [[DOI](https://doi.org/10.7544/issn1000-1239.202440265)]
- `TIFS'24` **Query-Efficient Model Inversion Attacks: An Information Flow View**.   
  Yixiao Xu, Binxing Fang, Mohan Li, <span style="color:blue">Xiaolei Liu</span>, and Zhihong Tian.   
  In *IEEE Transactions on Information Forensics and Security*, 2024. (<span style="color:red">CCF-A</span>)   
  [[Paper](https://cubernet.github.io/publications/TIFS24/TIFS24-Paperb.pdf)]
  [[DOI](https://doi.org/10.1109/TIFS.2024.3518779)]
- `TIFS'24` **Unstoppable Attack: Label-Only Model Inversion via Conditional Diffusion Model**.   
  Rongke Liu, Dong Wang, Yizhi Ren, Kaitian Guo, Qianqian Qin, and  <span style="color:blue">Xiaolei Liu</span>.   
  In *IEEE Transactions on Information Forensics and Security*, 2024. (<span style="color:red">CCF-A</span>)   
  [[Paper](https://cubernet.github.io/publications/TIFS24/TIFS24-Papera.pdf)]
  [[DOI](https://doi.org/10.1109/TIFS.2024.3372815)]
- `TCSS'24` **Backdoor Attack and Defense on Deep Learning: A Survey**.   
  Yang Bai, Gaojie Xing, Hongyan Wu, Zhihong Rao, Chuan Ma, Shiping Wang, <span style="color:blue">Xiaolei Liu</span>, Yimin Zhou, Jiajia Tang, Kaijun Huang, and Jiale Kang.   
  In *IEEE Transactions on Computational Social Systems*, 2024. (<span style="color:red">JCR-Q1</span>)   
  [[Paper](https://cubernet.github.io/publications/TCSS24/TCSS24-Paper.pdf)]
  [[DOI](https://doi.org/10.1109/TIFS.2024.3372815)] 
- `IEEE Network’24` **An Adversarial Example Defense Algorithm for Intelligent Driving**.   
  Jiazhong Lu, Chenli Wang, Yuanyuan Huang, Kangyi Ding, and  <span style="color:blue">Xiaolei Liu</span>.   
  In *IEEE Network*, 2024. (<span style="color:red">JCR-Q1</span>)   
  [[Paper](https://cubernet.github.io/publications/MNET24/MNET24-Paper.pdf)]
  [[DOI](https://doi.org/10.1109/MNET.2024.3392582)] 
- `IPM’21` **Transaction-based classification and detection approach for Ethereum smart contract**.   
  Teng Hu, <span style="color:blue">Xiaolei Liu</span>, Ting Chen, Xiaosong Zhang, Xiaoming Huang, Weina Niu, Jiazhong Lu, Kun Zhou, and Yuan Liu.   
  In *Information Processing & Management*, 2021. (<span style="color:red">ESI高被引论文, JCR-Q1</span>)     
  [[Paper](https://cubernet.github.io/publications/IPM21/IPM21-Paper.pdf)]
  [[DOI](https://doi.org/10.1016/j.ipm.2020.102462)]
- `TITS’21` **Compiler-Based Efficient CNN Model Construction for 5G Edge Devices**.   
  Kun Wan, <span style="color:blue">Xiaolei Liu</span>, Jianyu Yu, Xiaosong Zhang, Xiaojiang Du, and Nadra Guizani.   
  In *IEEE Transactions on Intelligent Transportation Systems*, 2021. (<span style="color:red">JCR-Q1</span>)   
  [[Paper](https://cubernet.github.io/publications/TITS21/TITS21-Paper.pdf)]
  [[DOI](https://doi.org/10.1109/TITS.2021.3056426)]
- `KBS’21` **A low-query black-box adversarial attack based on transferability**.   
  Kangyi Ding, <span style="color:blue">Xiaolei Liu</span>, Weina Niu, Teng Hu, Yanping Wang, and Xiaosong Zhang.   
  In *Knowledge-Based Systems*, 2021. (<span style="color:red">JCR-Q1</span>)   
  [[Paper](https://cubernet.github.io/publications/KBS21/KBS21-Paper.pdf)]
  [[DOI](https://doi.org/10.1016/j.knosys.2021.107102)]

# 🎖 Honors and Awards
- <span style="color:red">[2024.12]</span> 🏆 四川省高层次人才计划
- <span style="color:red">[2024.04]</span> 🏆 中国电子学会青年人才托举工程计划
- <span style="color:red">[2022.11]</span> 🏆 GeekPWN G-Outstanding Winner
- <span style="color:red">[2018.05]</span> 🏆 China Scholarship Council (CSC) Scholarship
- <span style="color:red">[2016.11]</span> 🏆 国家网络安全奖学金（首届）
  
# 👨‍💻 Services
- 中国电子学会网络空间安全专委会委员
- 中国图象图形学学会数字媒体取证与安全专委会委员
- 中国计算机学会第十三届会员代表
- 通信技术期刊执行编委
- 网络空间安全科学学报青年编委
- 信息网络安全青年编委
