import json
import pandas as pd
from pathlib import Path

# =========================
# PATHS
# =========================
BRONZE_PATH = Path("data/bronze/matches")
SILVER_PATH = Path("data/silver/matches")
SILVER_PATH.mkdir(parents=True, exist_ok=True)

# =========================
# LOAD ALL BRONZE FILES
# =========================
records = []

files = list(BRONZE_PATH.glob("*.json"))
print(f"📂 Bronze files found: {len(files)}")

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    competition = data.get("competition")
    season = data.get("season")
    matches = data.get("matches", [])

    print(f"⚽ {competition} {season} → {len(matches)} matches")

    for m in matches:
        records.append({
            "match_id": m["id"],
            "competition": competition,
            "season": season,
            "utc_date": m["utcDate"],
            "status": m["status"],
            "matchday": m.get("matchday"),

            "home_team_id": m["homeTeam"]["id"],
            "home_team": m["homeTeam"]["name"],
            "away_team_id": m["awayTeam"]["id"],
            "away_team": m["awayTeam"]["name"],

            "home_goals": m["score"]["fullTime"]["home"],
            "away_goals": m["score"]["fullTime"]["away"]
        })

# =========================
# CREATE DATAFRAME
# =========================
df = pd.DataFrame(records)
print(f"Silver DataFrame shape: {df.shape}")

# =========================
# SAVE TO SILVER
# =========================
output_file = SILVER_PATH / "matches_clean.parquet"
df.to_parquet(output_file, index=False)

print(f"Silver matches saved → {output_file}")