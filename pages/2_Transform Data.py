import streamlit as st
import pandas as pd
import numpy as py
import mypackage.mongoutil as mongoutil

st.set_page_config(layout='wide',page_title='Transform Data')
channellist = ['GHSS Rajamadam', 'DBestech', 'Chennai Super Kings', ]

with st.form(key='my_form'):
    choice = st.selectbox('Select the Channel for to extract data',channellist)
    text = st.text_input('Enter the channel ID to transfor data')
    btn = st.form_submit_button('Transform')
    if btn:
        doc = mongoutil.select_channel_info(text)
        print('trying to get the data...', doc)
        mongoutil.transform_data(doc)
        
            
        

    