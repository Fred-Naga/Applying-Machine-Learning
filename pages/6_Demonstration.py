import streamlit as st

if st.button("Home"):
    st.switch_page("Home.py")


st.page_link("Home.py", label="Home", icon="🏠")