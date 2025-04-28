import streamlit as st

st.set_page_config(page_title="Month", page_icon="🍾")
st.header('🍾 Explanatory Data Analysis: Month',divider=True)
st.markdown('''
            ...(Overview)
            ''')

tab1, tab2 = st.tabs(["tab1", "tab2"])

#############################################################

with tab1:
    st.markdown("""
                - ...(takeaway 1)
                - ...(takeaway 2)
                - ...(takeaway 3)
                """)
    
    st.subheader("sub title")

with tab2:
    st.markdown("""
                - ...(takeaway 1)
                - ...(takeaway 2)
                - ...(takeaway 3)
                """)

    st.subheader("sub title")