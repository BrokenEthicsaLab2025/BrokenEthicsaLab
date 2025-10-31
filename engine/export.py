import csv

def export_csv(telemetry, score):
    with open("terminal/logs/simulation_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            telemetry["uuid"],
            telemetry["timestamp"],
            ",".join(telemetry["techniques"]),
            telemetry["status"],
            score
        ])
