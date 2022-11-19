import pandas as pd
import numpy as np
import streamlit as st


def Sem3():
    st.header("Semester 3")
    st.subheader('Semester description by Fontys')
    st.markdown('The focus of this semester is on a medium to a large-sized organisation which is part of a supply chain. During this semester you show that you can **_systematically analyse organisational processes_** and **_advise_** how these processes can be **_optimised_**.') 
    st.markdown('In order to **_analyse_** these processes, you will **_create informal insight_** through an **_Exploratory Data Analysis (EDA)_**. Besides that, you will create formal insight into the data using **_basic modelling_**. Using these insights, you realise a suggested IT system (or part thereof) based on your **_design, implement_** this in the organisation using given techniques and **_measure and monitor_** the usage using given formats and/or methods.')
    
    st.markdown('In order to achieve these learning outcomes I worked on the four following subjects througout the semester:')
    
 #%% Business  
    with st.expander("Business"):
        st.markdown("""
        During the semester we had 2 major business modules, both containing mulitple subjects :
        - Business Analysis
            - test
        - Advice
            - test
        """)
#%% SQL
    with st.expander("SQL"):
        st.markdown("""
        During semester one and two, I learned basic query's, joins, sub query's and cte's. In semester 3 I learned how to use window functions to analyse data. With these I am able to sift through data, make partitions on them and apply calculative functions on the data related to the row it is applied to. 
        
        Think of article prices changing over time, with window functions we can group all articles with the same article number together and analyse the price increase and decrease over time.    
        """)
        st.image("OneDrive - Office 365 Fontys/School/portfolio/window function example.png", caption="Window function example")
#%% Power BI
    with st.expander("Power BI"):
        st.write("This was my first experience with Power BI. During the semster we learned about dimensional model, DAX and building visuals in Power BI. This knowledge was applied in our semester project, for which we build a Like4Like dashboard comparing clothing stores accross the world, with mulitple filter options for the end user.")
        st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
#%% R studio
    with st.expander("R Studio"):
        st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
        """)
    