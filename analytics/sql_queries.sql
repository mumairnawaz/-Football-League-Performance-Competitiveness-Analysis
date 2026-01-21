--  How many matches were analyzed per competition & seasonSELECT
  competition,
  season,
  COUNT(*) AS total_matches
FROM fact_matches
GROUP BY competition, season
ORDER BY competition, season;

-- How many matches were analyzed per competition & season

SELECT
  competition,
  season,
  ROUND(AVG(home_goals + away_goals), 2) AS avg_goals_per_match
FROM fact_matches
GROUP BY competition, season
ORDER BY avg_goals_per_match DESC;

-- Home vs Away scoring balance

SELECT
  competition,
  season,
  SUM(home_goals) AS home_goals,
  SUM(away_goals) AS away_goals,
  ROUND(SUM(home_goals) * 1.0 / NULLIF(SUM(away_goals),0), 2) AS home_away_ratio
FROM fact_matches
GROUP BY competition, season;

-- Which teams are the most dominant
SELECT
  competition,
  season,
  team,
  goal_difference
FROM team_performance
ORDER BY goal_difference DESC
LIMIT 10;

-- Competitive balance by league

SELECT
  competition,
  season,
  ROUND(STDDEV(goal_difference), 2) AS goal_diff_variability
FROM team_performance
GROUP BY competition, season;

-- Are leagues becoming more defensive or offensive over time

SELECT
  competition,
  season,
  ROUND(AVG(home_goals + away_goals), 2) AS avg_goals
FROM fact_matches
GROUP BY competition, season
ORDER BY competition, season;


-- Which teams rely heavily on scoring vs defending
SELECT
  team,
  SUM(goals_for) AS goals_scored,
  SUM(goals_against) AS goals_conceded,
  SUM(goal_difference) AS net_goal_difference
FROM team_performance
GROUP BY team
ORDER BY net_goal_difference DESC
LIMIT 10;

-- Contribution of top teams to total league goals

SELECT
  competition,
  season,
  ROUND(SUM(goals_for) * 100.0 /
        SUM(SUM(goals_for)) OVER (PARTITION BY competition, season), 2)
        AS team_goal_share_percent,
  team
FROM team_performance
ORDER BY team_goal_share_percent DESC
LIMIT 10;

-- Match outcome distribution

SELECT
  competition,
  season,
  SUM(CASE WHEN home_goals = away_goals THEN 1 ELSE 0 END) AS draws,
  COUNT(*) AS total_matches,
  ROUND(
    SUM(CASE WHEN home_goals = away_goals THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2
  ) AS draw_percentage
FROM fact_matches
GROUP BY competition, season;


-- Which competition delivers the highest overall goal volume
SELECT
  competition,
  season,
  SUM(home_goals + away_goals) AS total_goals
FROM fact_matches
GROUP BY competition, season
ORDER BY total_goals DESC;