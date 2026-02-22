import streamlit as st

def init_session():
    if "page" not in st.session_state:
        st.session_state.page = "Landing"
    if "data" not in st.session_state:
        st.session_state.data = None
