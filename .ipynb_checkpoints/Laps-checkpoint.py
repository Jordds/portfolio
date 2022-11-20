import pandas as pd
import numpy as np
import datetime
import streamlit as st
import plotly.express as px

url = "https://raw.githubusercontent.com/Jordds/portfolio/main/Spanje%20Jordi.csv"
laps = pd.read_csv(url, sep = '\t', index_col=None)
laps = laps[['carId','trackId', 'binIndex', 'lap_number', 'lap_distance', 'velocity_X', 'lap_time', 'fuel']]
laps = laps[laps['lap_number'] > 0]
laps['velocity_X'] = laps['velocity_X'] * 3.6
laps['binDistance'] = 1 # every bin is 1 meter on track, to get the total track this needs to be summed to a total
laps['totalDistance'] = laps['binDistance'].cumsum() / 1000
laps['Time'] = pd.to_datetime(laps.lap_time, unit='s').dt.time.astype(str).str[3:]
laps = laps[['carId', 'trackId', 'binIndex', 'lap_number', 'lap_distance', 'velocity_X', 'lap_time', 'Time', 'fuel', 'totalDistance']]

def telemetry():
    fig = px.line(laps, x="binIndex", y="velocity_X", color='lap_number')
    st.plotly_chart(fig, use_container_width=True)
    
def corners():    
    bocht1 = [dict(type='square',
                 xref='x', yref='y',
                 x0=750, y0=0,
                 x1=850, y1=320,
                 opacity=.25,
                 line=dict(color='#835AF1'),
                 fillcolor='#835AF1')]
    bocht3 = [dict(type='square',
                     xref='x', yref='y',
                     x0=1105, y0=0,
                     x1=1140, y1=320,
                     opacity=.25,
                     line=dict(color='#835AF1'),
                     fillcolor='#835AF1')]
    bocht4 = [dict(type='square',
                     xref='x', yref='y',
                     x0=1610, y0=0,
                     x1=1730, y1=320,
                     opacity=.25,
                     line=dict(color='#835AF1'),
                     fillcolor='#835AF1')]
    bocht5 = [dict(type='square',
                     xref='x', yref='y',
                     x0=2010, y0=0,
                     x1=2160, y1=320,
                     opacity=.25,
                     line=dict(color='#835AF1'),
                     fillcolor='#835AF1')]
    bocht7 = [dict(type='square',
                     xref='x', yref='y',
                     x0=2460, y0=0,
                     x1=2530, y1=320,
                     opacity=.25,
                     line=dict(color='#835AF1'),
                     fillcolor='#835AF1')]
    bocht10 = [dict(type='square',
                     xref='x', yref='y',
                     x0=3350, y0=0,
                     x1=3500, y1=320,
                     opacity=.25,
                     line=dict(color='#835AF1'),
                     fillcolor='#835AF1')]
    bocht13 = [dict(type='square',
                     xref='x', yref='y',
                     x0=3650, y0=0,
                     x1=3750, y1=320,
                     opacity=.25,
                     line=dict(color='#835AF1'),
                     fillcolor='#835AF1')]
    bocht14 = [dict(type='square',
                     xref='x', yref='y',
                     x0=3950, y0=0,
                     x1=4000, y1=320,
                     opacity=.25,
                     line=dict(color='#835AF1'),
                     fillcolor='#835AF1')]
    bocht15 = [dict(type='square',
                     xref='x', yref='y',
                     x0=4100, y0=0,
                     x1=4140, y1=320,
                     opacity=.25,
                     line=dict(color='#835AF1'),
                     fillcolor='#835AF1')]


    fig = px.line(laps, x="binIndex", y="velocity_X", color='lap_number')
    fig.update_layout(
        width=1100,
        height=1000,
        autosize=False,
        margin=dict(t=0, b=0, l=0, r=0),
        template="plotly_white",
    )
    fig.update_scenes(
        aspectratio=dict(x=1, y=1, z=0.7),
        aspectmode="manual"
    )
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                buttons=[
                    dict(label="None",
                         method="relayout",
                         args=["shapes", []]),
                    dict(label="bocht 1",
                         method="relayout",
                         args=["shapes", bocht1]),
                    dict(label="bocht 3",
                         method="relayout",
                         args=["shapes", bocht3]),
                    dict(label="bocht 4",
                         method="relayout",
                         args=["shapes", bocht4]),
                    dict(label="bocht 5",
                         method="relayout",
                         args=["shapes", bocht5]),
                    dict(label="bocht 7",
                         method="relayout",
                         args=["shapes", bocht7]),
                    dict(label="bocht 10",
                         method="relayout",
                         args=["shapes", bocht10]),
                    dict(label="bocht 13",
                         method="relayout",
                         args=["shapes", bocht13]),
                    dict(label="bocht 14",
                         method="relayout",
                         args=["shapes", bocht14]),
                    dict(label="bocht 15",
                         method="relayout",
                         args=["shapes", bocht15]),
                    dict(label="All",
                         method="relayout",
                         args=["shapes", bocht1 + bocht3 + bocht4 + bocht5 + bocht7 + bocht10 + bocht13 +bocht14 +bocht15]),
        ]
    )])

    # Update remaining layout properties
    fig.update_layout(
        title_text="Highlight Clusters",
        showlegend=True,
    )

    #fig.show()
    st.plotly_chart(fig, use_container_width=True)