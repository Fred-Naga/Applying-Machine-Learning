import streamlit as st
from pkg.mapping import income_map
from pkg.plotting import county_population_plot, plot_price_range_histogram
from pkg.load_data import connect_to_county
import pandas as pd

table='solid-dominion-452916-p4.aml_fl_tn.county'
url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
df_county = connect_to_county(table)
df_income = pd.read_csv("annual_income.csv")
df_county = df_county.merge(df_income, on="county", how="left")
df_county = df_county.groupby('county').first().reset_index()
df_ungrouped = connect_to_county(table).reset_index()
df_ungrouped = df_ungrouped.merge(df_income, on="county", how="left")



st.set_page_config(page_title="Liquor Types", page_icon="🧉")
st.header('🧉 Explanatory Data Analysis: Liquor Types',divider=True)
st.markdown('''
            ...(Overview)
            ''')

tab1, tab2, tab3 = st.tabs(["tab1", "tab2", "Price Effects"])

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

with tab3:
    st.markdown("""
                - ...(takeaway 1)
                - ...(takeaway 2)
                - ...(takeaway 3)
                """)
    
    st.subheader("Sold Liquors by Price Range")
    plot_price_range_histogram(df_ungrouped)
    
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
