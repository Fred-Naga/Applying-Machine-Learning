# https://advanced-computing-fred-naga-lab2-home-jczcrq.streamlit.app/
import streamlit as st

st.set_page_config(page_title="Predictive Analytics for Item-Level Gross Profits in Iowa Liquor Stores",
                   page_icon="🏠")
st.sidebar.header("Fred & Naga")

# st.title('🥂 Predictive Analytics for Item-Level Gross Profits in Iowa Liquor Stores 🍾')

st.markdown(
    """
    <h1 style='text-align: center;'>Predictive Analytics</h1>
    <h1 style='text-align: center;'>🥂 for Item-Level Gross Profits 🍾</h1>
    <h1 style='text-align: center;'>in Iowa Liquor Stores</h1>
    """,
    unsafe_allow_html=True
)

st.header('🍺 Problem',divider=True)
st.markdown('''
            Choosing where to start a business is always a difficult decision. Rather than relying on 
            evidence-based strategies, entrepreneurs often make decisions based on intuition or 
            outdated heuristics, which can lead to significant resource misallocation. A predictive 
            algorithm that estimates item-level gross profit can support data-driven decision making 
            and help entrepreneurs develop successful business strategies. As a first step, we 
            develop an algorithm to project item-level gross profits in liquor stores, using Iowa 
            liquor sales data.          

            **Research Question**
            - How can we leverage demographic, economic, and liquor sales data to develop a 
            predictive algorithm that helps liquor store owners identify optimal store locations and 
            product assortments?
            - Which geographic or socioeconomic groups are most associated with higher alcohol 
            consumption or preferences for specific types of liquor?

            **How to Use**
            - **Business Perspective.** The algorithm identifies which products sell best in 
            different types of areas (e.g., high-income cities may prefer Item B). This enables liquor 
            owners to tailor product assortments based on local demographics to maximize sales and 
            reduce inventory risk.
            - **Policy Perspective.** The model can help policymakers identify areas with high 
            predicted alcohol consumption, allowing for targeted interventions to mitigate public 
            health risks. It may also help local governments optimize alcohol-related tax revenues.
            ''')

st.header('🍷 Data',divider=True)
st.markdown('''
            **Outcome**
            - [Monthly Item-Level Gross Profit by Liquor Store](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data)
            
            **Features**
            - **Month:** Assumes season is one of the important factors influencing consumers' liquor preference.
            - [Adult Population Age Brackets by Gender](https://catalog.data.gov/dataset/iowa-population-18-years-and-over-by-sex-age-and-educational-attainment-acs-5-year-estimat?): This variable includes adult age categorized into the following buckets: (18–24, 25–34, 35–44, 45–64, and 65+) at the county level, separating male and female populations.
            - [Annual Income by County](https://data.iowa.gov/Economic-Statistics/Annual-Personal-Income-for-State-of-Iowa-by-County/st2k-2ti2/about_data): Denotes the county level average income.
            - [Fuel Sales by County](https://data.iowa.gov/Sales-Distribution/Iowa-Motor-Fuel-Sales-by-County-and-Year/hbwp-wys3/about_data) (Used as an interaction term when store type is gas station): Total motor fuel sold during the 2024 calendar year, measured in gallons.
            - [Excessive Drinking Percentage by County](https://www.countyhealthrankings.org/health-data/community-conditions/health-infrastructure/health-promotion-and-harm-reduction/excessive-drinking?state=19&tab=1&year=2025): Percentage of adults reporting binge or heavy drinking in the past 30 days. 
            - **Store Types:** Categories of class "E" liquor selling stores such as: grocery store, liquor store/bar, gas station, pharmacy, distillery/brewery, general store, convenience store, other, or unknown.
            - **Liquors** More detailed liquor items than general liquor types, such as whiskey liqueur, Canadian whisky, aged rum, etc.
            
            **Data Sourcing** 
            - **Iowa Liquor Sales in 2024:** Contains transaciton level records of stores licensed to sell liquor to be consumed off-premise. It includes product details, store name/location, quantities sold, and sale prices.
            - **U.S. Census Bureau American Community Survey (ACS 5-Year Estimates)**: This program aggregates demographic, social, economic, and housing data at a county level. It pools rolling 5-year periods to provide a larger sample size that is more reliable for small population areas.
            - **County Health Rankings**: Jointly run by the University of Wisconsin Population Health Institute and Robert Wood Johnson Foundation, this initiative produces annual rankings of U.S. counties based on health outcomes.    
            ''')

st.header('🍶 Strategy',divider=True)
st.markdown('''
            - Create random forests using training, validation, and testing data.
            - Perform Exploratory Data Analysis (EDA) to verify feature selection.
            - Project monthly item-level gross profits based on the stores' features.
            ''')

st.header('🍸 Limitations',divider=True)
st.markdown('''
            - **Observational data only:** We cannot infer causal relationships, this model is predictive.
            - **Limited external validity:** A model trained on Iowa may not generalize to other states, especially non-Midwestern ones.
            - **Complex interpretation:** Using many features makes it hard to pinpoint individual drivers, particularly after regularization.
            - **Scope of sales data:** We only have liquor transaction data—no beer, wine, or cider.
            - **Missing ancillary purchases:** There’s no data on complementary food or non‑liquor drinks, which could affect item‑level profit.
            ''')

st.header('🍹 Next Steps',divider=True)
st.markdown('''
            - Compare the current model with alternative approaches, such as linear regression.
            - Enhance model performance by incorporating additional features or increasing tree depth. 
            - Use income brackets to better capture income distribution, rather than relying on average county income.
            ''')