# https://advanced-computing-fred-naga-lab2-home-jczcrq.streamlit.app/
import streamlit as st

st.set_page_config(page_title="Predictive Analytics for Item-Level Gross Profits in Iowa Liquor Stores",
                   page_icon="🥂")
# st.sidebar.header("Fred & Naga")
# 🥂🍾🍹🍻🧉
# 🍺🍷🍶🍸🥃

st.markdown(
    """
    <h1 style='text-align: center;'>Predictive Analytics for Item-Level Gross Profits in Iowa Liquor Stores</h1>
    """,
    unsafe_allow_html=True
)
st.markdown("<h5 style='text-align: right;'>by Fred & Naga</h5>", unsafe_allow_html=True)
st.image("picture/cocktail.jpg", use_container_width=True)

st.header('🥂 Problem',divider=True)
st.markdown('''
            Choosing where to start a business is always a difficult decision. Rather than relying on 
            evidence-based strategies, entrepreneurs often make decisions based on intuition or 
            outdated heuristics, which can lead to significant resource misallocation. A predictive 
            algorithm that estimates item-level gross profit can support data-driven decision making 
            and help entrepreneurs develop successful business strategies. As a first step, we 
            develop an algorithm to project item-level gross profits in liquor stores, using Iowa 
            liquor sales data.          

            <u><b>Research Questions</b></u>
            - How can we leverage demographic, economic, and liquor sales data to develop a 
            predictive algorithm that helps liquor store owners identify optimal store locations and 
            product assortments?
            - Which geographic or socioeconomic groups are most associated with higher alcohol 
            consumption or preferences for specific types of liquor?

            <u><b>How to Use</b></u>
            - **Business Perspective:** The algorithm identifies which products sell best in 
            different types of areas (e.g., high-income cities may prefer Item B). This enables liquor 
            owners to tailor product assortments based on local demographics to maximize sales and 
            reduce inventory risk.
            - **Policy Perspective:** The model can help policymakers identify areas with high 
            predicted alcohol consumption, allowing for targeted interventions to mitigate public 
            health risks. It may also help local governments optimize alcohol-related tax revenues.
            ''',
            unsafe_allow_html=True)

st.header('🍷 Data',divider=True)
st.markdown('''<u><b>Outcome</b></u>''', unsafe_allow_html=True)
st.markdown('''
            - `gross_profit`: [Monthly item-level gross profit by store](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data). Gross profit by sold liquors.
            ''',
            unsafe_allow_html=True)
st.markdown('''<u><b>Features</b></u>''', unsafe_allow_html=True)
st.markdown('''
    1. `month`: [Months](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data). Assumes season is one of the important factors influencing consumers' liquor preference.
    2. `s_(store type)`: [Store types](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data). Categories of class "E" liquor selling stores such as: grocery store, liquor store/bar, gas station, pharmacy, distillery/brewery, general store, convenience store, other, or unknown.
    3. `l_(liquor type)`: [Liquor liters by types](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data). Liters for sold liquor types, such as whiskey liqueur, Canadian whisky, and aged rum.
    4. `c_(county)`: Counties. Since we are considering only stores in Iowa, this variable alone is used to capture geographical characteristics when creating the algorithm. However, we conduct exploratory data analysis using the following features to capture the effects of each county-level characteristic on gross profit.
        - [Adult population age brackets by gender](https://catalog.data.gov/dataset/iowa-population-18-years-and-over-by-sex-age-and-educational-attainment-acs-5-year-estimat?): This variable includes adult age categorized into the following buckets: (18–24, 25–34, 35–44, 45–64, and 65+) at the county level, separating male and female populations.
        - [Annual income](https://data.iowa.gov/Economic-Statistics/Annual-Personal-Income-for-State-of-Iowa-by-County/st2k-2ti2/about_data): Denotes the county level average income.
        - [Fuel sales](https://data.iowa.gov/Sales-Distribution/Iowa-Motor-Fuel-Sales-by-County-and-Year/hbwp-wys3/about_data) (Used as an interaction term when store type is gas station): Total motor fuel sold during the 2024 calendar year, measured in gallons.
        - [Excessive drinking percentage](https://www.countyhealthrankings.org/health-data/community-conditions/health-infrastructure/health-promotion-and-harm-reduction/excessive-drinking?state=19&tab=1&year=2025): Percentage of adults reporting binge or heavy drinking in the past 30 days. 
    ''')
