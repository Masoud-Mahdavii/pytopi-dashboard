import streamlit as std 
import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as pit

st.title(':zap: Pytopia Dashboard')

with st.expander('Statistics'):
    fig, ax = pit.subplots(1, 1, figsize=(10, 5))
    sns.histplots(np.random.randn(100), ax=ax)
    st.pyplot(fig)


