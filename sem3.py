import pandas as pd
import numpy as np
import streamlit as st


def Sem3():
    st.header("Semester 3")
    st.subheader('Semester description by Fontys')
    st.markdown('The focus of this semester is on a medium to large-sized organisation which is part of a supply chain. During this semester you show that you can **_systematically analyse organisational processes_** and **_advise_** how these processes can be **_optimised_**.') 
    st.markdown('In order to **_analyse_** these processes, you will **_create informal insight_** through an **_Exploratory Data Analysis (EDA)_**. Besides that, you will create formal insight into the data using **_basic modelling_**. Using these insights, you realise a suggested IT system (or part thereof) based on your **_design, implement_** this in the organisation using given techniques and **_measure and monitor_** the usage using given formats and/or methods.')
    
    st.markdown('In order to achieve these learning outcomes I worked on the four following subjects througout the semester:')
    
 #%% Business  
    with st.expander("Business"):
        st.markdown("""
        During the semester we had 2 major business modules, both containing mulitple subjects :
        - Business Analysis
            - Governance, Risk Management & Compliance (GRC)
            - Supply Chain Management
            - ERP systems 
            - Business Information Management (BIM)
            - Stakeholders analysis
            - Business Process Management Notation (BPMN)
        - Implementation plan
            - Requirements engineering 
            - Testing 
            - Functional management (BiSL Next)
        """)
#%% SQL
    with st.expander("SQL"):
        st.markdown("""
        During semester one and two, I learned basic query's, joins, sub query's and cte's. In semester 3 I learned how to use window functions to analyse data. With these I am able to sift through data, make partitions on them and apply calculative functions on the data related to the row it is applied to. 
        
        Think of prices changing over time, with window functions we can group all prices based on groups  analyse the price increase and decrease over time for specific groups.    
        """)
        wf = "OneDrive/Documents/GitHub/portfolio/window function example.png"
        st.image(wf, caption="Window function example")
#%% Power BI
    with st.expander("Power BI"):
        st.write("This was my first experience with Power BI. During the semster we learned about dimensional model, DAX and building visuals in Power BI. This knowledge was applied in our semester project, for which we build a Like4Like dashboard comparing clothing stores accross the world, with mulitple filter options for the end user.")
        st.image("OneDrive/Documents/GitHub/portfolio/powerBISem3.png", caption="Plainwear Like4Like dashboard")
        st.markdown("""
        This is a screenshot of the dashboard I came up with for my semester project. Ib the background, a Like4Like classification was made, so the stores shown would be an equal comparison. 
        
        The user is able in this dashboard to see Year over Year charts, this means that the moment of the current year is being compared to the same month af last year. On top of that the user can select countries, streets and date to slice through the visual as they need. 
        """)
#%% R studio
    with st.expander("R Studio"):
        st.write("""
        Through the first three semesters we also got taught R. This is a programming language developed for statitical and analytical purposes. Just like SQL, the first to semesters where about learning the basics (loading in data and basic aggregations). During this semester, I learned how to apply window functions in R. On top of that, I learned about regression. 
        
        At the end of the semester we had a personal project that required to source our own data, clean and combine datasets and lastly apply statics and regression on that cleaned data. The below picture shows a plot I made in my personal semester project regarding regression: 
        """)
        st.image("OneDrive/Documents/GitHub/portfolio/regression.png", caption="multiple regression plot")
    