import sys
from engine.runner import run_simulation
from engine.replay import replay_logs

def main():
    if len(sys.argv) < 2:
        print("Usage: cli.py [run <scenario_id> | replay]")
        return

    cmd = sys.argv[1]
    if cmd == "run" and len(sys.argv) == 3:
        run_simulation(sys.argv[2])
    elif cmd == "replay":
        replay_logs()
    else:
        print("[ERROR] Invalid command.")

if __name__ == "__main__":
    main()
