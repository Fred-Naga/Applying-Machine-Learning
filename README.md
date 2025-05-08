# Predictive Analytics for Item-Level Gross Profits in Iowa Liquor Stores

## Problem
Choosing where to start a business is always a difficult decision. Rather than relying on evidence-based strategies, entrepreneurs often make decisions based on intuition or outdated heuristics, which can lead to significant resource misallocation. A predictive algorithm that estimates item-level gross profit can support data-driven decision making and help entrepreneurs develop successful business strategies.
As a first step, we develop an algorithm to project item-level gross profits in liquor stores, using Iowa liquor sales data.

### Research Questions
- How can we leverage demographic, economic, and liquor sales data to develop a predictive algorithm that helps liquor store owners identify optimal store locations and product assortments?
- Which geographic or socioeconomic groups are most associated with higher alcohol consumption or preferences for specific types of liquor?

### How to Use
- **Business Perspective:** The algorithm identifies which products sell best in different types of areas (e.g., high-income cities may prefer Item B). This enables liquor owners to tailor product assortments based on local demographics to maximize sales and reduce inventory risk.
- **Policy Perspective:** The model can help policymakers identify areas with high predicted alcohol consumption, allowing for targeted interventions to mitigate public health risks. It may also help local governments optimize alcohol-related tax revenues.

## Data

### Outcome
- `gross_profit`: [Monthly item-level gross profit by store](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data)

### Features
1. `month`: [Months](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data)
2. `s_(store type)`: [Store types](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data)
3. `l_(liquor type)`: [Liquor liters by type](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data)
4. `c_(county)`:
   - [Adult population age brackets by gender](https://catalog.data.gov/dataset/iowa-population-18-years-and-over-by-sex-age-and-educational-attainment-acs-5-year-estimat?)
   - [Annual income brackets](https://data.census.gov/table?q=B19001&g=040XX00US19$0500000_860XX00US78940)
   - [Fuel sales](https://data.iowa.gov/Sales-Distribution/Iowa-Motor-Fuel-Sales-by-County-and-Year/hbwp-wys3/about_data)
   - [Excessive drinking (%)](https://www.countyhealthrankings.org/health-data/community-conditions/health-infrastructure/health-promotion-and-harm-reduction/excessive-drinking?state=19&tab=1&year=2025)

## Strategy
- Compare two algorithms: Ridge Regression and Random Forest
- Data split: 70% training, 15% validation, 15% testing
- Conduct EDA to validate feature importance
- Predict monthly item-level gross profit for Iowa in 2024

## Limitations
- **Observational data only:** Causal inference is not possible
- **Limited external validity:** Model may not generalize beyond Iowa
- **Complex interpretation:** Many features complicate clarity
- **Sales data scope:** 2024 data only; excludes beer, wine, cider
- **Missing ancillary purchases:** No data on food or non-liquor items

