import streamlit as st
from pkg.mapping import gas_sales_map
from pkg.plotting import county_population_plot
from pkg.load_data import connect_to_county

st.set_page_config(page_title="Fuel Sales", page_icon="🍸")
st.header('🍸 Explanatory Data Analysis: Fuel Sales',divider=True)
st.markdown('''
            This section explores county-level fuel sales and its relationship with liquor sales 
            gross profit. While we expect an increase in fuel sales to correlate with foot traffic 
            in counties and their stores, increasing profits, we also explore the relationship 
            between fuel sales per capita and average yearly gross profit by county.
            ''')

# county data
table='solid-dominion-452916-p4.aml_fl_tn.county'
df_county = connect_to_county(table)
df_county = df_county.groupby('county').first().reset_index()
# df_county['gross_profit_to_pop'] = df_county['gross_profit'] / df_county['pop_county']
df_county['gas_to_pop'] = df_county['gas_sales'] / df_county['pop_county']
# df_county['gross_profit_to_pop'] = df_county['gross_profit_to_pop'].astype(float)
df_county['gas_to_pop'] = df_county['gas_to_pop'].astype(float)

url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"

tab1, tab2 = st.tabs(["Map", "Gross Profit"])

#############################################################

with tab1:
    st.markdown("""
                - Fuel Sales appear to correlate with high population cities and interstate 
                highway locations.
                - Polk County has the highest gas sales by far, with the capital of Des Moines 
                and the intersection of Interstate 80 and 35.
                - Other cities such as Cedar Rapids, Iowa City, Omaha, or Sioux City are located 
                in Linn, Johnson, Pottawattamie, and Woodbury counties, respectively.
                - Each of the other cities also has one interstate highway which runs through them.
                """)
    
    st.subheader("Gas Sales by County")
    url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
    gas_sales_map(df_county, url)

with tab2:
    st.markdown("""
                - When plotting gas sales against gross profit, there appears to be a strong 
                positive correlation.
                - These findings are significantly impacted by Polk County (a high sales outlier).
                - The majority of Iowa counties have less than 3.5 million gallons per year; one 
                tenth of the sales in Polk County.
                - On the contrary, looking at the gas sales per capita, there is almost no 
                correlation with average yearly gross profit.
                """)

    st.subheader("Aggreagate Yearly Gross Profit by County vs Gas Sales")
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

    st.subheader("Average Yearly Gross Profit by County vs Gas Sales per Capita")
    county_population_plot( 
        df_county,
        x="gas_to_pop",
        y="avg_gross_profit",
        color="county",
        x_title="Gas sales per capita",
        y_title="Average yearly gross profit by county",
        trendline="ols"        # optional: adds a regression line
    )
    county_population_plot(
        df_county,
        x="gas_to_pop",
        y="avg_gross_profit",
        x_title="Gas sales per capita",
        y_title="Average yearly gross profit by county",
        trendline="ols"        # optional: adds a regression line
    )