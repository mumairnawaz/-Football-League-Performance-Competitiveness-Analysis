---

## Table of Contents

> - [Background](#background)
> - [Executive Summary](#executive-summary)
> - [Project Objective](#project-objective)
> - [Data Architecture & Methodology](#data-architecture--methodology)
> - [Business Insights](#business-insights)
>   - [Insight 1: Scoring Intensity Varies Across Competitions](#insight-1-scoring-intensity-varies-across-competitions)
>   - [Insight 2: Home Advantage Is Structural, Not Random](#insight-2-home-advantage-is-structural-not-random)
>   - [Insight 3: A Small Set of Teams Drive League Performance](#insight-3-a-small-set-of-teams-drive-league-performance)
>   - [Insight 4: Competitive Balance Differs by League](#insight-4-competitive-balance-differs-by-league)
>   - [Insight 5: Champions League Shows Higher Scoring Volatility](#insight-5-champions-league-shows-higher-scoring-volatility)
> - [Strategic Recommendations](#strategic-recommendations)
> - [Analytics Deliverables](#analytics-deliverables)
> - [Tools & Analytics Stack](#tools--analytics-stack)
> - [Final Outcome](#final-outcome)

---

<table width="90%" align="center"> <tr><td>
## Background

Elite football competitions generate substantial commercial value through broadcasting rights, sponsorships, and global fan engagement. However, leagues differ significantly in competitiveness, scoring behavior, and team dominance.

This project moves beyond basic match statistics to address business-critical questions, including:

How competitive are top football leagues in reality?

Are league outcomes driven by a small number of elite teams?

How predictable is goal scoring across competitions?

Where do structural advantages exist?

The analysis focuses on delivering decision-oriented insights, not descriptive statistics.

</td></tr> </table>
<table width="90%" align="center"> <tr><td>

  ---
  
## Executive Summary

This project evaluates UEFA Champions League, Premier League, and LaLiga performance across the 2024–2025 seasons using a purpose-built analytics warehouse.

Key Findings:

Scoring intensity and volatility vary meaningfully by competition

Home advantage remains a structural factor, not a seasonal anomaly

A small set of elite teams disproportionately influence league outcomes

Competitive balance differs sharply across leagues

The project delivers decision-ready KPIs, enabling strategic insight for:

League operators

Broadcasters

Club management

Football analysts

This is a business analytics project, not a fan-driven analysis.

</td></tr> </table>
<table width="90%" align="center"> <tr><td>

  ---

## Project Objective

The primary objectives of this project are to:

Build a scalable football analytics warehouse

Standardize performance metrics across competitions

Produce business-focused KPIs to support strategic decision-making

This is not a dashboard-only project — it demonstrates end-to-end analytics ownership, from ingestion to insight.

</td></tr> </table>
<table width="90%" align="center"> <tr><td>
Data Architecture & Methodology

A medallion-style analytics architecture was implemented to ensure reliability, auditability, and scalability.

🔹 Bronze Layer – Raw Ingestion

Raw match data ingested from official football data sources

Stored without transformation for full traceability

🔹 Silver Layer – Clean & Standardized

Data cleaning and normalization

Standardized team names and match structures

Consistent season and competition alignment

🔹 Gold Layer – Business Analytics

Match-level fact tables

Aggregated KPIs by competition, season, and team

Optimized for SQL analytics and BI consumption

This mirrors enterprise data warehouse design, not ad-hoc analysis.

</td></tr> </table>

---

Business Insights
<table width="90%" align="center"> <tr><td>
Insight 1: Scoring Intensity Across Competitions

💡 Insight
The UEFA Champions League consistently records the highest average goals per match, indicating a more open and aggressive scoring environment compared to domestic leagues.

<p align="center">
  <img src="visuals/Score%20Intensity.png" width="92%">
</p>


</td></tr> </table>
<table width="90%" align="center"> <tr><td>
Insight 2: Home Advantage Is Structural

💡 Insight
Home teams score more goals across all competitions and seasons, confirming home advantage as a structural factor rather than random variation.

<p align="center">
  <img src="visuals/Home%20Advantage%20KPI.png" width="92%">
</p>


</td></tr> </table>
<table width="90%" align="center"> <tr><td>

</td></tr> </table>
<table width="90%" align="center"> <tr><td>
Insight 4: Competitive Balance by League

💡 Insight
Domestic leagues such as LaLiga and the Premier League show wider performance gaps than the Champions League, indicating uneven competitiveness.

<p align="center">
  <img src="visuals/League%20Competitiveness.png" width="92%">
</p>


</td></tr> </table>
<table width="90%" align="center"> <tr><td>
Insight 5: Scoring Volatility in Champions League

💡 Insight
The Champions League exhibits higher year-over-year scoring volatility, driven by knockout dynamics and elite team concentration.

<p align="center">
  <img src="visuals/Scoring%20Volatility%20by%20Competition%20(2024%20vs%202025).png" width="92%">
</p>


</td></tr> </table>
Strategic Recommendations
<table width="90%" align="center"> <tr><td>

## Based on these findings:

League operators should monitor competitive balance to protect long-term fan engagement

Broadcasters can anticipate higher volatility in Champions League fixtures

Clubs can benchmark dominance relative to league norms

Analysts can integrate KPIs into forecasting and valuation models

</td></tr> </table>
<table width="90%" align="center"> <tr><td>
## Analytics Deliverables

This project delivers:

Analytics-ready Gold tables

Reusable SQL business queries

KPI CSV exports for reporting

Executive-level visualizations

Scalable warehouse design

</td></tr> </table>
<table width="90%" align="center"> <tr><td>
## Tools & Analytics Stack

SQL (DuckDB)

Python (Data Processing & Automation)

Excel / Power BI (Visualization)

GitHub (Version Control & Presentation)

</td></tr> </table>
<table width="90%" align="center"> <tr><td>
## Final Outcome

This project demonstrates:

End-to-end analytics ownership

Enterprise-style data warehouse design

Business storytelling through data

Decision-focused insights

This reflects real-world analytics work, not academic exercises.

</td></tr> </table>
