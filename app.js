/**
 * Jukugo Master - Japanese Kanji Learning Platform
 * Main Application Logic
 */

// ==========================================
// 1. STATE MANAGEMENT
// ==========================================
let allJukugoList = [];
let filteredList = [];
let currentWeekFilter = 0; // 0 = all
let currentKanjiFilter = null;
let currentSearchQuery = "";
let currentLevelFilter = "all";
let isFuriganaHidden = false;

// Favorites
let favorites = new Set();

// Flashcard State
let flashcardList = [];
let flashcardIndex = 0;
let isFlashcardShuffled = false;
let flashcardOriginalList = [];
let autoPlayTimer = null;
let autoPlaySpeed = 3000; // 3 seconds
let isAutoPlaying = false;
let isFlashcardFuriganaHidden = false;

// Quiz State
let quizQuestions = [];
let currentQuestionIndex = 0;
let quizScore = 0;
let quizStreak = 0;
let quizMaxStreak = 0;
let quizWrongAnswers = [];
let isAnswerSubmitted = false;
let quizSoundEnabled = true;

// ==========================================
// 2. INITIALIZATION
// ==========================================
document.addEventListener("DOMContentLoaded", () => {
  initStorage();
  flattenDatabase();
  setupEventListeners();
  setupWeekSelectors();
  renderWeeksSummaryGrid();
  applyFilters();
  initFlashcard();
});

function initStorage() {
  // Load Theme
  const savedTheme = localStorage.getItem("jukugo_theme") || "light";
  document.documentElement.setAttribute("data-theme", savedTheme);

  // Load Furigana Preference
  const savedFurigana = localStorage.getItem("jukugo_furigana_hide");
  if (savedFurigana === "true") {
    isFuriganaHidden = true;
    document.body.classList.add("hide-furigana");
    updateFuriganaToggleUI();
  }

  // Load Favorites
  try {
    const savedFavs = JSON.parse(localStorage.getItem("jukugo_favorites") || "[]");
    favorites = new Set(savedFavs);
    updateFavBadge();
  } catch (e) {
    favorites = new Set();
  }
}

function flattenDatabase() {
  allJukugoList = [];
  if (typeof JUKUGO_DATABASE === "undefined") {
    console.error("JUKUGO_DATABASE is not defined! Check data.js");
    return;
  }

  let idCounter = 1;
  JUKUGO_DATABASE.forEach((item) => {
    item.jukugo.forEach((j) => {
      allJukugoList.push({
        id: `jk_${idCounter++}`,
        word: j.word,
        furigana: j.furigana,
        romaji: j.romaji,
        meaning: j.meaning,
        level: j.level || "Umum",
        example: j.example || "",
        example_reading: j.example_reading || "",
        example_meaning: j.example_meaning || "",
        kanji: item.kanji,
        onyomi: item.onyomi,
        kunyomi: item.kunyomi,
        kanjiMeaning: item.meaning,
        week: item.week,
        note: item.note || ""
      });
    });
  });

  filteredList = [...allJukugoList];
}

function setupEventListeners() {
  // Keyboard navigation for Flashcard
  window.addEventListener("keydown", (e) => {
    const flashcardSection = document.getElementById("view-flashcard");
    if (flashcardSection && flashcardSection.classList.contains("active")) {
      if (e.key === "ArrowRight" || e.key === " ") {
        e.preventDefault();
        nextFlashcard();
      } else if (e.key === "ArrowLeft") {
        e.preventDefault();
        prevFlashcard();
      } else if (e.key.toLowerCase() === "s") {
        speakCurrentFlashcard();
      } else if (e.key.toLowerCase() === "f") {
        toggleCurrentFlashcardFav();
      }
    }
  });
}

function getAvailableWeeks() {
  const weeks = Array.from(new Set(JUKUGO_DATABASE.map(k => k.week)));
  return weeks.sort((a, b) => a - b);
}

