import json

import matplotlib.pyplot as pit
import numpy as np
import seaborn as sns
import streamlit as st

st.title(':zap: Pytopia Dashboard')


with st.expander('Statistics'):
    fig, ax = pit.subplots(1, 1, figsize=(10, 5))
    sns.histplots(np.random.randn(100), ax=ax)
    st.pyplot(fig)



with st.expander('User Profile:'):
    st.text_input('Name:')
    st.camera_input('camrta Input', key='camera_input')


