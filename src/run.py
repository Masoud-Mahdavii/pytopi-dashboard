import streamlit as st
import pandas as pd
import json

try:
    from StringIO import StringIO 
except ImportError:
    from io import StringIO 

st.title(':zap: Pytopia Dashboard')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)
    string_data = stringio.read()
    st.write(string_data)
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

data = json.loads(string_data)
st.json(data)
