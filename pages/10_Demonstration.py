import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

st.set_page_config(page_title="Demonstration", page_icon="🥂")
st.header('🥂 Demonstration',divider=True)

# month
months = [ "January", "February", "March", "April", "May", "June",
           "July", "August", "September", "October", "November", "December" ]

# store type
store_types = [
    "Convenience Store", "Distillery Brewery", "Gas Station", "General Store",
    "Grocery Store", "Liquor Store or Bar", "Pharmacy", "Other"
]

# liquor type
liquor_types_1 = [
    "100 Agave Tequila", "Aged Dark Rum", "American Brandies", "American Cordials & Liqueurs",
    "American Distilled Spirits Specialty", "American Dry Gins", "American Flavored Vodka",
    "American Schnapps", "American Sloe Gins", "American Vodkas", "Blended Whiskies",
    "Bottled-in-Bond Bourbon", "Canadian Whiskies", "Cocktails (Ready to Drink)",
    "Coffee Liqueurs"
]
liquor_types_2 = [
    "Corn Whiskies", "Cream Liqueurs", "Flavored Gin", "Flavored Rum",
    "Gold Rum", "Imported Brandies", "Imported Cordials & Liqueurs", "Imported Distilled Spirits Specialty",
    "Imported Dry Gins", "Imported Flavored Vodka", "Imported Schnapps", "Imported Vodkas",
    "Irish Whiskies", "Mezcal", "Mixto Tequila"
]
liquor_types_3 = [
    "Neutral Grain Spirits", "Neutral Grain Spirits (Flavored)", "Scotch Whiskies", 
    "Single Barrel Bourbon Whiskies", "Single Malt Scotch", "Special Order Items", 
    "Spiced Rum", "Straight Bourbon Whiskies", "Straight Rye Whiskies", 
    "Temporary Specialty Packages", "Tennessee Whiskies", "Triple Sec", "Whiskey Liqueur", 
    "White Rum"
]

# county
counties = [
    "Adair", "Adams", "Allamakee", "Appanoose", "Audubon", "Benton", "Black Hawk",
    "Boone", "Bremer", "Buchanan", "Buena Vista", "Butler", "Calhoun", "Carroll",
    "Cass", "Cedar", "Cerro Gordo", "Cherokee", "Chickasaw", "Clarke", "Clay",
    "Clayton", "Clinton", "Crawford", "Dallas", "Davis", "Decatur", "Delaware",
    "Des Moines", "Dickinson", "Dubuque", "Emmet", "Fayette", "Floyd", "Franklin",
    "Fremont", "Greene", "Grundy", "Guthrie", "Hamilton", "Hancock", "Hardin",
    "Harrison", "Henry", "Howard", "Humboldt", "Ida", "Iowa", "Jackson", "Jasper",
    "Jefferson", "Johnson", "Jones", "Keokuk", "Kossuth", "Lee", "Linn", "Louisa",
    "Lucas", "Lyon", "Madison", "Mahaska", "Marion", "Marshall", "Mills", "Mitchell",
    "Monona", "Monroe", "Montgomery", "Muscatine", "O'Brien", "Osceola", "Page",
    "Palo Alto", "Plymouth", "Pocahontas", "Polk", "Pottawattamie", "Poweshiek",
    "Ringgold", "Sac", "Scott", "Shelby", "Sioux", "Story", "Tama", "Taylor", "Union",
    "Van Buren", "Wapello", "Warren", "Washington", "Wayne", "Webster", "Winnebago",
    "Winneshiek", "Woodbury", "Worth", "Wright"
]

# Q1: County
st.markdown("**Q1. In which county are you planning to open a liquor store in Iowa?**")
selected_county = st.selectbox("Select County", counties)

# Q2: Month
st.markdown("**Q2. For which month would you like to project the item-level gross profit?**")
selected_month = st.selectbox("Select Month", months)

# Q3: Store Type
st.markdown("**Q3. What type of store are you planning to open?**")
selected_store_type = st.selectbox("Select Store Type", store_types)

