import streamlit as st
from pkg.mapping import population_map, gross_profit_map
from pkg.plotting import county_population_plot, city_population_plot
from pkg.load_data import connect_to_iowa, connect_to_county, connect_to_city, connect_to_spring, connect_to_summer, connect_to_fall, connect_to_winter

st.set_page_config(page_title="Population", page_icon="🥃")
st.header('🥃 Explanatory Data Analysis: Population',divider=True)
st.markdown('''
            This section investigates how population characteristics, including gender and age, 
            relate to liquor store gross profit in Iowa. By visualizing spatial and 
            demographic patterns, we aim to understand whether densely populated areas or certain 
            population segments are associated with higher alcohol-related revenue. We also explore 
            seasonal variations to detect possible trends in consumer behavior across different 
            times of the year.
            ''')

# county data
table='solid-dominion-452916-p4.aml_fl_tn.county'
df_county = connect_to_county(table)
df_county = df_county.groupby('county').first().reset_index()

# city data
table='solid-dominion-452916-p4.aml_fl_tn.city'
df_city = connect_to_city(table)

# gross profit data by season
table='solid-dominion-452916-p4.aml_fl_tn.iowa_with_month'
df_spring = connect_to_spring(table)
df_summer = connect_to_summer(table)
df_fall = connect_to_fall(table)
df_winter = connect_to_winter(table)

table='solid-dominion-452916-p4.aml_fl_tn.iowa_without_month'
df = connect_to_iowa(table)

tab1, tab2, tab3, tab4 = st.tabs(["Map", "County-Level", "City-Level", "Gender & Age by County"])

#############################################################

with tab1:
    st.markdown("""
                - High-grossing liquor stores are concentrated in densely populated counties 
                such as Polk, Linn, and Scott.
                - Seasonal trends do not drastically change the spatial distribution of profit, 
                suggesting location and population may be more influential than season.
                """)

    st.subheader("Iowa Population by County")
    url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
    population_map(df_county, url)

    st.subheader("Monthly Item-Level Gross Profit by Store")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Spring (March-May)")
        gross_profit_map(df_spring)
        st.write("Fall (September-November)")
        gross_profit_map(df_fall)
    with col2:
        st.write("Summer (June-August)")
        gross_profit_map(df_summer)
        st.write("Winter (December-February)")
        gross_profit_map(df_winter)

with tab2:
    st.markdown("""
                - Aggregate gross profit by county has a strong positive correlation with county 
                population.
                - However, at the individual store level, this correlation weakens, suggesting 
                store-level factors (e.g., liquor assortments, store type) play a role.
                - Population alone cannot explain store-level performance.
                """)
    
    st.subheader("Aggregate Gross Profit vs County Population")
    county_population_plot(df_county, 
                           x="pop_county", 
                           y="gross_profit",
                           color="",
                           trendline="ols",
                           title="",
                           x_title="County population",
                           y_title="Aggregate yearly item-level gross profit by county")

    st.subheader("Gross Profit by Store vs County Population")
    county_population_plot(df, 
                           x="pop_county", 
                           y="gross_profit",
                           color="county",
                           trendline=None,
                           title="",
                           x_title="County population",
                           y_title="Yearly item-level gross profit by store")
    county_population_plot(df, 
                           x="pop_county", 
                           y="gross_profit",
                           color=None,
                           trendline="ols",
                           title="",
                           x_title="County population",
                           y_title="Yearly item-level gross profit by store")

with tab3:
    st.markdown("""
                - Similar to county-level results, city population correlates strongly with 
                aggregate gross profit.
                - At the store level, the relationship is weak, reinforcing that other 
                store-specific factors must be considered.
                - Larger cities tend to have more profitable stores overall, but not necessarily 
                more profitable individual stores.
                """)
    
    st.subheader("Aggregate Gross Profit vs City Population")
    city_population_plot(df_city, 
                         x="pop_city", 
                         y="gross_profit",
                         color=None,
                         trendline="ols",
                         title="",
                         x_title="City population",
                         y_title="Aggregate yearly item-level gross profit by city")
    
    st.subheader("Gross Profit by Store vs City Population")
    city_population_plot(df, 
                         x="pop_city", 
                         y="gross_profit",
                         color="county",
                         trendline=None,
                         title="",
                         x_title="City population",
                         y_title="Yearly item-level gross profit by store")
    city_population_plot(df, 
                         x="pop_city", 
                         y="gross_profit",
                         color=None,
                         trendline="ols",
                         title="",
                         x_title="City population",
                         y_title="Yearly item-level gross profit by store")
    
with tab4:
    st.markdown("""
                - Gender alone shows minimal impact on liquor store gross profit at the county 
                level.
                - Age groups between 25–44 show a strong correlation with gross profit, likely 
                due to higher purchasing power and social consumption patterns.
                - Correlation weakens notably in populations over 45, suggesting younger 
                demographics are more predictive of liquor sales.
                """)
    
    st.subheader("Aggregate Gross Profit vs Geder & Age Population")
    col1, col2 = st.columns(2)
    with col1:
        county_population_plot(df_county, 
                           x="female_18_24", 
                           y="gross_profit",
                           color=None,
                           trendline="ols",
                           title="",
                           x_title="Female 18 to 24 years old population",
                           y_title="Aggregate yearly item-level gross profit by county")
        county_population_plot(df_county, 
                    x="female_25_34", 
                    y="gross_profit",
                    color=None,
                    trendline="ols",
                    title="",
                    x_title="Female 25 to 34 years old population",
                    y_title="Aggregate yearly item-level gross profit by county")
        county_population_plot(df_county, 
                    x="female_35_44", 
                    y="gross_profit",
                    color=None,
                    trendline="ols",
                    title="",
                    x_title="Female 35 to 44 years old population",
                    y_title="Aggregate yearly item-level gross profit by county")
        county_population_plot(df_county, 
                    x="female_45_64", 
                    y="gross_profit",
                    color=None,
                    trendline="ols",
                    title="",
                    x_title="Female 45 to 64 years old population",
                    y_title="Aggregate yearly item-level gross profit by county")
        county_population_plot(df_county, 
                    x="female_65_over", 
                    y="gross_profit",
                    color=None,
                    trendline="ols",
                    title="",
                    x_title="Female over 65 years old population",
                    y_title="Aggregate yearly item-level gross profit by county")
    with col2: 
        county_population_plot(df_county, 
                           x="male_18_24", 
                           y="gross_profit",
                           color=None,
                           trendline="ols",
                           title="",
                           x_title="Male 18 to 24 years old population",
                           y_title="Aggregate yearly item-level gross profit by county")
        county_population_plot(df_county, 
                    x="male_25_34", 
                    y="gross_profit",
                    color=None,
                    trendline="ols",
                    title="",
                    x_title="Male 25 to 34 years old population",
                    y_title="Aggregate yearly item-level gross profit by county")
        county_population_plot(df_county, 
                    x="male_35_44", 
                    y="gross_profit",
                    color=None,
                    trendline="ols",
                    title="",
                    x_title="Male 35 to 44 years old population",
                    y_title="Aggregate yearly item-level gross profit by county")
        county_population_plot(df_county, 
                    x="male_45_64", 
                    y="gross_profit",
                    color=None,
                    trendline="ols",
                    title="",
                    x_title="Male 45 to 64 years old population",
                    y_title="Aggregate yearly item-level gross profit by county")
        county_population_plot(df_county, 
                    x="male_65_over", 
                    y="gross_profit",
                    color=None,
                    trendline="ols",
                    title="",
                    x_title="Male over 65 years old population",
                    y_title="Aggregate yearly item-level gross profit by county")
