import streamlit as st
import plotly.express as px
import requests
import pydeck as pdk

# population
@st.cache_resource
def population_map(df, url):
    response = requests.get(url)
    shapes = response.json()

    fig = px.choropleth(
        df,
        geojson=shapes,
        locations="fips",
        color="pop_county",
        color_continuous_scale="Viridis",
        range_color=(df["pop_county"].min(), df["pop_county"].max()),
        scope="usa",
        labels={"pop_county": "Population"},
        hover_name="county", 
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False,
        bgcolor="#2e2e2e",
        landcolor="#000000",
        lakecolor="#2e2e2e"
    )

    fig.update_layout(
        # title_text="Iowa Population by County",
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        height=400,
        paper_bgcolor='#2e2e2e',
        plot_bgcolor='#2e2e2e' 
    )

    fig.update_traces(
        colorbar=dict(
            len=1,
            y=0.5, 
            thickness=10
        )
    )

    st.plotly_chart(fig, use_container_width=True)

# store
@st.cache_resource
def gross_profit_map(df):
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=pdk.ViewState(
                latitude=df['latitude'].mean(),
                longitude=df['longitude'].mean(),
                zoom=5,
                pitch=45,
            ),
            layers=[
                # 3D columns for store gross profit
                pdk.Layer(
                    "ColumnLayer",
                    data=df,
                    get_position='[longitude, latitude]',
                    get_elevation="gross_profit",
                    elevation_scale=1,
                    radius=1000,
                    get_fill_color="[255, 140, 0, 200]",
                    pickable=True,
                    auto_highlight=True,
                ),
            ],
            tooltip={
                "html": "<b>County:</b> {county}<br/>"
                        "<b>City:</b> {city}<br/>"
                        "<b>Gross Profit:</b> ${gross_profit}<br/>",
                "style": {
                    "backgroundColor": "rgba(0, 0, 0, 0.8)",
                    "color": "white"
                }
            }
        ), height=200
    )


@st.cache_resource
def income_map(df, url):
    response = requests.get(url)
    shapes = response.json()

    fig = px.choropleth(
        df,
        geojson=shapes,
        locations="fips",
        color="annual_income",
        color_continuous_scale="Viridis",
        range_color=(df["annual_income"].min(), df["annual_income"].max()),
        scope="usa",
        labels={"annual_income": "Annual Income"},
        hover_name="county", 
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False,
        bgcolor="#2e2e2e",
        landcolor="#000000",
        lakecolor="#2e2e2e"
    )

    fig.update_layout(
        # title_text="Average Income by County",
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        height=400,
        paper_bgcolor='#2e2e2e',
        plot_bgcolor='#2e2e2e' 
    )

    fig.update_traces(
        colorbar=dict(
            len=1,
            y=0.5, 
            thickness=10
        )
    )

    st.plotly_chart(fig, use_container_width=True)
    
    
@st.cache_resource
def gas_sales_map(df, url):
    response = requests.get(url)
    shapes = response.json()

    fig = px.choropleth(
        df,
        geojson=shapes,
        locations="fips",
        color="gas_sales",
        color_continuous_scale="YlOrRd",
        range_color=(df["gas_sales"].min(), df["gas_sales"].max()),
        scope="usa",
        labels={"gas_sales": "Total Gallons Sold (2024)"},
        hover_name="county", 
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False,
        bgcolor="#2e2e2e",
        landcolor="#000000",
        lakecolor="#2e2e2e"
    )

    fig.update_layout(
        # title_text="Average Income by County",
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        height=400,
        paper_bgcolor='#2e2e2e',
        plot_bgcolor='#2e2e2e' 
    )

    fig.update_traces(
        colorbar=dict(
            len=1,
            y=0.5, 
            thickness=10
        )
    )
    
    fig.update_traces(
    hovertemplate="County: %{hovertext}<br>Gallons Sold: %{z:,.0f}<extra></extra>"
)

    st.plotly_chart(fig, use_container_width=True)

@st.cache_resource
def drinking_map(df, url):
    response = requests.get(url)
    shapes = response.json()

    fig = px.choropleth(
        df,
        geojson=shapes,
        locations="fips",
        color="excessive_drinking",
        color_continuous_scale="Cividis",
        range_color=(df["excessive_drinking"].min(), df["excessive_drinking"].max()),
        scope="usa",
        labels={"excessive_drinking": "Excessive Drinking (Percentage)"},
        hover_name="county", 
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False,
        bgcolor="#2e2e2e",
        landcolor="#000000",
        lakecolor="#2e2e2e"
    )

    fig.update_layout(
        # title_text="Average Income by County",
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        height=400,
        paper_bgcolor='#2e2e2e',
        plot_bgcolor='#2e2e2e' 
    )
    
    fig.update_coloraxes(
        colorbar=dict(
            title="Excessive Drinking (%)",
            tickformat=".1%"
        )
    )

    fig.update_traces(
        hovertemplate="County: %{hovertext}<br>Excessive Drinking: %{z:.1%}<extra></extra>"
    )

    st.plotly_chart(fig, use_container_width=True)
