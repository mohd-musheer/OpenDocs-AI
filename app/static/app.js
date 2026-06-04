/* ============================================================
   MYCONTEXTAI — app.js
   Premium AI SaaS interface logic
   ============================================================ */

(function () {
  'use strict';

  /* ── DOM refs ─────────────────────────────────────────── */
  const questionInput  = document.getElementById('question');
  const messagesList   = document.getElementById('messages');
  const sendBtn        = document.getElementById('sendBtn');
  const welcomeScreen  = document.getElementById('welcomeScreen');
  const chatViewport   = document.getElementById('chatViewport');
  const sidebarToggle  = document.getElementById('sidebarToggle');
  const sidebar        = document.querySelector('.sidebar');

  /* ── State ────────────────────────────────────────────── */
  let isLoading   = false;
  let hasMessages = false;

  /* ── Sidebar (mobile) ─────────────────────────────────── */
  let overlay = null;

  function createOverlay() {
    overlay = document.createElement('div');
    overlay.className = 'sidebar-overlay';
    document.body.appendChild(overlay);
    overlay.addEventListener('click', closeSidebar);
  }

  function openSidebar() {
    sidebar.classList.add('open');
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeSidebar() {
    sidebar.classList.remove('open');
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (sidebarToggle) {
    createOverlay();
    sidebarToggle.addEventListener('click', () => {
      if (sidebar.classList.contains('open')) {
        closeSidebar();
      } else {
        openSidebar();
      }
    });
  }

  /* ── Auto-resize textarea ─────────────────────────────── */
  function autoResize(el) {
    el.style.height = 'auto';
    el.style.height = Math.min(el.scrollHeight, 180) + 'px';
  }

  questionInput.addEventListener('input', () => autoResize(questionInput));

  /* ── Keyboard shortcuts ───────────────────────────────── */
  questionInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      if (!isLoading) askQuestion();
    }
  });

  /* ── Welcome screen interaction ──────────────────────── */
  document.querySelectorAll('.wcard').forEach((card) => {
    card.addEventListener('click', () => {
      const prompt = card.dataset.prompt;
      if (prompt) {
        questionInput.value = prompt;
        autoResize(questionInput);
        questionInput.focus();
        askQuestion();
      }
    });
  });

  document.querySelectorAll('.quick-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      const prompt = btn.dataset.prompt;
      if (prompt) {
        questionInput.value = prompt;
        autoResize(questionInput);
        questionInput.focus();
        closeSidebar();
        askQuestion();
      }
    });
  });

  /* ── Transition welcome → chat ───────────────────────── */
  function hideWelcome() {
    if (hasMessages) return;
    hasMessages = true;
    welcomeScreen.style.transition = 'opacity 300ms ease, transform 300ms ease';
    welcomeScreen.style.opacity    = '0';
    welcomeScreen.style.transform  = 'translateY(-10px)';
    welcomeScreen.style.pointerEvents = 'none';
    setTimeout(() => {
      welcomeScreen.style.display = 'none';
    }, 320);
  }

  /* ── Build message elements ───────────────────────────── */
  function createUserMessage(text) {
    const msg = document.createElement('div');
    msg.className = 'message user';

    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.textContent = text;

    msg.appendChild(bubble);
    return msg;
  }

  function createLoadingMessage() {
    const msg = document.createElement('div');
    msg.className = 'message ai loading';

    const header = buildAIHeader();
    const bubble = document.createElement('div');
    bubble.className = 'bubble shimmer';

    const dots = document.createElement('div');
    dots.className = 'typing-indicator';
    dots.innerHTML = '<span></span><span></span><span></span>';

    bubble.appendChild(dots);
    msg.appendChild(header);
    msg.appendChild(bubble);
    return msg;
  }

  function createAIMessage(text) {
    const msg = document.createElement('div');
    msg.className = 'message ai';

    const header = buildAIHeader();
    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.innerHTML = marked.parse(text);

    msg.appendChild(header);
    msg.appendChild(bubble);
    return msg;
  }

  function createErrorMessage(errText) {
    const msg = document.createElement('div');
    msg.className = 'message ai error';

    const header = buildAIHeader();
    const bubble = document.createElement('div');
    bubble.className = 'bubble';

    const p = document.createElement('p');
    p.className = 'error-text';
    p.textContent = '⚠ ' + errText;

    bubble.appendChild(p);
    msg.appendChild(header);
    msg.appendChild(bubble);
    return msg;
  }

  function buildAIHeader() {
    const header = document.createElement('div');
    header.className = 'msg-header';

    const avatar = document.createElement('div');
    avatar.className = 'ai-avatar';
    avatar.textContent = '✦';

    const name = document.createElement('span');
    name.className = 'ai-name';
    name.textContent = 'MyContextAI';

    header.appendChild(avatar);
    header.appendChild(name);
    return header;
  }

  /* ── Format AI answer (basic markdown-like) ──────────── */
