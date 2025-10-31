from engine.runner import run_simulation

def test_run_valid():
    run_simulation("T1055_POS_01")

def test_run_invalid():
    run_simulation("INVALID_ID")
