import streamlit as st # added
from google.cloud import storage
from google.oauth2 import service_account #added
import pandas_gbq # added
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
import joblib
import tempfile
import requests

#@st.cache_resource
def connect_to_county(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT *
    FROM `{table}`
    """
    
    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def connect_to_city(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT *
    FROM `{table}`
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def connect_to_iowa(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT store,
            city,
            county,
            pop_city,
            pop_county,
            gross_profit,
            annual_income,
    FROM `{table}`
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def connect_to_spring(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT latitude, 
            longitude,
            city,
            county,
            pop_city,
            gross_profit,
    FROM `{table}`
    WHERE month=3 OR month=4 OR month=5
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def connect_to_summer(table):
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT latitude, 
           longitude,
           city,
           county,
           gross_profit
    FROM `{table}`
    WHERE month=6 OR month=7 OR month=8
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def connect_to_fall(table):
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT latitude, 
           longitude,
           city,
           county,
           gross_profit
    FROM `{table}`
    WHERE month=9 OR month=10 OR month=11
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def connect_to_winter(table):
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT latitude, 
           longitude,
           city,
           county,
           gross_profit
    FROM `{table}`
    WHERE month=12 OR month=1 OR month=2
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def connect_to_iowa_algorithm(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT *
    FROM `{table}`
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def random_forest1(url):
    # X = df.drop(columns=['store', 'city', 'liter', 'gross_profit'])
    # y = df['gross_profit']
    # X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.15, random_state=123)
    # X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.176, random_state=123)
    # forest_model = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=100)
    # return forest_model.fit(X_train, y_train)

    response = requests.get(url)
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(response.content)
        tmp_file_path = tmp_file.name
    model = joblib.load(tmp_file_path)

    return model

@st.cache_resource
def random_forest(bucket_name, blob_name):
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)
    client = storage.Client(credentials=credentials)
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        blob.download_to_filename(tmp_file.name)
        tmp_file_path = tmp_file.name

    model = joblib.load(tmp_file_path)

    return model

@st.cache_resource
def connect_to_month(table, month):
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT latitude, 
           longitude,
           city,
           county,
           gross_profit
    FROM `{table}`
    WHERE month={month}
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)