function setupWeekSelectors() {
  const weeks = getAvailableWeeks();
  const countAll = allJukugoList.length;

  // 1. Week Selector Pills in List View
  const pillsContainer = document.getElementById("weekSelectorPills");
  if (pillsContainer) {
    pillsContainer.innerHTML = "";
    
    // Semua Minggu Pill
    const allBtn = document.createElement("button");
    allBtn.className = `week-pill ${currentWeekFilter === 0 ? 'active' : ''}`;
    allBtn.innerHTML = `Semua Minggu <span class="badge" id="pillCountAll">${countAll} Jukugo</span>`;
    allBtn.onclick = () => filterByWeek(0, allBtn);
    pillsContainer.appendChild(allBtn);

    // Individual Week Pills
    weeks.forEach(w => {
      const kanjisInW = JUKUGO_DATABASE.filter(k => k.week === w).length;
      const jukugosInW = allJukugoList.filter(j => j.week === w).length;
      
      const btn = document.createElement("button");
      btn.className = `week-pill ${currentWeekFilter === w ? 'active' : ''}`;
      btn.innerHTML = `Minggu ${w} <span class="badge">${kanjisInW} Kanji (${jukugosInW})</span>`;
      btn.onclick = () => filterByWeek(w, btn);
      pillsContainer.appendChild(btn);
    });
  }

  // 2. Flashcard Dropdown
  const fcSelect = document.getElementById("flashcardWeekSelect");
  if (fcSelect) {
    const currentVal = fcSelect.value || "0";
    fcSelect.innerHTML = `<option value="0">Semua Minggu (${countAll} Jukugo)</option>`;
    weeks.forEach(w => {
      const kanjisInW = JUKUGO_DATABASE.filter(k => k.week === w).length;
      const jukugosInW = allJukugoList.filter(j => j.week === w).length;
      fcSelect.innerHTML += `<option value="${w}">Minggu ${w} Saja (${kanjisInW} Kanji - ${jukugosInW} Jukugo)</option>`;
    });
    fcSelect.innerHTML += `<option value="fav">Hanya Favorit ⭐</option>`;
    fcSelect.value = currentVal;
  }

  // 3. Quiz Dropdown
  const quizSelect = document.getElementById("quizWeekSelect");
  if (quizSelect) {
    const currentVal = quizSelect.value || "0";
    quizSelect.innerHTML = `<option value="0">Semua Minggu (Semua ${weeks.length} Minggu)</option>`;
    weeks.forEach(w => {
      const kanjisInW = JUKUGO_DATABASE.filter(k => k.week === w).length;
      quizSelect.innerHTML += `<option value="${w}">Minggu ${w} Saja (${kanjisInW} Kanji)</option>`;
    });
    quizSelect.innerHTML += `<option value="fav">Hanya Soal Dari Favorit ⭐</option>`;
    quizSelect.value = currentVal;
  }
}

function renderWeeksSummaryGrid() {
  const container = document.getElementById("weeksSummaryGrid");
  if (!container) return;
  container.innerHTML = "";

  const weeks = getAvailableWeeks();
  weeks.forEach(w => {
    const kanjiObjs = JUKUGO_DATABASE.filter(k => k.week === w);
    const jukugoCount = allJukugoList.filter(j => j.week === w).length;
    const kanjiListStr = kanjiObjs.map(k => k.kanji).join("、");

    const card = document.createElement("div");
    card.className = "stat-item";
    card.style.textAlign = "left";
    card.innerHTML = `
      <div class="lbl" style="font-weight: 700; color: var(--primary);">MINGGU ${w}</div>
      <div class="val">${kanjiObjs.length} Kanji</div>
      <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">${jukugoCount} Jukugo Berfrekuensi Tinggi</div>
      <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.35rem; font-family: var(--font-serif-jp); word-break: break-all;">
        ${kanjiListStr}
      </div>
    `;
    container.appendChild(card);
  });
}

// ==========================================
// 3. NAVIGATION & VIEW SWITCHING
// ==========================================
function switchView(viewName) {
  // Pause autoplay if leaving flashcard
  if (viewName !== "flashcard" && isAutoPlaying) {
    toggleFlashcardAutoPlay();
  }

  // Update tabs UI
  const tabButtons = document.querySelectorAll(".nav-tabs .tab-btn");
  tabButtons.forEach(btn => btn.classList.remove("active"));

  const targetTabIdx = {
    'list': 0,
    'flashcard': 1,
    'quiz': 2,
    'favorites': 3,
    'info': 4
  }[viewName];

  if (tabButtons[targetTabIdx]) {
    tabButtons[targetTabIdx].classList.add("active");
  }

  // Update sections
  document.querySelectorAll(".view-section").forEach(sec => sec.classList.remove("active"));
  const targetSection = document.getElementById(`view-${viewName}`);
  if (targetSection) {
    targetSection.classList.add("active");
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });

  if (viewName === "flashcard") {
    updateFlashcardCard();
  } else if (viewName === "favorites") {
    renderFavoritesView();
  }
}

function toggleTheme() {
  const current = document.documentElement.getAttribute("data-theme");
  const next = current === "dark" ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", next);
  localStorage.setItem("jukugo_theme", next);
}

// ==========================================
// 4. LIST VIEW CONTROLLER & FILTERS
// ==========================================
function filterByWeek(weekNumber, element) {
  currentWeekFilter = weekNumber;
  currentKanjiFilter = null; // reset specific kanji

  // Update active pill UI
  const pills = document.querySelectorAll("#weekSelectorPills .week-pill");
  pills.forEach(p => p.classList.remove("active"));
  if (element) {
    element.classList.add("active");
  }

  renderKanjiRibbon();
  applyFilters();
}

function filterByKanji(kanjiChar, element) {
  if (currentKanjiFilter === kanjiChar) {
    currentKanjiFilter = null; // toggle off
  } else {
    currentKanjiFilter = kanjiChar;
  }

  renderKanjiRibbon();
  applyFilters();
}

function renderKanjiRibbon() {
  const ribbon = document.getElementById("kanjiRibbon");
  ribbon.innerHTML = "";

  // Get kanjis in current week filter
  let kanjiList = JUKUGO_DATABASE;
  if (currentWeekFilter > 0) {
    kanjiList = JUKUGO_DATABASE.filter(k => k.week === currentWeekFilter);
  }

  // "Semua" chip
  const allChip = document.createElement("button");
  allChip.className = `kanji-chip ${currentKanjiFilter === null ? 'active' : ''}`;
  allChip.textContent = "Semua";
  allChip.style.fontSize = "0.85rem";
  allChip.style.minWidth = "auto";
  allChip.onclick = () => filterByKanji(null);
  ribbon.appendChild(allChip);

  kanjiList.forEach(k => {
    const chip = document.createElement("button");
    chip.className = `kanji-chip ${currentKanjiFilter === k.kanji ? 'active' : ''}`;
    chip.textContent = k.kanji;
    chip.title = `${k.kanji} (${k.onyomi} / ${k.kunyomi || '-'}) - ${k.meaning}`;
    chip.onclick = () => filterByKanji(k.kanji);
    ribbon.appendChild(chip);
  });
}

