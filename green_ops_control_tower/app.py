
# app.py
import streamlit as st
from core.session import init_session
from green_ops_control_tower.data import generate_dummy_data
from green_ops_control_tower.diagnostics.boiler import boiler_efficiency
from green_ops_control_tower.pages import landing, plant, boiler, dryer

st.set_page_config(layout="wide")

# ---- Initialise session safely ----
init_session()

# ---- Load data once ----
if st.session_state.data is None:
    st.session_state.data = generate_dummy_data()

df = st.session_state.data

# ---- Compute corporate KPIs safely ----
df = df.copy()
df["boiler_eff"] = boiler_efficiency(df)

energy_cost_rs = (df["fuel_kgph"] * 6.5).sum()
co2_t = (df["fuel_kgph"] * 1.8).sum() / 1000
cost_intensity = energy_cost_rs / df["api_kg"].sum()

st.session_state.corporate_kpis = {
    "energy_cost_cr": energy_cost_rs / 1e7,
    "co2_t": co2_t,
    "cost_intensity": round(cost_intensity, 2),
    "top_opportunity_cr": round(energy_cost_rs * 0.08 / 1e7, 2)  # placeholder
}

# ---- Router ----
page = st.session_state.page

if page == "Landing":
    landing.render()
elif page == "Plant":
    plant.render()
elif page == "Boiler":
    boiler.render(df)
elif page == "Dryer":
    dryer.render(df)
