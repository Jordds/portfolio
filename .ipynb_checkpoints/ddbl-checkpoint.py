import pandas as pd
import numpy as np
import duckdb
import plotly.express as px
import streamlit as st
import pydeck as pdk
from datetime import datetime
from Laps import telemetry, corners, spainMap, maxTime


def DDBL():
    with st.container():
        st.header("Data driven business lab")
        st.markdown("""
            I chose the minor Data Driven Business Lab, because it gave me freedom to explore other concepts and techniques to work with data. During my specialisation, I learned to work with Python and I wanted to learn more. 

            Within the minor you are free to explore these options as long as they contribute towards the set learning goals of the minor. Our minor project was for the Municipality of Eindhoven and during the semester we setup a side project with the F1 2021 game. 

            During this semester I improved my Python data cleaning and anlysis skills. I also learned how to use multiple new libraries, one of which allowed me to build this online portfolio. 

            Besides that, one of my teachers told me about DuckDB, which helped us with working with big amounts of data we got from the municipality. Our hardware systems ran into bottlenecks, not being able to process the amount of data we got from the municipality.
            """)
    
    with st.container(): 
        st.header("Municipality project")
        with st.expander("Assignment"):
            st.write("")
            
        with st.expander("building the backend and cleaning data"):
            st.markdown("""
            I cleaned the data with a Python script. The different CSV's we got are loaded in and mulitple steps for each are taken to clean them. In the end we end up with 3 cleaned datasets, which are loaded into a DuckDB file to do analysis on in Python. Using pandas dataframes for this was not feasable. 
            
           The dataframes are also exported to new CSV's, which then are run through an Azure pipeline to be stored in a cloud database. This is done for the people in our group that are using Power BI insteas of Python. This way they can connect to this database and work in Power BI with the cleaned data. 
            """)
            
        with st.expander("visualisations"):
            st.write("These are some of the visualisations I worked on during the semester. This data is stored in DuckDB, which is accessed during the loading in of the data.")
            #%% werkt niet in GitHub
            """
            con = duckdb.connect(database= 'OneDrive/Documents/GitHub/portfolio/my-db.duckdb', read_only=False)
            df = con.execute("select lon, lat from dust GROUP BY lon, lat").df()
            df2 = con.execute("select Date, lon, lat, AVG(pm10) as pm10, AVG(pm25) as pm25 from fijnstof GROUP BY lon, lat, Date").df()
            df3 = con.execute("select Date, lon, lat, AVG(pm10) as pm10, AVG(pm25) as pm25, date_part('hour', cast(Time as time)) as hour from fijnstof where lon between 5.47 and 5.49 and lat between 51.452 and 51.454 GROUP BY lon, lat, Date, date_part('hour', cast(Time as time))").df()
            con.close()
            start_date = '2022-09-01'
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            d = st.date_input(
            "date filter", start_date)
            st.write('Selected date:', d)
            tab1, tab2 = st.tabs(["Map", "Data"])

            tab2.subheader('Data gemiddelde PM10 uitstoot per dag') #titel voor tab
            tab2.write(df2) #toont dataframe
            #st.dataframe(df2)
            view = pdk.data_utils.compute_view(df[["Lon", "Lat"]])
            view.pitch = 75
            view.bearing = 60
            view.longitude = 5.3582
            view.latitude=51.4379
            view.zoom= 15
            tooltip = {
                "html": "<b>{pm25}</b> gem van 25 mm grootte, <b>{pm10}</b> gem van 10 mm grootte",
                "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
            }

            column_layer = pdk.Layer(
                "ColumnLayer",
                data=df2,
                get_position=["Lon", "Lat"],
                get_elevation="pm10",
                elevation_scale=24,
                elevation_range=[100, 1000],
                radius=2,
                get_color='[200, 30, 0, 160]',
               # get_fill_color=["pm25 * 10", "pm25", "pm25 * 10", 140],
                pickable=True,
                auto_highlight=True,
                extruded=True,
            )
            tab1.subheader('Gemiddelde PM10 uitstoot')
            tab1.pydeck_chart(pdk.Deck(
                column_layer,
                initial_view_state=view,
                tooltip=tooltip,
               # map_provider="mapbox",
                map_style=None,
            ))
            avgPM = px.bar(df3, x='hour', y='pm10', color='Date', pattern_shape='Lon',barmode='group', width = 10)
            st.plotly_chart(avgPM, use_container_width=True)
           """
            url = "https://i.imgur.com/ekVO3dv.png"
            st.image(url, caption="Screenshot of the map visualisation (placeholder till DuckDB works")


        
        
    with st.container(): 
        st.header("F1 game")
        
        with st.expander("setup"):
            st.write("")
        st.markdown("""
        Here you can see some of the visuals I made during this project.
        """)
        maxTime()
        st.empty()
        telemetry()
        st.markdown("""
        This is a plot I made that is able to show the telemetry of different laps. With this I can compare the best lap to other laps to see where time is lost and won. The user is able to select the laps he wants to see by clicking on the legend to the side. This plot is one of the best ways for drivers and their teams to see their track performance time wise. 
        """)
        st.empty()
        corners()
        st.markdown("""
        This plot is a variation on the firts plot. In this one I mapped out the corners that required heavy to medium breaking. This way I could see the difference between those and where I was losing or winning times over different laps.
        """)
        st.empty()
        spainMap()
        st.markdown("""
        This last plot shows the different lines driven on the track. Combined with the other plots the driver can work out which lines or winning or losing him lap time.
        """)