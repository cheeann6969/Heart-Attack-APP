import sys
import subprocess
import streamlit as st
st.set_page_config(page_title="Anna", page_icon=":hospital:", layout="wide")

@st.cache
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
install('pickle-mixin')
install('sklearn')
install('streamlit-lottie')
install('streamlit-aggrid')
install('requests')

import os
import time
import pickle
import joblib
import requests
import numpy as np
import pandas as pd
from PIL import Image
#import warnings
#warnings.filterwarnings('ignore')

from st_aggrid import AgGrid
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 666:
        return None
    return r.json()


# MODEL LOADING
MODEL_PATH=os.path.join(os.getcwd(),'best_estimator.pkl')

with open(MODEL_PATH,'rb') as file:
    model=pickle.load(file)

    
Use local CSS
def local_css(file_name):
   with open(file_name) as f:
       st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# LOAD ASSETS
lottie_anna = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_l8t8exmj.json")
#img_contact_form = Image.open("images/yt_contact_form.png")
#img_lottie_animation = Image.open("images/yt_lottie_animation.png")
    
# HEADER
with st.container(): 
    st.subheader('Good Afternoon')
    #st.title
    #st.write("Anna will predict which of your patients are prone to heart attack based on symptoms reported")    

    
ANNA_PATH=os.path.join(os.getcwd(),"anna-1.gif")
# WHAT ANNA DO
with st.container():
    st.write("---")
    col1, col2 = st.columns(2,1)
    with col1:
             st.subheader("Meet Anna,")
             st.title('Your Patient Monitoring Assistant')
             st.write(
                 """
                 Anna will predict which of your patients are prone to heart attack based on symptoms reported.
                 """)

    with col2:
             st.markdown("![Alt Text](https://bit.ly/3RVuBxU)")
             
# THE APP             
with st.container():    
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))           
    st.subheader('Please fill in the details of the person under consideration and click on the button below!')
    with st.form("Diabetes Predictor App"):
        age = st.number_input("Age in Years", 1, 150, 25, 1)
        sex = st.slider("Glucose Level", 0, 200, 25, 1)
        cp  = st.slider("Skin Thickness", 0, 99, 20, 1)
        bloodpressure = st.slider('Blood Pressure', 0, 122, 69, 1)
        insulin = st.slider("Insulin", 0, 846, 79, 1)
        bmi = st.slider("BMI", 0.0, 67.1, 31.4, 0.1)
        dpf = st.slider("Diabetics Pedigree Function", 0.000, 2.420, 0.471, 0.001)
        row = [age, sex, cp, trtbps, chol, restecg, thalachh, exng, oldpeak, slp, caa, thall]
        
        
        submitted = st.form_submit_button("Analyse")
        if submitted:
            new_data=np.expand_dims(row,axis=0)
            outcome=model.predict(new_data)[0]
            if outcome==0:
                st.subheader("You're healthy! Keep it Up!!")
                image = Image.open('healthy.png')
                st.image(image)
            else:
                st.subheader('High Risk!')
                image1 = Image.open('nothealthy.png')
                st.image(image1)

                
                
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
