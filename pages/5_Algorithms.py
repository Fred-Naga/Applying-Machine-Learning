# https://advanced-computing-fred-naga-lab2-home-jczcrq.streamlit.app/
import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.title('Random Forest')

st.header('🍻 Training (70%) & Validation (15%)',divider=True)

df = pd.read_csv('table/rmse.csv')
fig = px.line(
    df,
    x='depth',
    y='rmse',
    color='n_trees',
    markers=True,
    title='RMSE vs Tree Depth'
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

st.header('🍾 Testing (15%)',divider=True)

df_diff = pd.read_csv('table/diff_actu_predi.csv')
fig = px.scatter(
    df_diff,
    x='store',
    y='gross_profit',
    color='comparison',
    title='Actual vs Projected Monthly Gross Profit',
    labels={
        'store': 'Stores in testing',
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
        x=0,               
        y=1,                
        xanchor='left',  
        yanchor='top')
)
st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
            **Model**
            - Number of Trees: 50
            - Tree Depth: 15
            - RMSE: 4,949.21
            """)
    st.markdown('')
    st.markdown('**Monthly Summary of Gross Profit by Store**')
    with open('table/gross_profit_summary.json', 'r') as f:
        profit = json.load(f)
    st.json(profit)
    
with col2: 
    st.markdown('**Importance of 4,534 features**')
    df = pd.read_csv('table/feat_importance.csv')
    df