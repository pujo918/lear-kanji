/*
  Kanji Learning MVP
  - 3 modes: Learning, Practice, Test (only one visible)
  - Canvas supports mouse + touch
  - Stroke counting: each pointer down = 1 stroke
  - No shape / order validation (MVP)
*/

// KANJI DATA (USE THIS DATA EXACTLY)
const kanjiData = [
  {
    kanji: "水",
    meaning_id: "air",
    furigana: "みず",
    onyomi: ["スイ"],
    kunyomi: ["みず"],
    bushu: {
      radical: "水",
      meaning_id: "air / air (elemen)"
    },
    strokes: 4,
    shape: "tall",
    density: "medium",
    zones: {}
  },
  {
    kanji: "火",
    meaning_id: "api",
    furigana: "ひ",
    onyomi: ["カ"],
    kunyomi: ["ひ"],
    bushu: {
      radical: "火",
      meaning_id: "api"
    },
    strokes: 4,
    shape: "wide",
    density: "medium",
    zones: {}
  },
  {
    kanji: "木",
    meaning_id: "pohon",
    furigana: "き",
    onyomi: ["モク", "ボク"],
    kunyomi: ["き", "こ"],
    bushu: {
      radical: "木",
      meaning_id: "kayu / pohon"
    },
    strokes: 4,
    shape: "balanced",
    density: "medium",
    zones: {
      bottomHorizontal: true
    }
  },
  {
    kanji: "語",
    meaning_id: "bahasa",
    furigana: "ご",
    onyomi: ["ゴ"],
    kunyomi: ["かた.る", "かた.らう"],
    bushu: {
      radical: "言",
      meaning_id: "kata / bicara"
    },
    strokes: 14,
    shape: "balanced",
    density: "high",
    zones: {}
  }
];

// Jukugo data (kanji practiced one-by-one)
const jukugoData = [
  {
    jukugo: "学校",
    reading: "がっこう",
    meaning_id: "sekolah",
    kanji: ["学", "校"]
  },
  {
    jukugo: "火山",
    reading: "かざん",
    meaning_id: "gunung berapi",
    kanji: ["火", "山"]
  },
  {
    jukugo: "水中",
    reading: "すいちゅう",
    meaning_id: "di dalam air",
    kanji: ["水", "中"]
  }
];

// Build a lookup map for kanji objects.
// This lets us add missing kanji for jukugo without changing the existing dropdowns too much.
const kanjiMap = {};
kanjiData.forEach((k) => {
  kanjiMap[k.kanji] = k;
});

// Ensure required kanji exist for jukugo practice.
// Note: values are heuristic-friendly defaults; they do not change evaluation thresholds.
const requiredJukugoKanji = [
  {
    kanji: "学",
    meaning_id: "belajar",
    furigana: "がく",
    onyomi: ["ガク"],
    kunyomi: ["まな.ぶ"],
    bushu: { radical: "子", meaning_id: "anak" },
    strokes: 8,
    shape: "balanced",
    density: "high",
    zones: {}
  },
  {
    kanji: "校",
    meaning_id: "sekolah",
    furigana: "こう",
    onyomi: ["コウ"],
    kunyomi: [],
    bushu: { radical: "木", meaning_id: "kayu / pohon" },
    strokes: 10,
    shape: "balanced",
    density: "high",
    zones: {}
  },
  {
    kanji: "山",
    meaning_id: "gunung",
    furigana: "やま",
    onyomi: ["サン"],
    kunyomi: ["やま"],
    bushu: { radical: "山", meaning_id: "gunung" },
    strokes: 3,
    shape: "tall",
    density: "medium",
    zones: {}
  },
  {
    kanji: "中",
    meaning_id: "tengah / dalam",
    furigana: "なか",
    onyomi: ["チュウ"],
    kunyomi: ["なか"],
    bushu: { radical: "丨", meaning_id: "garis" },
    strokes: 4,
    shape: "balanced",
    density: "medium",
    zones: {}
  }
];

requiredJukugoKanji.forEach((k) => {
  if (!kanjiMap[k.kanji]) {
    kanjiData.push(k);
    kanjiMap[k.kanji] = k;
  }
});

// ----------------------
// Small helpers
// ----------------------
function $(id) {
  return document.getElementById(id);
}

function setText(el, value) {
  el.textContent = value;
}

