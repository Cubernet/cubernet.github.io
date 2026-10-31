# Homepage maintenance

The site remains a Jekyll project, deployed from `master` using the existing GitHub Pages workflow. The public homepage is `https://xlliu.org.cn/` and the underlying Pages endpoint is `https://cubernet.github.io/`.

## Content

- `_pages/about.md`: bilingual homepage, news, recognition, service, contact and student note.
- `_data/publications.json`: all 29 original publications, full authors and resource links. `featured`, `rank` and bilingual summaries select five homepage entries. Add new papers here and update the homepage count and archive date range.
- `_pages/publications.html`: server-rendered complete archive. Search, year and topic filters are progressive enhancements.
- `_layouts/profile.html`: shared navigation, metadata, canonical URL and Person schema.
- `assets/css/profile.css`, `assets/js/profile.js`: responsive design and bilingual/filter controls.

Chinese is the initial language; the visitor’s explicit choice is remembered locally. All content and paper links are accessible without JavaScript. All visual and font assets are hosted locally. Literata is distributed under its bundled SIL Open Font License.

## Sources and editorial decisions (2026-10-31)

Baseline: existing homepage and all publications at repository commit `6e13df8`. Existing news, awards and service records are retained from the owner’s page. No citation metrics, customer names, financing details or unconfirmed founder title are added.

- Current position / supervisor: https://zsxx.gscaep.ac.cn/teacher-detail/200
- Recent author bio confirming position and email: https://www.ejournal.org.cn/zh/article/doi/10.12263/DZXB.20260444/
- MAIVER current public positioning: https://maiver.ai/ — machine behavior governance / The AI that governs AI. Presented as current practice, without an unconfirmed founder title.
- NEO formal title is **Closed-Box**, corrected from Black-Box: https://ieeexplore.ieee.org/abstract/document/11616686 (DOI 10.1109/TDSC.2026.3715804).
- TCSS survey DOI corrected from the unrelated TIFS DOI to 10.1109/TCSS.2024.3482723 (confirmed against the existing PDF first page).
- PSFuzzer author version / DOI: https://zyingp.github.io/pubs.html ; https://zyingp.github.io/files/26-PSFuzzer.pdf ; https://doi.org/10.1109/TSE.2026.3726519
- TrajGuard is explicitly identified as **Findings of ACL 2026**: https://aclanthology.org/2026.findings-acl.655/ ; https://github.com/neuron-insight-lab/Trajguard
- LoopLLM code: https://github.com/neuron-insight-lab/LoopLLM
- MADA-Attack code: https://github.com/RaymundoTheWolf/MADA-Attack

Empty paper/DOI links were removed. Papers with no available resource are identified as accepted with links forthcoming. The broken CCS24 paper and slides URLs are restored by copying the existing files from the misspelled `CSS24` directory; both paths continue to work. The TITS21 paper file was absent in the repository, so its dead download link is removed while retaining the DOI. All other original local paper and slide links remain available.

The student note was edited for a professional public audience while preserving the owner’s emphasis on intellectual honesty, strong foundations, independent thinking and focused research.

## Verification

Run `bundle exec jekyll build` and `node --check assets/js/profile.js`. Check new publications against primary sources, verify local PDFs, and preview both languages on desktop and mobile. Existing deep links and `/about/` redirects are retained. The source docs directory is excluded from the public build.
