import pandas as pd
import numpy as np
import streamlit as st


def work():
    st.header("Work experience")
    col1, col2 = st.columns(2)
       
    with col1:
        url = "https://i.imgur.com/jaIzA1p.png"
        st.image(url)
        hide_img_fs = '''
        <style> button[title="View fullscreen"]{visibility: hidden;</style>
        '''
        st.markdown(hide_img_fs, unsafe_allow_html=True)
        st.header("BI-consultant")
        st.write("Period: 01/02/2022-Active")
        st.write("My day to day at MTA consists of working on BI questions from the different departments. This was ranging from backend development till deployment of the BI solutions and changes to existing BI solutions. I worked at MTA one day a week next to my study.")
        st.markdown("""
        Key responsibilities:
        - SQL development
            - ETL
        - Power BI
            - Data modelling
            - DAX
            - Visualisations
            - Deployment
        """)
        
    with col2:
        st.empty()