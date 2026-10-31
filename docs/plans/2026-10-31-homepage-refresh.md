# Personal Homepage Refresh Implementation Plan

> **For Claude:** Execute the approved homepage refresh in this session.

**Goal:** Deliver a refined bilingual personal homepage reflecting verified current research, open-source work, and MAIVER practice without adding an unconfirmed founder title.

**Architecture:** Preserve Jekyll, existing publication URLs and Pages deployment. Introduce a dedicated editorial layout, structured publication data, a focused homepage and searchable complete publication archive. Use progressive enhancement so all content and links remain available without JavaScript.

**Tech Stack:** Jekyll / Liquid, HTML, CSS, small dependency-free JavaScript.

---

1. Extract every existing publication into `_data/publications.json`; preserve authors and PDFs, correct verified metadata and replace empty links with plain availability notes.
2. Create `_layouts/profile.html`, `_includes/publication.html`, `assets/css/profile.css` and `assets/js/profile.js`; implement bilingual text, mobile navigation, keyboard access and reduced-motion support.
3. Replace `_pages/about.md` with the bilingual homepage; add `_pages/publications.html`. Preserve old deep links and redirects.
4. Update canonical domain and descriptions in `_config.yml`. Add publication provenance and a concise maintenance guide under excluded `docs/`.
5. Build with `bundle exec jekyll build`; check local links, publication retention and metadata. Inspect desktop/mobile rendering, translation, filtering, no-results and keyboard behavior in the browser.
6. Commit reviewed files, push the verified site update and observe the GitHub Pages deployment. Verify the served homepage contains the new revision.
