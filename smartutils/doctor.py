def run_doctor():
    import sys
    import os
    import platform
    import requests

    print("🩺 smartutils doctor report\n")

    print(f"✔ Python version: {platform.python_version()}")
    print(f"✔ SMARTUTILS_LOG: {'ON' if os.getenv('SMARTUTILS_LOG', '1') == '1' else 'OFF'}")

    try:
        import requests
        print("✔ requests installed")
    except ImportError:
        print("✖ requests NOT installed")

    # 🌐 Network check (SAFE)
    try:
        requests.get("https://httpbin.org/get", timeout=3)
        print("✔ Internet access: OK")
    except Exception as e:
        print("⚠ Internet access: FAILED (this is OK)")
        print(f"  Reason: {e.__class__.__name__}")

    print("\n✅ Doctor check complete")