function handleSearch() {
  const query = document.getElementById("searchInput").value.trim().toLowerCase();
  currentSearchQuery = query;
  const clearBtn = document.getElementById("searchClearBtn");
  clearBtn.style.display = query ? "block" : "none";
  applyFilters();
}

function clearSearch() {
  document.getElementById("searchInput").value = "";
  handleSearch();
}

function applyFilters() {
  currentLevelFilter = document.getElementById("levelFilterSelect").value;

  filteredList = allJukugoList.filter(item => {
    // Week filter
    if (currentWeekFilter > 0 && item.week !== currentWeekFilter) {
      return false;
    }
    // Specific kanji filter
    if (currentKanjiFilter && item.kanji !== currentKanjiFilter) {
      return false;
    }
    // Level filter
    if (currentLevelFilter !== "all" && item.level !== currentLevelFilter) {
      return false;
    }
    // Search query
    if (currentSearchQuery) {
      const q = currentSearchQuery;
      const matchWord = item.word.includes(q);
      const matchFurigana = item.furigana.toLowerCase().includes(q);
      const matchRomaji = item.romaji.toLowerCase().includes(q);
      const matchMeaning = item.meaning.toLowerCase().includes(q);
      const matchKanji = item.kanji.includes(q);
      if (!matchWord && !matchFurigana && !matchRomaji && !matchMeaning && !matchKanji) {
        return false;
      }
    }
    return true;
  });

  // Update info bar
  const resultsCountEl = document.getElementById("resultsCount");
  resultsCountEl.textContent = `Menampilkan ${filteredList.length} dari ${allJukugoList.length} jukugo`;

  let filterDesc = currentWeekFilter === 0 ? "Semua Minggu" : `Minggu ${currentWeekFilter}`;
  if (currentKanjiFilter) {
    filterDesc += ` • Kanji: ${currentKanjiFilter}`;
  }
  if (currentLevelFilter !== "all") {
    filterDesc += ` • Level: ${currentLevelFilter}`;
  }
  document.getElementById("activeFilterDesc").textContent = filterDesc;

  renderJukugoGrid(filteredList, "jukugoGrid");
}

function toggleGlobalFurigana() {
  isFuriganaHidden = !isFuriganaHidden;
  document.body.classList.toggle("hide-furigana", isFuriganaHidden);
  localStorage.setItem("jukugo_furigana_hide", isFuriganaHidden.toString());
  updateFuriganaToggleUI();
}

function updateFuriganaToggleUI() {
  const icon = document.getElementById("furiganaIcon");
  const label = document.getElementById("furiganaLabel");
  const btn = document.getElementById("toggleFuriganaBtn");

  if (isFuriganaHidden) {
    icon.textContent = "🙈";
    label.textContent = "Furigana: Tersembunyi (Klik Intip)";
    btn.classList.add("active");
  } else {
    icon.textContent = "👁️";
    label.textContent = "Furigana: Tampil";
    btn.classList.remove("active");
  }
}

// Build ruby tag for jukugo
function buildRuby(word, furigana) {
  return `<ruby>${word}<rt>${furigana}</rt></ruby>`;
}

