import streamlit as st
from diagnostics.boiler import boiler_efficiency, boiler_losses
from ai.boiler_ai import boiler_ai

def render(df):
    st.title("🔥 Boiler Diagnostics")

    df["boiler_eff"] = boiler_efficiency(df)

    st.line_chart(df.set_index("timestamp")["boiler_eff"])

    st.subheader("Loss Diagnostics")
    st.area_chart(boiler_losses(df))

    rs, co2 = boiler_ai(df)
    st.metric("Savings Potential (₹ Cr)", rs / 1e7)
    st.metric("CO₂ Reduction (t/y)", co2)

    if st.button("⬅ Back"):
        st.session_state.page = "Plant"