function randomItem(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function randomIndex(max) {
  return Math.floor(Math.random() * max);
}

// ----------------------
// Handwriting heuristics (Test Mode)
// ----------------------

// Get bounding box (min/max/width/height/area) from a list of {x,y} points.
function getBoundingBox(points) {
  if (!points || points.length === 0) return null;

  let minX = Infinity;
  let maxX = -Infinity;
  let minY = Infinity;
  let maxY = -Infinity;

  for (const p of points) {
    if (p.x < minX) minX = p.x;
    if (p.x > maxX) maxX = p.x;
    if (p.y < minY) minY = p.y;
    if (p.y > maxY) maxY = p.y;
  }

  const width = Math.max(0, maxX - minX);
  const height = Math.max(0, maxY - minY);
  const area = width * height;

  return { minX, maxX, minY, maxY, width, height, area };
}

// Check the overall proportion using width/height ratio.
// - tall: height noticeably greater than width
// - wide: width noticeably greater than height
// - balanced: roughly equal
function checkShape(points, shapeType) {
  const box = getBoundingBox(points);
  if (!box) return false;

  // Too tiny drawings are treated as invalid shape.
  if (box.width < 20 || box.height < 20) return false;

  const ratio = box.width / box.height;

  // Tolerant rules (MVP tuning for beginners)
  if (shapeType === "tall") {
    return ratio < 1.25;
  }

  if (shapeType === "wide") {
    return ratio > 0.75;
  }

  if (shapeType === "balanced") {
    return ratio > 0.7 && ratio < 1.4;
  }

  return true;
}

// Check stroke distribution using a 3x3 grid over the drawing bounding box.
// Returns { distributionCorrect, occupiedCells }.
function checkDistribution(points) {
  const box = getBoundingBox(points);
  if (!box) return { distributionCorrect: false, occupiedCells: 0 };
  if (box.width <= 0 || box.height <= 0) return { distributionCorrect: false, occupiedCells: 0 };

  const cellWidth = box.width / 3;
  const cellHeight = box.height / 3;
  if (cellWidth <= 0 || cellHeight <= 0) return { distributionCorrect: false, occupiedCells: 0 };

  const occupied = new Set();

  for (const p of points) {
    const relX = p.x - box.minX;
    const relY = p.y - box.minY;

    let col = Math.floor(relX / cellWidth);
    let row = Math.floor(relY / cellHeight);

    // Clamp 0..2
    if (col < 0) col = 0;
    if (col > 2) col = 2;
    if (row < 0) row = 0;
    if (row > 2) row = 2;

    occupied.add(`${row},${col}`);
  }

  const occupiedCells = occupied.size;
  const MIN_GRID_OCCUPANCY = 4;
  const distributionCorrect = occupiedCells >= MIN_GRID_OCCUPANCY;

  return { distributionCorrect, occupiedCells };
}

// Check how "filled" the drawing is inside its bounding box.
// We count number of sampled points and divide by area.
function checkDensity(points, densityType) {
  const box = getBoundingBox(points);
  if (!box) return false;
  if (box.area <= 0) return false;

  const density = points.length / box.area;

  // Loose thresholds (MVP tuning)
  if (densityType === "medium") {
    return density > 0.002;
  }

  if (densityType === "high") {
    return density > 0.004;
  }

  return true;
}

// ----------------------
// Mode switching
// ----------------------
const modes = [
  { key: "learning", section: $("modeLearning"), button: $("btnModeLearning") },
  { key: "practice", section: $("modePractice"), button: $("btnModePractice") },
  { key: "test", section: $("modeTest"), button: $("btnModeTest") },
  { key: "flashcard", section: $("modeFlashcard"), button: $("btnModeFlashcard") },
  { key: "jukugoWrite", section: $("modeJukugoWrite"), button: $("btnModeJukugoWrite") }
];

function setMode(modeKey) {
  modes.forEach((m) => {
    const isActive = m.key === modeKey;
    m.section.classList.toggle("active", isActive);
    m.button.classList.toggle("active", isActive);
  });

  // Reset canvases (and stored points) when switching modes.
  // This prevents one mode's drawing affecting another mode's evaluation.
  if (modeKey === "learning") {
    practiceDrawer.clear();
    testDrawer.clear();
    const hintBox = $("practiceHintBox");
    if (hintBox) hintBox.textContent = "";
    setText($("testResult"), "");
  }
  if (modeKey === "practice") {
    testDrawer.clear();
    setText($("testResult"), "");
  }
  if (modeKey === "test") {
    practiceDrawer.clear();
    const hintBox = $("practiceHintBox");
    if (hintBox) hintBox.textContent = "";
  }

  if (modeKey === "flashcard") {
    practiceDrawer.clear();
    testDrawer.clear();
    const hintBox = $("practiceHintBox");
    if (hintBox) hintBox.textContent = "";
    setText($("testResult"), "");
  }

  if (modeKey === "jukugoWrite") {
    practiceDrawer.clear();
    testDrawer.clear();
    const hintBox = $("practiceHintBox");
    if (hintBox) hintBox.textContent = "";
    setText($("testResult"), "");
    setText($("jukugoWriteResult"), "");
  }

  // Clear per-mode transient UI to keep behavior predictable
  if (modeKey === "practice") {
    updatePracticeStrokeMessage();
  }
  if (modeKey === "test") {
    updateTestStrokeMessage();
  }
}

// ----------------------
// Kanji dropdown + display binding
// ----------------------
function fillSelect(selectEl) {
  selectEl.innerHTML = "";
  kanjiData.forEach((k, idx) => {
    const opt = document.createElement("option");
    opt.value = String(idx);
    opt.textContent = `${k.kanji} - ${k.furigana} - ${k.meaning_id}`;
    selectEl.appendChild(opt);
  });
}

function getSelectedKanji(selectEl) {
  const idx = Number(selectEl.value);
  return kanjiData[idx];
}

function renderKanjiInfo(target, k) {
  setText(target.kanjiEl, k.kanji);
  setText(target.furiganaEl, k.furigana);
  setText(target.meaningEl, k.meaning_id);
  setText(target.strokesEl, String(k.strokes));

  // Optional fields (Learning/Practice)
  if (target.kunyomiEl) setText(target.kunyomiEl, (k.kunyomi || []).join(", "));
  if (target.onyomiEl) setText(target.onyomiEl, (k.onyomi || []).join(", "));
  if (target.bushuEl) {
    const bushuText = k.bushu ? `${k.bushu.radical} (${k.bushu.meaning_id})` : "";
    setText(target.bushuEl, bushuText);
  }
}

// ----------------------
// Pembelajaran mode (meeting-based)
// ----------------------

const learningMeetings = [
  {
    meetingId: 1,
    title: "Pertemuan 1",
    description: "Kanji pertemuan pertama",
    kanjiList: [
      {
        kanji: "平",
        onyomi: ["ヘイ", "ビョウ"],
        kunyomi: ["たい-ら", "ひら"],
        meaning: "datar, rata, damai",
        strokeCount: 5
      },
      {
        kanji: "均",
        onyomi: ["キン"],
        kunyomi: ["ひと-しい"],
        meaning: "seimbang, rata, sama",
        strokeCount: 7
      },
      {
        kanji: "寿",
        onyomi: ["ジュ"],
        kunyomi: ["ことぶき"],
        meaning: "umur panjang, selamat",
        strokeCount: 7
      },
      {
        kanji: "比",
        onyomi: ["ヒ"],
        kunyomi: ["くら-べる"],
        meaning: "membandingkan, rasio",
        strokeCount: 4
      },
      {
        kanji: "博",
        onyomi: ["ハク"],
        kunyomi: ["ひろ-い"],
        meaning: "luas, ahli, doktor",
        strokeCount: 12
      },
      {
        kanji: "胸",
        onyomi: ["キョウ"],
        kunyomi: ["むね", "むな-"],
        meaning: "dada, hati, perasaan",
        strokeCount: 10
      },
      {
        kanji: "粧",
        onyomi: ["ショウ"],
        kunyomi: ["よそお-う"],
        meaning: "berdandan, berhias",
        strokeCount: 12
      }
    ]
  }
];

const learningMeetingSelect = $("learningMeetingSelect");
const learningMeetingDescription = $("learningMeetingDescription");
const learningKanjiList = $("learningKanjiList");

let selectedMeetingId = 1;

// Practice mode elements
const practiceMeetingSelect = $("practiceMeetingSelect");
const practiceTargetKanji = $("practiceTargetKanji");
const practiceTargetOnyomi = $("practiceTargetOnyomi");
const practiceTargetKunyomi = $("practiceTargetKunyomi");
const practiceTargetMeaning = $("practiceTargetMeaning");
const practiceEmptyMsg = $("practiceEmptyMsg");
const btnPracticeNext = $("btnPracticeNext");

let practiceSelectedMeetingId = 1;
let currentKanji = null;

// (Practice) no grid toggle UI; keep overlay hidden by default
const practiceGrid = $("practiceGrid");
if (practiceGrid) practiceGrid.classList.add("hidden");

function fillLearningMeetingSelect() {
  if (!learningMeetingSelect) return;
  learningMeetingSelect.innerHTML = "";
  learningMeetings.forEach((m) => {
    const opt = document.createElement("option");
    opt.value = String(m.meetingId);
    opt.textContent = m.title;
    learningMeetingSelect.appendChild(opt);
  });
}

function renderLearningMeeting() {
  const meeting = learningMeetings.find((m) => m.meetingId === selectedMeetingId);
  if (!learningKanjiList || !learningMeetingDescription) return;
  learningKanjiList.innerHTML = "";

  if (!meeting) {
    setText(learningMeetingDescription, "");
    const empty = document.createElement("div");
    empty.className = "learning-empty";
    empty.textContent = "Kanji untuk pertemuan ini belum tersedia.";
    learningKanjiList.appendChild(empty);
    return;
  }

  setText(learningMeetingDescription, meeting.description || "");

  if (!meeting.kanjiList || meeting.kanjiList.length === 0) {
    const empty = document.createElement("div");
    empty.className = "learning-empty";
    empty.textContent = "Kanji untuk pertemuan ini belum tersedia.";
    learningKanjiList.appendChild(empty);
    return;
  }

  meeting.kanjiList.forEach((k) => {
    const block = document.createElement("div");
    block.className = "learning-kanji";

    const charEl = document.createElement("div");
    charEl.className = "learning-kanji-char";
    charEl.textContent = k.kanji;

    const meta = document.createElement("div");
    meta.className = "learning-kanji-meta";
    meta.innerHTML =
      `<div><strong>Onyomi:</strong> ${(k.onyomi || []).join(", ")}</div>` +
      `<div><strong>Kunyomi:</strong> ${(k.kunyomi || []).join(", ")}</div>` +
      `<div><strong>Arti:</strong> ${k.meaning || ""}</div>` +
      `<div><strong>Jumlah coretan:</strong> ${String(k.strokeCount ?? "")}</div>`;

    block.appendChild(charEl);
    block.appendChild(meta);
    learningKanjiList.appendChild(block);
  });
}

function initLearningMeetings() {
  if (!learningMeetingSelect || !learningKanjiList || !learningMeetingDescription) return;
  fillLearningMeetingSelect();
  selectedMeetingId = 1;
  learningMeetingSelect.value = String(selectedMeetingId);
  renderLearningMeeting();
}

if (learningMeetingSelect) {
  learningMeetingSelect.addEventListener("change", () => {
    selectedMeetingId = Number(learningMeetingSelect.value);
    renderLearningMeeting();
  });
}

// ----------------------
// Canvas drawing (shared logic)
// ----------------------
function createCanvasDrawer(canvas) {
  const ctx = canvas.getContext("2d");
  const state = {
    isDrawing: false,
    lastX: 0,
    lastY: 0,
    strokeCount: 0,
    points: [],
    strokes: [],
    currentStroke: null
  };

  // Basic pen style
  ctx.lineWidth = 10;
  ctx.lineCap = "round";
  ctx.lineJoin = "round";
  ctx.strokeStyle = "#e9ecf5";

  function getPointFromEvent(ev) {
    const rect = canvas.getBoundingClientRect();
    const clientX = ev.clientX;
    const clientY = ev.clientY;

    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;

    return {
      x: (clientX - rect.left) * scaleX,
      y: (clientY - rect.top) * scaleY
    };
  }

  function pointerDown(ev) {
    ev.preventDefault();

    const p = getPointFromEvent(ev);
    state.isDrawing = true;
    state.lastX = p.x;
    state.lastY = p.y;

    // Store points for heuristic validation (Test Mode)
    state.points.push({ x: p.x, y: p.y });

    // Store points per stroke
    state.currentStroke = [{ x: p.x, y: p.y }];
    state.strokes.push(state.currentStroke);

    // Count a new stroke at each start
    state.strokeCount += 1;

    ctx.beginPath();
    ctx.moveTo(state.lastX, state.lastY);
  }

  function pointerMove(ev) {
    if (!state.isDrawing) return;
    ev.preventDefault();

    const p = getPointFromEvent(ev);

     // Store points for heuristic validation (Test Mode)
    state.points.push({ x: p.x, y: p.y });

    // Store points per stroke
    if (state.currentStroke) state.currentStroke.push({ x: p.x, y: p.y });

    ctx.lineTo(p.x, p.y);
    ctx.stroke();

    state.lastX = p.x;
    state.lastY = p.y;
  }

  function pointerUp(ev) {
    if (!state.isDrawing) return;
    ev.preventDefault();
    state.isDrawing = false;
    state.currentStroke = null;
    ctx.closePath();
  }

  function clear() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    state.isDrawing = false;
    state.strokeCount = 0;
    state.points = [];
    state.strokes = [];
    state.currentStroke = null;
  }

  // Pointer Events = works for mouse + touch
  canvas.addEventListener("pointerdown", pointerDown);
  canvas.addEventListener("pointermove", pointerMove);
  canvas.addEventListener("pointerup", pointerUp);
  canvas.addEventListener("pointercancel", pointerUp);
  canvas.addEventListener("pointerleave", pointerUp);

  return {
    clear,
    getStrokeCount: () => state.strokeCount,
    getPoints: () => state.points,
    getStrokes: () => state.strokes
  };
}

