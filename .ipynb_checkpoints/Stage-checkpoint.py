import pandas as pd
import numpy as np
import streamlit as st

# %%    
def stage():
    st.header("Stage")

    with st.expander('Internship requirements'):    
        st.markdown("""
        """)
    with st.expander('Internship assignment'):
        st.subheader('Intership assignment')
        st.markdown("""
        My third year internship I did at MTA Group. This is a high tech manufacturing company based in Helmond. My assignment was for the logistics department of MTA. 

          The aim of the assignment was to shift from Excel to a BI solution with a stable back-end solution. MTA already had an existing datawarehouse with an ETL-process. 


        The start was researching the current sitaution, what was wrong and needed to be improved on. Besides that, I gathered new requirements for the new dashboard. Once the requirements were gathered, I applied the MoSCoW method with my stakeholder on them, to get a list with high priority requirements I could focus on for my internship duration. 

        The next step was getting familiar with ETL and ELT-processes. This was new to me, but very important for the assignment. ETL and ELT are ways to move data from production enviroments, which are aimed at perfomance, to datawarehouses or datalakes. 

        After I learned about the concepts, I made an iventory of the correct tables from the production database, which were needed to meet the requirements agreed on for the internship. After this, a data quality check was done on those tables: 
        - are there inconsistencies? 
        - are there empty records? how much records? 
        - relevance of data 

        (add fishbone diagram)

        The next step was importing the tables as staging tables. This is copying the tables from production database to the data warehouse. Based on those staging table fact and dimension tables were created to load into Power BI.

        With the fact and dimension tables in Power BI, a data model was made connecting the tables toghether. This way the visuals can be filtered based on dimensions. 

        Next was creating the actual dashboard with the visuals. For this I first designed a new dashboard design. During my research I found that the existing dashboards were all over the place style wise. So, as part of my advice, I designed a new lay-out. 
        """)
        st.image("https://i.imgur.com/d1qg1r8.png", caption= 'Dashboard design')
        st.markdown("""
        With the datamodel in place and an accompanying design, I made the visuals that were agreed upon from the requirements list. We went through a couple of iterations on the dashboard till before it was finished. 

        This meant all that was left, was publishing the dashboard in the Power BI service, so the logistics department could start working with their new dashboard. 
        """)
#with st.expander('Techniques learned'):
    st.subheader('Techniques learned during internship')
    st.markdown("""
    - working with an ERP system (Isah)
    - ETL and ELT processes
    - BI consultancy within a company
    - Stakeholder management
    - Advanced SQL
    - Communication
    """)