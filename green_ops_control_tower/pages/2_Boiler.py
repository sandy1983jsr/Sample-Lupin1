import streamlit as st
from diagnostics.boiler_diagnostics import compute_boiler_losses
from ai.boiler_ai import recommend_boiler_actions

st.title("🔥 Boiler Performance & Diagnostics")

df = st.session_state["plant_data"]

st.subheader("Boiler Efficiency Trend")
st.line_chart(df["boiler_efficiency_pct"])

st.subheader("Loss Diagnostics")
loss_df = compute_boiler_losses(df)
st.area_chart(loss_df)

st.subheader("AI-Recommended Improvement Options")
recs = recommend_boiler_actions(df)
st.table(recs)