st.markdown('''<u><b>Data Source</b></u>''',unsafe_allow_html=True)
st.markdown('''
    - **Liquor Sales of Iowa Open Data:** Contains transaciton level records of stores licensed to sell liquor to be consumed off-premise. It includes product details, store name/location, quantities sold, and sale prices.
    - **Fuel Sales of Iowa Open Data:** This dataset provides information on the total gallons of motor fuel sold in Iowa by county.
    - **U.S. Census Bureau American Community Survey (ACS 5-Year Estimates):** This program aggregates demographic, social, economic, and housing data at a county level. It pools rolling 5-year periods to provide a larger sample size that is more reliable for small population areas.
    - **County Health Rankings:** Jointly run by the University of Wisconsin Population Health Institute and Robert Wood Johnson Foundation, this initiative produces annual rankings of U.S. counties based on health outcomes.    
    ''')
st.markdown("<u><b>Explanatory Data Analysis (EDA)</b></u>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("EDA: Month"):
        st.switch_page("pages/1_EDA:_Month.py")
    if st.button("EDA: Income"):
        st.switch_page("pages/5_EDA:_Income.py")
with col2:
    if st.button("EDA: Store Types"):
        st.switch_page("pages/2_EDA:_Store_Types.py")
    if st.button("EDA: Fuel Sales"):
        st.switch_page("pages/6_EDA:_Fuel_Sales.py")
with col3:
    if st.button("EDA: Liquor Types"):
        st.switch_page("pages/3_EDA:_Liquor_Types.py")
    if st.button("EDA: Excessive_Drinking"):
        st.switch_page("pages/7_EDA:_Excessive_Drinking.py")
with col4:
    if st.button("EDA: Population"):
        st.switch_page("pages/4_EDA:_Population.py")

st.header('🍶 Strategy',divider=True)
st.markdown('''
            - Create two algorithms and compare them with each other: the ridge regression 
            model and random forest model. 
            - In both models, 70%, 15% and 15% of data are used as training, validation, 
            and testing data, respectively.
            - Perform Exploratory Data Analysis (EDA) for all the features to verify 
            their effects on monthly gross profit.
            - Project monthly item-level gross profits based on 2024 liquor transactions 
            by store in Iowa.
            ''')
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Algorithm: Ridge Regression"):
        st.switch_page("pages/8_Algorithm:_Ridge_Regression.py")
with col2:
    if st.button("Algorithm: Random Forest"):
        st.switch_page("pages/9_Algorithm:_Random_Forest.py")
with col3:
    if st.button("Demonstration for Decision Makers"):
        st.switch_page("pages/10_Demonstration_for Decision_Makers.py")
st.image("picture/algorithm.png",
         caption="Image of the algorithm",
         use_container_width=True)

st.header('🍸 Limitations',divider=True)
st.markdown('''
            - **Observational data only:** We cannot infer causal relationships as this 
            model is only predictive.
            - **Limited external validity:** A model trained on Iowa may not generalize 
            to other states, especially non-Midwestern ones.
            - **Complex interpretation:** Using many features makes it hard to pinpoint 
            individual drivers, particularly after regularization.
            - **Scope of sales data:** We only have liquor transaction, not inventory data. 
            Additionally, they do not include beer, wine, or cider.
            - **Missing ancillary purchases:** There’s no data on complementary food or 
            non‑liquor drinks, which could affect gross profit.
            ''')

# st.header('🍹 Next Steps',divider=True)
# st.markdown('''
#             - Compare the current model with alternative approaches, such as linear regression.
#             - Enhance model performance by incorporating additional features or increasing tree depth. 
#             - Use income brackets to better capture income distribution, rather than relying on average county income.
#             ''')