function renderJukugoGrid(list, targetElementId) {
  const grid = document.getElementById(targetElementId);
  grid.innerHTML = "";

  if (list.length === 0) {
    grid.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 3rem 1rem; color: var(--text-muted);">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔍</div>
        <div style="font-size: 1.1rem; font-weight: 700; color: var(--text-main);">Tidak ada jukugo yang cocok</div>
        <p style="font-size: 0.9rem; margin-top: 0.25rem;">Coba ganti filter minggu, kata kunci pencarian, atau level.</p>
      </div>
    `;
    return;
  }

  list.forEach(item => {
    const isFav = favorites.has(item.id);
    const card = document.createElement("div");
    card.className = "jukugo-card";

    card.innerHTML = `
      <div class="card-top-row">
        <div class="card-badges">
          <span class="badge-week">Minggu ${item.week}</span>
          <span class="badge-level">${item.level}</span>
          <span class="badge-kanji-root" title="${item.kanjiMeaning} (On: ${item.onyomi} / Kun: ${item.kunyomi || '-'})">
            Kanji: ${item.kanji}
          </span>
        </div>
        <div class="card-tools">
          <button class="card-btn" title="Dengarkan Pengucapan Jepang" onclick="speakJapanese('${item.word}')">
            🔊
          </button>
          <button class="card-btn ${isFav ? 'favorited' : ''}" title="Simpan ke Favorit" onclick="toggleFavorite('${item.id}', this)">
            ${isFav ? '★' : '☆'}
          </button>
          <button class="card-btn" title="Salin Kata" onclick="copyJukugo('${item.word}', '${item.furigana}', '${item.meaning.replace(/'/g, "\\'")}')">
            📋
          </button>
        </div>
      </div>

      <div class="card-main-word">
        <div class="kanji-text jp-font" onclick="revealFurigana(this)">
          ${buildRuby(item.word, item.furigana)}
        </div>
        <div class="romaji-text">${item.romaji}</div>
      </div>

      <div class="meaning-box">
        <div class="meaning-text">${item.meaning}</div>
      </div>

      ${item.example ? `
      <div class="example-box">
        <div class="example-jp jp-font">${item.example}</div>
        <div class="example-id">${item.example_meaning}</div>
      </div>
      ` : ''}
    `;

    grid.appendChild(card);
  });
}

function revealFurigana(element) {
  const rt = element.querySelector("rt");
  if (rt) {
    rt.classList.toggle("revealed");
  }
}

function copyJukugo(word, furigana, meaning) {
  const text = `${word} (${furigana}) - ${meaning}`;
  navigator.clipboard.writeText(text).then(() => {
    showToast(`Disalin: ${text}`);
  }).catch(() => {
    showToast(`Tersalin: ${word}`);
  });
}

// Toast notification helper
function showToast(message) {
  const existing = document.getElementById("siteToast");
  if (existing) existing.remove();

  const toast = document.createElement("div");
  toast.id = "siteToast";
  toast.style.position = "fixed";
  toast.style.bottom = "24px";
  toast.style.right = "24px";
  toast.style.zIndex = "9999";
  toast.style.backgroundColor = "var(--primary)";
  toast.style.color = "white";
  toast.style.padding = "0.75rem 1.25rem";
  toast.style.borderRadius = "var(--radius-full)";
  toast.style.boxShadow = "var(--shadow-lg)";
  toast.style.fontSize = "0.875rem";
  toast.style.fontWeight = "600";
  toast.style.animation = "fadeIn 0.2s ease";
  toast.textContent = message;

  document.body.appendChild(toast);
  setTimeout(() => {
    toast.style.opacity = "0";
    toast.style.transition = "opacity 0.3s ease";
    setTimeout(() => toast.remove(), 300);
  }, 2200);
}

// ==========================================
// 5. FAVORITES MANAGEMENT
// ==========================================
function toggleFavorite(id, buttonElement) {
  if (favorites.has(id)) {
    favorites.delete(id);
    if (buttonElement) {
      buttonElement.textContent = "☆";
      buttonElement.classList.remove("favorited");
    }
    showToast("Dihapus dari favorit");
  } else {
    favorites.add(id);
    if (buttonElement) {
      buttonElement.textContent = "★";
      buttonElement.classList.add("favorited");
    }
    showToast("Ditambahkan ke favorit ⭐");
  }

  localStorage.setItem("jukugo_favorites", JSON.stringify(Array.from(favorites)));
  updateFavBadge();

  // If in favorites view, re-render
  const favSection = document.getElementById("view-favorites");
  if (favSection && favSection.classList.contains("active")) {
    renderFavoritesView();
  }
}

function updateFavBadge() {
  const badge = document.getElementById("favCountBadge");
  if (badge) {
    badge.textContent = favorites.size;
  }
}

function renderFavoritesView() {
  const favList = allJukugoList.filter(item => favorites.has(item.id));
  renderJukugoGrid(favList, "favoritesGrid");
}

function clearAllFavorites() {
  if (favorites.size === 0) return;
  if (confirm("Apakah kamu yakin ingin menghapus semua bookmark favorit?")) {
    favorites.clear();
    localStorage.setItem("jukugo_favorites", JSON.stringify([]));
    updateFavBadge();
    renderFavoritesView();
    applyFilters();
  }
}

function studyFavoritesInFlashcard() {
  if (favorites.size === 0) {
    alert("Kamu belum menandai jukugo favorit apapun! Klik ikon bintang (☆) pada kartu yang ingin kamu tandai.");
    return;
  }
  document.getElementById("flashcardWeekSelect").value = "fav";
  changeFlashcardScope();
  switchView("flashcard");
}

// ==========================================
// 6. FLASHCARD (Front-Only, No Flip Needed)
// ==========================================
function initFlashcard() {
  changeFlashcardScope();
}

function changeFlashcardScope() {
  const val = document.getElementById("flashcardWeekSelect").value;
  if (val === "0") {
    flashcardList = [...allJukugoList];
  } else if (val === "fav") {
    flashcardList = allJukugoList.filter(item => favorites.has(item.id));
  } else {
    const weekNum = parseInt(val, 10);
    flashcardList = allJukugoList.filter(item => item.week === weekNum);
  }

  flashcardOriginalList = [...flashcardList];
  flashcardIndex = 0;

  if (isFlashcardShuffled) {
    shuffleArray(flashcardList);
  }

  updateFlashcardCard();
}

function updateFlashcardCard() {
  if (flashcardList.length === 0) {
    document.getElementById("fcKanji").innerHTML = "—";
    document.getElementById("fcRomaji").textContent = "Tidak ada kartu";
    document.getElementById("fcMeaning").textContent = "Pilih minggu lain atau tambahkan jukugo ke favorit.";
    document.getElementById("fcWeekBadge").textContent = "Kosong";
    document.getElementById("fcLevelBadge").textContent = "-";
    document.getElementById("fcRootBadge").textContent = "-";
    document.getElementById("fcExampleJp").textContent = "";
    document.getElementById("fcExampleId").textContent = "";
    document.getElementById("flashcardCounter").textContent = "0 / 0";
    document.getElementById("flashcardProgressBar").style.width = "0%";
    return;
  }

  // Bound index
  if (flashcardIndex >= flashcardList.length) flashcardIndex = 0;
  if (flashcardIndex < 0) flashcardIndex = flashcardList.length - 1;

  const item = flashcardList[flashcardIndex];

  // Update Content
  document.getElementById("fcKanji").innerHTML = buildRuby(item.word, item.furigana);
  document.getElementById("fcRomaji").textContent = item.romaji;
  document.getElementById("fcMeaning").textContent = item.meaning;
  document.getElementById("fcWeekBadge").textContent = `Minggu ${item.week}`;
  document.getElementById("fcLevelBadge").textContent = item.level;
  document.getElementById("fcRootBadge").textContent = `Kanji Asal: ${item.kanji} (${item.kanjiMeaning})`;

  document.getElementById("fcExampleJp").textContent = item.example || "—";
  document.getElementById("fcExampleId").textContent = item.example_meaning || "";

  // Favorite button state
  const isFav = favorites.has(item.id);
  const fcFavBtn = document.getElementById("fcFavBtn");
  fcFavBtn.textContent = isFav ? "★" : "☆";
  fcFavBtn.classList.toggle("favorited", isFav);

  // Counter & Progress
  document.getElementById("flashcardCounter").textContent = `${flashcardIndex + 1} / ${flashcardList.length}`;
  const pct = ((flashcardIndex + 1) / flashcardList.length) * 100;
  document.getElementById("flashcardProgressBar").style.width = `${pct}%`;
}

function nextFlashcard() {
  if (flashcardList.length <= 1) return;
  flashcardIndex++;
  if (flashcardIndex >= flashcardList.length) {
    flashcardIndex = 0;
  }
  updateFlashcardCard();
}

function prevFlashcard() {
  if (flashcardList.length <= 1) return;
  flashcardIndex--;
  if (flashcardIndex < 0) {
    flashcardIndex = flashcardList.length - 1;
  }
  updateFlashcardCard();
}

function resetFlashcardIndex() {
  flashcardIndex = 0;
  updateFlashcardCard();
  showToast("Kembali ke kartu pertama");
}

function toggleFlashcardShuffle() {
  isFlashcardShuffled = !isFlashcardShuffled;
  const btn = document.getElementById("flashcardShuffleBtn");
  btn.classList.toggle("active", isFlashcardShuffled);

  if (isFlashcardShuffled) {
    shuffleArray(flashcardList);
    flashcardIndex = 0;
    showToast("🔀 Urutan kartu diacak!");
  } else {
    flashcardList = [...flashcardOriginalList];
    flashcardIndex = 0;
    showToast("Urutan kartu dikembalikan semula");
  }
  updateFlashcardCard();
}

function toggleFlashcardAutoPlay() {
  isAutoPlaying = !isAutoPlaying;
  const btn = document.getElementById("flashcardAutoPlayBtn");
  btn.classList.toggle("active", isAutoPlaying);

  if (isAutoPlaying) {
    btn.innerHTML = `⏸️ <span>Stop Auto</span>`;
    showToast("▶️ Auto-play berjalan (3s per kartu)");
    autoPlayTimer = setInterval(() => {
      nextFlashcard();
    }, autoPlaySpeed);
  } else {
    btn.innerHTML = `▶️ <span>Auto (3s)</span>`;
    clearInterval(autoPlayTimer);
    autoPlayTimer = null;
    showToast("Auto-play dihentikan");
  }
}

function toggleFlashcardFurigana() {
  isFlashcardFuriganaHidden = !isFlashcardFuriganaHidden;
  const card = document.getElementById("flashcardCard");
  const btn = document.getElementById("fcToggleFuriganaBtn");

  if (isFlashcardFuriganaHidden) {
    card.classList.add("hide-furigana");
    btn.classList.add("active");
    btn.innerHTML = `🙈 Furigana Disembunyikan`;
    showToast("Furigana disembunyikan (arahkan mouse untuk melihat)");
  } else {
    card.classList.remove("hide-furigana");
    btn.classList.remove("active");
    btn.innerHTML = `👁️ Sembunyikan/Tampilkan Furigana`;
    showToast("Furigana ditampilkan kembali");
  }
}

function speakCurrentFlashcard() {
  if (flashcardList.length === 0) return;
  const item = flashcardList[flashcardIndex];
  speakJapanese(item.word);
}

function toggleCurrentFlashcardFav() {
  if (flashcardList.length === 0) return;
  const item = flashcardList[flashcardIndex];
  toggleFavorite(item.id, document.getElementById("fcFavBtn"));
}

// ==========================================
// 7. LATIHAN SOAL ACAK (QUIZ / LATSOL)
// ==========================================
function startQuiz() {
  const mode = document.getElementById("quizModeSelect").value;
  const weekScope = document.getElementById("quizWeekSelect").value;
  const count = parseInt(document.getElementById("quizCountSelect").value, 10);
  quizSoundEnabled = document.getElementById("quizSoundToggle").value === "on";

  // Filter pool
  let pool = [];
  if (weekScope === "0") {
    pool = [...allJukugoList];
  } else if (weekScope === "fav") {
    pool = allJukugoList.filter(item => favorites.has(item.id));
  } else {
    const w = parseInt(weekScope, 10);
    pool = allJukugoList.filter(item => item.week === w);
  }

  if (pool.length < 4) {
    alert("Jumlah materi jukugo pada pilihan ini kurang dari 4 kata. Silakan pilih minggu lain atau tambahkan lebih banyak favorit!");
    return;
  }

  // Shuffle pool
  const shuffledPool = [...pool];
  shuffleArray(shuffledPool);

  const selectedCount = Math.min(count, shuffledPool.length);
  const targetItems = shuffledPool.slice(0, selectedCount);

  // Generate Questions
  quizQuestions = targetItems.map((target, idx) => {
    // Determine question type for this question
    let qType = mode;
    if (mode === "mixed") {
      const types = ["reading", "meaning", "kanji"];
      qType = types[Math.floor(Math.random() * types.length)];
    }

    // Pick 3 distractors from allJukugoList (excluding target)
    const otherItems = allJukugoList.filter(i => i.id !== target.id);
    shuffleArray(otherItems);
    const distractors = otherItems.slice(0, 3);

    // Build options
    let correctText = "";
    let options = [];

    if (qType === "reading") {
      correctText = target.furigana;
      options = [
        { text: target.furigana, isCorrect: true },
        { text: distractors[0].furigana, isCorrect: false },
        { text: distractors[1].furigana, isCorrect: false },
        { text: distractors[2].furigana, isCorrect: false },
      ];
    } else if (qType === "meaning") {
      correctText = target.meaning;
      options = [
        { text: target.meaning, isCorrect: true },
        { text: distractors[0].meaning, isCorrect: false },
        { text: distractors[1].meaning, isCorrect: false },
        { text: distractors[2].meaning, isCorrect: false },
      ];
    } else if (qType === "kanji") {
      correctText = target.word;
      options = [
        { text: target.word, isCorrect: true },
        { text: distractors[0].word, isCorrect: false },
        { text: distractors[1].word, isCorrect: false },
        { text: distractors[2].word, isCorrect: false },
      ];
    }

    shuffleArray(options);

    return {
      index: idx + 1,
      target: target,
      qType: qType,
      options: options,
      correctText: correctText
    };
  });

  currentQuestionIndex = 0;
  quizScore = 0;
  quizStreak = 0;
  quizMaxStreak = 0;
  quizWrongAnswers = [];

  // Switch to active quiz view
  document.getElementById("quizSetupCard").style.display = "none";
  document.getElementById("quizResultsCard").style.display = "none";
  document.getElementById("quizActiveView").style.display = "block";

  renderCurrentQuestion();
}

function renderCurrentQuestion() {
  isAnswerSubmitted = false;
  const q = quizQuestions[currentQuestionIndex];
  const total = quizQuestions.length;

  // Header badges
  document.getElementById("quizProgressBadge").textContent = `Soal ${currentQuestionIndex + 1} / ${total}`;
  document.getElementById("quizScoreBadge").textContent = `Skor: ${quizScore}`;
  document.getElementById("quizStreakBadge").textContent = `🔥 Streak ${quizStreak}`;

  const pct = ((currentQuestionIndex + 1) / total) * 100;
  document.getElementById("quizProgressBar").style.width = `${pct}%`;

  // Hide explanation and next button
  document.getElementById("quizExplanationCard").style.display = "none";
  document.getElementById("quizNextBtn").style.display = "none";

  // Prompt & Badges
  const typeBadge = document.getElementById("quizTypeBadge");
  const promptEl = document.getElementById("quizQuestionPrompt");
  const hintEl = document.getElementById("quizQuestionHint");

  if (q.qType === "reading") {
    typeBadge.textContent = "TEBAK CARA BACA / FURIGANA";
    promptEl.textContent = q.target.word;
    hintEl.textContent = `Bagaimanakah cara baca hiragana untuk kata di atas? (Arti: ${q.target.meaning})`;
  } else if (q.qType === "meaning") {
    typeBadge.textContent = "TEBAK ARTI BAHASA INDONESIA";
    promptEl.innerHTML = buildRuby(q.target.word, q.target.furigana);
    hintEl.textContent = `Apakah arti bahasa Indonesia yang paling tepat dari jukugo di atas?`;
  } else if (q.qType === "kanji") {
    typeBadge.textContent = "TEBAK JUKUGO KANJI";
    promptEl.textContent = q.target.furigana;
    hintEl.textContent = `Pilih kanji majemuk yang tepat untuk arti: "${q.target.meaning}"`;
  }

  // Options
  const grid = document.getElementById("quizOptionsGrid");
  grid.innerHTML = "";

  q.options.forEach((opt, idx) => {
    const btn = document.createElement("button");
    btn.className = "quiz-option-btn jp-font";
    btn.innerHTML = `
      <span><strong>${['A', 'B', 'C', 'D'][idx]}.</strong> ${opt.text}</span>
      <span class="option-icon"></span>
    `;
    btn.onclick = () => handleOptionClick(opt, btn, q);
    grid.appendChild(btn);
  });
}

function handleOptionClick(selectedOption, buttonElement, question) {
  if (isAnswerSubmitted) return;
  isAnswerSubmitted = true;

  const allOptionBtns = document.querySelectorAll("#quizOptionsGrid .quiz-option-btn");
  allOptionBtns.forEach(btn => btn.disabled = true);

  if (selectedOption.isCorrect) {
    buttonElement.classList.add("correct");
    buttonElement.querySelector(".option-icon").textContent = "✓";
    quizScore += 10;
    quizStreak++;
    if (quizStreak > quizMaxStreak) quizMaxStreak = quizStreak;
    if (quizSoundEnabled) playChimeSound(true);
  } else {
    buttonElement.classList.add("wrong");
    buttonElement.querySelector(".option-icon").textContent = "✗";
    quizStreak = 0;
    if (quizSoundEnabled) playChimeSound(false);

    // Highlight correct option
    allOptionBtns.forEach(btn => {
      if (btn.textContent.includes(question.correctText)) {
        btn.classList.add("correct");
        btn.querySelector(".option-icon").textContent = "✓";
      }
    });

    // Record wrong answer
    quizWrongAnswers.push({
      target: question.target,
      userAnswer: selectedOption.text,
      correctAnswer: question.correctText,
      qType: question.qType
    });
  }

  // Update Header Badges
  document.getElementById("quizScoreBadge").textContent = `Skor: ${quizScore}`;
  document.getElementById("quizStreakBadge").textContent = `🔥 Streak ${quizStreak}`;

  // Show Explanation Card
  const expCard = document.getElementById("quizExplanationCard");
  expCard.innerHTML = `
    <div style="font-size: 0.85rem; font-weight: 700; color: var(--primary); margin-bottom: 0.35rem;">
      PENJELASAN & CONTOH:
    </div>
    <div style="font-size: 1.25rem; font-weight: 700; margin-bottom: 0.25rem;" class="jp-font">
      ${buildRuby(question.target.word, question.target.furigana)} (${question.target.romaji})
    </div>
    <div style="font-size: 0.95rem; font-weight: 600; color: var(--text-main); margin-bottom: 0.5rem;">
      Arti: ${question.target.meaning}
    </div>
    ${question.target.example ? `
    <div style="background: var(--bg-main); padding: 0.6rem 0.8rem; border-radius: var(--radius-sm); font-size: 0.85rem;">
      <div class="jp-font" style="font-weight: 600; color: var(--text-main);">${question.target.example}</div>
      <div style="color: var(--text-muted); font-size: 0.8rem;">${question.target.example_meaning}</div>
    </div>
    ` : ''}
  `;
  expCard.style.display = "block";

  // Show Next Button
  const nextBtn = document.getElementById("quizNextBtn");
  if (currentQuestionIndex < quizQuestions.length - 1) {
    nextBtn.innerHTML = `<span>Lanjut ke Soal Berikutnya</span> <span>➔</span>`;
  } else {
    nextBtn.innerHTML = `<span>Lihat Hasil Akhir Kuis</span> <span>🏆</span>`;
  }
  nextBtn.style.display = "inline-flex";
}

function nextQuestion() {
  currentQuestionIndex++;
  if (currentQuestionIndex < quizQuestions.length) {
    renderCurrentQuestion();
  } else {
    finishQuiz();
  }
}

function finishQuiz() {
  document.getElementById("quizActiveView").style.display = "none";
  const resultsCard = document.getElementById("quizResultsCard");
  resultsCard.style.display = "block";

  const total = quizQuestions.length;
  const correct = total - quizWrongAnswers.length;
  const wrong = quizWrongAnswers.length;
  const percent = Math.round((correct / total) * 100);

  // Grade determination
  let grade = "C";
  let title = "Tetap Semangat!";
  let desc = "Bagus sudah mencoba! Pelajari kembali kosakata yang salah agar makin ingat.";

  if (percent === 100) {
    grade = "S";
    title = "Sempurna! Luar Biasa Sekali! 🌟";
    desc = "Hebat sekali! Semua soal berhasil kamu jawab dengan benar tanpa cela!";
  } else if (percent >= 85) {
    grade = "A";
    title = "Sangat Hebat! Kerja Bagus! 🎉";
    desc = "Pemahaman jukugo kamu sudah sangat kuat. Pertahankan performamu!";
  } else if (percent >= 70) {
    grade = "B";
    title = "Bagus! Terus Tingkatkan! 👍";
    desc = "Kamu sudah menguasai sebagian besar materi dengan cukup baik.";
  }

  document.getElementById("resGrade").textContent = grade;
  document.getElementById("resPercent").textContent = `${percent}%`;
  document.getElementById("resTitle").textContent = title;
  document.getElementById("resDesc").textContent = desc;

  document.getElementById("resCorrectCount").textContent = correct;
  document.getElementById("resWrongCount").textContent = wrong;
  document.getElementById("resMaxStreak").textContent = quizMaxStreak;

  // Review Wrong Answers Section
  const wrongSec = document.getElementById("wrongAnswersSection");
  const reviewBtn = document.getElementById("btnReviewWrong");

  if (wrong > 0) {
    reviewBtn.style.display = "inline-flex";
    wrongSec.style.display = "block";

    const list = document.getElementById("wrongAnswersList");
    list.innerHTML = "";

    quizWrongAnswers.forEach((w, idx) => {
      const card = document.createElement("div");
      card.className = "wrong-answer-card";
      card.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.35rem;">
          <span style="font-weight: 700; font-size: 1.15rem;" class="jp-font">
            ${buildRuby(w.target.word, w.target.furigana)} (${w.target.romaji})
          </span>
          <span class="badge-week">Minggu ${w.target.week}</span>
        </div>
        <div style="font-size: 0.9rem; margin-bottom: 0.25rem;">
          <span style="color: var(--text-muted);">Arti:</span> <strong>${w.target.meaning}</strong>
        </div>
        <div style="font-size: 0.85rem; color: #ef4444; margin-bottom: 0.2rem;">
          Jawaban Kamu: ${w.userAnswer}
        </div>
        <div style="font-size: 0.85rem; color: #10b981; font-weight: 600;">
          Jawaban Benar: ${w.correctAnswer}
        </div>
      `;
      list.appendChild(card);
    });
  } else {
    reviewBtn.style.display = "none";
    wrongSec.style.display = "none";
  }
}

