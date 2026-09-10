# 📦 Walmart Supply Chain Intelligence System

An end-to-end Supply Chain Analytics platform built on Walmart M5 sales data. This project combines machine learning forecasting, inventory analytics, scenario planning, and model explainability into an interactive Streamlit dashboard.

---

# 🚀 Project Overview

This project provides a complete supply chain decision-support system capable of:

* Demand Forecasting
* Inventory Analytics
* Warehouse Utilization Analysis
* Risk Segmentation
* ABC Inventory Classification
* Scenario Planning
* Model Explainability using SHAP
* Interactive Dashboard Visualization

---

# 📊 Dashboard Pages

## 1. Demand Forecasting Analytics

Provides:

* RMSE
* MAE
* R²
* WAPE
* SMAPE
* Forecast Accuracy

### Visualizations

* Forecast evaluation metrics
* Feature importance
* SHAP feature importance

---

## 2. Inventory Analytics Dashboard

Includes:

### Executive KPIs

* Total Forecast Demand
* Total Inventory
* Total Replenishment
* Service Level
* Fill Rate

### Analytics

* Warehouse Utilization
* Risk Segmentation
* ABC Analysis
* Store Performance
* Category Performance

Business insights are generated from inventory and demand patterns.

---

## 3. Scenario Planning

Simulates multiple business conditions:

* Base Scenario
* Demand Surge
* Demand Drop
* Price Shock
* Supply Disruption
* Holiday Surge

Evaluates:

* Demand
* Inventory
* Shortage
* Service Level
* Fill Rate

Provides business recommendations for each scenario.

---

## 4. Model Explainability

Explains model behavior using:

* Feature Importance
* SHAP Feature Importance

Key drivers identified include:

* Lag features
* Rolling averages
* Event effects
* Price effects
* SNAP variables

---

# 🧠 Machine Learning Pipeline

### Feature Engineering

* Lag Features
* Rolling Means
* Event Variables
* SNAP Variables
* Price Features
* Calendar Features

### Model Evaluation Metrics

* RMSE
* MAE
* R²
* WAPE
* SMAPE
* Forecast Accuracy

### Explainability

* Feature Importance
* SHAP Values

---

# 📁 Project Structure

```text
Walmart_supply_chain_Intelligence/

│
├── app.py
├── main.ipynb
├── requirements.txt
│
├── executive_kpi.csv
├── warehouse_kpi.csv
├── store_kpi.csv
├── category_kpi.csv
├── risk_summary.csv
├── abc_analysis.csv
│
├── scenario_planning_results.csv
│
├── forecast_evaluation_summary.csv
├── baseline_forecasting_results.csv
├── timeseries_cv_results.csv
├── feature_importance.csv
├── shap_feature_importance.csv
├── final_lightgbm_forecasting_model.pkl
│
├── production_forecasting_dataset.csv
├── store_category_daily.csv
├── store_category_daily_enriched.csv
├── store_category_daily_feature_engineered.csv
│
├── inventory_modeling_output.csv
├── inventory_optimization_input.csv
├── inventory_summary.csv
│
└── README.md
```

---

# 🛠 Technologies Used

### Python

* Pandas
* NumPy

### Machine Learning

* LightGBM
* Scikit-Learn

### Explainability

* SHAP

### Visualization

* Plotly

### Dashboard

* Streamlit

---

# 📈 Key Results

### Forecast Performance

* R² = 0.935
* Forecast Accuracy ≈ 85.6%

### Inventory Performance

* Service Level ≈ 100%
* Fill Rate ≈ 100%

### Scenario Planning

Evaluated impacts of:

* Demand Surge
* Demand Drop
* Price Shock
* Supply Disruption
* Holiday Surge

---

# ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/KhusiSoni/Walmart_supply_chain_Intelligence.git
cd Walmart_supply_chain_Intelligence
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit dashboard

```bash
streamlit run app.py
```

---

# 🔮 Future Improvements

* Deep Learning Models (LSTM/Transformer)
* Real-time Data Pipelines
* Streamlit Cloud Deployment
* Docker Containerization

---

# 👤 Author

**Khusi Soni**
Indian Institute of Technology Kharagpur

Applied Machine Learning | Data Science | Supply Chain Analytics

---

## About

End-to-End Walmart Supply Chain Intelligence System featuring Demand Forecasting, Inventory Analytics, Scenario Planning, SHAP Explainability, and Interactive Streamlit Dashboard.