function formatAnswer(text) {

  let html = escapeHTML(text);

  // Horizontal rule
  html = html.replace(/^---$/gm, '<hr>');

  // Headers
  html = html.replace(/^###### (.*)$/gm, '<h6>$1</h6>');
  html = html.replace(/^##### (.*)$/gm, '<h5>$1</h5>');
  html = html.replace(/^#### (.*)$/gm, '<h4>$1</h4>');
  html = html.replace(/^### (.*)$/gm, '<h3>$1</h3>');
  html = html.replace(/^## (.*)$/gm, '<h2>$1</h2>');
  html = html.replace(/^# (.*)$/gm, '<h1>$1</h1>');

  // Bold
  html = html.replace(
    /\*\*(.*?)\*\*/g,
    '<strong>$1</strong>'
  );

  // Italic
  html = html.replace(
    /\*(.*?)\*/g,
    '<em>$1</em>'
  );

  // Inline code
  html = html.replace(
    /`([^`]+)`/g,
    '<code>$1</code>'
  );

  // Bullet lists
  html = html.replace(
    /^[\-•]\s+(.+)$/gm,
    '<li>$1</li>'
  );

  html = html.replace(
    /(<li>.*?<\/li>)/gs,
    '<ul>$1</ul>'
  );

  const blocks = html.split(/\n{2,}/);

  html = blocks.map(block => {

    block = block.trim();

    if (!block) return '';

    if (
      block.startsWith('<h') ||
      block.startsWith('<ul') ||
      block.startsWith('<hr')
    ) {
      return block;
    }

    return `<p>${block.replace(/\n/g,'<br>')}</p>`;

  }).join('');

  return html;
}

  function escapeHTML(str) {
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  /* ── Scroll helpers ────────────────────────────────────── */
  function scrollToBottom(smooth = true) {
    requestAnimationFrame(() => {
      chatViewport.scrollTo({
        top: chatViewport.scrollHeight,
        behavior: smooth ? 'smooth' : 'instant',
      });
    });
  }

  /* ── Set loading UI state ─────────────────────────────── */
  function setLoading(state) {
    isLoading = state;
    sendBtn.disabled = state;
    questionInput.disabled = state;
  }

  /* ── Main ask function (globally exposed) ─────────────── */
  window.askQuestion = async function () {
    const question = questionInput.value.trim();
    if (!question || isLoading) return;

    // Transition out welcome screen
    hideWelcome();

    // Append user message
    const userMsg = createUserMessage(question);
    messagesList.appendChild(userMsg);

    // Clear input
    questionInput.value = '';
    questionInput.style.height = 'auto';
    questionInput.focus();

    scrollToBottom();

    // Show loading
    setLoading(true);
    const loadingMsg = createLoadingMessage();
    messagesList.appendChild(loadingMsg);
    scrollToBottom();

    try {
      const response = await fetch('/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question }),
      });

      if (!response.ok) {
        throw new Error(`Server error (${response.status})`);
      }

      const data = await response.json();

      // Replace loader with answer
      loadingMsg.remove();
      const aiMsg = createAIMessage(data.answer || 'No response received.');
      messagesList.appendChild(aiMsg);
      scrollToBottom();

    } catch (error) {
      loadingMsg.remove();
      const errMsg = createErrorMessage(
        error.message || 'Something went wrong. Please try again.'
      );
      messagesList.appendChild(errMsg);
      scrollToBottom();
    } finally {
      setLoading(false);
    }
  };

  /* ── Init ─────────────────────────────────────────────── */
  questionInput.focus();

})();