Yes — here is the **entire `README.md` as one single block**. Copy everything inside the block and paste it directly into VS Code.

````markdown
# 📦 Walmart Supply Chain Intelligence System

An end-to-end **Supply Chain Analytics and Machine Learning platform** built using the Walmart M5 sales dataset. The system combines demand forecasting, inventory analytics, risk segmentation, scenario planning, and model explainability into an interactive Streamlit dashboard.

---

## 🚀 Project Overview

The platform provides data-driven insights for **demand planning, inventory management, and supply chain decision-making**.

### Core Capabilities

- 📈 Demand Forecasting
- 📦 Inventory Analytics
- 🏭 Warehouse Utilization Analysis
- ⚠️ Inventory Risk Segmentation
- 🔤 ABC Inventory Classification
- 🔮 Scenario Planning
- 🧠 Model Explainability using SHAP
- 📊 Interactive Streamlit Dashboard

---

# 📊 Dashboard

## 1. Demand Forecasting Analytics

The forecasting module predicts future demand using historical sales patterns and engineered temporal and business features.

### Evaluation Metrics

- RMSE
- MAE
- R²
- WAPE
- SMAPE
- Forecast Accuracy

### Visualizations

- Forecast evaluation metrics
- Feature importance
- SHAP feature importance
- Model performance analysis

---

## 2. Inventory Analytics

The inventory module analyzes demand and inventory patterns to identify operational risks and improvement opportunities.

### Executive KPIs

- Total Forecast Demand
- Total Inventory
- Total Replenishment
- Service Level
- Fill Rate

### Analytics

- Warehouse Utilization
- Inventory Risk Segmentation
- ABC Inventory Classification
- Store Performance
- Category Performance

The dashboard generates business insights based on inventory levels, demand patterns, and operational performance.

---

## 3. Scenario Planning

The scenario planning module evaluates how different business conditions can affect demand and inventory performance.

### Scenarios

- Base Scenario
- Demand Surge
- Demand Drop
- Price Shock
- Supply Disruption
- Holiday Surge

### Scenario Metrics

Each scenario evaluates changes in:

- Demand
- Inventory
- Shortage
- Service Level
- Fill Rate

The results are used to identify potential supply chain risks and generate scenario-specific business recommendations.

---

## 4. Model Explainability

The forecasting model is analyzed using feature importance and SHAP to understand the factors driving predictions.

### Explainability Techniques

- Model Feature Importance
- SHAP Feature Importance
- SHAP-based Model Interpretation

### Key Predictive Drivers

- Lag Features
- Rolling Demand Averages
- Event Variables
- Price Features
- SNAP Variables
- Calendar Features

---

# 🧠 Machine Learning Pipeline

The forecasting pipeline combines historical demand patterns with temporal and business features.

## Feature Engineering

### Temporal Features

- Lag Features
- Rolling Means
- Calendar Features
- Seasonal Patterns

### Business Features

- Event Variables
- SNAP Variables
- Price Features

These features are used to capture historical demand behavior, seasonality, promotional effects, and other demand drivers.

---

## 🤖 Machine Learning Model

The project uses **LightGBM** for demand forecasting due to its ability to efficiently model nonlinear relationships and interactions across large tabular datasets.

### Model Evaluation

The forecasting model is evaluated using:

- RMSE
- MAE
- R²
- WAPE
- SMAPE
- Forecast Accuracy

### Model Explainability

**SHAP (SHapley Additive exPlanations)** is used to identify the features that have the greatest influence on model predictions.

---

# 📈 Key Results

## Forecast Performance

- **R²:** 0.935
- **Forecast Accuracy:** ≈ 85.6%

## Inventory Performance

- **Service Level:** ≈ 100%
- **Fill Rate:** ≈ 100%

## Scenario Analysis

The system evaluates the potential impact of:

- Demand Surges
- Demand Drops
- Price Shocks
- Supply Disruptions
- Holiday Demand Surges

---

# 🔄 End-to-End Workflow

