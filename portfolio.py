import pandas as pd
import numpy as np
import streamlit as st
from sem3 import Sem3

# %%
      
        
# %%        
def AI():
    st.header("AI Specialisatie")
    
# %%    
def stage():
    st.header("Stage")
    
# %%    
def sem6():
    st.header("Semester 6")
    
# %%    
def DDBL():
    st.header("Data driven business lab")

# %%
def work():
    st.header("Work experience")

# %%
def aboutMe():
    st.header("About me")
#%%
with st.sidebar:
    options= st.selectbox('Projects',options=['Semester 3','AI specialisatie', 'Stage', 'Semester 6', 'DDBL Minor', 'Work experience', 'About me'])
    
if options == 'AI specialisatie':
    AI()
elif options == 'Stage':
    stage()
elif options == 'Semester 6':
    sem6()
elif options == 'DDBL Minor':
    DDBL()
elif options == 'Semester 3':
    Sem3()
elif options == 'Work experience':
    work()
elif options == 'About me':
    aboutMe()