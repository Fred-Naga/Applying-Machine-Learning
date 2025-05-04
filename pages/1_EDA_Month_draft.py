import streamlit as st
from pkg.load_data import connect_to_county, connect_to_month
from pkg.mapping import gross_profit_map
from pkg.plotting import county_month_plot, month_plot

st.set_page_config(page_title="Month", page_icon="🍾")
st.header('🍾 Explanatory Data Analysis: Month',divider=True)
st.markdown('''
            We explore seasonal trends in item-level gross profit across Iowa by using 
            state- and county-level data. Additionally, county-level aggregations provide 
            insight into whether these trends hold consistently across different regions.
            ''')

# county data
table='solid-dominion-452916-p4.aml_fl_tn.county_with_month'
df = connect_to_county(table)
df_month = df.groupby(['month'])['gross_profit'].sum().reset_index()
df_county = df.groupby(['county', 'month'])['gross_profit'].sum().reset_index()

# store data
table2='solid-dominion-452916-p4.aml_fl_tn.iowa_with_month'
df_jan = connect_to_month(table2, month=1)
# df_feb = connect_to_month(table2, month=2)
# df_mar = connect_to_month(table2, month=3)
df_apr = connect_to_month(table2, month=4)
#df_may = connect_to_month(table2, month=5)
#df_jun = connect_to_month(table2, month=6)
df_jul = connect_to_month(table2, month=7)
#df_aug = connect_to_month(table2, month=8)
#df_sep = connect_to_month(table2, month=9)
df_oct = connect_to_month(table2, month=10)
#df_nov = connect_to_month(table2, month=11)
#df_dec = connect_to_month(table2, month=12)

tab1, tab2, tab3 = st.tabs(["Map", "State-Level", "County-Level"])

#############################################################

with tab1:
    st.markdown("""
               - To capture seasonal patterns, we focused on four 
                representative months: January (winter), April (spring), 
                July (summer), and October (fall).
                - Spatial distribution of gross profit remains relatively 
                consistent across these months, with clusters of high profit 
                concentrated in a few urban areas.
                - This concentration likely reflects underlying population 
                density and economic activity, rather than seasonal shifts.
                """)
    
    st.subheader("Monthly Item-Level Gross Profit by Store")
    col1, col2 = st.columns(2)
    with col1:
        st.write("January")
        gross_profit_map(df_jan)
        # st.write("March")
        # gross_profit_map(df_mar)
        # st.write("May")
        # gross_profit_map(df_may)
        st.write("July")
        gross_profit_map(df_jul)
        # st.write("September")
        # gross_profit_map(df_sep)
        # st.write("November")
        # gross_profit_map(df_nov)
    with col2:
        # st.write("February")
        # gross_profit_map(df_feb)
        st.write("April")
        gross_profit_map(df_apr)
        # st.write("June")
        # gross_profit_map(df_jun)
        # st.write("August")
        # gross_profit_map(df_aug)
        st.write("October")
        gross_profit_map(df_oct)
        # st.write("December")
        # gross_profit_map(df_dec)

with tab2:
    st.markdown("""
                - At the state level, gross profit peaks in October and hits a 
                low in January, suggesting a seasonal effect on liquor sales.
                - The sharp rise from January to October suggests that demand 
                may be influenced by weather, holidays, or economic cycles.
                """)

    st.subheader("Aggregate Gross Profit in Iowa vs Month")
    month_plot(df_month, 
               x="month", 
               y="gross_profit",
               x_title="Month", 
               y_title="Aggregate gross profit in Iowa")
    
with tab3:
    st.markdown("""
                - County-level trends mirror the state-level pattern, indicating 
                a consistent seasonal cycle across regions.
                """)
    
    st.subheader("Aggregate Gross Profit by County vs Month")
    county_month_plot(df_county, 
                      x="month", 
                      y="gross_profit",
                      color="county",
                      x_title="Month", 
                      y_title="Aggregate gross profit by county")
