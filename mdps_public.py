# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text('* Pregnancies: Number of times pregnant')
    st.text('* Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test') 
    st.text('* BloodPressure: Diastolic blood pressure (mm Hg)')
    st.text('* SkinThickness: Triceps skin fold thickness (mm')
    st.text('* Insulin: 2-Hour serum insulin (mu U/ml)')
    st.text('* Body mass index (weight in kg/(height in m)^2)')
    st.text('* DiabetesPedigreeFunction:indicates the function which scores likelihood of diabetes based on family history(0.4 to 2)')
    st.text('* Age: indicates the age of the person')
    




# Heart disease Prediction pages
if (selected == 'Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction using MachineLearning')

    #columns for input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Your Age')

    with col2:
        sex = st.number_input('Gender Type')

    with col3:
        cp = st.number_input('Chest Pain Types')

    with col1:
        trestbps = st.number_input('Resting Blood Pressure')

    with col2:
        chol = st.number_input('Serum cholestoral in mg/dL')

    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dL')

    with col1:
        restecg =st.number_input('Resting Electrocardiographic Results')

    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved')

    with col3:
        exang = st.number_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.number_input('St Depression Induced By Exercise')

    with col2:
        slope = st.number_input('Slope Of The Peak Exercise')

    with col3:
        ca = st.number_input('Vessels Colored by Flouroscopy')

    with col1:
        thal = st.number_input('Thalassemia (0 = normal; 1 = fixed defect; 2 = reversable defect)')



    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text('* Age from 16 to 100 only')
    st.text('* Gender Type (0 = Female , 1 = Male)') 
    st.text('* Chest Pain (0: asymptomatic,1: atypical angina,2: non-anginal pain,3: typical angina)')
    st.text('* Serum cholestoral in mg/dL (150 <= Normal , 886 <= Moderate , 888 >= Very High)')
    st.text('* Fasting Blood Sugar > 120 mg/dL (> 120 mg/dl, 1 = true; 0 = false)')
    st.text('* Resting Electrocardiographic Results (0 = normal; 1 = having ST-T; 2 = hypertrophy)')
    st.text('* Exercise Induced Angina (1 = yes; 0 = no)')
    st.text('* Slope Of The Peak Exercise (0: downsloping; 1: flat; 2: upsloping)')
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")   
    st.text('* name - ASCII subject name and recording number')
    st.text('* MDVP:Fo(Hz) - Average vocal fundamental frequency') 
    st.text('* MDVP:Fhi(Hz) - Maximum vocal fundamental frequency')
    st.text('* MDVP:Flo(Hz) - Minimum vocal fundamental frequency')
    st.text('* MDVP:Jitter(%), MDVP:Jitter(Abs), MDVP:RAP, MDVP:PPQ, Jitter:DDP - Several measures of variation in fundamental frequency')
    st.text('* MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA - Several measures of variation in amplitude')
    st.text('* NHR, HNR - Two measures of the ratio of noise to tonal components in the voice')
    st.text("* status - The health status of the subject (one) - Parkinson's, (zero) - healthy")
    st.text("* RPDE, D2 - Two nonlinear dynamical complexity measures")
    st.text("* DFA - Signal fractal scaling exponent") 
    st.text("* spread1,spread2,PPE - Three nonlinear measures of fundamental frequency variation")
















