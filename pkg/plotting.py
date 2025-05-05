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

def liquor_type_plot(df, x, y, counties=None, color=None, trendline=None, 
                     title="", x_title="", y_title=""):
    
    if counties:
        df = df[df['county'].isin(counties)]
        
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

@st.cache_data
def plot_sales_profit_pie_by_county(df, county_selected, key=None):
    """
    Displays side-by-side pie charts for a selected county's liquor sales and gross-profit distributions by liquor type,
    grouping all categories below 1% into 'Other'.

    Parameters:
    - df: DataFrame containing 'county', 'liquor_type', 'bottles', and 'gross_profit' columns
    - county_selected: the county to filter on
    - key: unique Streamlit key prefix
    """
    # Filter to the selected county
    df_sub = df[df['county'] == county_selected]
    if df_sub.empty:
        st.warning(f"County '{county_selected}' not found.")
        return

    # Aggregate bottles sold and gross profit by liquor_type
    df_grouped = (
        df_sub
        .groupby('liquor_type', as_index=False)
        .agg({'bottles': 'sum', 'gross_profit': 'sum'})
    )

    # --- Prepare sales pie data, grouping <1% into 'Other' ---
    sales_total = df_grouped['bottles'].sum()
    df_sales = df_grouped.copy()
    df_sales['pct'] = df_sales['bottles'] / sales_total
    df_sales['category'] = df_sales['liquor_type'].where(df_sales['pct'] >= 0.01, other='Other')
    df_sales = df_sales.groupby('category', as_index=False).agg({'bottles': 'sum'})

    # --- Prepare profit pie data, grouping <1% into 'Other' ---
    profit_total = df_grouped['gross_profit'].sum()
    df_profit = df_grouped.copy()
    df_profit['pct'] = df_profit['gross_profit'] / profit_total
    df_profit['category'] = df_profit['liquor_type'].where(df_profit['pct'] >= 0.01, other='Other')
    df_profit = df_profit.groupby('category', as_index=False).agg({'gross_profit': 'sum'})

    # Render two pie charts side by side
    col1, col2 = st.columns(2)
    with col1:
        fig_sales = px.pie(
            df_sales,
            names='category',
            values='bottles',
            title=f"{county_selected.title()} Liquor Sales Distribution"
        )
        st.plotly_chart(fig_sales, use_container_width=True, key=(key or '') + f"_sales_pie_{county_selected}")

    with col2:
        fig_profit = px.pie(
            df_profit,
            names='category',
            values='gross_profit',
            title=f"{county_selected.title()} Liquor Profit Distribution"
        )
        st.plotly_chart(fig_profit, use_container_width=True, key=(key or '') + f"_profit_pie_{county_selected}")