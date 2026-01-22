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

💡 **Insight**  
The UEFA Champions League consistently records the highest average goals per match, indicating a more open and aggressive scoring environment compared to domestic leagues.

<p align="center">
  <img src="visuals/Score%20Intensity.png" width="92%">
</p>


---



## Home Advantage Is Structural

💡 **Insight**  
Home teams score more goals across all competitions and seasons, confirming home advantage as a structural factor rather than random variation.

<p align="center">
  <img src="visuals/Home%20Advantage%20KPI.png" width="92%">
</p>



---



## Competitive Balance by League

💡 **Insight**  
Domestic leagues such as LaLiga and the Premier League show wider performance gaps than the Champions League, indicating uneven competitiveness.

<p align="center">
  <img src="visuals/League%20Competitiveness.png" width="92%">
</p>


---



## Scoring Volatility in Champions League

💡 **Insight**  
The Champions League exhibits higher year-over-year scoring volatility, driven by knockout dynamics and elite team concentration.

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

