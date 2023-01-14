import json

import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import datetime
from PIL import Image

#login
login_option = st.sidebar.radio('Login/Singup', ('Login', 'Singup'))
if login_option == 'Login':
    with st.sidebar.form("Login"):
        st.write("Login Here.")
        username = st.text_input("Username:")
        password = st.text_input("Passwoed:", type="password")

        submitted = st.form_submit_button("Login")
        if submitted:
            pass
else:
    with st.sidebar.form("singup"):
        st.write("Singup Here.")
        username = st.text_input("Username:")
        password = st.text_input("Passwoed:", type="password")
        email = st.text_input("Email")

        ubmitted = st.form_submit_button("Singup")
        if submitted:
            pass

#banner
banner = Image.open('./data/banner.png', )
st.image(banner)
st.title(':zap: Pytopia Dashboard')

#Metrisc
col1, col2 = st.columns(2)
col1.metric(label="Pytopia Telegram Members", value="4800", delta=("+30"))
col2.metric(label="Website Members", value="2150", delta=("+40"))

#Statistics
with st.expander('Statistics'):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(100), ax=ax)
    st.pyplot(fig)

#Userimpot
with st.expander('User Profile'):
    col1, col2 = st.columns(2)
    col1.text_input('Name:')
    col2.text_input('Location:')
    st.camera_input('Camera Input:', key='camera_input')







