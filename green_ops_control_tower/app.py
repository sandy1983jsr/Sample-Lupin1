import streamlit as st
from core.session import init_session
from data.dummy_data import generate_dummy_data
from pages import landing, plant, boiler, dryer

st.set_page_config(layout="wide")
init_session()

if st.session_state.data is None:
    st.session_state.data = generate_dummy_data()

page = st.session_state.page
df = st.session_state.data

if page == "Landing":
    landing.render()
elif page == "Plant":
    plant.render()
elif page == "Boiler":
    boiler.render(df)
elif page == "Dryer":
    dryer.render(df)
