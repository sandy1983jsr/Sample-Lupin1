# pages/landing.py
import streamlit as st

def render():
    st.title("🟢 Green Operations Command & Control Tower")

    corp = st.session_state.corporate_kpis

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Energy Cost (₹ Cr)", f"{corp['energy_cost_cr']:.2f}")
    c2.metric("CO₂ Emissions (t)", f"{corp['co2_t']:.0f}")
    c3.metric("₹ / kg API", corp["cost_intensity"])
    c4.metric("Top Opportunity (₹ Cr)", corp["top_opportunity_cr"])

    st.divider()

    if st.button("Go to Plant View"):
        st.session_state.page = "Plant"
