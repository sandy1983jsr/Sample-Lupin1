import streamlit as st
import pandas as pd

from diagnostics.dryer_diagnostics import (
    compute_dryer_kpis,
    identify_dryer_losses
)
from ai.dryer_ai import (
    train_dryer_baseline_model,
    detect_dryer_opportunities
)

st.title("🌀 Dryer Performance, Loss Diagnostics & AI Opportunities")

# Retrieve plant data
df = st.session_state.get("plant_data")

if df is None or df.empty:
    st.warning("No plant data available.")
    st.stop()

# ---------------- KPI SECTION ----------------
st.subheader("Dryer Performance KPIs")

kpis = compute_dryer_kpis(df)

c1, c2, c3 = st.columns(3)
c1.metric("SEC (kWh / kg API)", f"{kpis['SEC_kWh_per_kg']:.2f}")
c2.metric("Avg Drying Time (hr)", f"{kpis['avg_drying_time_hr']:.1f}")
c3.metric("Energy Intensity (kWh/hr)", f"{kpis['kWh_per_hr']:.1f}")

st.divider()

# ---------------- PERFORMANCE TRENDS ----------------
st.subheader("Dryer Energy & Drying Time Trends")

col1, col2 = st.columns(2)
with col1:
    st.line_chart(
        df.set_index("timestamp")["dryer_kwh"],
        height=300
    )

with col2:
    st.line_chart(
        df.set_index("timestamp")["time_in_dryer_hr"],
        height=300
    )

st.divider()

# ---------------- LOSS DIAGNOSTICS ----------------
st.subheader("Loss Diagnostics (Explainable)")

loss_df = identify_dryer_losses(df)

st.area_chart(
    loss_df[[
        "overdrying_loss_kwh",
        "high_temp_loss_kwh",
        "vacuum_loss_kwh"
    ]]
)

st.caption(
    "Losses shown are diagnostic proxies to identify dominant inefficiencies, "
    "not exact thermodynamic losses."
)

st.divider()

# ---------------- AI OPPORTUNITY ENGINE ----------------
st.subheader("AI-Identified Improvement Opportunities")

model = train_dryer_baseline_model(df)

opps_df = detect_dryer_opportunities(
    df,
    model,
    power_cost=8.0,   # ₹ / kWh
    grid_ef=0.82      # tCO2 / MWh
)

if opps_df.empty:
    st.success("No significant dryer inefficiencies detected in this period.")
else:
    st.dataframe(opps_df)

    st.metric(
        "Total Annual Saving Potential (₹ Cr)",
        opps_df["annual_cost_saving_rs"].sum() / 1e7
    )

    st.metric(
        "CO₂ Reduction Potential (t/year)",
        opps_df["co2_reduction_tpy"].sum()
    )

st.divider()

# ---------------- RECOMMENDED NEXT ACTIONS ----------------
st.subheader("Recommended Next Actions (Consulting View)")

st.markdown("""
**Immediate (0–30 days)**  
• Implement AI-assisted drying end-point for selected APIs  
• Train operators on stopping criteria  

**Medium Term (1–3 months)**  
• Review dryer temperature & vacuum SOP bands  
• Integrate moisture / PAT proxy if available  

**Strategic**  
• Link dryer end-point AI with batch scheduling to unlock capacity
""")
