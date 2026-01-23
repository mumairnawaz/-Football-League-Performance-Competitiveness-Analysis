# football-league-performance-analysis

---

## Table of Contents

> - [Background](#background)
> - [Executive Summary](#executive-summary)
> - [Project Objective](#project-objective)
> - [Data Architecture & Methodology](#data-architecture--methodology)
> - [Business Insights](#business-insights)
>   - [Scoring Intensity Across Competitions](#scoring-intensity-across-competitions)
>   - [Home Advantage Is Structural](#home-advantage-is-structural)
>   - [Competitive Balance by League](#competitive-balance-by-league)
>   - [Scoring Volatility in Champions League](#scoring-volatility-in-champions-league)
> - [Strategic Recommendations](#strategic-recommendations)
> - [Analytics Deliverables](#analytics-deliverables)
> - [Tools & Analytics Stack](#tools--analytics-stack)
> - [Final Outcome](#final-outcome)

---

<table width="90%" align="center">
<tr><td>

# Background

Modern football has evolved into a data-driven commercial ecosystem. Broadcasting rights, sponsorship deals, player valuation, and fan engagement are increasingly influenced by league competitiveness, scoring behavior, and performance concentration.

Despite the availability of large volumes of football data, many analyses remain:
- Match-centric rather than decision-centric
- Descriptive instead of strategic
- Disconnected from how analytics systems operate in real organizations

In real business environments, decision-makers rarely work with static datasets. Instead, data is retrieved dynamically from external sources, ingested via APIs, and processed through analytics pipelines before insights are delivered.

This project was created to replicate that real-world scenario and answer questions such as:

- Are elite football leagues truly competitive, or dominated by a few teams?

- How does scoring behavior differ across competitions and seasons?

- Is home advantage a structural phenomenon or seasonal noise?

- Which competitions exhibit higher unpredictability and volatility?

 The focus is on business relevance, not fan opinion.

</td></tr>
</table>


---

<table width="90%" align="center">
<tr><td>

# Executive Summary

This project presents an end-to-end football analytics case study analyzing performance across the **UEFA Champions League, Premier League, and LaLiga for the 2024–2025 seasons**. Rather than relying on pre-packaged datasets, match data was retrieved directly from an external football API, simulating how analytics teams ingest live or third-party data in production environments.

**The project combines:**

- Data ingestion via APIs

- A structured analytics warehouse

-SQL-based KPI development

- Business-focused insight delivery

The final output is a set of decision-ready KPIs, suitable for strategic use by:

- League operators

- Broadcasters

- Club management

- Data analysts and consultants

</td></tr>
</table>


---



<table width="90%" align="center">
<tr><td>


# Project Structure & Analytics Deliverables
 
This repository is structured to reflect a real-world, enterprise-style analytics workflow, covering the complete lifecycle from API ingestion → data warehousing → business insights → executive visuals. Each directory represents a clear responsibility within the analytics pipeline.
```
FOOTBALLDATALAKEHOUSE/
│
├── analytics/
│   └── sql_queries.sql
│       # Final business-grade SQL queries
│       # Used to generate KPIs, insights, and CSV exports
│
├── data/
│   ├── bronze/
│   │   └── matches/
│   │       # Raw JSON match data ingested directly from the Football API
│   │       # Stored without transformation for full traceability
│   │
│   ├── silver/
│   │   └── matches/
│   │       └── matches_clean.parquet
│   │           # Cleaned and standardized match-level dataset
│   │           # Ready for analytical modeling
│   │
│   ├── gold/
│   │   ├── fact_matches.parquet
│   │   │   # Match-level fact table (grain: one row per match)
│   │   │
│   │   ├── league_kpis.parquet
│   │   │   # Aggregated KPIs by competition and season
│   │   │
│   │   └── team_performance.parquet
│   │       # Team-level performance metrics
│   │       # (goals, goals conceded, goal difference, dominance)
│   │
│   └── exports/
│       # Business-ready KPI outputs generated from SQL
│       ├── kpi_score_intensity.csv
│       ├── kpi_home_advantage.csv
│       ├── kpi_top_teams.csv
│       ├── kpi_competitiveness_gap.csv
│       └── kpi_scoring_volatility.csv
│
├── ingestion/
│   └── fetch_matches.py
│       # API ingestion script
│       # Fetches match data by competition and season
│
├── transformation/
│   ├── clean_matches.py
│   │   # Transforms raw JSON into standardized Silver layer
│   │
│   └── build_gold.py
│       # Builds Gold-layer fact tables and business KPIs
│
├── notebooks/
│   └── validate_gold.py
│       # Data validation and quality checks
│
├── visuals/
│   # Executive-level visual outputs used in README and presentations
│   ├── score_intensity.png
│   ├── home_advantage.png
│   ├── top_teams.png
│   ├── competitiveness_gap.png
│   └── scoring_volatility.png
│
├── README.md
│   # Business-focused case study documentation
│
├── LICENSE
│   # MIT License
│
└── requirements.txt
    # Python dependencies for reproducibility
```

</td></tr>
</table>


---


<table width="90%" align="center">
<tr><td>
 
# Data Architecture & Methodology

This project was architected to mirror **production-grade analytics and analytics engineering workflows**, demonstrating end-to-end ownership of data ingestion, transformation, and business modeling.

Rather than relying on pre-curated datasets, all data was **programmatically sourced, standardized, and modeled** to reflect how analytics teams operate in real-world environments.

---

### 🔹 Bronze Layer — External API Ingestion (Source of Truth)

The Bronze layer captures raw match data directly from an external football data API, serving as the **immutable source of truth**.

**Key Responsibilities**
- Designed and implemented a Python-based ingestion pipeline
- Parameterized API requests by competition and season
- Persisted raw API responses as timestamped JSON files
- Preserved original payloads without transformation to support reprocessing and auditing

**Why This Matters**
- Enables reproducibility and historical backfills
- Separates data collection from analytics logic
- Reflects how modern data platforms handle external data sources

This layer demonstrates **data acquisition, automation, and traceability**, not manual data collection.

---

### 🔹 Silver Layer — Data Cleaning & Standardization

The Silver layer converts raw API responses into a **clean, analytics-ready dataset**.

**Transformations Performed**
- Normalized nested JSON structures into tabular format
- Standardized team names, identifiers, and competition fields
- Enforced consistent season definitions across leagues
- Validated match completeness and schema consistency
- Removed malformed or non-analytical records

**Output**
- A single, standardized match-level dataset (`matches_clean.parquet`)
- One row per match with consistent semantics across competitions

**Why This Matters**
- Eliminates downstream analytical complexity
- Ensures comparability across leagues and seasons
- Creates a reliable foundation for KPI development

This layer reflects **analytics engineering best practices**, not ad-hoc cleaning.

---

### 🔹 Gold Layer — Analytical Models & Business KPIs

The Gold layer represents **business-facing analytical models** optimized for SQL analytics and BI tools.

**Analytical Tables**
- `fact_matches`  
  Match-level fact table (grain: one row per match)

- `league_kpis`  
  Aggregated league-level KPIs by competition and season  
  (scoring intensity, total goals, competitiveness indicators)

- `team_performance`  
  Team-level performance metrics  
  (goals scored, conceded, goal difference, dominance)

**Design Principles**
- Clear grain definition
- Business-aligned metrics
- Optimized for downstream consumption (SQL, BI, exports)

**Why This Matters**
- Translates raw data into decision-ready insights
- Enables consistent KPI definitions across analyses
- Supports both ad-hoc analysis and executive reporting

---

### Analytical Access & Consumption

To support fast iteration and exploration:

- Gold-layer data is queried using **DuckDB (SQL-first analytics engine)**
- Business questions are expressed as **reusable SQL queries**
- KPI outputs are exported as CSVs for visualization and reporting
- Gold models are directly consumable by BI tools (e.g. Power BI)

This approach reflects how analytics teams **bridge engineering and business stakeholders**.

---

### Why This Architecture Was Chosen

This architecture demonstrates capabilities expected of **Senior Data Analysts and Analytics Engineers**, including:

- Designing ingestion pipelines from external sources
- Implementing layered data models
- Enforcing data quality and consistency
- Modeling business KPIs with clear definitions
- Preparing data for BI and executive consumption


</td></tr>
</table>

---

# Business Insights

<table width="90%" align="center">
<tr><td>

## Scoring Intensity Across Competitions

The UEFA Champions League consistently demonstrates the highest scoring intensity, with average goals per match exceeding both **LaLiga and the Premier League across the 2024 and 2025 seasons**. As shown in the visualization, Champions League matches average above 3.3 goals per match, compared to approximately 2.6–2.9 goals in domestic leagues. This indicates a structurally more open style of play driven by elite team quality, tactical risk-taking, and knockout-stage incentives.

From a business perspective, higher scoring intensity directly enhances:

- Viewer engagement and match entertainment value

- Broadcast attractiveness and advertising premiums

- Global audience retention for marquee fixtures

This reinforces why the Champions League commands premium broadcasting rights relative to domestic competitions.

<p align="center">
  <img src="visuals/Score%20Intensity.png" width="92%">
</p>


---



## Home Advantage Is Structural

Across all competitions and seasons, home teams consistently score more goals than away teams, confirming that home advantage is a persistent structural factor, not a short-term anomaly. The table highlights a clear home-goal **premium ranging from +0.29 to +0.42 goals per match**, with the Champions League exhibiting the strongest home advantage. Even in the Premier League—often considered tactically balanced—the home advantage remains statistically meaningful.

For stakeholders, this insight has direct implications for:

- Match outcome forecasting and betting markets

- Fixture scheduling and competitive fairness

- Team performance evaluation and tactical planning

Home advantage remains an embedded feature of football economics and performance modeling.

<p align="center">
  <img src="visuals/Home%20Advantage%20KPI.png" width="92%">
</p>



---



## Competitive Balance by League

Domestic leagues exhibit significantly wider competitiveness gaps than the Champions League, indicating a higher concentration of performance among top teams. As visualized, LaLiga and the Premier League show competitiveness gaps exceeding 100 points in 2024, compared to sub-50 gaps in the Champions League. This suggests that domestic leagues are more frequently dominated by a small group of elite clubs.

From a commercial standpoint, uneven competitive balance can:

- Reduce long-term fan engagement

- Increase predictability of outcomes

- Concentrate commercial value around top clubs

The Champions League’s comparatively tighter gap supports its positioning as a more competitively balanced global product.

<p align="center">
  <img src="visuals/League%20Competitiveness.png" width="92%">
</p>


---



## Scoring Volatility in Champions League

The Champions League demonstrates higher year-over-year scoring volatility compared to domestic leagues, reflecting its knockout structure and dynamic team composition.The volatility chart shows noticeable shifts in scoring patterns between 2024 and 2025, unlike the more stable trends observed in LaLiga and the Premier League. This volatility is driven by:

- Knockout match pressure

- Short tournament horizons

- Elite team rotation and tactical adaptation

For broadcasters and analysts, higher volatility increases:

- Match unpredictability

- Viewer suspense

- Demand for advanced forecasting and analytics

This reinforces the Champions League’s identity as a high-risk, high-reward competition.

<p align="center">
  <img src="visuals/Scoring%20Volatility%20by%20Competition%20(2024%20vs%202025).png" width="92%">
</p>

</td></tr>
</table>

---


<table width="90%" align="center">
<tr><td>

# Strategic Recommendations

Based on the analytical findings, the following strategic recommendations are proposed for key stakeholders across the football ecosystem:

---

### Actively Manage Competitive Balance to Sustain Fan Engagement

The analysis reveals widening performance gaps in domestic leagues, particularly in **LaLiga** and the **Premier League**. Persistent dominance by a small group of clubs reduces match unpredictability and poses a long-term risk to fan engagement.

**Recommended actions:**
- Monitor competitive balance KPIs on a season-over-season basis
- Introduce or refine financial and regulatory mechanisms to limit excessive performance concentration
- Use competitiveness metrics as early-warning indicators of declining league parity

Maintaining competitive balance is critical to protecting audience growth, match attendance, and long-term commercial value.

---

### Leverage Champions League Volatility for Broadcast & Commercial Strategy

The **UEFA Champions League** demonstrates higher scoring volatility and intensity than domestic leagues, driven by knockout-stage dynamics and elite team concentration.

**Recommended actions:**
- Prioritize high-volatility fixtures for prime-time scheduling
- Align advertising and sponsorship pricing with match intensity metrics
- Explicitly incorporate volatility indicators into broadcast rights valuation models

These characteristics directly support the Champions League’s premium global positioning.

---

### Use Home Advantage Metrics for Tactical & Operational Planning

Home advantage remains a persistent structural factor across all competitions, with a measurable goal premium ranging from **+0.29 to +0.42 goals per match**.

**Recommended actions:**
- Incorporate home-advantage adjustments into tactical planning and squad rotation
- Evaluate fixture scheduling fairness using home-bias indicators
- Adjust predictive and performance models to reflect structural home advantage

Ignoring home advantage introduces systematic bias into forecasting and evaluation processes.

---

### Benchmark Club Dominance for Performance & Investment Decisions

A limited number of elite clubs consistently drive league outcomes and scoring dominance, creating high performance concentration.

**Recommended actions:**
- Benchmark club performance against league-level dominance thresholds
- Identify high-impact clubs for sponsorship and long-term investment decisions
- Use dominance metrics to evaluate whether league outcomes align with competitive objectives

Objective benchmarking enables performance assessment beyond league position alone.

---

### Institutionalize KPI-Driven Decision Making

The KPIs developed in this project—**scoring intensity, volatility, home advantage, and competitive balance**—form a reusable analytical framework.

**Recommended actions:**
- Integrate these KPIs into recurring league and club performance reviews
- Standardize metrics across competitions for consistent comparison
- Extend the framework into forecasting, valuation, and risk modeling use cases

This enables a shift from intuition-based decisions to **evidence-driven strategic planning**.

---

# Strategic Value Delivered

By operationalizing these insights, stakeholders can:

- Protect long-term fan engagement
- Maximize broadcast and sponsorship value
- Improve competitive fairness
- Enable data-driven league and club strategy

This project demonstrates how **well-structured sports data can function as a strategic business asset**, not merely a reporting tool.


</td></tr>
</table>

---





