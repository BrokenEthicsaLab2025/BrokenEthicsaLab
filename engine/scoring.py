def score_simulation(telemetry):
    techniques = telemetry.get("techniques", [])
    score = 0
    for t in techniques:
        if t in ["T1210", "T1055", "T1574"]:
            score += 30
        else:
            score += 10
    return min(score, 100)
