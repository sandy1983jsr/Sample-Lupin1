import streamlit as st
from diagnostics.dryer import dryer_kpis, dryer_losses
from ai.dryer_ai import dryer_ai

def render(df):
    st.title("🌀 Dryer Diagnostics")

    kpis = dryer_kpis(df)
    st.metric("SEC (kWh/kg)", f"{kpis['SEC']:.2f}")
    st.metric("Avg Drying Time (hr)", f"{kpis['Avg Time']:.1f}")

    st.line_chart(df.set_index("timestamp")["dryer_kwh"])

    st.subheader("Loss Diagnostics")
    st.area_chart(dryer_losses(df))

    rs, co2 = dryer_ai(df)
    st.metric("Savings Potential (₹ Cr)", rs / 1e7)
    st.metric("CO₂ Reduction (t/y)", co2)

    if st.button("⬅ Back"):
        st.session_state.page = "Plant"
