import streamlit as st
import plotly.express as px
import pandas as pd

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
    
@st.cache_data
def plot_income_distribution_by_county(df, key=None):
    """
    Creates a 100% stacked bar chart of household income distribution by county,
    using ACS income bracket columns.
    """
    desired_brackets = [
        'less_than_10000', '10000_to_14999', '15000_to_19999',
        '20000_to_24999', '25000_to_29999', '30000_to_34999',
        '35000_to_39999', '40000_to_44999', '45000_to_49999',
        '50000_to_59999', '60000_to_74999', '75000_to_99999',
        '100000_to_124999', '125000_to_149999', '150000_to_199999',
        '200000_or_more'
    ]
    bracket_cols = [col for col in desired_brackets if col in df.columns]

    df_unique = df[['county'] + bracket_cols].drop_duplicates(subset=['county'])
    df_wide = df_unique.groupby('county', as_index=False)[bracket_cols].sum()

    df_perc = df_wide.copy()
    df_perc[bracket_cols] = df_perc[bracket_cols].div(df_perc[bracket_cols].sum(axis=1), axis=0) * 100

    fig = px.bar(
        df_perc,
        x='county',
        y=bracket_cols,
        labels={'value': '% of Households', 'variable': 'Income Bracket'}
    )

    fig.update_layout(
        barmode='stack',
        xaxis_tickangle=-45,
        yaxis=dict(range=[0, 100], title='% of Households', ticksuffix='%', tickformat='.2f'),
        showlegend=False,
        title=None
    )

    st.plotly_chart(fig, use_container_width=True, key=key or 'income_distribution_by_county_all')
    
    
@st.cache_data
def plot_income_heatmap(df, key=None):
    """
    Plots a heatmap of household income distribution by county.
    Rows are counties, columns are income brackets, and values are % of households.
    """
    desired_brackets = [
        'less_than_10000', '10000_to_14999', '15000_to_19999',
        '20000_to_24999', '25000_to_29999', '30000_to_34999',
        '35000_to_39999', '40000_to_44999', '45000_to_49999',
        '50000_to_59999', '60000_to_74999', '75000_to_99999',
        '100000_to_124999', '125000_to_149999', '150000_to_199999',
        '200000_or_more'
    ]
    bracket_cols = [col for col in desired_brackets if col in df.columns]

    df_unique = df[['county'] + bracket_cols].drop_duplicates(subset=['county'])
    df_wide = df_unique.groupby('county', as_index=False)[bracket_cols].sum()

    df_perc = df_wide.copy()
    df_perc[bracket_cols] = df_perc[bracket_cols].div(df_perc[bracket_cols].sum(axis=1), axis=0) * 100

    df_long = df_perc.melt(id_vars='county', var_name='income_bracket', value_name='percentage')

    fig = px.imshow(
        df_long.pivot(index='county', columns='income_bracket', values='percentage').round(2),
        labels=dict(color='% of Households'),
        color_continuous_scale='YlGnBu',
        aspect='auto'
    )

    fig.update_layout(
        title=None,
        xaxis_title="Income Bracket",
        yaxis_title="County",
        xaxis={'side': 'top'},
        coloraxis_colorbar=dict(ticksuffix="%", title='%')
    )

    st.plotly_chart(fig, use_container_width=True, key=key or 'income_distribution_heatmap')


@st.cache_data
def plot_income_pie_by_county(df, county_selected, key=None):
    """
    Displays a pie chart for a selected county's household income bracket distribution.
    """
    desired_brackets = [
        'less_than_10000', '10000_to_14999', '15000_to_19999',
        '20000_to_24999', '25000_to_29999', '30000_to_34999',
        '35000_to_39999', '40000_to_44999', '45000_to_49999',
        '50000_to_59999', '60000_to_74999', '75000_to_99999',
        '100000_to_124999', '125000_to_149999', '150000_to_199999',
        '200000_or_more'
    ]
    bracket_cols = [col for col in desired_brackets if col in df.columns]

    df_unique = df[['county'] + bracket_cols].drop_duplicates(subset=['county'])
    df_grouped = df_unique.groupby('county', as_index=False)[bracket_cols].sum()

    if county_selected not in df_grouped['county'].values:
        st.warning(f"County '{county_selected}' not found.")
        return

    row = df_grouped[df_grouped['county'] == county_selected].iloc[0]
    df_pie = row[bracket_cols].reset_index()
    df_pie.columns = ['income_bracket', 'households']

    fig = px.pie(df_pie, names='income_bracket', values='households', title=f"Income Distribution: {county_selected.title()}")
    st.plotly_chart(fig, use_container_width=True, key=key or f"income_pie_{county_selected}")
