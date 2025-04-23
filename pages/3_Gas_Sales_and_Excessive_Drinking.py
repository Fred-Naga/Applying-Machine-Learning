import streamlit as st
from pkg.mapping import gas_sales_map, drinking_map
from pkg.plotting import county_population_plot
from pkg.load_data import connect_to_iowa, connect_to_county


# county data
table='solid-dominion-452916-p4.aml_fl_tn.county'
df_county = connect_to_county(table)
df_county = df_county.groupby('county').first().reset_index()

df_ungrouped = connect_to_county(table)

# iowa data
table='solid-dominion-452916-p4.aml_fl_tn.iowa_without_month'
df_iowa = connect_to_iowa(table)

df_grouped = (
    df_county.groupby("county", as_index=False)
      .agg({
          "fips": "first",                
          "excessive_drinking": "first",
          "gross_profit": "sum"    
      })
)

df_grouped["excessive_drinking"] = df_grouped["excessive_drinking"] / 100

url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"

tab1, tab2 = st.tabs(["Gas Sales", "Excessive Drinking"])

with tab1:
    st.title("Gas Sales by County")
    url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
    gas_sales_map(df_county, url)

    # This function is generic
    st.title("")
    st.subheader("Gas Sales vs. Gross Profit by County")
    county_population_plot(
        df_county,
        x="gas_sales",
        y="gross_profit",
        color="county",
        title="Income vs. Gross Profit by Store",
        x_title="County Level Gas Sales",
        y_title="County Level Gross Profit",
        trendline="ols"        # optional: adds a regression line
    )

    st.subheader("Gas Sales vs. Gross Profit by County")
    county_population_plot(
        df_county,
        x="gas_sales",
        y="gross_profit",
        title="Income vs. Gross Profit by Store",
        x_title="County Level Gas Sales",
        y_title="County Level Gross Profit",
        trendline="ols"        # optional: adds a regression line
    )

with tab2:
    st.title("Excessive Drinking (%) by County")
    drinking_map(df_grouped, url)

    st.title("")
    st.subheader("Excessive Drinking (%) vs. Gross Profit by County")
    county_population_plot(
        df_grouped,
        x="excessive_drinking",
        y="gross_profit",
        title="Income vs. Gross Profit by Store",
        x_title="County Level Excessive Drinking",
        y_title="County Level Gross Profit",
        trendline="ols"        # optional: adds a regression line
    )