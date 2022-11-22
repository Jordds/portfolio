import pandas as pd
import numpy as np
import streamlit as st

from sem3 import Sem3
from AIspec import AI
from Stage import stage
from ddbl import DDBL
from workExp import work
# %%
      
        

    

# %%    
def sem6():
    st.header("Semester 6")


# %%


# %%
def aboutMe():
    st.header("About me")
    
# %%

def home():
    st.header("Welcome!")
    st.subheader("I'm Jordi and I like to work with data")
    st.markdown("""
    I decided to make this, to be able to not just tell you about the stuff I did but show some of it as well. It gives a small peak off projects I have worked on, some of the results and the scope of my education. This app itself is also part of my learning growth, it allowed me to learn another way to make data accesable to the public through Python, building a small web app and adding features to it. 
    """)
    st.header(":mailbox: Get in contact with me!")
    st.markdown(
    """
    Feel free to contact me with any questions!
    """)
    #inline css, can not access css file from github
    st.markdown("""
    <style> .input[type=text], input[type=email], textarea {
      width: 100%; /* Full width */
      padding: 12px; /* Some padding */ 
      border: 1px solid #ccc; /* Gray border */
      border-radius: 4px; /* Rounded borders */
      box-sizing: border-box; /* Make sure that padding and width stays in place */
      margin-top: 6px; /* Add a top margin */
      margin-bottom: 16px; /* Bottom margin */
      resize: vertical}
      button[type=submit] {
      background-color: #04AA6D;
      color: white;
      padding: 12px 20px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button[type=submit]:hover {
    background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)
    
    contact_form = """
    <form action="https://formsubmit.co/jordivanbelzen@live.nl" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
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