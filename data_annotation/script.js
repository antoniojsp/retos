// Get references to HTML elements
const display = document.getElementById("display");
const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const resetBtn = document.getElementById("resetBtn");

const lapBtn = document.getElementById("lapBtn");
const lapsList = document.getElementById("laps");

let startTime = 0;
let elapsedTime = 0;
let timerInterval;

// Function to format time components (hours, minutes, seconds)
function formatTime(time) {
  const hours = Math.floor(time / 3600000); // 3600000 ms in an hour
  const minutes = Math.floor((time % 3600000) / 60000); // 60000 ms in a minute
  const seconds = Math.floor((time % 60000) / 1000);
  return `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`;
}

// Function to add leading zero if needed (e.g., "9" becomes "09")
function pad(number) {
  return number < 10 ? "0" + number : number;
}

// Start button click handler
startBtn.addEventListener("click", () => {
  startTime = Date.now() - elapsedTime;
  timerInterval = setInterval(() => {
    elapsedTime = Date.now() - startTime;
    display.textContent = formatTime(elapsedTime);
  }, 10);
});

// Stop button click handler
stopBtn.addEventListener("click", () => {
  clearInterval(timerInterval);
});

// Reset button click handler
resetBtn.addEventListener("click", () => {
  clearInterval(timerInterval);
  elapsedTime = 0;
  display.textContent = "00:00:00";
});

function recordLap() {
  const lapTime = formatTime(elapsedTime);
  const lapItem = document.createElement("li");
  lapItem.textContent = lapTime;
  lapsList.appendChild(lapItem);
}

lapBtn.addEventListener("click", recordLap);