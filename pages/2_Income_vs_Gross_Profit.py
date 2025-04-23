import streamlit as st
from pkg.mapping import income_map
from pkg.plotting import income_histogram_plot, county_population_plot, plot_price_range_histogram
from pkg.load_data import connect_to_county


# county data
table='solid-dominion-452916-p4.aml_fl_tn.county'
url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"

df_county = connect_to_county(table)
df_county = df_county.groupby('county').first().reset_index()

df_ungrouped = connect_to_county(table).reset_index()


# Average income map and table
st.title("Average Income by County")
income_map(df_county, url)

st.title("Distributions")
income_histogram_plot(df_county,30)

plot_price_range_histogram(df_ungrouped)
        
# This function is generic
st.subheader("Income vs. Gross Profit by County")
county_population_plot(
    df_county,
    x="annual_income",
    y="gross_profit",
    color="county",
    title="Income vs. Gross Profit by County",
    x_title="Annual Income",
    y_title="Gross Profit",
    trendline="ols"        # optional: adds a regression line
)

st.subheader("Income vs. Gross Profit with Trendline")
county_population_plot(
    df_county,
    x="annual_income",
    y="gross_profit",
    title="Income vs. Gross Profit (w/ Trendline)",
    x_title="Annual Income",
    y_title="Gross Profit",
    trendline="ols"        # optional: adds a regression line
)

st.header("Comparing Price's Effect on Profits")

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