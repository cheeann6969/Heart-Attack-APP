# -*- coding: utf-8 -*-
"""ha_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DNRdEEb7DSgXnHHflnskrAJ0NcKapzGi
"""

import pickle
import os
import numpy as np
import warnings
warnings.filterwarnings('ignore')

MODEL_PATH=os.path.join(os.getcwd(),'best_estimator.pkl')

with open(MODEL_PATH,'rb') as file:
    model=pickle.load(file)
#%%# new_data=[106,72,100,40,36.6,0.178,45]# print(model.predict(np.expand_dims(new_data,axis=0)))#%%

import streamlit as st
import joblib
import pandas as pd
from PIL import Image
st.set_page_config( page_title="Diabetes Prediction App", page_icon=":muscle:", layout="wide")col1, col2 = st.columns(2)
with col1:
    st.title('Heart Attack Prediction App')
    st.write("Input your information and let's find out is the patient prones to heart attack.")
    my_expander = st.expander(label='The Awesome Team Behind This App')
    with my_expander:'Intan, Chee Ann, Dinie, N, Warren(Not a real name)!'    
with col2:
    st.subheader('Please fill in the details of the person under consideration and click on the button below!')
    with st.form("Diabetes Predictor App"):
        age =           st.number_input("Age in Years", 1, 150, 25, 1)
        sex =           st.slider("Glucose Level", 0, 200, 25, 1)
        cp  =           st.slider("Skin Thickness", 0, 99, 20, 1)
        bloodpressure = st.slider('Blood Pressure', 0, 122, 69, 1)
        insulin =       st.slider("Insulin", 0, 846, 79, 1)
        bmi =           st.slider("BMI", 0.0, 67.1, 31.4, 0.1)
        dpf =           st.slider("Diabetics Pedigree Function", 0.000, 2.420, 0.471, 0.001)
        row = [age, sex, cp, trtbps, chol, restecg, thalachh, exng,
       oldpeak, slp, caa, thall]
        # Every form must have a submit button.
        submitted = st.form_submit_button("Analyse")
        if submitted:
            new_data=np.expand_dims(row,axis=0)
            outcome=model.predict(new_data)[0]
            if outcome==0:
                st.subheader("You're healthy! Keep it Up!!")
                image = Image.open('healthy.png')
                st.image(image)
            else:
                st.subheader('From our database, you are not healthy so go work yourself out!')
                image1 = Image.open('nothealthy.png')
                st.image(image1