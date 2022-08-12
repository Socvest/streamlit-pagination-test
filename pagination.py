import streamlit as st
import random
import string
import pandas as pd
import numpy as np

st.markdown("<style> div[data-testid='stStatusWidget']{display:none}</style>", unsafe_allow_html=True)
st.markdown('<style>' + open('./iFrame.css').read() + '</style>', unsafe_allow_html=True)#

if 'foo' not in st.session_state:
    st.session_state['foo'] = 0 
    
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

print(random_char(5))


data = pd.DataFrame(np.random.randint(0,100,size=(1000, 4)), columns=list('ABCD')) 

n = 100  
list_df = [data[i:i+n] for i in range(0,data.shape[0],n)] 

data_l = list_df[st.session_state['foo']] 

st.dataframe(data_l, width=300, height=700)

layout = {  'color':"primary", 
            'style':{'margin-top':'10px'}}
test = pagination_component(len(list_df), layout=layout, key="foo")
