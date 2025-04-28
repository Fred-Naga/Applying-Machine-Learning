import streamlit as st

st.set_page_config(page_title="Demonstration", page_icon="🥂")
st.header('🥂 Demonstration',divider=True)

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

# months
months = [ "January", "February", "March", "April", "May", "June",
           "July", "August", "September", "October", "November", "December" ]

# store types
store_types = [
    "Convenience Store", "Distillery Brewery", "Gas Station", "General Store",
    "Grocery Store", "Liquor Store or Bar", "Pharmacy", "Other"
]

# liquor_types = [
#     "100 Agave Tequila", "Aged Dark Rum", "American Brandies", "American Cordials & Liqueurs",
#     "American Distilled Spirits Specialty", "American Dry Gins", "American Flavored Vodka",
#     "American Schnapps", "American Sloe Gins", "American Vodkas", "Blended Whiskies",
#     "Bottled-in-Bond Bourbon", "Canadian Whiskies", "Cocktails (Ready to Drink)",
#     "Coffee Liqueurs", "Corn Whiskies", "Cream Liqueurs", "Flavored Gin", "Flavored Rum",
#     "Gold Rum", "Imported Brandies", "Imported Cordials & Liqueurs", "Imported Distilled Spirits Specialty",
#     "Imported Dry Gins", "Imported Flavored Vodka", "Imported Schnapps", "Imported Vodkas",
#     "Irish Whiskies", "Mezcal", "Mixto Tequila", "Neutral Grain Spirits",
#     "Neutral Grain Spirits (Flavored)", "Scotch Whiskies", "Single Barrel Bourbon Whiskies",
#     "Single Malt Scotch", "Special Order Items", "Spiced Rum", "Straight Bourbon Whiskies",
#     "Straight Rye Whiskies", "Temporary Specialty Packages", "Tennessee Whiskies",
#     "Triple Sec", "Whiskey Liqueur", "White Rum"
# ]

# liquor types
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

# # Q1: County
# with col1:
#     st.markdown("**1. In which county are you planning to open a liquor store in Iowa?**")
# with col2:
#     selected_county = st.selectbox("Select County", counties)

# # Q2: Month
# with col1:
#     st.markdown("**2. For which month would you like to project the item-level gross profit?**")
# with col2:
#     selected_month = st.selectbox("Select Month", months)

# # Q3: Store Type
# with col1:
#     st.markdown("**3. What type of store are you planning to open?**")
# with col2:
#     selected_store_type = st.selectbox("Select Store Type", store_types)

# # Q4: Liquor Types
# with col1:
#     st.markdown("**4. How many liters of each of the following liquor types will you stock?**")
# with col2:
#     liquor_stock = {}
#     for liquor in liquor_types:
#         liters = st.number_input(f"{liquor} (liters)", min_value=0.0, step=0.1)
#         liquor_stock[liquor] = liters

if st.button("Submit"):
    st.write("Selected County:", selected_county)
    st.write("Selected Month:", selected_month)
    st.write("Store Type:", selected_store_type)
    st.write("Liquor Stock:", liquor_stock_1, liquor_stock_2, liquor_stock_3)
