import streamlit as st
from pkg.mapping import gas_sales_map, drinking_map
from pkg.plotting import county_population_plot
from pkg.load_data import connect_to_iowa, connect_to_county

st.set_page_config(page_title="Fuel Sales", page_icon="🍸")
st.header('🍸 Explanatory Data Analysis: Fuel Sales',divider=True)
st.markdown('''
            ...(Overview)
            ''')

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

tab1, tab2 = st.tabs(["Map", "Gross Profit"])

#############################################################

with tab1:
    st.markdown("""
                - Fuel Sales appear to correlate with high population cities and interstate highway locations
                - Polk County has the highest gas sales by far, with the capital of Des Moines and the intersection of Interstate 80 and 35
                - Other cities such as Cedar Rapids, Iowa City, Omaha, or Sioux City are located in Linn, Johnson, Pottawattamie, and Woodbury counties, respectively
                - Each of the other cities also has one interstate highway which runs through them
                """)
    
    st.subheader("Gas Sales by County")
    url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
    gas_sales_map(df_county, url)

with tab2:
    st.markdown("""
                - When plotting gas Sales against Gross Profit, there appears to be a strong positive correlation 
                - These findings are significantly impacted by Polk County (a high sales outlier)
                - The majority of Iowa counties have less than 3.5 million gallons per year; one tenth of the sales in Polk County
                """)

    st.subheader("Gas Sales vs. Gross Profit by County")
    county_population_plot(
        df_county,
        x="gas_sales",
        y="gross_profit",
        color="county",
        x_title="Gas sales",
        y_title="Aggregate yearly gross profit by county",
        trendline="ols"        # optional: adds a regression line
    )
    county_population_plot(
        df_county,
        x="gas_sales",
        y="gross_profit",
        x_title="Gas sales",
        y_title="Aggregate yearly gross profit by county",
        trendline="ols"        # optional: adds a regression line
    )
