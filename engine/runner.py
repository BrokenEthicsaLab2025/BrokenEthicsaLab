import json
import time
from engine.scoring import score_simulation
from engine.export import export_csv

def run_simulation(scenario_id):
    with open("config/scenarios.json") as f:
        scenarios = json.load(f)
    scenario = scenarios.get(scenario_id)
    if not scenario:
        print(f"[ERROR] Scenario {scenario_id} not found.")
        return

    print(f"[RUNNING] {scenario['name']} ({scenario_id})")
    time.sleep(1)
    telemetry = {
        "uuid": scenario_id,
        "techniques": scenario["mitre_chain"],
        "timestamp": time.time(),
        "status": "executed"
    }

    score = score_simulation(telemetry)
    export_csv(telemetry, score)
    print(f"[COMPLETE] Simulation {scenario_id} finished. Score: {score}")
