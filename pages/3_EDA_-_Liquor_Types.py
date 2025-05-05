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

default_counties = ['polk', 'linn', 'johnson', 'scott', 'woodbury']



st.set_page_config(page_title="Liquor Types", page_icon="🧉")
st.header('🧉 Explanatory Data Analysis: Liquor Types',divider=True)
st.markdown('''
            ...(Overview)
            ''')

tab1, tab2, tab3 = st.tabs(["Map", "State and County Trends", "Price Ranges on Gross Profit"])

#############################################################

with tab1:
    st.markdown("""
                - ...(takeaway 1)
                - ...(takeaway 2)
                - ...(takeaway 3)
                """)
    
    st.subheader("Liquor Type Gross Profits by County")
    
    liquor_options = ['All'] + sorted(df_county['liquor_type'].unique().tolist())
    selected_liquor = st.selectbox("Choose Liquor Type", liquor_options)
    map_gross_profit_choropleth(
        df_county,
        url="https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json",
        liquor_type=selected_liquor
    )
    
    st.subheader("State-Level Liquor Preferences")
    liquor_type_plot(df_liquor,
                     x="liquor_type",
                     y="gross_profit",
                     x_title="Liquor type",
                     y_title="Aggregate yearly gross profit")
    

with tab2:
    st.markdown("""
                - ...(takeaway 1)
                - ...(takeaway 2)
                - ...(takeaway 3)
                """)  
    
    st.subheader("County-Level")
    counties1 = st.multiselect(
        "Choose counties to display", 
        options=df_county['county'].unique(), 
        default=[c for c in default_counties if c in df_county['county'].unique()],
        key="chart_a_counties")
    liquor_type_plot(df_county, x="liquor_type", y="gross_profit", counties=counties1, color="price_range",
                    title="Price vs Profit by County", x_title="Liquor Type", y_title="Gross Profit")


    st.subheader("Liquor Bottle Sales and Profits by County")
    st.markdown('Note: all liquor categories less than one percent are aggregated into the other category.')
    county = st.selectbox("Select county", df_county['county'].unique())
    plot_sales_profit_pie_by_county(df_county, county)

with tab3:
    st.markdown("""
                - ...(takeaway 1)
                - ...(takeaway 2)
                - ...(takeaway 3)
                """)
    
    st.subheader("Sold Liquors by Price Range")
    plot_price_range_histogram(df_ungrouped)
    
    st.subheader("Gross Profits by Price Range")
    counties2 = st.multiselect(
        "Choose counties to display", 
        options=df_county['county'].unique(), 
        default=[c for c in default_counties if c in df_county['county'].unique()], 
        key="chart_b_counties"
    )
    liquor_type_plot(df_county, x="price_per_liter", y="gross_profit", counties=counties2, color="price_range",
                    title="Price vs Profit by County", x_title="Price per Liter", y_title="Gross Profit")
    
    st.subheader("Comparing Price Effects on Profit")
    # Create two columns
    col1, col2 = st.columns(2)

    tiers = ["cheap", "medium", "expensive"]

    with col1:
        tier1 = st.selectbox("Choose tier for Plot 1", tiers, key="tier1")
        df1 = df_ungrouped[df_ungrouped["price_range"] == tier1]
        county_population_plot(
            df1,
            x="annual_income",
            y="gross_profit",
            color="county",
            title=f"{tier1.capitalize()} Tier: Income vs Gross Profit",
            x_title="Annual Income",
            y_title="Gross Profit",
            trendline="ols"
        )
        county_population_plot(
            df1,
            x="annual_income",
            y="gross_profit",
            title=f"{tier1.capitalize()} Tier: Income vs Gross Profit",
            x_title="Annual Income",
            y_title="Gross Profit",
            trendline="ols"
        )

    with col2:
        tier2 = st.selectbox("Choose tier for Plot 2", tiers, key="tier2", index=2)
        df2 = df_ungrouped[df_ungrouped["price_range"] == tier2]
        county_population_plot(
            df2,
            x="annual_income",
            y="gross_profit",
            color="county",
            title=f"{tier2.capitalize()} Tier: Income vs Gross Profit",
            x_title="Annual Income",
            y_title="Gross Profit",
            trendline="ols"
        )
        county_population_plot(
            df2,
            x="annual_income",
            y="gross_profit",
            title=f"{tier1.capitalize()} Tier: Income vs Gross Profit",
            x_title="Annual Income",
            y_title="Gross Profit",
            trendline="ols"
        )
