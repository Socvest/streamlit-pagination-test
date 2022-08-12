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
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

num_of_cols = st.slider("number of columns", 0,100, value=4)


data = pd.DataFrame(np.random.randint(0,100,size=(1000, num_of_cols)), columns=list(random_char(num_of_cols))) 

n = 100  
list_df = [data[i:i+n] for i in range(0,data.shape[0],n)] 

data_l = list_df[st.session_state['foo']] 

st.dataframe(data_l, width=300, height=700)

layout = {  'color':"primary", 
            'style':{'margin-top':'10px'}}
test = pagination_component(len(list_df), layout=layout, key="foo")
