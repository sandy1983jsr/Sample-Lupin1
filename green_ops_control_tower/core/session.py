# core/session.py
import streamlit as st

def init_session():
    if "page" not in st.session_state:
        st.session_state.page = "Landing"

    if "data" not in st.session_state:
        st.session_state.data = None

    # ---- NEW: corporate KPIs ----
    if "corporate_kpis" not in st.session_state:
        st.session_state.corporate_kpis = {
            "energy_cost_cr": 0.0,
            "co2_t": 0.0,
            "cost_intensity": 0.0,
            "top_opportunity_cr": 0.0
        }
