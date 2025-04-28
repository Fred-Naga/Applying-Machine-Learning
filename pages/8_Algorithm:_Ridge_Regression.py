# https://advanced-computing-fred-naga-lab2-home-jczcrq.streamlit.app/
import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.set_page_config(page_title="Ridge Regression", page_icon="🍶")
st.header('🍶 Algorithm: Ridge Regression',divider=True)
st.markdown('''
            ...(Overview)
            ''')

tab1, tab2 = st.tabs(["Training (70%) & Validation (15%)", "Testing (15%)"])

#############################################################

with tab1:
    st.markdown("""
                - ...(takeaway 1)
                - ...(takeaway 2)
                - ...(takeaway 3)
                """)
    
    st.subheader("RMSE vs Lambda")

    df = pd.read_csv('table/rmse_ridge.csv')
    fig = px.line(
        df,
        x='log_lambda',
        y='rmse',
        markers=True,
    )
    fig.update_layout(
        xaxis_title='Log(Lambda)',
        yaxis_title='RMSE',
        legend=dict(
            orientation='v',    
            x=1,               
            y=1,                
            xanchor='right',  
            yanchor='top')
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown("""
                - ...(takeaway 1)
                - ...(takeaway 2)
                - ...(takeaway 3)
                """)

    st.subheader("Actual vs Projected Monthly Gross Profit")

    df_diff = pd.read_csv('table/diff_actu_predi_ridge.csv')
    fig = px.scatter(
        df_diff,
        x='store',
        y='gross_profit',
        color='comparison',
        title='',
        labels={
            'store': 'Stores in testing data',
            'gross_profit': 'Monthly Gross Profit',
            'comparison': 'Comparison'
        },
        color_discrete_map={
            'actual gross profit': 'red',
            'projected gross profit': 'yellow'
        },
        opacity=0.6
    )
    fig.update_layout(
        xaxis_title='Stores in testing',
        yaxis_title='Monthly Gross Profit',
        legend_title_text=None,
        legend=dict(
            orientation='v',    
            x=1,               
            y=1,                
            xanchor='right',  
            yanchor='top')
    )
    st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
            **Selected Model**
            - Lambda: 11
            - RMSE: 8294.92
            """)
    st.markdown('')
    st.markdown('**Monthly Summary of Gross Profit by Store**')
    with open('table/gross_profit_summary.json', 'r') as f:
        profit = json.load(f)
    st.json(profit)
    
with col2: 
    st.markdown('**Beta Hat of 153 features**')
    df = pd.read_csv('table/beta_hat_test_labeled.csv')
    df