// Optional zone check (lightweight). Only used when kanji has zones defined.
// Example rule: bottomHorizontal stroke must exist in lower 40% of bounding box.
function checkZones(points, zones) {
  if (!zones || Object.keys(zones).length === 0) return true;

  const box = getBoundingBox(points);
  if (!box || box.height <= 0 || box.width <= 0) return false;

  let ok = true;

  if (zones.bottomHorizontal) {
    const yThreshold = box.minY + box.height * 0.6;
    const bottomPoints = points.filter((p) => p.y >= yThreshold);
    if (bottomPoints.length < 10) ok = false;

    if (ok) {
      let minX = Infinity;
      let maxX = -Infinity;
      for (const p of bottomPoints) {
        if (p.x < minX) minX = p.x;
        if (p.x > maxX) maxX = p.x;
      }
      const span = maxX - minX;
      // A "horizontal" presence should cover at least some meaningful width.
      if (span < box.width * 0.35) ok = false;
    }
  }

  return ok;
}

// ----------------------
// Practice mode behavior
// ----------------------
const practiceCanvas = $("practiceCanvas");
const practiceDrawer = createCanvasDrawer(practiceCanvas);

function fillPracticeMeetingSelect() {
  if (!practiceMeetingSelect) return;
  practiceMeetingSelect.innerHTML = "";
  learningMeetings.forEach((m) => {
    const opt = document.createElement("option");
    opt.value = String(m.meetingId);
    opt.textContent = m.title;
    practiceMeetingSelect.appendChild(opt);
  });
}

