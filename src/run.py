import streamlit as st
import pandas as pd 
import json

try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3


st.title(':zap: Pytopia Dashboard')

with st.expander('Statistics'):
    pass

