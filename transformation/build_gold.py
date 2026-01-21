import pandas as pd
from pathlib import Path

# =========================
# PATHS
# =========================
SILVER_FILE = Path("data/silver/matches/matches_clean.parquet")
GOLD_PATH = Path("data/gold")
GOLD_PATH.mkdir(parents=True, exist_ok=True)

# =========================
# LOAD SILVER
# =========================
df = pd.read_parquet(SILVER_FILE)
print("Silver loaded:", df.shape)

# =========================
# FACT MATCHES
# =========================
fact_matches = df.copy()
fact_matches["total_goals"] = fact_matches["home_goals"] + fact_matches["away_goals"]

print("fact_matches rows:", len(fact_matches))

if len(fact_matches) > 0:
    fact_matches.to_parquet(GOLD_PATH / "fact_matches.parquet", index=False)

# =========================
# LEAGUE KPIs
# =========================
league_kpis = (
    df.groupby(["competition", "season"])
      .agg(
          total_matches=("match_id", "count"),
          total_home_goals=("home_goals", "sum"),
          total_away_goals=("away_goals", "sum")
      )
      .reset_index()
)

league_kpis["total_goals"] = (
    league_kpis["total_home_goals"] + league_kpis["total_away_goals"]
)
league_kpis["avg_goals_per_match"] = (
    league_kpis["total_goals"] / league_kpis["total_matches"]
)

print("league_kpis rows:", len(league_kpis))

if len(league_kpis) > 0:
    league_kpis.to_parquet(GOLD_PATH / "league_kpis.parquet", index=False)

# =========================
# TEAM PERFORMANCE
# =========================
home = df[[
    "competition", "season",
    "home_team", "home_goals", "away_goals"
]].copy()

home.columns = [
    "competition", "season",
    "team", "goals_for", "goals_against"
]

away = df[[
    "competition", "season",
    "away_team", "away_goals", "home_goals"
]].copy()

away.columns = [
    "competition", "season",
    "team", "goals_for", "goals_against"
]

teams = pd.concat([home, away], ignore_index=True)

team_performance = (
    teams.groupby(["competition", "season", "team"])
         .agg(
             matches_played=("team", "count"),
             goals_for=("goals_for", "sum"),
             goals_against=("goals_against", "sum")
         )
         .reset_index()
)

team_performance["goal_difference"] = (
    team_performance["goals_for"] - team_performance["goals_against"]
)

print("team_performance rows:", len(team_performance))

if len(team_performance) > 0:
    team_performance.to_parquet(
        GOLD_PATH / "team_performance.parquet",
        index=False
    )

print("🏆 Gold layer successfully rebuilt")