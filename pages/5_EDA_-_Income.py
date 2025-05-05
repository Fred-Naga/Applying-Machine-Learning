import streamlit as st
from pkg.mapping import income_map
from pkg.plotting import income_histogram_plot, plot_income_distribution_by_county, county_population_plot, plot_income_pie_by_county, plot_price_range_histogram, plot_income_heatmap
from pkg.load_data import connect_to_county
import pandas as pd

st.set_page_config(page_title="Income", page_icon="🍷")
st.header('🍷 Explanatory Data Analysis: Income',divider=True)
st.markdown('''
            ...(Overview)
            ''')

# county data
table='solid-dominion-452916-p4.aml_fl_tn.county'
url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
df_county = connect_to_county(table)
df_income = pd.read_csv("annual_income.csv")
df_county = df_county.merge(df_income, on="county", how="left")
df_county = df_county.groupby('county').first().reset_index()
df_ungrouped = connect_to_county(table).reset_index()
df_ungrouped = df_ungrouped.merge(df_income, on="county", how="left")


tab1, tab2, tab3 = st.tabs(["Map", "Distributions", "Gross Profit"])

#############################################################

with tab1:
    st.markdown("""
                - Average income seems to be highest in Dallas and Warren counties: affluent suburbs outside of Des Moines
                - Alternatively, the more agriculturally dependent and sparsely populated counties in the South have lower incomes.
                - Other higher income counties are also proximal to cities
                """)

    # Average income map and table
    st.subheader("Average Income by County")
    income_map(df_county, url)
    

    
    st.subheader("County Income Pie Chart")
    county = st.selectbox("Choose a county", df_county['county'].unique())
    plot_income_pie_by_county(df_county, county)

with tab2:
    st.markdown("""
                - There is a double peak of income distribution at 64k-65k and 72k-74k 
                - The histogram is positively skewed, with extreme values pulling the mean to the right
                - Apart from Warren, Benton, and Dallas, most counties have similar income bracket distributions
                """)

    st.subheader("Income Distribution Across Counties")
    income_histogram_plot(df_county,30)

    st.subheader("Income Bracket Distributions")
    plot_income_distribution_by_county(df_county)    

with tab3:
    st.markdown("""
                - ...(takeaway 1)
                - ...(takeaway 2)
                - ...(takeaway 3)
                """)
    
    # This function is generic
    st.subheader("Income vs. Gross Profit by County")
    county_population_plot(
        df_county,
        x="annual_income",
        y="gross_profit",
        color="county",
        title="",
        x_title="Annual Income",
        y_title="Gross Profit",
        trendline="ols"        # optional: adds a regression line
    )
    county_population_plot(
        df_county,
        x="annual_income",
        y="gross_profit",
        title="",
        x_title="Annual Income",
        y_title="Gross Profit",
        trendline="ols"        # optional: adds a regression line
    )