function getRandomKanji(meetingId) {
  const meeting = learningMeetings.find((m) => m.meetingId === meetingId);
  if (!meeting || !meeting.kanjiList || meeting.kanjiList.length === 0) return null;
  return meeting.kanjiList[Math.floor(Math.random() * meeting.kanjiList.length)];
}

function renderPracticeTarget() {
  if (!practiceTargetKanji || !practiceTargetMeaning || !practiceEmptyMsg) return;

  if (!currentKanji) {
    setText(practiceTargetKanji, "");
    if (practiceTargetOnyomi) setText(practiceTargetOnyomi, "");
    if (practiceTargetKunyomi) setText(practiceTargetKunyomi, "");
    setText(practiceTargetMeaning, "");
    practiceEmptyMsg.classList.remove("hidden");
    practiceEmptyMsg.textContent = "Belum ada kanji untuk pertemuan ini";
    if (btnPracticeNext) btnPracticeNext.disabled = true;
    return;
  }

  practiceEmptyMsg.classList.add("hidden");
  if (btnPracticeNext) btnPracticeNext.disabled = false;
  setText(practiceTargetKanji, currentKanji.kanji);
  if (practiceTargetOnyomi) {
    const onyomi = (currentKanji.onyomi || []).join(", ");
    setText(practiceTargetOnyomi, onyomi ? `Onyomi: ${onyomi}` : "");
  }
  if (practiceTargetKunyomi) {
    const kunyomi = (currentKanji.kunyomi || []).join(", ");
    setText(practiceTargetKunyomi, kunyomi ? `Kunyomi: ${kunyomi}` : "");
  }
  setText(practiceTargetMeaning, currentKanji.meaning || "");
}

function loadNewPracticeKanji() {
  currentKanji = getRandomKanji(practiceSelectedMeetingId);
  renderPracticeTarget();
  practiceDrawer.clear();
  updatePracticeStrokeMessage();
}

function updatePracticeStrokeMessage() {
  const userStrokes = practiceDrawer.getStrokeCount();
  setText($("practiceStrokeMsg"), `Jumlah coretan kamu: ${userStrokes}`);
}

practiceCanvas.addEventListener("pointerdown", () => {
  updatePracticeStrokeMessage();
});
practiceCanvas.addEventListener("pointerup", () => {
  updatePracticeStrokeMessage();
});
practiceCanvas.addEventListener("pointercancel", () => {
  updatePracticeStrokeMessage();
});

$("btnPracticeClear").addEventListener("click", () => {
  practiceDrawer.clear();
  updatePracticeStrokeMessage();
});

if (btnPracticeNext) {
  btnPracticeNext.addEventListener("click", () => {
    loadNewPracticeKanji();
  });
}

function initPracticeMode() {
  fillPracticeMeetingSelect();
  practiceSelectedMeetingId = 1;
  if (practiceMeetingSelect) practiceMeetingSelect.value = String(practiceSelectedMeetingId);
  loadNewPracticeKanji();
}

if (practiceMeetingSelect) {
  practiceMeetingSelect.addEventListener("change", () => {
    practiceSelectedMeetingId = Number(practiceMeetingSelect.value);
    loadNewPracticeKanji();
  });
}

// ----------------------
// Test mode behavior
// ----------------------
const testCanvas = $("testCanvas");
const testDrawer = createCanvasDrawer(testCanvas);

let currentTestKanji = null;
let testFinished = false;
let testAutoTimerId = null;

