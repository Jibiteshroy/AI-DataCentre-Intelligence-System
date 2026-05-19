# AI-Powered Enterprise Data Centre Intelligence System

## 📌 Executive Summary
This project is an end-to-end business intelligence pipeline designed to monitor, analyze, and predict mission-critical infrastructure health for a global data centre network. Moving beyond basic reporting, this system simulates an AI-driven predictive maintenance model to flag high-risk assets before they fail, optimizing uptime and reducing reactive maintenance costs.

## 🏗️ Architecture & Tech Stack
* **Data Generation:** Python (`pandas`, `faker`) to simulate 5,000+ realistic hardware incidents, maintenance logs, and telemetry data.
* **Database Pipeline:** Microsoft SQL Server (T-SQL) for relational data warehousing and enforcing a star schema architecture.
* **Business Intelligence:** Power BI (DAX, Data Modeling) for executive-level visualization and predictive risk scoring.

## 📊 Dashboard 1: Executive Operations Center (NOC)
<img width="1467" height="832" alt="dashboard_page1" src="https://github.com/user-attachments/assets/0a3100ae-1ea3-4478-970d-b1b8aba98388" />


**Key Features:**
* **Global Threat Mapping:** Real-time visibility into revenue bleeding across 6 international facilities.
* **SLA Compliance Tracking:** DAX-driven calculation to monitor penalty thresholds for downtime exceeding 120 minutes.
* **Risk Heatmap:** Matrix visualization isolating exact facilities and failure severities.

## 🤖 Dashboard 2: Predictive Maintenance & Asset Health
<img width="1466" height="826" alt="dashboard_page2" src="https://github.com/user-attachments/assets/f7e7edc8-f945-439c-b6e8-2d518a84d299" />


**Key Features:**
* **Algorithmic Risk Scoring:** Custom DAX logic penalizes older assets with a history of emergency (reactive) maintenance.
* **Actionable Target List:** Prioritized engineering queue showing exactly which assets require immediate intervention.
* **ROI Justification:** Financial proof demonstrating the cost-savings of predictive maintenance vs. reactive emergency repairs.

## 🧠 Core DAX Logic (Predictive Risk Score)
To simulate the predictive intelligence, I developed a risk-scoring algorithm prioritizing asset age and historical failure severity:
```dax
Asset Risk Score = 
VAR BaseRisk = AVERAGE(Asset_Inventory[Age_Years]) * 5
VAR ReactivePenalty = CALCULATE(COUNTROWS(Maintenance), Maintenance[Maintenance_Type] = "Reactive") * 15
RETURN
BaseRisk + ReactivePenalty
