import streamlit as st
from pkg.mapping import drinking_map
from pkg.plotting import county_population_plot
from pkg.load_data import connect_to_iowa, connect_to_county

st.set_page_config(page_title="Excessive Drinking", page_icon="🍻")
st.header('🍻 Explanatory Data Analysis: Excessive Drinking',divider=True)
st.markdown('''
            This section explores county-level excessive drinking and its effects on liquor sales 
            gross profits. While this variable is related to health outcomes, it may also serve as 
            a proxy for consumer behavior; an important consideration when deciding where to place 
            a liquor store. 
            ''')

# county data
table='solid-dominion-452916-p4.aml_fl_tn.county'
df_county = connect_to_county(table)
df_county = df_county.groupby('county').first().reset_index()

# df_ungrouped = connect_to_county(table)

# # iowa data
# table='solid-dominion-452916-p4.aml_fl_tn.iowa_without_month'
# df_iowa = connect_to_iowa(table)

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
                - The average percentage of adults in Iowa that drink excessively is 24%.
                - There is not much variation between counties; the range is only 8%.
                - Excessive drinking does not appear to be correlated with population.
                """)
    
    st.subheader("Excessive Drinking (%) by County")
    drinking_map(df_grouped, url)

with tab2:
    st.markdown("""
                - The distribution shows how profit is highest around 24-25%. This does not
                necessarily reflects higher population counties, such as Polk, Linn, Pottawattamie.
                - Buchanan county has the highest excessive drinking rate, but has low average 
                yearly profit.
                - Referencing the trendline, there is a slight negative association between 
                excessive drinking percentage and average yearly gross profit.
                """)

    st.subheader("Average Yearly Gross Profit by County vs Excessive Drinking (%)")
    county_population_plot(
        df_county,
        x="excessive_drinking",
        y="avg_gross_profit",
        color="county",
        x_title="Excessive drinking perventage",
        y_title="Average yearly gross profit by county",
        trendline="ols"        # optional: adds a regression line
    )
    county_population_plot(
        df_county,
        x="excessive_drinking",
        y="avg_gross_profit",
        x_title="Excessive drinking perventage",
        y_title="Average yearly gross profit by county",
        trendline="ols"        # optional: adds a regression line
    )
