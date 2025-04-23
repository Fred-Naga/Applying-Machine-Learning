import pandas_gbq
import pandas as pd

project_id = "solid-dominion-452916-p4"
table_id = 'solid-dominion-452916-p4.aml_fl_tn.city'

# load data
df = pd.read_csv('data/city.csv')

# make a table
pandas_gbq.to_gbq(df,
                  table_id,
                  project_id=project_id,
                  if_exists='replace')