import streamlit as st # added
from google.oauth2 import service_account #added
import pandas_gbq # added

@st.cache_resource
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