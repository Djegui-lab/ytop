import pandas as pd
import streamlit as st
import numpy as np


=pickle.load(open('C:/ProgramData/Anaconda3/envs/djegui/deployement_machine_learning/modelWAGUE.PK

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
   
        
if __name__ == "__master__":
    master()  
    
   
