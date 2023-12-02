import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
import json
import requests  # pip install requests
from streamlit_lottie import st_lottie
    

st.set_page_config(page_title="Diabetes Prediciton", page_icon=":syringe:", layout="centered")
signature = '<p style="color:#FFFFFF; font-size: 27px; margin-left:14px;padding-top: 20px;">Predict/Explore</p>'
p = st.sidebar.markdown(signature,unsafe_allow_html=True)
st.divider()
page= st.sidebar.selectbox(" ", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
    
    