function startNewTest() {
  currentTestKanji = randomItem(kanjiData);
  testFinished = false;

  setText($("testFurigana"), currentTestKanji.furigana);
  setText($("testMeaning"), currentTestKanji.meaning_id);

  testDrawer.clear();
  setText($("testResult"), "");
  updateTestStrokeMessage();
}

function reloadSameTest() {
  if (!currentTestKanji) {
    startNewTest();
    return;
  }

  testFinished = false;
  setText($("testFurigana"), currentTestKanji.furigana);
  setText($("testMeaning"), currentTestKanji.meaning);
  testDrawer.clear();
  setText($("testResult"), "");
  updateTestStrokeMessage();
}

function updateTestStrokeMessage() {
  const userStrokes = testDrawer.getStrokeCount();
  setText($("testStrokeMsg"), `Jumlah coretan kamu (ujian): ${userStrokes}`);
}

testCanvas.addEventListener("pointerdown", () => {
  updateTestStrokeMessage();
});

testCanvas.addEventListener("pointerup", () => {
  updateTestStrokeMessage();
});

$("btnTestClear").addEventListener("click", () => {
  testDrawer.clear();
  updateTestStrokeMessage();
  setText($("testResult"), "");
  testFinished = false;
});

$("btnTestNew").addEventListener("click", () => {
  startNewTest();
});

$("btnTestDone").addEventListener("click", () => {
  if (!currentTestKanji) startNewTest();

  // Prevent stacking timers / double submits
  if (testAutoTimerId) return;

  const user = testDrawer.getStrokeCount();
  const expected = currentTestKanji.strokes;

  const points = testDrawer.getPoints();

  // Canvas normalization: reject drawings that are too small
  const box = getBoundingBox(points);
  const canvasArea = testCanvas.width * testCanvas.height;
  const boxArea = box ? box.area : 0;
  const isBigEnough = boxArea >= canvasArea * 0.15;

  // We still compute ratio/density for debugging output.
  const ratio = box && box.height > 0 ? box.width / box.height : 0;
  const density = box && box.area > 0 ? points.length / box.area : 0;

  const strokeCorrect = isBigEnough && user === expected;
  const shapeCorrect = isBigEnough && checkShape(points, currentTestKanji.shape);
  const densityCorrect = isBigEnough && checkDensity(points, currentTestKanji.density);

  const { distributionCorrect: rawDistributionCorrect, occupiedCells } = checkDistribution(points);
  const distributionCorrect = isBigEnough && rawDistributionCorrect;

  const zonesDefined = currentTestKanji.zones && Object.keys(currentTestKanji.zones).length > 0;
  const zoneCorrect = zonesDefined ? (isBigEnough && checkZones(points, currentTestKanji.zones)) : true;

  // Scoring: +1 each signal. Zone check only counts when defined.
  let score = 0;
  if (strokeCorrect) score++;
  if (shapeCorrect) score++;
  if (densityCorrect) score++;
  if (distributionCorrect) score++;

  if (zonesDefined && zoneCorrect) score++;

  const requiredScore = zonesDefined ? 4 : 3;

  const isCorrect = score >= requiredScore;

  // Temporary debugging (required for tuning)
  console.log({
    strokeCorrect,
    shapeCorrect,
    densityCorrect,
    gridCorrect: distributionCorrect,
    zoneCorrect,
    score,
    occupiedCells,
    ratio,
    density
  });

  const lines = [];
  if (isCorrect) {
    lines.push("✅ Tulisan kamu sudah cukup sesuai. Bagus!");
  } else {
    if (!isBigEnough) {
      lines.push("❌ Tulisan kamu masih terlalu kecil. Coba tulis lebih besar ya.");
    } else {
      lines.push("❌ Bentuk atau proporsi kanji masih kurang tepat. Coba lagi ya.");
    }
  }

  lines.push(`Kanji yang benar: ${currentTestKanji.kanji}`);

  setText($("testResult"), lines.join("\n"));

  testFinished = true;

  // UX auto behavior (strict):
  // - If correct: wait 700ms then clear + next kanji
  // - If wrong: wait 1000ms then clear + same kanji
  const waitMs = isCorrect ? 700 : 1000;
  testAutoTimerId = window.setTimeout(() => {
    testAutoTimerId = null;
    if (isCorrect) {
      startNewTest();
    } else {
      reloadSameTest();
    }
  }, waitMs);
});

// ----------------------
// Wire up mode buttons + init
// ----------------------
$("btnModeLearning").addEventListener("click", () => {
  setMode("learning");
  initLearningMeetings();
});
$("btnModePractice").addEventListener("click", () => {
  setMode("practice");
  initPracticeMode();
});
$("btnModeTest").addEventListener("click", () => {
  setMode("test");
  // Ensure test has a kanji ready every time you enter
  startNewTest();
});

$("btnModeFlashcard").addEventListener("click", () => {
  setMode("flashcard");
  initFlashcardMode();
});

$("btnModeJukugoWrite").addEventListener("click", () => {
  setMode("jukugoWrite");
  initJukugoWriteMode();
});

// Reuse existing evaluation logic for multi-kanji writing.
// NOTE: thresholds are unchanged; only stroke count gets a small tolerance (±1) in this advanced mode.
function evaluateKanjiAttemptFromData(k, points, strokeCount, canvasAreaForNormalization) {
  const expected = k.strokes;

  const box = getBoundingBox(points);
  const boxArea = box ? box.area : 0;
  const isBigEnough = boxArea >= canvasAreaForNormalization * 0.15;

  const ratio = box && box.height > 0 ? box.width / box.height : 0;
  const density = box && box.area > 0 ? points.length / box.area : 0;

  // Small tolerance for multi-kanji writing: allow ±1 stroke
  const strokeCorrect = isBigEnough && Math.abs(strokeCount - expected) <= 1;
  const shapeCorrect = isBigEnough && checkShape(points, k.shape);
  const densityCorrect = isBigEnough && checkDensity(points, k.density);

  const { distributionCorrect: rawDistributionCorrect } = checkDistribution(points);
  const gridCorrect = isBigEnough && rawDistributionCorrect;

  const zonesDefined = k.zones && Object.keys(k.zones).length > 0;
  const zoneCorrect = zonesDefined ? (isBigEnough && checkZones(points, k.zones)) : true;

  let score = 0;
  if (strokeCorrect) score++;
  if (shapeCorrect) score++;
  if (densityCorrect) score++;
  if (gridCorrect) score++;
  if (zonesDefined && zoneCorrect) score++;

  const requiredScore = zonesDefined ? 4 : 3;
  const isCorrect = score >= requiredScore;

  return {
    isCorrect,
    isBigEnough,
    strokeCorrect,
    shapeCorrect,
    densityCorrect,
    gridCorrect,
    zoneCorrect,
    score,
    ratio,
    density
  };
}

