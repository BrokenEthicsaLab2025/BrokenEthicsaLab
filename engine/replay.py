import csv
import time

def replay_logs():
    try:
        with open("terminal/logs/simulation_log.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                print(f"[REPLAY] UUID: {row[0]} | Techniques: {row[2]} | Score: {row[4]}")
                time.sleep(0.5)
    except FileNotFoundError:
        print("[ERROR] No logs found.")
