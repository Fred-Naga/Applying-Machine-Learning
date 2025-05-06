import streamlit as st
from pkg.load_data import connect_to_county
from pkg.plotting import store_type_plot, plot_store_type_profit_by_county, plot_total_profit_by_store_type
from pkg.mapping import map_store_count_choropleth

st.set_page_config(page_title="Store Types", page_icon="🍹")
st.header('🍹 Explanatory Data Analysis: Store Types',divider=True)
st.markdown('''
            This section explores how different store types contribute to average monthly 
            gross profit from liquor sales in Iowa. By analyzing both statewide and 
            county-level trends, we aim to identify which types of stores tend to be the most 
            profitable, providing insights for business planning, licensing strategies, and 
            market targeting.
            ''')

table='solid-dominion-452916-p4.aml_fl_tn.store_type'
url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
df = connect_to_county(table)
df_store = df.groupby(['category', 'county', 'store'])['gross_profit'].mean().reset_index()
df_county = df.groupby(['category', 'county'])['gross_profit'].mean().reset_index()


table2='solid-dominion-452916-p4.aml_fl_tn.county'
df_fips = connect_to_county(table2)
df_fips = df_fips[['county', 'fips']]

df_store = df_store.merge(df_fips[['county', 'fips']], on='county', how='left')

store_types = df_store['category'].dropna().unique().tolist()
store_types.sort()
store_types.insert(0, "All")


tab1, tab2, tab3 = st.tabs(["Map", "State-Level", " County-Level"])

#############################################################

with tab1:
    st.markdown("""
                - Polk county has the most stores by far (293 total), while the minimum includes Davis and Ringgold with 2 stores each.
                - All but 3 counties have at least 1 grocery store and 1 gas station. Most counties in the south do not have a liquor store or bar.
                - The remaining categories are not present throughout the majority of Iowa counties.
                """)
    
    st.subheader("Count of Stores by County")
    
    # Selectbox for user input
    selected_store_type = st.selectbox("Select store type", store_types)

    # Filter the dataframe
    if selected_store_type != "All":
        df_filtered = df_store[df_store["category"] == selected_store_type]
    else:
        df_filtered = df_store.copy()

    # Plot the map
    map_store_count_choropleth(df_filtered, url, key=f"store_map_{selected_store_type}")

with tab2:
    st.markdown("""
                - Grocery stores and liquor stores or bars generate the highest average 
                monthly gross profit, followed closely by convenience stores.
                - These top-performing store types likely benefit from high customer traffic 
                and broader product selection.
                - Specific categories, such as pharmacies or gas stations, tend to 
                generate lower average gross profit statewide.
                """)
    
    st.subheader("Average Monthly Gross Profit by Store Type")
    store_type_plot(df_store,
                     x="category",
                     y="gross_profit",
                     x_title="Store type",
                     y_title="Average monthly gross profit")
    
    st.subheader("Average Monthly Gross Profit in Iowa by Store Type")
    plot_total_profit_by_store_type(df_store)

with tab3:
    st.markdown("""
                - In Johnson County, grocery stores and distilleries/breweries report high 
                average monthly gross profit.
                - Liquor stores or bars are top performers in Clinton and Dallas Counties, 
                highlighting their local demand.
                - Grocery stores accounts for a large portion of metropolitan county profits, which suggests that customers buy liquor as an ancillary to food.
                """)

    st.subheader("Average Monthly Gross Profit by County vs Store Types")
    store_type_plot(df_county,
                     x="category",
                     y="gross_profit",
                     color="county",
                     x_title="Store type",
                     y_title="Average monthly gross profit")
    
    st.subheader("Gross Profit by Store Type")
    
    counties = df_store["county"].dropna().unique()
    selected_counties = st.multiselect(
        "Select counties to compare summed store-type profits:",
        options=sorted(counties),
        default=["polk", "linn", "scott", 'johnson', 'woodbury']  # or whatever default you'd like
    )
    plot_store_type_profit_by_county(df_store, counties=selected_counties)
