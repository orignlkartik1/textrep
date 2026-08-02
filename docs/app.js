// TextRep Interactive Web Engine
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initPlayground();
  initFunctionSearch();
  initCopyButtons();
  initSmoothScroll();
});

// Theme Management
function initTheme() {
  const toggleBtn = document.getElementById('theme-toggle-btn');
  const themeIcon = document.getElementById('theme-icon');
  const themeText = document.getElementById('theme-text');

  // Check saved theme or system preference
  const savedTheme = localStorage.getItem('textrep-theme') || 
    (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');

  applyTheme(savedTheme);

  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      applyTheme(newTheme);
      localStorage.setItem('textrep-theme', newTheme);
    });
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    if (theme === 'light') {
      if (themeText) themeText.textContent = 'Dark Mode';
      if (themeIcon) {
        themeIcon.innerHTML = `<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>`;
      }
    } else {
      if (themeText) themeText.textContent = 'Light Mode';
      if (themeIcon) {
        themeIcon.innerHTML = `<circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>`;
      }
    }
  }
}

// Sample Text Datasets for Playground
const SAMPLE_TEXTS = {
  editorial: `TextRep is a lightweight Python library designed for developers, data scientists, and technical writers who need rapid, accurate text profiling without installing heavy natural language processing models like NLTK or SpaCy. 

With zero external dependencies for core functionality, TextRep quickly extracts document statistics, word frequency counts, readability metrics, and character distributions in a fraction of a millisecond. Whether you are building content management systems, automated doc checkers, or lightweight analytics tools, TextRep keeps your Python applications clean and fast.`,

  code: `import textrep as tr

def process_user_submission(file_path: str):
    # Load document using TextRep loader
    doc = tr.load(file_path)
    
    # Calculate key statistics
    stats = doc.stats()
    readability = doc.readability()
    
    print(f"Document: {doc.metadata.file_name}")
    print(f"Total Words: {stats.word_count}")
    print(f"Estimated Read Time: {readability.reading_time_minutes} min")
    
    return doc.to_dict()`,

  review: `The new mechanical keyboard exceeds all expectations! The tactile feedback is crisp, typing feel is incredibly smooth, and keycap legends are sharp and durable. Battery life on Bluetooth mode easily lasts over three weeks of daily coding. Highly recommended for software engineers and writers looking for a premium desktop experience.`,

  simple: `Hello world! TextRep analyzes text fast. Simple Python text profiling for everyone.`
};

// Playground Live Analytics Engine
function initPlayground() {
  const textarea = document.getElementById('playground-text');
  if (!textarea) return;

  const presetBtns = document.querySelectorAll('.preset-btn');
  presetBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      presetBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const presetKey = btn.getAttribute('data-preset');
      if (SAMPLE_TEXTS[presetKey]) {
        textarea.value = SAMPLE_TEXTS[presetKey];
        runAnalytics(textarea.value);
      }
    });
  });

  textarea.addEventListener('input', () => {
    runAnalytics(textarea.value);
  });

  // Tab switching in playground (Word Frequency vs Character Breakdown)
  const tabBtns = document.querySelectorAll('.playground-tab-btn');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const targetTab = btn.getAttribute('data-tab');
      document.querySelectorAll('.tab-content').forEach(content => {
        content.style.display = content.id === targetTab ? 'block' : 'none';
      });
    });
  });

  // Initial Calculation
  runAnalytics(textarea.value);
}

// Full TextRep Calculation Algorithm (Implemented in JS matching TextRep spec)
function runAnalytics(text) {
  const wordTokens = tokenizeWords(text);
  const wordCount = wordTokens.length;
  const charCount = text.length;
  const letterCount = (text.match(/[a-zA-Z]/g) || []).length;
  const digitCount = (text.match(/[0-9]/g) || []).length;
  const spaceCount = (text.match(/\s/g) || []).length;
  const symbolCount = charCount - (letterCount + digitCount + spaceCount);
  
  const uniqueWords = new Set(wordTokens.map(w => w.toLowerCase())).size;
  const avgWordLen = wordCount > 0 
    ? (wordTokens.reduce((sum, w) => sum + w.length, 0) / wordCount).toFixed(2)
    : "0.00";

  // Sentences
  const sentences = text.split(/[.!?]+/).filter(s => s.trim().length > 0);
  const sentenceCount = sentences.length || 1;
  const avgSentenceLen = (wordCount / sentenceCount).toFixed(1);
  const readingTime = (wordCount / 200).toFixed(2);

  // Update DOM Elements
  updateVal('res-words', wordCount.toLocaleString());
  updateVal('res-chars', charCount.toLocaleString());
  updateVal('res-unique', uniqueWords.toLocaleString());
  updateVal('res-avg-word', avgWordLen);
  updateVal('res-sentences', sentenceCount);
  updateVal('res-avg-sent', avgSentenceLen);
  updateVal('res-read-time', `${readingTime} min`);
  updateVal('res-letters', letterCount.toLocaleString());
  updateVal('res-digits', digitCount.toLocaleString());
  updateVal('res-spaces', spaceCount.toLocaleString());
  updateVal('res-symbols', symbolCount.toLocaleString());

  // Render Frequency Lists
  renderWordFrequency(wordTokens);
  renderCharacterFrequency(text);
}

