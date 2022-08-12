import streamlit as st
import random
import string
import pandas as pd
import numpy as np
from streamlit_pagination import pagination_component

st.markdown("<style> div[data-testid='stStatusWidget']{display:none}</style>", unsafe_allow_html=True)
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)#

if 'foo' not in st.session_state:
    st.session_state['foo'] = 0 
    
def random_char(y):
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    return ''.join(random.choice(alphabet) for x in range(y))

num_of_cols = st.slider("number of columns", 0,100, value=4)
num_of_rows = st.slider("number of rows", 0,10000, value=1000)
num_of_row_chunks = st.number_input("Number of rows per chunk of data", value=100)


data = pd.DataFrame(np.random.randint(0,100,size=(int(num_of_rows), int(num_of_cols))), columns=list(random_char(num_of_cols))) 

n = int(num_of_row_chunks)
list_df = [data[i:i+n] for i in range(0,data.shape[0],n)] 

data_l = list_df[st.session_state['foo']] 

st.dataframe(data_l, width=300, height=700)

layout = {  'color':"primary", 
            'style':{'margin-top':'10px'}}
test = pagination_component(len(list_df), layout=layout, key="foo")
