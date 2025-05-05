import streamlit as st
from pkg.mapping import map_gross_profit_choropleth
from pkg.plotting import county_population_plot, plot_price_range_histogram, plot_sales_profit_pie_by_county, liquor_type_plot
from pkg.load_data import connect_to_county
import pandas as pd

table='solid-dominion-452916-p4.aml_fl_tn.county'
url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
df_county = connect_to_county(table).reset_index()
df_income = pd.read_csv("annual_income.csv")
df_ungrouped = connect_to_county(table).reset_index()
df_ungrouped = df_ungrouped.merge(df_income, on="county", how="left")
df_liquor = df_county.groupby(['liquor_type'])['gross_profit'].sum().reset_index()
df_county2 = df_county.groupby(['county', 'liquor_type'])['gross_profit'].sum().reset_index()

st.set_page_config(page_title="Store Types", page_icon="🍹")
st.header('🍹 Explanatory Data Analysis: Store Types',divider=True)
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
    liquor_type_plot()

with tab2:
    st.markdown("""
                - ...(takeaway 1)
                - ...(takeaway 2)
                - ...(takeaway 3)
                """)

    st.subheader("sub title")