// ----------------------
// Flashcard mode
// ----------------------

const flashcardCard = $("flashcardCard");
const flashcardInner = $("flashcardInner");
const flashcardFrontMain = $("flashcardFrontMain");
const flashcardBackMain = $("flashcardBackMain");
const flashcardBackReading = $("flashcardBackReading");
const flashcardBackMeaning = $("flashcardBackMeaning");
const flashcardBackDetails = $("flashcardBackDetails");
const flashcardCta = $("flashcardCta");
const btnFlashcardWriteJukugo = $("btnFlashcardWriteJukugo");
const flashcardFilterJukugo = $("flashcardFilterJukugo");
const flashcardFilterKanji = $("flashcardFilterKanji");
const btnFlashcardDetail = $("btnFlashcardDetail");

let flashcardIsFlipped = false;
let flashcardDetailOn = false;
let flashcardAllCards = [];
let flashcardQueue = [];
let flashcardCurrentIndex = 0;
let flashcardAdvanceTimerId = null;
const flashcardMarks = {};

function shuffleInPlace(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
}

function buildFlashcardItemsFromData() {
  const items = [];

  // Primary focus: jukugo
  jukugoData.forEach((j, idx) => {
    const breakdown = (j.kanji || []).map((ch) => {
      const k = kanjiMap[ch];
      return { kanji: ch, meaning: k ? k.meaning_id : "" };
    });

    /** @type {{id:string,type:"jukugo"|"kanji",text:string,reading:string,meaning:string,breakdown?:{kanji:string,meaning:string}[],notes?:string}} */
    const item = {
      id: `jukugo-${idx + 1}`,
      type: "jukugo",
      text: j.jukugo,
      reading: j.reading,
      meaning: j.meaning_id
    };
    if (breakdown.length) item.breakdown = breakdown;
    items.push(item);
  });

  // Temporary support: kanji
  kanjiData.forEach((k, idx) => {
    items.push({
      id: `kanji-${idx + 1}`,
      type: "kanji",
      text: k.kanji,
      reading: k.furigana || "",
      meaning: k.meaning_id
    });
  });

  return items;
}

function isFlashcardModeActive() {
  const section = $("modeFlashcard");
  return !!section && section.classList.contains("active");
}

function setFlashcardFlip(nextFlipped) {
  flashcardIsFlipped = nextFlipped;
  flashcardInner.classList.toggle("flipped", flashcardIsFlipped);
}

function setFlashcardDetail(nextOn) {
  flashcardDetailOn = nextOn;
  flashcardBackDetails.classList.toggle("hidden", !flashcardDetailOn);
}

function applyFlashcardFilterAndShuffle() {
  const filter = [];
  if (flashcardFilterJukugo.checked) filter.push("jukugo");
  if (flashcardFilterKanji.checked) filter.push("kanji");

  // Prevent empty filter state (keep deterministic + no dead screen)
  if (!filter.length) {
    flashcardFilterJukugo.checked = true;
    filter.push("jukugo");
  }

  flashcardQueue = flashcardAllCards.filter((c) => filter.includes(c.type));
  shuffleInPlace(flashcardQueue);
  flashcardCurrentIndex = 0;
}

function getCurrentFlashcard() {
  if (!flashcardQueue.length) return null;
  const idx = ((flashcardCurrentIndex % flashcardQueue.length) + flashcardQueue.length) % flashcardQueue.length;
  return flashcardQueue[idx];
}

function renderFlashcard(card) {
  setFlashcardFlip(false);
  setFlashcardDetail(false);

  if (!card) return;

  // Front: text only
  setText(flashcardFrontMain, card.text);

  // Back: minimal meta + optional details
  setText(flashcardBackMain, card.text);
  setText(flashcardBackReading, card.reading ? `Reading: ${card.reading}` : "");
  setText(flashcardBackMeaning, card.meaning ? `Arti: ${card.meaning}` : "");

  if (card.type === "jukugo") {
    flashcardCta.classList.remove("hidden");
  } else {
    flashcardCta.classList.add("hidden");
  }

  if (card.breakdown && card.breakdown.length) {
    const rows = card.breakdown.map((b) => `${b.kanji} → ${b.meaning}`).join("<br>");
    flashcardBackDetails.innerHTML = `<div><strong>Breakdown:</strong><br>${rows}</div>`;
    btnFlashcardDetail.disabled = false;
  } else {
    flashcardBackDetails.innerHTML = "";
    btnFlashcardDetail.disabled = true;
  }
}

function goNextFlashcardAfterDelay() {
  if (flashcardAdvanceTimerId) return;
  flashcardAdvanceTimerId = window.setTimeout(() => {
    flashcardAdvanceTimerId = null;
    flashcardCurrentIndex += 1;
    renderFlashcard(getCurrentFlashcard());
  }, 300);
}

function answerFlashcardExposure(mark) {
  const card = getCurrentFlashcard();
  if (!card) return;

  flashcardMarks[card.id] = mark;
  goNextFlashcardAfterDelay();
}

