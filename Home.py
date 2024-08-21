import pandas as pd


import streamlit as st

clothing_selection = ['Hats', 'Shirts']


st.set_page_config(layout="wide")



#css styling
with open('style.css', 'r') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


#background image
import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('images/transparent background.png')




# logo image
st.image('images/Red graphic circle PoizdP.png',  width=500)    

with open('index.html', 'r') as f:
    st.markdown(f.read(), unsafe_allow_html=True)
    


st.divider()

# select clothing type
st.selectbox('Select Clothing Type', clothing_selection)