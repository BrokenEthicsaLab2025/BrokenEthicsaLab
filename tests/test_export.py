from engine.export import export_csv

def test_export():
    telemetry = {
        "uuid": "T1055_POS_01",
        "techniques": ["T1210", "T1055", "T1574"],
        "timestamp": 1234567890,
        "status": "executed"
    }
    score = 90
    export_csv(telemetry, score)
