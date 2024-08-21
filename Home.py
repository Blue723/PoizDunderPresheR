import pandas as pd


import streamlit as st

clothing_selection = ['Hats', 'Shirts']


st.set_page_config(layout="wide")

with open('style.css', 'r') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


#image
st.image('images/Red graphic circle PoizdP.png',  width=500, )    


with open('index.html', 'r') as f:
    st.markdown(f.read(), unsafe_allow_html=True)
    


st.divider()

# select clothing type
st.selectbox('Select Clothing Type', clothing_selection)