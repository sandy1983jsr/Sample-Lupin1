import streamlit as st

def render():
    st.title("🏭 Plant Overview")

    if st.button("Boiler"):
        st.session_state.page = "Boiler"
    if st.button("Dryer"):
        st.session_state.page = "Dryer"

    if st.button("⬅ Back"):
        st.session_state.page = "Landing"
