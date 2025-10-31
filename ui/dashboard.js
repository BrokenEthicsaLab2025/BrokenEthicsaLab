function runScenario() {
  const scenarioId = document.getElementById("scenarioInput").value;
  const logText = document.getElementById("logText");
  if (!scenarioId) {
    logText.textContent = "Please enter a scenario ID.";
    return;
  }

  logText.textContent = `[RUNNING] ${scenarioId}...\n[COMPLETE] Simulation finished. Score: 90`;
}

function replayLogs() {
  const logText = document.getElementById("logText");
  logText.textContent = `[REPLAY] UUID: T1055_POS_01 | Techniques: T1210,T1055,T1574 | Score: 90\n[REPLAY] UUID: T1574_POS_02 | Techniques: T1574 | Score: 30`;
}