# Q4: Liquor Types
st.markdown("**Q4. How many liters of each of the following liquor types will you stock?**")

col1, col2, col3 = st.columns(3)

with col1:
    liquor_stock_1 = {}
    for liquor in liquor_types_1:
        liters = st.number_input(liquor, min_value=0.0, step=0.1)
        liquor_stock_1[liquor] = liters

with col2:
    liquor_stock_2 = {}
    for liquor in liquor_types_2:
        liters = st.number_input(liquor, min_value=0.0, step=0.1)
        liquor_stock_2[liquor] = liters

with col3:
    liquor_stock_3 = {}
    for liquor in liquor_types_3:
        liters = st.number_input(liquor, min_value=0.0, step=0.1)
        liquor_stock_3[liquor] = liters

# Submission
if st.button("Submit"):

    # month
    month_mapping = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, 
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
    }
    month_value = month_mapping[selected_month]

    # store type
    store_variables = {
        "s_convenience_store": 0,
        "s_distillery_brewery": 0,
        "s_gas_station": 0,
        "s_general_store": 0,
        "s_grocery_store": 0,
        "s_liquor_store_bar": 0,
        "s_other": 0,
        "s_pharmacy": 0,
        "s_unknown": 0
    }
    store_mapping = {
        "Convenience Store": "s_convenience_store",
        "Distillery Brewery": "s_distillery_brewery",
        "Gas Station": "s_gas_station",
        "General Store": "s_general_store",
        "Grocery Store": "s_grocery_store",
        "Liquor Store or Bar": "s_liquor_store_bar",
        "Pharmacy": "s_pharmacy",
        "Other": "s_other"
    }
    selected_store_var = store_mapping[selected_store_type]
    store_variables[selected_store_var] = 1

    # county
    county_variables = {f"c_{county.lower()}": 0 for county in counties}
    selected_county_var = f"c_{selected_county.lower()}"
    county_variables[selected_county_var] = 1

    # liquor type
    liquor_variables = {
        "l_100_agave_tequila": 0,
        "l_aged_dark_rum": 0,
        "l_american_brandies": 0,
        "l_american_cordials_liqueurs": 0,
        "l_american_distilled_spirits_specialty": 0,
        "l_american_dry_gins": 0,
        "l_american_flavored_vodka": 0,
        "l_american_schnapps": 0,
        "l_american_sloe_gins": 0,
        "l_american_vodkas": 0,
        "l_blended_whiskies": 0,
        "l_bottled_in_bond_bourbon": 0,
        "l_canadian_whiskies": 0,
        "l_cocktails_rtd": 0,
        "l_coffee_liqueurs": 0,
        "l_corn_whiskies": 0,
        "l_cream_liqueurs": 0,
        "l_flavored_gin": 0,
        "l_flavored_rum": 0,
        "l_gold_rum": 0,
        "l_imported_brandies": 0,
        "l_imported_cordials_liqueurs": 0,
        "l_imported_distilled_spirits_specialty": 0,
        "l_imported_dry_gins": 0,
        "l_imported_flavored_vodka": 0,
        "l_imported_schnapps": 0,
        "l_imported_vodkas": 0,
        "l_irish_whiskies": 0,
        "l_mezcal": 0,
        "l_mixto_tequila": 0,
        "l_neutral_grain_spirits": 0,
        "l_neutral_grain_spirits_flavored": 0,
        "l_scotch_whiskies": 0,
        "l_single_barrel_bourbon_whiskies": 0,
        "l_single_malt_scotch": 0,
        "l_special_order_items": 0,
        "l_spiced_rum": 0,
        "l_straight_bourbon_whiskies": 0,
        "l_straight_rye_whiskies": 0,
        "l_temporary_specialty_packages": 0,
        "l_tennessee_whiskies": 0,
        "l_triple_sec": 0,
        "l_whiskey_liqueur": 0,
        "l_white_rum": 0
    }
    liquor_mapping = {
        "100 Agave Tequila": "l_100_agave_tequila",
        "Aged Dark Rum": "l_aged_dark_rum",
        "American Brandies": "l_american_brandies",
        "American Cordials & Liqueurs": "l_american_cordials_liqueurs",
        "American Distilled Spirits Specialty": "l_american_distilled_spirits_specialty",
        "American Dry Gins": "l_american_dry_gins",
        "American Flavored Vodka": "l_american_flavored_vodka",
        "American Schnapps": "l_american_schnapps",
        "American Sloe Gins": "l_american_sloe_gins",
        "American Vodkas": "l_american_vodkas",
        "Blended Whiskies": "l_blended_whiskies",
        "Bottled-in-Bond Bourbon": "l_bottled_in_bond_bourbon",
        "Canadian Whiskies": "l_canadian_whiskies",
        "Cocktails (Ready to Drink)": "l_cocktails_rtd",
        "Coffee Liqueurs": "l_coffee_liqueurs",
        "Corn Whiskies": "l_corn_whiskies",
        "Cream Liqueurs": "l_cream_liqueurs",
        "Flavored Gin": "l_flavored_gin",
        "Flavored Rum": "l_flavored_rum",
        "Gold Rum": "l_gold_rum",
        "Imported Brandies": "l_imported_brandies",
        "Imported Cordials & Liqueurs": "l_imported_cordials_liqueurs",
        "Imported Distilled Spirits Specialty": "l_imported_distilled_spirits_specialty",
        "Imported Dry Gins": "l_imported_dry_gins",
        "Imported Flavored Vodka": "l_imported_flavored_vodka",
        "Imported Schnapps": "l_imported_schnapps",
        "Imported Vodkas": "l_imported_vodkas",
        "Irish Whiskies": "l_irish_whiskies",
        "Mezcal": "l_mezcal",
        "Mixto Tequila": "l_mixto_tequila",
        "Neutral Grain Spirits": "l_neutral_grain_spirits",
        "Neutral Grain Spirits (Flavored)": "l_neutral_grain_spirits_flavored",
        "Scotch Whiskies": "l_scotch_whiskies",
        "Single Barrel Bourbon Whiskies": "l_single_barrel_bourbon_whiskies",
        "Single Malt Scotch": "l_single_malt_scotch",
        "Special Order Items": "l_special_order_items",
        "Spiced Rum": "l_spiced_rum",
        "Straight Bourbon Whiskies": "l_straight_bourbon_whiskies",
        "Straight Rye Whiskies": "l_straight_rye_whiskies",
        "Temporary Specialty Packages": "l_temporary_specialty_packages",
        "Tennessee Whiskies": "l_tennessee_whiskies",
        "Triple Sec": "l_triple_sec",
        "Whiskey Liqueur": "l_whiskey_liqueur",
        "White Rum": "l_white_rum"
    }
    all_liquor_stock = {**liquor_stock_1, **liquor_stock_2, **liquor_stock_3}
    for liquor_name, amount in all_liquor_stock.items():
        if liquor_name in liquor_mapping:
            mapped_liquor_var = liquor_mapping[liquor_name]
            liquor_variables[mapped_liquor_var] = amount

    # X
    full_features = {
        "month": month_value,
        **store_variables,
        **county_variables,
        **liquor_variables
    }
    X_sample = pd.DataFrame([full_features])
    X_long = pd.melt(X_sample, var_name='feat', value_name='value')
    
    # random forest model
    df = pd.read_csv('data/iowa_algorithm.csv')
    X = df.drop(columns=['store', 'city', 'liter', 'gross_profit'])
    y = df['gross_profit']
    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.15, random_state=123)
    X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.176, random_state=123)
    forest_test = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=100)
    forest_test.fit(X_train, y_train)
    prediction = forest_test.predict(X_sample)

    col1, col2 = st.columns(2)
    with col1:
        st.write("Input Features:")
        X_long
       
    with col2:        
        # st.write("Month:", selected_month)
        # st.write("Store Type:", selected_store_type)
        # st.write("County:", selected_county)
        st.write("Predicted Gross Profit:")
        st.write(f"${prediction[0]:,.2f}")