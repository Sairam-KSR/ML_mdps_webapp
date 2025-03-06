# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 18:49:58 2025

@author: konda
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = pickle.load(open("diabetes_model.sav",'rb'))
heart_disease_model = pickle.load(open("heart_disease_model.sav",'rb'))
parkinson_model = pickle.load(open("parkinsons_model.sav",'rb'))

#Side bar for navigation
with st.sidebar:
    selected = option_menu("Multiple Disease Predictive System", 
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson Prediction'],
                           icons=['activity','heart','person'],
                           default_index=0)
                           

# Diabetic Prediction page
if (selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction')
    
    Pregnancies = st.text_input('Pregnancies')
    Glucose = st.text_input('Glucose')
    BloodPressure = st.text_input('BloodPressure')
    SkinThickness = st.text_input('SkinThickness')
    Insulin = st.text_input('Insulin')
    BMI = st.text_input('BMI')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
    Age = st.text_input('Age')
    
    #Code for prediction
    diab_diagnosis = ''
    
    # Creating buttion for results
    if st.button('Show Diabetes result'):
        prediction =diabetes_model.predict([['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']])
        
        if prediction[0] == 0:
          print("Non Diabetic")
        else:
          print("Diabetic")        
    st.success(diab_diagnosis)
        
        
    
if (selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction')
    age = st.text_input('age')
    sex =st.text_input('sex')
    cp=st.text_input('cp')
    trestbps=st.text_input('trestbps')
    chol=st.text_input('chol')
    fbs=st.text_input('fbs')
    restecg=st.text_input('restecg')
    thalach=st.text_input('thalach')
    exang=st.text_input('exang')
    oldpeak=st.text_input('oldpeak')
    slope=st.text_input('slope')
    ca=st.text_input('ca')
    thal=st.text_input('thal')
    
    #Code for prediction
    heart_diagnosis = ''
    
    # Creating buttion for results
    if st.button('Show Heart result'):
        prediction =heart_disease_model.predict([['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal']])
        
        if prediction[0] == 0:
          print("Un Healthy")
        else:
          print("Healthy")        
    st.success(heart_diagnosis)

if (selected == 'Parkinson Prediction'):
    
    #page title
    st.title('Parkinson Prediction')
    
    MDVP_Fo_Hz =st.text_input('MDVP:Fo(Hz)')
    MDVP_Fhi_Hz=st.text_input('MDVP:Fhi(Hz)')
    MDVP_Flo_Hz=st.text_input('MDVP:Flo(Hz)')
    MDVP_Jitter_percentage=st.text_input('MDVP:Jitter(%)')
    MDVP_Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')
    RAP=st.text_input('MDVP:RAP') 
    PPQ=st.text_input('MDVP:PPQ')
    Jitter_DDP=st.text_input('Jitter:DDP')
    Shimmer=st.text_input('MDVP:Shimmer')
    Shimmer_dB=st.text_input('MDVP:Shimmer(dB)')
    Shimmer_APQ3=st.text_input('Shimmer:APQ3')
    Shimmer_APQ5=st.text_input('Shimmer:APQ5')
    APQ=st.text_input('MDVP:APQ')
    Shimmer_DDA=st.text_input('Shimmer:DDA')
    NHR=st.text_input('NHR')
    HNR=st.text_input('HNR')
    RPDE=st.text_input('RPDE')
    DFA=st.text_input('DFA')
    spread1=st.text_input('spread1')
    spread2=st.text_input('spread2')
    D2=st.text_input('D2')
    PPE=st.text_input('PPE')
    
    #Code for prediction
    park_diagnosis = ''
    
    # Creating buttion for results
    if st.button('Show Parkinson result'):
        prediction =parkinson_model.predict([['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)',
       'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP',
       'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
       'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'spread1',
       'spread2', 'D2', 'PPE']])
        
        if prediction[0] == 0:
          print("No Parkinson Disease")
        else:
          print("Parkinson Disease")        
    st.success(park_diagnosis)
