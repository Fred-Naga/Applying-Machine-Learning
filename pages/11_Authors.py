import streamlit as st

st.set_page_config(page_title="Authors", page_icon="👥")
st.image('picture/authors.png', use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
    """
    <div style='text-align: center;'>
        <a href='https://www.linkedin.com/in/takaaki-nagasawa-b74146297/' target='_blank' style='text-decoration: none; font-size: 18px;'>
            Takaaki Nagasawa (Naga)
        </a>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown('''
                - Pronouns: he/him
                - GitHub username: [NGSWTKK](https://github.com/NGSWTKK)
                - Hometown: Yamanashi, Japan
                - Education: 
                    - School of International and Public Affairs | Columbia University (2023-2025)
                    - Hokkaido University (2011-2017)
                ''')

with col2:
    st.markdown(
    """
    <div style='text-align: center;'>
        <a href='https://www.linkedin.com/in/frederick-t-lee/' target='_blank' style='text-decoration: none; font-size: 18px;'>
            Fred Lee
        </a>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown('''
                - Pronouns: he/him
                - GitHub username: [Ftl2110](https://github.com/Ftl2110)
                - Hometown: Flemington, NJ
                - Education: 
                    - School of International and Public Affairs | Columbia University (2023-2025)
                    - Stetson University (2013-2017)
                ''')