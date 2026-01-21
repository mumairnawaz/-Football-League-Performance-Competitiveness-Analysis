import requests
import json
import time
from pathlib import Path
from datetime import datetime

# =========================
# CONFIG
# =========================
API_TOKEN = "21df38ed000f43768930ad49b5ff5aba"  # keep local, DO NOT push to GitHub
BASE_URL = "https://api.football-data.org/v4/competitions"

COMPETITIONS = {
    "CL": {
        "name": "champions_league",
        "seasons": [2024, 2025]
    },
    "PL": {
        "name": "premier_league",
        "seasons": [2024, 2025]
    },
    "PD": {
        "name": "laliga",
        "seasons": [2024, 2025]
    }
}

HEADERS = {
    "X-Auth-Token": API_TOKEN
}

# =========================
# PATHS
# =========================
BRONZE_PATH = Path("data/bronze/matches")
BRONZE_PATH.mkdir(parents=True, exist_ok=True)

# =========================
# INGESTION LOGIC
# =========================
for comp_code, cfg in COMPETITIONS.items():
    for season in cfg["seasons"]:
        print(f"\n📥 Fetching {cfg['name'].upper()} | Season {season}")

        url = f"{BASE_URL}/{comp_code}/matches"
        params = {"season": season}

        response = requests.get(url, headers=HEADERS, params=params)

        if response.status_code != 200:
            print(f"Failed {comp_code} {season} → {response.status_code}")
            print(response.text[:200])
            time.sleep(30)
            continue

        data = response.json()
        matches = data.get("matches", [])

        print(f"Matches received: {len(matches)}")

        output = {
            "competition": comp_code,
            "season": season,
            "matches": matches
        }

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = BRONZE_PATH / f"{comp_code}_{season}_matches_{timestamp}.json"

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2)

        print(f"💾 Saved → {file_path}")

        # VERY IMPORTANT: Free API throttle
        time.sleep(25)