function tokenizeWords(text) {
  if (!text) return [];
  // Match lowercased words
  return text.toLowerCase().match(/\b[a-z0-9'-]+\b/gi) || [];
}

function renderWordFrequency(tokens) {
  const freqContainer = document.getElementById('freq-word-list');
  if (!freqContainer) return;

  const freqMap = {};
  tokens.forEach(t => {
    const word = t.toLowerCase();
    freqMap[word] = (freqMap[word] || 0) + 1;
  });

  const sorted = Object.entries(freqMap)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 7);

  const maxCount = sorted[0] ? sorted[0][1] : 1;

  if (sorted.length === 0) {
    freqContainer.innerHTML = '<div class="text-dim" style="font-size:0.85rem;">No words detected yet.</div>';
    return;
  }

  freqContainer.innerHTML = sorted.map(([word, count]) => {
    const pct = Math.round((count / maxCount) * 100);
    return `
      <div class="freq-item">
        <span class="freq-word" title="${escapeHtml(word)}">${escapeHtml(word)}</span>
        <div class="freq-bar-wrapper">
          <div class="freq-bar" style="width: ${pct}%"></div>
        </div>
        <span class="freq-count">${count}</span>
      </div>
    `;
  }).join('');
}

function renderCharacterFrequency(text) {
  const container = document.getElementById('freq-char-list');
  if (!container) return;

  const charMap = {};
  for (let char of text.toLowerCase()) {
    if (/\s/.test(char)) continue; // skip spaces for clarity
    charMap[char] = (charMap[char] || 0) + 1;
  }

  const sorted = Object.entries(charMap)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 7);

  const maxCount = sorted[0] ? sorted[0][1] : 1;

  if (sorted.length === 0) {
    container.innerHTML = '<div class="text-dim" style="font-size:0.85rem;">No non-whitespace characters detected.</div>';
    return;
  }

  container.innerHTML = sorted.map(([char, count]) => {
    const pct = Math.round((count / maxCount) * 100);
    const displayChar = char === '\n' ? '\\n' : char;
    return `
      <div class="freq-item">
        <span class="freq-word" title="${escapeHtml(displayChar)}">'${escapeHtml(displayChar)}'</span>
        <div class="freq-bar-wrapper">
          <div class="freq-bar" style="width: ${pct}%; background: linear-gradient(90deg, var(--accent-purple), var(--accent-blue));"></div>
        </div>
        <span class="freq-count">${count}</span>
      </div>
    `;
  }).join('');
}

function updateVal(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value;
}

// Function Search & Category Filtering
function initFunctionSearch() {
  const searchInput = document.getElementById('func-search-input');
  const filterBtns = document.querySelectorAll('.filter-btn');
  const funcCards = document.querySelectorAll('.func-card');

  let activeCategory = 'all';
  let searchQuery = '';

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.toLowerCase().trim();
      filterCards();
    });
  }

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeCategory = btn.getAttribute('data-filter');
      filterCards();
    });
  });

  function filterCards() {
    funcCards.forEach(card => {
      const category = card.getAttribute('data-category');
      const sig = card.getAttribute('data-sig').toLowerCase();
      const desc = card.getAttribute('data-desc').toLowerCase();

      const matchesCat = activeCategory === 'all' || category === activeCategory;
      const matchesSearch = sig.includes(searchQuery) || desc.includes(searchQuery);

      if (matchesCat && matchesSearch) {
        card.style.display = 'grid';
      } else {
        card.style.display = 'none';
      }
    });
  }
}

// Copy Code Buttons with Toast Notifications
function initCopyButtons() {
  const copyButtons = document.querySelectorAll('[data-copy-target]');
  copyButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-copy-target');
      let textToCopy = '';

      if (targetId) {
        const targetEl = document.getElementById(targetId);
        if (targetEl) textToCopy = targetEl.innerText || targetEl.value;
      } else if (btn.getAttribute('data-copy-text')) {
        textToCopy = btn.getAttribute('data-copy-text');
      }

      if (textToCopy) {
        navigator.clipboard.writeText(textToCopy.trim()).then(() => {
          showToast('Copied to clipboard!');
        }).catch(() => {
          showToast('Failed to copy', true);
        });
      }
    });
  });
}

function showToast(message, isError = false) {
  let container = document.querySelector('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = 'toast';
  if (isError) toast.style.borderColor = 'var(--accent-rose)';

  toast.innerHTML = `
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="${isError ? 'var(--accent-rose)' : 'var(--accent-teal)'}" stroke-width="2">
      <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
      <polyline points="22 4 12 14.01 9 11.01"></polyline>
    </svg>
    <span>${escapeHtml(message)}</span>
  `;

  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 2400);
}

// Smooth Scrolling with active nav highlighting
function initSmoothScroll() {
  const navItems = document.querySelectorAll('.nav-item');
  const sections = document.querySelectorAll('section[id], header[id]');

  window.addEventListener('scroll', () => {
    let currentSection = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop - 100;
      if (window.scrollY >= sectionTop) {
        currentSection = section.getAttribute('id');
      }
    });

    navItems.forEach(item => {
      item.classList.remove('active');
      if (item.getAttribute('href') === `#${currentSection}`) {
        item.classList.add('active');
      }
    });
  });
}

function escapeHtml(str) {
  return str.replace(/[&<>"']/g, match => {
    const escapes = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' };
    return escapes[match];
  });
}
