import streamlit as st
from pkg.load_data import connect_to_county
from pkg.plotting import store_type_plot

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
df = connect_to_county(table)
df_store = df.groupby(['category'])['gross_profit'].mean().reset_index()
df_county = df.groupby(['category', 'county'])['gross_profit'].mean().reset_index()

tab1, tab2 = st.tabs(["State-Level", " County-Level"])

#############################################################

with tab1:
    st.markdown("""
                - Grocery stores and liquor stores or bars generate the highest average 
                monthly gross profit, followed closely by convenience stores.
                - These top-performing store types likely benefit from high customer traffic 
                and broader product selection.
                - Less common store types, such as pharmacies or gas stations, tend to 
                generate lower average gross profit statewide.
                """)
    
    st.subheader("Average Monthly Gross Profit in Iowa vs Liquor Types")
    store_type_plot(df_store,
                     x="category",
                     y="gross_profit",
                     x_title="Store type",
                     y_title="Average monthly gross profit")

with tab2:
    st.markdown("""
                - In Johnson County, grocery stores and distilleries/breweries report high 
                average monthly gross profit.
                - Liquor stores or bars are top performers in Clinton and Dallas Counties, 
                highlighting their local demand.
                - These differences suggest that optimal store types may vary by region, 
                and tailoring business strategies to local preferences could improve 
                profitability.
                """)

    st.subheader("Average Monthly Gross Profit by County vs Liquor Types")
    store_type_plot(df_county,
                     x="category",
                     y="gross_profit",
                     color="county",
                     x_title="Store type",
                     y_title="Average monthly gross profit")
