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
    st.subheader("I'm Jordi and I like to work with data")
    st.markdown("""
    I decided to make this, to be able to not just tell you about the stuff I did but show some of it as well. It gives a small peak off projects I have worked on, some of the results and the scope of my education. This app itself is also part of my learning growth, it allowed me to learn another way to make data accesable to the public through Python. 
    """)
    st.header(":mailbox: Get in contact with me!")
    contact_form = """
    <form action="https://formsubmit.co/jordivanbelzen@live.nl" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form>
    """
    st.markdown(contact_form, unsafe_allow_html = True)
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