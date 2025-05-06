# https://advanced-computing-fred-naga-lab2-home-jczcrq.streamlit.app/
import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.set_page_config(page_title="Ridge Regression", page_icon="🍶")
st.header('🍶 Algorithm: Ridge Regression',divider=True)
st.markdown('''
            We built a Ridge Regression model to project monthly gross profit for each 
            store. 70% of the data was used for training, and 15% for validation. During 
            validation, we obtained an RMSE of 8,395.12 when λ = 10.99, so we adopted 
            λ = 11 for our final model and applied it to the testing data.
            ''')

tab1, tab2 = st.tabs(["Training (70%) & Validation (15%)", "Testing (15%)"])

#############################################################

with tab1:
    st.markdown("""
                - The RMSE decreases as lambda increases up to a point, but the 
                improvement is marginal.
                - After log(λ) = 1.5, the RMSE starts to increase sharply, suggesting 
                over-regularization.
                - The optimal λ balances the trade-off between model complexity and 
                prediction error.
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
                - The model struggles to accurately predict stores with very high or very 
                low gross profits.
                - An RMSE of 8,294.92 indicates relatively poor accuracy ginven an average 
                actual profit of $6,463.
                - The Ridge model may not generalize well to unseen data, and alternative 
                models should be explored.
                """)
    if st.button("Algorithm - Random Forest"):
        st.switch_page("pages/9_Algorithm_-_Random_Forest.py")

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
