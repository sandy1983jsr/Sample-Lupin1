import streamlit as st
import pandas as pd

from data.dummy_generator import generate_dummy_data
from data.csv_loader import load_csv
from twins.boiler import boiler_efficiency
from ai.boiler_ai import detect_boiler_opportunities
from ai.dryer_ai import detect_dryer_opportunities
from analytics.opportunity_register import build_register
from ui.roles import ROLES

st.set_page_config("Green Ops AI Control Tower", layout="wide")

st.title("🟢 Green Operations AI Command & Control Tower")

role = st.sidebar.selectbox("Role", list(ROLES.keys()))
mode = st.sidebar.radio("Data Source", ["Dummy","CSV"])

if mode == "Dummy":
    df = generate_dummy_data()
else:
    files = st.sidebar.file_uploader("Upload CSV", type="csv", accept_multiple_files=True)
    if not files:
        st.stop()
    df = load_csv(files)

df["boiler_efficiency_pct"] = df.apply(boiler_efficiency, axis=1)

boiler_opps = detect_boiler_opportunities(df, fuel_cost=6.5, fuel_ef=1.8)
dryer_opps = detect_dryer_opportunities(df, power_cost=8, grid_ef=0.82)

opp_df = build_register(boiler_opps, dryer_opps)

st.subheader("AI Opportunity Register")
st.dataframe(opp_df)

st.metric("Total Savings Potential (₹ Cr)", opp_df["annual_savings_rs"].sum()/1e7)
st.metric("Total CO₂ Reduction (t)", opp_df["co2_reduction_tpy"].sum())
