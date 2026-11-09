import subprocess
import time
import urllib.request
import json
import sys

def probe_server():
    print("Starting server process...")
    proc = subprocess.Popen([sys.executable, "backend/app/main.py"])
    time.sleep(3)
    try:
        # Probe Health
        with urllib.request.urlopen("http://127.0.0.1:8000/api/health") as response:
            health = json.loads(response.read().decode())
            print("Health Check Response:", health)
            assert health["status"] == "online"

        # Probe Flows
        with urllib.request.urlopen("http://127.0.0.1:8000/api/flows") as response:
            flows = json.loads(response.read().decode())
            print("Verified Flows Count:", len(flows["flows"]))
            for f in flows["flows"]:
                print(f" - {f['app_name']}: {f['intent']} ({', '.join(f['available_languages'])})")

        # Probe Frontend HTML
        with urllib.request.urlopen("http://127.0.0.1:8000/") as response:
            html = response.read().decode()
            print("Frontend HTML length:", len(html))
            assert "<title>Sahayak AI" in html
            print("Frontend HTML served with correct title!")

        print("\nALL SERVER ENDPOINTS PROBED SUCCESSFULLY!")
    finally:
        print("Stopping server process...")
        proc.terminate()
        proc.wait(timeout=5)

if __name__ == "__main__":
    probe_server()

