import streamlit as st

st.title("🟢 Green Operations Command & Control Tower")

corp = st.session_state["corporate_kpis"]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Energy Cost (₹ Cr)", corp["energy_cost"])
c2.metric("CO₂ Emissions (t)", corp["co2"])
c3.metric("₹ / kg API", corp["cost_intensity"])
c4.metric("Top Opportunity (₹ Cr)", corp["top_opportunity"])
