import pandas as pd
import numpy as np
import streamlit as st

from sem3 import Sem3
from AIspec import AI
from Stage import stage
from ddbl import DDBL
# %%
      
        

    

# %%    
def sem6():
    st.header("Semester 6")


# %%
def work():
    st.header("Work experience")

# %%
def aboutMe():
    st.header("About me")
    
# %%
def home():
    st.header("Welcome!")
# %%
def cv():
    st.header("CV")
#%%
with st.sidebar:
    options= st.radio('Select an option',options=['Home','Semester 3','AI specialisatie', 'Stage', 'Semester 6', 'DDBL Minor', 'Work experience', 'About me'])

    
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
elif options == 'Home':
    home()
elif options == 'cv':
    cv()