import streamlit as st
import plotly.express as px

def county_population_plot(df, x, y, 
                           color=None, trendline=None,
                           title="", x_title="", y_title=""):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color if color else None,     
        hover_data={"county": True, x: False, y: False},
        trendline=trendline if trendline else None, 
        labels={title: title, x: x_title, y: y_title},
    )
    fig.update_layout(showlegend=False, height=500)
    st.plotly_chart(fig, use_container_width=True)

def city_population_plot(df, x, y, color=None, trendline=None,
                         title="", x_title="", y_title=""):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color if color else None,     
        hover_data={"city": True, x: False, y: False},
        trendline=trendline if trendline else None,
        labels={title: title, x: x_title, y: y_title},
    )
    fig.update_layout(showlegend=False, height=500)
    st.plotly_chart(fig, use_container_width=True)
    
def income_histogram_plot(df, bins=30):

    fig = px.histogram(
        df,
        x="annual_income",
        nbins=bins,
        title="",
        labels={"annual_income": "Annual Income", "count": "Number of Counties"}
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)    
    

@st.cache_data
def plot_price_range_histogram(df):

    fig = px.histogram(
        df,
        x="price_range",
        color="price_range",
        category_orders={"price_range": ["cheap", "medium", "expensive"]},
        labels={"price_range": "Price Category", "count": "Number of Items"},
        title=""
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

def month_plot(df, x, y, color=None, trendline=None, 
               title="", x_title="", y_title=""):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color if color else None,   
        trendline=trendline if trendline else None, 
        labels={title: title, x: x_title, y: y_title},
    )
    fig.update_layout(showlegend=False, height=500)
    st.plotly_chart(fig, use_container_width=True)

def county_month_plot(df, x, y, 
                      color=None, trendline=None,
                      title="", x_title="", y_title=""):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color if color else None,     
        hover_data={"county": True, x: False, y: False},
        trendline=trendline if trendline else None, 
        labels={title: title, x: x_title, y: y_title},
    )
    fig.update_layout(showlegend=False, height=500)
    st.plotly_chart(fig, use_container_width=True)

def liquor_type_plot(df, x, y, color=None, trendline=None, 
                     title="", x_title="", y_title=""):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color if color else None,
        trendline=trendline if trendline else None,
        labels={x: x_title, y: y_title}
    )
    fig.update_layout(
        showlegend=False,
        height=500,
        margin=dict(l=10, r=10, t=30, b=150), 
        xaxis=dict(
            tickangle=-45,         
            tickfont=dict(size=8) 
        )
    )
    st.plotly_chart(fig, use_container_width=True)

def store_type_plot(df, x, y, 
                      color=None, trendline=None,
                      title="", x_title="", y_title=""):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color if color else None,     
        trendline=trendline if trendline else None, 
        labels={title: title, x: x_title, y: y_title},
    )
    fig.update_layout(showlegend=False, 
                      height=500,
                      xaxis=dict(tickangle=-45))
    st.plotly_chart(fig, use_container_width=True)