```text
Walmart M5 Sales Data
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Demand Forecasting
        ↓
Model Evaluation
        ↓
SHAP Explainability
        ↓
Inventory Analytics
        ↓
Risk & ABC Analysis
        ↓
Scenario Planning
        ↓
Interactive Streamlit Dashboard
````

---

# 📁 Project Structure

```text
Walmart-Supply-Chain-Intelligence/
│
├── app.py
│
├── executive_kpi.csv
├── warehouse_kpi.csv
├── store_kpi.csv
├── category_kpi.csv
├── risk_summary.csv
├── abc_analysis.csv
├── scenario_planning_results.csv
├── forecast_evaluation_summary.csv
├── feature_importance.csv
├── shap_feature_importance.csv
│
├── notebooks/
│
├── screenshots/
│
├── requirements.txt
│
└── README.md
```

---

# 🛠 Technologies Used

## Programming & Data Processing

* Python
* Pandas
* NumPy

## Machine Learning

* LightGBM
* Scikit-Learn

## Model Explainability

* SHAP

## Visualization

* Plotly

## Dashboard

* Streamlit

---

# 🎯 Business Applications

The system can support supply chain teams in:

* Understanding future demand
* Identifying inventory risks
* Monitoring warehouse utilization
* Prioritizing high-value inventory
* Evaluating demand and supply shocks
* Comparing different business scenarios
* Understanding the drivers behind demand forecasts
* Supporting data-driven inventory decisions

---

# 📊 Supply Chain Analytics

The platform combines multiple analytical techniques to provide a broader view of supply chain performance.

### ABC Analysis

Classifies inventory based on business importance and contribution to overall value.

### Risk Segmentation

Identifies inventory and operational risk based on demand and stock-related indicators.

### Warehouse Analysis

Evaluates warehouse-level inventory utilization and operational performance.

### Store Analysis

Compares demand and inventory performance across individual stores.

### Category Analysis

Analyzes demand and inventory patterns across product categories.

---

# 🔮 Scenario Planning Framework

The scenario engine allows users to simulate potential changes in supply chain conditions.

```text
Base Conditions
      │
      ├── Demand Surge
      ├── Demand Drop
      ├── Price Shock
      ├── Supply Disruption
      └── Holiday Surge
              │
              ↓
        Scenario Simulation
              │
              ↓
    Demand / Inventory Impact
              │
              ↓
 Shortage / Service Level / Fill Rate
              │
              ↓
       Business Recommendation
```

This enables users to evaluate potential operational risks before making inventory decisions.

---

# 🧠 Explainability Framework

The forecasting pipeline provides both model performance evaluation and interpretability.

```text
LightGBM Forecasting Model
          ↓
Feature Importance
          ↓
SHAP Analysis
          ↓
Identify Key Demand Drivers
```

The explainability layer helps understand how historical demand, lagged sales, rolling averages, events, pricing, SNAP indicators, and calendar variables influence forecasts.

---

# 📌 Dataset

This project uses the **Walmart M5 Forecasting dataset**, which contains historical Walmart sales data across stores, products, departments, calendar events, prices, and SNAP indicators.

The dataset provides the foundation for demand forecasting and downstream supply chain analytics.

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd Walmart-Supply-Chain-Intelligence
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the Streamlit dashboard using:

```bash
streamlit run app.py
```

The application will open in your default browser.

---

# 📋 Requirements

The main dependencies include:

```text
Python
Pandas
NumPy
Scikit-Learn
LightGBM
SHAP
Plotly
Streamlit
```

---

# 🚀 Project Highlights

* End-to-end supply chain analytics workflow
* Machine learning-based demand forecasting
* Feature engineering for time-series demand
* LightGBM forecasting model
* SHAP-based model explainability
* Inventory risk segmentation
* ABC inventory classification
* Warehouse and store-level analytics
* Scenario-based supply chain planning
* Interactive Streamlit dashboard

---

# 👤 Author

**Khusi Soni**

B.Arch
Indian Institute of Technology Kharagpur

**Interests:** Applied Machine Learning · Data Science · Supply Chain Analytics

```
```