function initFlashcardMode() {
  if (!flashcardAllCards.length) {
    flashcardAllCards = buildFlashcardItemsFromData();
    applyFlashcardFilterAndShuffle();
  }
  renderFlashcard(getCurrentFlashcard());
}

flashcardCard.addEventListener("click", () => {
  setFlashcardFlip(!flashcardIsFlipped);
});

$("btnFlashcardBelumTahu").addEventListener("click", () => answerFlashcardExposure("belum_tahu"));
$("btnFlashcardTahu").addEventListener("click", () => answerFlashcardExposure("tahu"));

btnFlashcardDetail.addEventListener("click", (ev) => {
  ev.stopPropagation();
  setFlashcardDetail(!flashcardDetailOn);
});

flashcardFilterJukugo.addEventListener("change", () => {
  flashcardAllCards = buildFlashcardItemsFromData();
  applyFlashcardFilterAndShuffle();
  renderFlashcard(getCurrentFlashcard());
});

flashcardFilterKanji.addEventListener("change", () => {
  flashcardAllCards = buildFlashcardItemsFromData();
  applyFlashcardFilterAndShuffle();
  renderFlashcard(getCurrentFlashcard());
});

window.addEventListener("keydown", (ev) => {
  if (!isFlashcardModeActive()) return;

  if (ev.code === "Space") {
    ev.preventDefault();
    setFlashcardFlip(!flashcardIsFlipped);
    return;
  }
});

btnFlashcardWriteJukugo.addEventListener("click", () => {
  const card = getCurrentFlashcard();
  if (!card || card.type !== "jukugo") return;
  const idx = jukugoData.findIndex((j) => j.jukugo === card.text);
  if (idx < 0) return;

  setMode("jukugoWrite");
  jukugoWriteSelect.value = String(idx);
  jukugoWriteIndex = idx;
  loadJukugoWrite(idx);
});

// ----------------------
// Jukugo writing mode (multi-kanji single wide canvas)
// ----------------------

const jukugoWriteSelect = $("jukugoWriteSelect");
const jukugoWriteCanvas = $("jukugoWriteCanvas");
const jukugoWriteGuides = $("jukugoWriteGuides");
const jukugoWriteInnerGrid = $("jukugoWriteInnerGrid");
const jukugoWriteHighlight = $("jukugoWriteHighlight");

const jukugoWriteDrawer = createCanvasDrawer(jukugoWriteCanvas);

let jukugoWriteIndex = 0;
let jukugoWriteAutoTimerId = null;
let currentJukugoWriteBoxCount = 1;

function fillJukugoWriteSelect() {
  jukugoWriteSelect.innerHTML = "";
  jukugoData.forEach((j, idx) => {
    const opt = document.createElement("option");
    opt.value = String(idx);
    opt.textContent = `${j.jukugo} - ${j.reading} - ${j.meaning_id}`;
    jukugoWriteSelect.appendChild(opt);
  });
}

function updateJukugoWriteStrokeMessage() {
  const userStrokes = jukugoWriteDrawer.getStrokeCount();
  setText($("jukugoWriteStrokeMsg"), `Jumlah coretan kamu: ${userStrokes}`);
}

function setJukugoWriteGuidesEnabled(enabled) {
  jukugoWriteGuides.classList.toggle("hidden", !enabled);
  if (!enabled) {
    jukugoWriteInnerGrid.classList.add("hidden");
  } else {
    const innerOn = $("jukugoWriteInnerGridToggle").checked;
    jukugoWriteInnerGrid.classList.toggle("hidden", !innerOn);
  }
}

function setJukugoWriteInnerGridEnabled(enabled) {
  if (!$("jukugoWriteGuideToggle").checked) {
    jukugoWriteInnerGrid.classList.add("hidden");
    return;
  }
  jukugoWriteInnerGrid.classList.toggle("hidden", !enabled);
}

function setJukugoWriteCanvasForKanjiCount(count) {
  const BOX_SIZE = 360;
  currentJukugoWriteBoxCount = count;

  jukugoWriteCanvas.width = BOX_SIZE * count;
  jukugoWriteCanvas.height = 360;

  // Vertical dotted divider lines (visual only)
  if (count <= 1) {
    jukugoWriteGuides.style.backgroundImage = "none";
    jukugoWriteGuides.style.webkitMaskImage = "none";
    jukugoWriteGuides.style.maskImage = "none";
    jukugoWriteInnerGrid.style.backgroundImage = "none";
    return;
  }

  jukugoWriteGuides.style.backgroundImage =
    "repeating-linear-gradient(to right, transparent 0 calc(100%/var(--boxCount) - 1px), rgba(233, 236, 245, 0.35) calc(100%/var(--boxCount) - 1px) calc(100%/var(--boxCount)))";
  jukugoWriteGuides.style.backgroundSize = "auto";
  jukugoWriteGuides.style.backgroundPosition = "0 0";
  jukugoWriteGuides.style.setProperty("--boxCount", String(count));
  jukugoWriteGuides.style.webkitMaskImage =
    "repeating-linear-gradient(to bottom, rgba(0,0,0,1) 0 2px, rgba(0,0,0,0) 2px 10px)";
  jukugoWriteGuides.style.maskImage =
    "repeating-linear-gradient(to bottom, rgba(0,0,0,1) 0 2px, rgba(0,0,0,0) 2px 10px)";

  // Optional faint 3x3 grid inside each sub-box
  // We draw a global grid with 3*count columns and 3 rows.
  jukugoWriteInnerGrid.style.backgroundImage =
    "linear-gradient(to right, rgba(233, 236, 245, 0.16) 1px, transparent 1px), linear-gradient(to bottom, rgba(233, 236, 245, 0.16) 1px, transparent 1px)";
  jukugoWriteInnerGrid.style.backgroundSize =
    `calc(100% / ${count * 3}) 100%, 100% calc(100% / 3)`;
}

function clearJukugoWriteHighlight() {
  jukugoWriteHighlight.classList.add("hidden");
  jukugoWriteHighlight.classList.remove("show");
}

