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



## Background

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



---



## Executive Summary

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


---


## Project Objective

The primary objectives of this project are to:

- Build a scalable football analytics warehouse
- Standardize performance metrics across competitions
- Produce business-focused KPIs to support strategic decision-making

This is not a dashboard-only project — it demonstrates **end-to-end analytics ownership**, from ingestion to insight.



---

## Data Architecture & Methodology

A **medallion-style analytics architecture** was implemented to ensure reliability, auditability, and scalability.

### 🔹 Bronze Layer – Raw Ingestion
- Raw match data ingested from official football data sources
- Stored without transformation for full traceability

### 🔹 Silver Layer – Clean & Standardized
- Data cleaning and normalization
- Standardized team names and match structures
- Consistent season and competition alignment

### 🔹 Gold Layer – Business Analytics
- Match-level fact tables
- Aggregated KPIs by competition, season, and team
- Optimized for SQL analytics and BI consumption

This mirrors **enterprise data warehouse design**, not ad-hoc analysis.



---

# Business Insights



## Scoring Intensity Across Competitions

The UEFA Champions League consistently demonstrates the highest scoring intensity, with average goals per match exceeding both **LaLiga and the Premier League across the 2024 and 2025 seasons**. As shown in the visualization, Champions League matches average above 3.3 goals per match, compared to approximately 2.6–2.9 goals in domestic leagues. This indicates a structurally more open style of play driven by elite team quality, tactical risk-taking, and knockout-stage incentives.

From a business perspective, higher scoring intensity directly enhances:

- Viewer engagement and match entertainment value

- Broadcast attractiveness and advertising premiums

- Global audience retention for marquee fixtures

This reinforces why the Champions League commands premium broadcasting rights relative to domestic competitions.

<br/>

<p align="center">
  <img src="visuals/Score%20Intensity.png" width="100%" />
</p>

<br/>

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



---

# Strategic Recommendations



Based on these findings:

- League operators should monitor competitive balance to protect long-term fan engagement
- Broadcasters can anticipate higher volatility in Champions League fixtures
- Clubs can benchmark dominance relative to league norms
- Analysts can integrate KPIs into forecasting and valuation models



---



## Analytics Deliverables

This project delivers:

- Analytics-ready Gold tables
- Reusable SQL business queries
- KPI CSV exports for reporting
- Executive-level visualizations
- Scalable warehouse design



---



## Tools & Analytics Stack

- SQL (DuckDB)
- Python (Data Processing & Automation)
- Excel / Power BI (Visualization)
- GitHub (Version Control & Presentation)



---



## Final Outcome

This project demonstrates:

- End-to-end analytics ownership
- Enterprise-style data warehouse design
- Business storytelling through data
- Decision-focused insights

This reflects **real-world analytics work**, not academic exercises.