function restartQuiz() {
  document.getElementById("quizResultsCard").style.display = "none";
  document.getElementById("quizSetupCard").style.display = "block";
}

function reviewWrongAnswersOnly() {
  if (quizWrongAnswers.length === 0) return;

  // Re-run quiz using only wrong items
  quizQuestions = quizWrongAnswers.map((w, idx) => {
    const target = w.target;
    const otherItems = allJukugoList.filter(i => i.id !== target.id);
    shuffleArray(otherItems);
    const distractors = otherItems.slice(0, 3);

    let options = [];
    if (w.qType === "reading") {
      options = [
        { text: target.furigana, isCorrect: true },
        { text: distractors[0].furigana, isCorrect: false },
        { text: distractors[1].furigana, isCorrect: false },
        { text: distractors[2].furigana, isCorrect: false },
      ];
    } else if (w.qType === "meaning") {
      options = [
        { text: target.meaning, isCorrect: true },
        { text: distractors[0].meaning, isCorrect: false },
        { text: distractors[1].meaning, isCorrect: false },
        { text: distractors[2].meaning, isCorrect: false },
      ];
    } else {
      options = [
        { text: target.word, isCorrect: true },
        { text: distractors[0].word, isCorrect: false },
        { text: distractors[1].word, isCorrect: false },
        { text: distractors[2].word, isCorrect: false },
      ];
    }
    shuffleArray(options);

    return {
      index: idx + 1,
      target: target,
      qType: w.qType,
      options: options,
      correctText: w.correctAnswer
    };
  });

  currentQuestionIndex = 0;
  quizScore = 0;
  quizStreak = 0;
  quizMaxStreak = 0;
  quizWrongAnswers = [];

  document.getElementById("quizResultsCard").style.display = "none";
  document.getElementById("quizActiveView").style.display = "block";

  renderCurrentQuestion();
}

