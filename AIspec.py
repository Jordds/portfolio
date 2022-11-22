import pandas as pd
import numpy as np
import streamlit as st

# %%  
def AI():
    st.header("AI Specialisatie")
    with st.container():
        st.subheader("AI methodology")
        st.markdown("""
        my 4th semester at Fontys was my specialisation. I chose for AI out of interest in the subject. You hear a lot about it, and I wanted to learn a more about it. The subject in the semester was machine learning and applying ML algorithms to data. We got taught a methodology when going through ML projects. It is about more then just applying an algorithm. See the image below:
        """)
        url = "https://raw.githubusercontent.com/Jordds/portfolio/main/AI-ProjectMethodology.svg"
        st.image(url, caption ="AI methodology", width = 700)
    with st.container():
        st.subheader("Music Project")
        with st.expander("Getting data"):
            st.markdown("I did a personal project during the semester involving music. I wanted to see if I could learn more about music through a ML project about it. I decided on working on a genre classification model. The first challenge was getting data. For this I made a script that went through folders containing music from different genres and extracting data points that could be used in a machine learning model. see below pictures for some of the steps taken:")
            st.image("https://i.imgur.com/RJGcUu3.png", caption="alter MP3's to WAV files")
            st.markdown("The extraction of data from music was only working correct when using WAV files, therefore I had to change all the extensions from MP3 to WAV")
            st.image("https://i.imgur.com/LiqeKq0.png", caption="removing redundant files")
            st.markdown("After conversion I removed the duplicate files no longer needed from the directory")
            st.image("https://i.imgur.com/eKgI8Fn.png", caption="removing special characters and whitespaces")
        with st.expander("Explanatory Data Analysis"):
            st.markdown("""
            During the EDA I focussed on waveforms, tempograms and freqeuncy of different genres. This allowed me to get a better understanding of music and made for some cool visuals.
            """)
            st.image("https://i.imgur.com/FrFxmaz.png", caption="Tempogram with explanation", width = 1200)
            
            st.image("https://i.imgur.com/7Pf15Hw.png", caption="spectogram with explanation", width = 1200)
        
        with st.expander("ML algortihm"):
            st.markdown("""
            The last step was creating a model based on the dataset. Since I want classification, I used three classification models from Scikit-learn to see which one yielded the best result. I ended up with a Support Vector Machine algorithms. It is strong with images, but can also work well with other types of data and in this case gave me the best results. You can see the accuracy below:
            """)
            st.image("https://i.imgur.com/o3vynyi.png", caption="Accuracy SVM model")
        