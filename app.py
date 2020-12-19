import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 


model=pickle.load(open('classifier.pkl','rb'))


def prediction_for(rate):
    result = model.predict([rate])
    return result

def main():
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Amazon Prime Video Rating ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    rate = st.text_input("Enter text")
    if st.button("Predict"):
        ans = prediction_for(rate)
        st.write(ans)



if __name__=='__main__': 
    main() 