function highlightJukugoWriteBox(boxIndex) {
  const N = currentJukugoWriteBoxCount;
  if (N <= 0) return;

  const leftPercent = (boxIndex / N) * 100;
  const widthPercent = (1 / N) * 100;

  jukugoWriteHighlight.style.left = `${leftPercent}%`;
  jukugoWriteHighlight.style.width = `${widthPercent}%`;
  jukugoWriteHighlight.style.right = "auto";

  jukugoWriteHighlight.classList.remove("hidden");
  // trigger show transition
  window.requestAnimationFrame(() => {
    jukugoWriteHighlight.classList.add("show");
  });
}

function loadJukugoWrite(idx) {
  const j = jukugoData[idx];
  const N = j.kanji.length;

  setText($("jukugoWriteHint"), `Tulis ${N} kanji dalam satu kata (dibagi menjadi ${N} kotak).`);
  setJukugoWriteCanvasForKanjiCount(N);

  jukugoWriteDrawer.clear();
  clearJukugoWriteHighlight();
  setText($("jukugoWriteResult"), "");
  updateJukugoWriteStrokeMessage();

  // Apply guidance toggles
  setJukugoWriteGuidesEnabled($("jukugoWriteGuideToggle").checked);
  setJukugoWriteInnerGridEnabled($("jukugoWriteInnerGridToggle").checked);
}

function initJukugoWriteMode() {
  if (!jukugoWriteSelect.options.length) fillJukugoWriteSelect();
  if (jukugoWriteSelect.value === "") jukugoWriteSelect.value = "0";

  jukugoWriteIndex = Number(jukugoWriteSelect.value);
  loadJukugoWrite(jukugoWriteIndex);
}

jukugoWriteSelect.addEventListener("change", () => {
  if (jukugoWriteAutoTimerId) return;
  jukugoWriteIndex = Number(jukugoWriteSelect.value);
  loadJukugoWrite(jukugoWriteIndex);
});

$("jukugoWriteGuideToggle").addEventListener("change", (ev) => {
  setJukugoWriteGuidesEnabled(ev.target.checked);
});

$("jukugoWriteInnerGridToggle").addEventListener("change", (ev) => {
  setJukugoWriteInnerGridEnabled(ev.target.checked);
});

jukugoWriteCanvas.addEventListener("pointerdown", updateJukugoWriteStrokeMessage);
jukugoWriteCanvas.addEventListener("pointerup", updateJukugoWriteStrokeMessage);
jukugoWriteCanvas.addEventListener("pointercancel", updateJukugoWriteStrokeMessage);

$("btnJukugoWriteClear").addEventListener("click", () => {
  if (jukugoWriteAutoTimerId) return;
  jukugoWriteDrawer.clear();
  clearJukugoWriteHighlight();
  updateJukugoWriteStrokeMessage();
  setText($("jukugoWriteResult"), "");
});

function assignStrokesToBoxes(strokes, boxWidth, boxCount) {
  const assigned = Array.from({ length: boxCount }, () => ({ strokes: [], points: [] }));

  for (const stroke of strokes) {
    if (!stroke || stroke.length === 0) continue;
    let sumX = 0;
    for (const p of stroke) sumX += p.x;
    const avgX = sumX / stroke.length;

    let idx = Math.floor(avgX / boxWidth);
    if (idx < 0) idx = 0;
    if (idx >= boxCount) idx = boxCount - 1;

    assigned[idx].strokes.push(stroke);
    assigned[idx].points.push(...stroke);
  }

  return assigned;
}

$("btnJukugoWriteDone").addEventListener("click", () => {
  if (jukugoWriteAutoTimerId) return;

  const j = jukugoData[jukugoWriteIndex];
  const N = j.kanji.length;
  const boxWidth = jukugoWriteCanvas.width / N;
  const perBoxCanvasArea = boxWidth * jukugoWriteCanvas.height;

  const strokes = jukugoWriteDrawer.getStrokes();
  const assigned = assignStrokesToBoxes(strokes, boxWidth, N);

  const results = [];
  for (let kanjiIndex = 0; kanjiIndex < N; kanjiIndex++) {
    const kanjiChar = j.kanji[kanjiIndex];
    const k = kanjiMap[kanjiChar];
    const points = assigned[kanjiIndex].points;
    const strokeCount = assigned[kanjiIndex].strokes.length;

    const evalRes = evaluateKanjiAttemptFromData(k, points, strokeCount, perBoxCanvasArea);

    // Temporary debug (required)
    console.log({
      kanji: kanjiChar,
      strokes: strokeCount,
      shape: evalRes.shapeCorrect,
      density: evalRes.densityCorrect,
      grid: evalRes.gridCorrect,
      zone: evalRes.zoneCorrect,
      score: evalRes.score
    });

    results.push(evalRes);
  }

  const jukugoCorrect = results.every((r) => r.isCorrect);

  clearJukugoWriteHighlight();

  if (jukugoCorrect) {
    setText($("jukugoWriteResult"), "✅ Jukugo kamu sudah cukup sesuai. Bagus!");
  } else {
    const firstFailIndex = results.findIndex((r) => !r.isCorrect);
    setText($("jukugoWriteResult"), `❌ Kanji ke-${firstFailIndex + 1} belum tepat.`);
    highlightJukugoWriteBox(firstFailIndex);
  }

  const waitMs = jukugoCorrect ? 700 : 1000;
  jukugoWriteAutoTimerId = window.setTimeout(() => {
    jukugoWriteAutoTimerId = null;
    if (jukugoCorrect) {
      jukugoWriteIndex = (jukugoWriteIndex + 1) % jukugoData.length;
      jukugoWriteSelect.value = String(jukugoWriteIndex);
    }
    loadJukugoWrite(jukugoWriteIndex);
  }, waitMs);
});

initLearningMeetings();
startNewTest();

// Start app in Learning mode
setMode("learning");