// ==========================================
// 8. AUDIO & SPEECH SYNTHESIS
// ==========================================
function speakJapanese(text) {
  if (!('speechSynthesis' in window)) {
    alert("Maaf, browser ini tidak mendukung fitur pengucapan audio (Web Speech API).");
    return;
  }

  window.speechSynthesis.cancel(); // Cancel any ongoing speech
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "ja-JP";
  utterance.rate = 0.9; // natural Japanese reading speed

  // Try to pick Japanese voice if available
  const voices = window.speechSynthesis.getVoices();
  const jaVoice = voices.find(v => v.lang.startsWith("ja") || v.lang.includes("JP"));
  if (jaVoice) {
    utterance.voice = jaVoice;
  }

  window.speechSynthesis.speak(utterance);
}

// Synthesize pleasant sound effects with Web Audio API
function playChimeSound(isCorrect) {
  try {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) return;
    const ctx = new AudioContext();

    if (isCorrect) {
      // High bell chime
      const osc1 = ctx.createOscillator();
      const osc2 = ctx.createOscillator();
      const gain = ctx.createGain();

      osc1.type = "sine";
      osc2.type = "sine";
      osc1.frequency.setValueAtTime(587.33, ctx.currentTime); // D5
      osc2.frequency.setValueAtTime(880, ctx.currentTime + 0.08); // A5

      gain.gain.setValueAtTime(0.15, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.5);

      osc1.connect(gain);
      osc2.connect(gain);
      gain.connect(ctx.destination);

      osc1.start();
      osc2.start(ctx.currentTime + 0.08);
      osc1.stop(ctx.currentTime + 0.5);
      osc2.stop(ctx.currentTime + 0.5);
    } else {
      // Gentle buzz
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = "triangle";
      osc.frequency.setValueAtTime(180, ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(120, ctx.currentTime + 0.25);

      gain.gain.setValueAtTime(0.15, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.3);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start();
      osc.stop(ctx.currentTime + 0.3);
    }
  } catch (e) {
    // Audio context not allowed or unsupported
  }
}

// ==========================================
// 9. UTILITIES
// ==========================================
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}
