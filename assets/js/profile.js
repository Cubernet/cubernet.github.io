(() => {
  'use strict';
  const root = document.documentElement;
  const toggle = document.querySelector('.language-toggle');
  const setLanguage = (language) => {
    const english = language === 'en';
    root.lang = english ? 'en' : 'zh-CN';
    toggle.replaceChildren(document.createTextNode(english ? '中文 ↗' : 'EN ↗'));
    toggle.setAttribute('aria-label', english ? '切换至中文' : 'Switch to English');
    document.querySelectorAll('option[data-zh]').forEach(option => {
      option.textContent = option.dataset[english ? 'en' : 'zh'];
    });
    const search = document.querySelector('#publication-search');
    if (search) search.placeholder = english ? 'Title, author, venue' : '标题、作者、会议';
    try { localStorage.setItem('xlliu-language', language); } catch (_) { /* Storage may be unavailable. */ }
  };
  let savedLanguage = 'zh';
  try { savedLanguage = localStorage.getItem('xlliu-language') || 'zh'; } catch (_) {}
  setLanguage(savedLanguage);
  toggle.hidden = false;
  toggle.addEventListener('click', () => setLanguage(root.lang === 'en' ? 'zh' : 'en'));

  const tools = document.querySelector('.archive-tools');
  if (!tools) return;
  const search = document.querySelector('#publication-search');
  const topic = document.querySelector('#publication-topic');
  const year = document.querySelector('#publication-year');
  const reset = document.querySelector('#reset-filters');
  const papers = Array.from(document.querySelectorAll('.all-publications .publication'));
  const searchablePapers = papers.map(element => ({element, text: element.textContent.toLocaleLowerCase()}));
  const query = new URLSearchParams(location.search);
  if (Array.from(topic.options).some(option => option.value === query.get('topic'))) topic.value = query.get('topic');
  if (Array.from(year.options).some(option => option.value === query.get('year'))) year.value = query.get('year');
  search.value = query.get('q') || '';
  const applyFilters = () => {
    const terms = search.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let count = 0;
    searchablePapers.forEach(({element, text}) => {
      const visible = terms.every(term => text.includes(term)) &&
        (topic.value === 'all' || element.dataset.topic === topic.value) &&
        (year.value === 'all' || element.dataset.year === year.value);
      element.hidden = !visible;
      if (visible) count++;
    });
    document.querySelectorAll('.publication-year-group').forEach(group => {
      group.hidden = !Array.from(group.querySelectorAll('.publication')).some(paper => !paper.hidden);
    });
    document.querySelector('#publication-count').textContent = count;
    document.querySelector('.no-results').hidden = count !== 0;
    reset.hidden = terms.length === 0 && topic.value === 'all' && year.value === 'all';
    const params = new URLSearchParams();
    if (search.value.trim()) params.set('q', search.value.trim());
    if (topic.value !== 'all') params.set('topic', topic.value);
    if (year.value !== 'all') params.set('year', year.value);
    try { history.replaceState(null, '', location.pathname + (params.size ? '?' + params : '') + location.hash); } catch (_) {}
  };
  tools.hidden = false;
  search.addEventListener('input', applyFilters);
  topic.addEventListener('change', applyFilters);
  year.addEventListener('change', applyFilters);
  reset.addEventListener('click', () => { search.value = ''; topic.value = 'all'; year.value = 'all'; applyFilters(); search.focus(); });
  applyFilters();
})();
