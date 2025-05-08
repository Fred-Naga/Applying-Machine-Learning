# https://advanced-computing-fred-naga-lab2-home-jczcrq.streamlit.app/
import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.set_page_config(page_title="Random Forest", page_icon="🍺")
st.header('🍺 Algorithm: Random Forest',divider=True)
st.markdown('''
            We built four Random Forest models, each with a different number of trees and varying 
            tree depths, to examine how these hyperparameters affect prediction accuracy. Like the 
            Ridge Regression model, 70% of the data was used for training and 15% for validation. 
            The best performance was achieved with 100 trees and a maximum tree depth of 15, yielding 
            a validation RMSE of 4,672.04. We selected this configuration for our final model and 
            evaluated its performance on the test set.
            ''')

tab1, tab2 = st.tabs(["Training (70%) & Validation (15%)", "Testing (15%)"])

#############################################################

with tab1:
    st.markdown("""
                - As tree depth increases, the RMSE initially decreases, but it starts rising again 
                after depth 15.  
                - This suggests that the model begins to overfit when the tree depth exceeds 15.
                - A depth of 15 balances model complexity and generalization performance, achieving 
                the lowest RMSE in validation.
                """)
    
    st.subheader("RMSE vs Tree Depth")

    df = pd.read_csv('table/rmse.csv')
    fig = px.line(
        df,
        x='depth',
        y='rmse',
        color='n_trees',
        markers=True,
    )
    fig.update_layout(
        xaxis_title='Tree Depth',
        yaxis_title='RMSE',
        legend_title='Number of Trees',
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
                - The model demonstrates strong predictive performance, with projected values closely 
                matching actual values for most stores.
                - An RMSE of 4,672.04 is approximately 55% lower than that of the Ridge Regression 
                model (8,395.12), indicating significantly improved accuracy.
                - This level of precision makes the model suitable for real-world applications, 
                such as supporting decision makers in inventory planning or revenue forecasting.
                - We applied this model in an app to demonstrate its potential for predicting 
                monthly item-level gross profit by store.
                """)

    st.subheader("Actual vs Projected Monthly Gross Profit")

    df_diff = pd.read_csv('table/diff_actu_predi.csv')
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
            - Number of Trees: 100
            - Tree Depth: 15
            - RMSE: 4672.04
            """)
    st.markdown('')
    st.markdown('**Monthly Summary of Gross Profit by Store**')
    with open('table/gross_profit_summary.json', 'r') as f:
        profit = json.load(f)
    st.json(profit)
    
with col2: 
    st.markdown('**Importance of 153 features**')
    df = pd.read_csv('table/feat_importance_algorithm.csv')
    df
