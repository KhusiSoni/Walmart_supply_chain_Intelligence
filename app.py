import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Walmart Supply Chain Intelligence",
    page_icon="📦",
    layout="wide"
)

# ==========================
# LOAD DATA
# ==========================

executive_kpi = pd.read_csv("executive_kpi.csv")

warehouse_kpi = pd.read_csv("warehouse_kpi.csv")

store_kpi = pd.read_csv("store_kpi.csv")

category_kpi = pd.read_csv("category_kpi.csv")

risk_summary = pd.read_csv("risk_summary.csv")

abc_analysis = pd.read_csv("abc_analysis.csv")

scenario_summary = pd.read_csv("scenario_planning_results.csv")

forecast_eval = pd.read_csv("forecast_evaluation_summary.csv")

feature_importance = pd.read_csv("feature_importance.csv")

shap_importance = pd.read_csv("shap_feature_importance.csv")

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Dashboard",
    [
        "Forecasting Analytics",
        "Inventory Optimization",
        "Scenario Planning",
        "Model Explainability"
    ]
)

# ==========================================================
# PAGE 1
# ==========================================================

if page == "Forecasting Analytics":

    st.title("📈 Demand Forecasting Analytics")

    st.markdown("### Model Evaluation Metrics")

    c1, c2, c3 = st.columns(3)

    rmse = forecast_eval.loc[
        forecast_eval["Metric"] == "RMSE",
        "Value"
    ].values[0]

    mae = forecast_eval.loc[
        forecast_eval["Metric"] == "MAE",
        "Value"
    ].values[0]

    r2 = forecast_eval.loc[
        forecast_eval["Metric"] == "R2",
        "Value"
    ].values[0]

    c1.metric("RMSE", round(rmse,2))
    c2.metric("MAE", round(mae,2))
    c3.metric("R²", round(r2,4))

    c4, c5, c6 = st.columns(3)

    wape = forecast_eval.loc[
        forecast_eval["Metric"] == "WAPE",
        "Value"
    ].values[0]

    smape = forecast_eval.loc[
        forecast_eval["Metric"] == "SMAPE",
        "Value"
    ].values[0]

    accuracy = forecast_eval.loc[
        forecast_eval["Metric"] == "Forecast Accuracy",
        "Value"
    ].values[0]

    c4.metric("WAPE %", round(wape,2))
    c5.metric("SMAPE %", round(smape,2))
    c6.metric("Forecast Accuracy %", round(accuracy,2))

    st.subheader("Forecast Evaluation Summary")

    st.dataframe(
        forecast_eval,
        use_container_width=True
    )

    # ======================
    # Feature Importance
    # ======================

    st.subheader("Feature Importance")

    fi = (
        feature_importance
        .sort_values(
            "importance",
            ascending=False
        )
        .head(15)
    )

    fig = px.bar(
        fi,
        x="importance",
        y="feature",
        orientation="h",
        title="Top 15 Features"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ======================
    # SHAP Importance
    # ======================

    st.subheader("SHAP Feature Importance")

    shap_df = (
        shap_importance
        .sort_values(
            "mean_abs_shap",
            ascending=False
        )
        .head(15)
    )

    fig = px.bar(
        shap_df,
        x="mean_abs_shap",
        y="feature",
        orientation="h",
        title="Top SHAP Features"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
# ==========================================================
# PAGE 2
# ==========================================================

elif page == "Inventory Optimization":

    st.title("📦 Inventory Optimization Dashboard")

    st.subheader("Executive KPIs")

    kpi_dict = dict(
        zip(
            executive_kpi["KPI"],
            executive_kpi["Value"]
        )
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Forecast Demand",
        round(
            kpi_dict.get(
                "Total Forecast Demand",
                0
            ),
            0
        )
    )

    c2.metric(
        "Inventory",
        round(
            kpi_dict.get(
                "Total Inventory",
                0
            ),
            0
        )
    )

    c3.metric(
        "Replenishment",
        round(
            kpi_dict.get(
                "Total Replenishment",
                0
            ),
            0
        )
    )

    c4, c5 = st.columns(2)

    c4.metric(
        "Service Level %",
        round(
            kpi_dict.get(
                "Service Level",
                0
            ),
            2
        )
    )

    c5.metric(
        "Fill Rate %",
        round(
            kpi_dict.get(
                "Fill Rate",
                0
            ),
            2
        )
    )

    st.subheader("Warehouse Utilization")

    fig = px.bar(
        warehouse_kpi,
        x="Warehouse",
        y="Utilization_%",
        text="Utilization_%"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Risk Segmentation")

    fig = px.pie(
        risk_summary,
        names="Risk Segment",
        values="Count"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("ABC Analysis")

    fig = px.bar(
        abc_analysis,
        x="cat_id",
        y="forecast_28",
        color="ABC_Class"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Store Performance")

    st.dataframe(
        store_kpi,
        use_container_width=True
    )

    st.subheader("Category Performance")

    st.dataframe(
        category_kpi,
        use_container_width=True
    )
    st.subheader("Business Insights")

    foods_pct = round(
        abc_analysis.iloc[0]["demand_pct"]*100,
        1
    )
    
    st.info(
    f"""
    • FOODS contributes {foods_pct}% of total demand.

    • CA_DC has highest warehouse utilization.

    • Supply disruption creates maximum shortages.

    • Holiday surge generates highest demand.

    • Inventory optimization maintains service level close to 100%.
    """
    )

# ==========================================================
# PAGE 3
# ==========================================================

elif page == "Scenario Planning":

    st.title("📊 Scenario Planning")

    st.subheader("Scenario Comparison")

    st.dataframe(
        scenario_summary,
        use_container_width=True
    )

    st.subheader("Demand by Scenario")

    fig = px.bar(
        scenario_summary,
        x="Scenario",
        y="Total_Demand"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Service Level")

    fig = px.bar(
        scenario_summary,
        x="Scenario",
        y="Service_Level"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Shortage by Scenario")

    fig = px.bar(
        scenario_summary,
        x="Scenario",
        y="Shortage",
        color="Scenario"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Fill Rate")

    fig = px.bar(
        scenario_summary,
        x="Scenario",
        y="Fill_Rate"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.subheader("Business Recommendations")

    st.info("""
    Demand Surge → Increase replenishment and safety stock.

    Demand Drop → Reduce inventory holding costs.

    Price Shock → Monitor demand elasticity.

    Supply Disruption → Maintain emergency inventory buffers.

    Holiday Surge → Increase replenishment quantities by 20–40%.
    """)
# ==========================================================
# PAGE 4
# ==========================================================

elif page == "Model Explainability":

    st.title("🧠 Model Explainability")

    st.subheader("Feature Importance")

    fig = px.bar(
        feature_importance
        .sort_values(
            "importance",
            ascending=False
        )
        .head(20),

        x="importance",
        y="feature",
        orientation="h"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("SHAP Feature Importance")

    fig = px.bar(
        shap_importance
        .sort_values(
            "mean_abs_shap",
            ascending=False
        )
        .head(20),

        x="mean_abs_shap",
        y="feature",
        orientation="h"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Key Drivers")

    st.info(
    """
    Top demand drivers:

    • Lag features dominate demand forecasting.

    • Rolling averages capture seasonality.

    • Event variables affect spikes.

    • Price changes influence demand patterns.

    • SNAP variables contribute to demand variation.
    """
    )
# ==========================
# DOWNLOADS
# ==========================

st.sidebar.markdown("---")

st.sidebar.download_button(
    "Download Executive KPI",
    executive_kpi.to_csv(index=False),
    file_name="executive_kpi.csv"
)

st.sidebar.download_button(
    "Download Scenario Results",
    scenario_summary.to_csv(index=False),
    file_name="scenario_planning_results.csv"
)