import json

import matplotlib.pyplot as pit
import numpy as np
import seaborn as sns
import streamlit as st

st.title(':zap: Pytopia Dashboard')



with st.expander('User Profile:'):
    col1, col2 = st.colums(2)
    col1.text_input('Name:')
    col2.text_input('Location:')
    st.camera_input('camrta Input', key='camera_input')


