import sys
import subprocess
import streamlit as st
st.set_page_config(page_title="Anna", page_icon=":hospital:",layout='wide')

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
import warnings
warnings.filterwarnings('ignore')


# MODEL LOADING
MODEL_PATH=os.path.join(os.getcwd(),'model','model.pkl')

with open(MODEL_PATH,'rb') as file:
    model=pickle.load(file)

# HEADER
with st.container(): 
    st.subheader('Hello!')
    st.write("---")

# FRONT PAGE
with st.container():
    col1, col2 = st.columns(2)
    with col1:
             st.subheader("Meet Anna,")
             st.title('Your Patient Monitoring Assistant')
             st.write("##")
             st.write("______________________________________________")
             st.subheader(
                 """
                 Anna will predict which of your patients are prone to heart attack based on symptoms reported.
                 """)

    with col2:
             st.markdown("![Alt Text](https://bit.ly/anna-find)")
             
# THE APP             
with st.container():    
    st.write("---")
    st.header("Try Anna")
        
    st.subheader('Please fill in the details of the patient and click on the button below!')
    txt_col,img_col,  = st.columns(2)

    with txt_col:
        with st.form("Heart Attack Predictor App"):
            sex =           st.selectbox("Gender: (0 = Male ; 1 = Female)",(0,1))
            age =           st.number_input("Age in Years", 1, 100, 25, 1)
            chol  =         st.number_input("Serum Cholestoral in mg/dl",120, 430)
            thalachh =      st.slider('Maximum Heart Rate Achieved', 50, 220, 120, 1)
            trtbps =        st.slider('Resting Blood Pressure', 90, 200, 69, 1)
            oldpeak =       st.slider('ST Depression Induced by Exercise Relative to Rest', 0.0, 10.0, 0.01)
            exng =          st.selectbox('Exercise Induced Angina (1 = yes; 0 = no)',(0,1))
            thall =         st.selectbox('Thallium Stress Test(2 = normal; 1 = fixed defect; 3 = reversable defect)',(1,2,3))
            caa =           st.selectbox('Number of Major Vessels (0-3) colored by flourosopy',(0,1,2,3))
            cp =            st.selectbox('Chest Pain Type ( 0 = asymptomatic ; 1 = typical angina; 2 = atypical angina; 3 = non-anginal pain)',(0,1,2,3))
            slp =           st.selectbox('The Slope of the Peak Exercise ST segment(0 = downsloping;1 = flat;2 = upsloping)',(0,1,2)) 
            restecg =       st.selectbox('Resting Electrocardiographic Results (0 = hypertrophy;1 = normal; 2 = having ST-T wave abnormality)',(0,1,2))

            row = [age, sex, cp, trtbps, chol, restecg, thalachh, exng, oldpeak, slp, caa, thall]

            submitted = st.form_submit_button("Analyse")
            if submitted:
                new_data=np.expand_dims(row,axis=0)
                outcome=model.predict(new_data)[0]
                                     
                if outcome==0:
                    st.subheader('Anna says,')
                    st.title("Great! This patient is unlikely to get a heart attack!")
                    st.markdown("![Alt Text](https://bit.ly/anna-good)")
                else:
                    st.subheader('Anna says,')
                    st.title("Oops! This patient has high risk of getting a heart attack!")
                    st.subheader('Please pay more attention.') 
                    st.markdown("![Alt Text](https://bit.ly/p-sick)")
            
    with img_col:
        st.markdown("![Alt Text](https://bit.ly/anna-form)")
        st.subheader("Hold on, Anna is learning about the data...")
        


                
# CONTACT
with st.container():
    st.write("---")

