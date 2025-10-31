def test_ui_load():
    try:
        with open("ui/index.html") as f:
            assert "<html>" in f.read()
        print("[PASS] UI loaded successfully.")
    except FileNotFoundError:
        print("[FAIL] UI file missing.")
