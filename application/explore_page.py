import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json
import requests  # pip install requests
from streamlit_lottie import st_lottie
from PIL import Image
import seaborn as sns

#def load_lottieurl(url): #for animations
 #       r = requests.get(url)
  #      if r.status_code != 200:
   #         return None
    #    return r.json()




def load_data():
    df=pd.read_csv("diabetes.csv")
    return df

df=load_data()
@st.cache_data
def show_explore_page():
    left_column,right_column = st.columns([2,0.001],gap="medium")
    
    
    
    with left_column:
        plt.style.use("fivethirtyeight")
        
        
        st.markdown("<h1 style='text-align: center; color: black;'>Graphical Analysis</h1>", unsafe_allow_html=True)
        st.divider()
        plt.figure(figsize=(10,10)) #corr table
        fig, ax = plt.subplots()
        x1=[0,1]
        labels=["No","Yes"]
        sns.countplot(data=df,x="Outcome")
        plt.xticks(x1, labels)
        plt.show()
        text='<p style="color:#000000;text-align: center; font-size: 29px; margin-left:14px;padding: 25px 50px 45px 90px;">1) Diabetes-Outcome</p>'
        st.markdown(text,unsafe_allow_html=True)
        st.write(fig)

        st.divider()
        text='<p style="color:#000000;text-align: center; font-size: 29px; margin-left:14px;padding: 25px 50px 45px 90px;">2) Correlation Table</p>'
        st.markdown(text,unsafe_allow_html=True)
        st.divider()
        plt.figure(figsize=(10,10)) #corr table
        fig, ax = plt.subplots()
        fig.set_facecolor("#ADD8E6")
        sns.set_theme(style="whitegrid", palette="pastel")
        sns.heatmap(df.corr(),annot=True,cmap="BuPu",fmt=".1f",ax=ax)
        st.write(fig)

        C=pd.DataFrame(df.corr()["Outcome"])
        plt.figure(figsize=(6,6))
        plt.style.use("fivethirtyeight")
        fig, ax = plt.subplots()
        sns.heatmap(C,annot=True,cmap="Blues",fmt=".2f",ax=ax)
        st.divider()
        text1='<p style="color:#000000;text-align: center; font-size: 29px; margin-left:14px;padding: 25px 50px 45px 90px;">3) Correlation-Outcome</p>'
        st.markdown(text1,unsafe_allow_html=True)
        st.divider()
        st.write(fig)
        st.divider()
        st.divider()
        st.divider()
        #img=Image.open("image/b1.png")
        #st.image(img,width=650)
        page_img="""
        <style>
        [data-testid="stAppViewContainer"]> .main{
        background-image: url(https://i.graphicmama.com/blog/wp-content/uploads/2021/04/22080458/free-medical-background-09.png);
        background-size:137%;
        background-attachment: local;
        }

        [data-testid="stHeader"]{
        background-color: rgba(0,0,0,0);
        }
        [data-testid="stToolbar"]{
        right: 1rem;
        }
        [data-testid="stSidebar"]{
        background-image: url(https://i.graphicmama.com/blog/wp-content/uploads/2021/04/22092628/free-medical-background-35.png);
        background-position: 70%;
        background-size:530%; 
        }
        #Graphical Analysis :earth_americas:c{
           text-align: center
        
        }
         
        </style>
        """
        
        st.markdown(page_img,unsafe_allow_html=True)
        
        
    #with right_column:
     #st_lottie(lottie_hello, width=150, key="coding")
        


        
        

