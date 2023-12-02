import streamlit as st
import pickle
import numpy as np
import json
import requests  # pip install requests
from streamlit_lottie import st_lottie
from PIL import Image
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing




def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model() 

regressor = data["model"]

def show_predict_page():
    left_column, right_column = st.columns([2,0.5])
    with left_column:
        st.title("Diabetes Prediction :dna:")
        st.divider()
        text='<h4 style="color:#07092F; font-size:21px; margin-left:8px;padding: 25px 50px 45px 90px;">Required information for the Prediction</h4>'
        st.markdown(text,unsafe_allow_html=True)
    

        st.divider()
        Glucose = st.slider("Glucose level",80, 148 , 80)
        BloodPressure = st.slider("Bloodpressure level", 24, 122, 24)
        Insulin = st.slider("Insulin level", 50, 150, 50)
        BMI = st.slider("BMI", 18, 55, 18)
        

        ok = st.button("Predict Diabetes Outcome")
        if ok:
            X = np.array([[Glucose,BloodPressure,Insulin,BMI]])
            X = X.astype(float)
            #scaler=StandardScaler()
            #X=scaler.fit_transform(X)

            Outcome = regressor.predict(X)
            percentage=Outcome*100
            st.markdown(f"The estimated outcome is {percentage[0]:.2f}% of having diabetes")
        page_i="""
        <style>
        [data-testid="stAppViewContainer"]{
        background-image: url(https://www.shutterstock.com/image-vector/abstract-blue-white-technology-digital-260nw-1432089008.jpg);
        background-size:75%;
        }
        [data-testid="stHeader"]{
        background-color: rgba(0,0,0,0);
        }
        [data-testid="stSidebar"]{
        background-image: url(https://i.graphicmama.com/blog/wp-content/uploads/2021/04/22080427/free-medical-background-08.png);
        background-size:180%;
        }
        [data-testid="stToolbar"]{
        right: 1rem;
        }
        </style>
        """
        st.markdown(page_i,unsafe_allow_html=True)
    def load_lottieurl(url): #for animations
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_pcqghvjn.json")
    with right_column:
        st_lottie(lottie_hello, height=200, key="coding")



   

