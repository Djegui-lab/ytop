import pandas as pd
import streamlit as st
import numpy as np



def diabete_prediction(input_data):

    tableau_numpy = np.array(input_data)
    input_data_reshape = tableau_numpy.reshape(1, -1)
    prediction =clf.predict(input_data_reshape)

    if (prediction[0]) == 1:
        return " La personne est  diabetique"
    else:
        return "La personne n'est pas  diabetique"


def main():

    st.title("APPLICATION MOBILE POUR LA DETECTION DE DIABETE")
    st.subheader("(AUTEUR: Mr.DJEGUI_WAGUE)")
    Pregnancies = st.number_input('Nombre de fois enceinte')
    Glucose = st.number_input('Taux de glucose')
    BloodPressure = st.number_input('Pression arterielle')
    SkinThickness = st.number_input('Epaisseur de Peau')
    Insulin = st.number_input("INSULIN")
    BMI = st.number_input('Indice de masse corporelle')
    DiabetesPedigreeFunction = st.number_input('FonctionPedigreeDiabete')
    Age = st.number_input('Votre age ')
    diagnostique = ""

    if st.button("resultat_du_test_diabete"):
        diagnostique = diabete_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        st.balloons()     
        st.success('The output is {}'.format(diagnostique))
   
    st.success(diagnostique)

    
    
   
