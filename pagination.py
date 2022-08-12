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
    
words = ['light',
'bed',
'colorful',
'boiling',
'well-off',
'overrated',
'immense',
'hard',
'relieved',
'precious',
'ludicrous',
'eatable',
'cruel',
'discovery',
'sloppy',
'tray',
'disagreeable',
'telephone',
'lovely',
'godly',
'cause',
'pointless',
'theory',
'spooky',
'drop',
'bite-sized',
'reminiscent',
'wicked',
'hug',
'hate',
'ashamed',
'unused',
'jazzy',
'known',
'chief',
'disapprove',
'admit',
'gaping',
'vivacious',
'hollow',
'eight',
'popcorn',
'exciting',
'whimsical',
'faint',
'new',
'tire',
'pizzas',
'internal',
'effect',
'start',
'unarmed',
'worm',
'awake',
'string',
'humor',
'cautious',
'notebook',
'wide-eyed',
'month',
'same',
'cover',
'receive',
'clover',
'misty',
'step',
'dislike',
'vague',
'flat',
'neck',
'voice',
'stitch',
'apparatus',
'boundless',
'lunchroom',
'team',
'receipt',
'disagree',
'ruin',
'meeting',
'honorable',
'groovy',
'cherry',
'scissors',
'bizarre',
'steady',
'cannon',
'ship',
'soothe',
'mundane',
'verdant',
'tiger',
'request',
'home',
'quizzical',
'head',
'loving',
'interfere',
'argument',
'imported']

def random_char(y):
    
    return [random.choice(words) for x in range(y)]

num_of_cols = st.slider("number of columns", 0,100, value=4)
num_of_rows = st.slider("number of rows", 0,10000, value=1000)
num_of_row_chunks = st.number_input("Number of rows per chunk of data", value=100)


data = pd.DataFrame(np.random.randint(0,100,size=(int(num_of_rows), int(num_of_cols))), columns=random_char(num_of_cols))

n = int(num_of_row_chunks)
list_df = [data[i:i+n] for i in range(0,data.shape[0],n)] 

data_l = list_df[st.session_state['foo']] 

st.dataframe(data_l, width=300, height=700)

layout = {  'color':"primary", 
            'style':{'margin-top':'10px'}}
test = pagination_component(len(list_df), layout=layout, key="foo")
