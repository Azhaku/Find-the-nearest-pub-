import streamlit as st 
import numpy as np
import pandas as pd
import Home


st.set_page_config(page_title='Pub Locations',page_icon =':map:')

st.markdown(
    f"""
    <style>
    .stApp {{
        background-size: cover
        default-zoom=200%
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.subheader("Search and Find the Location")
selection = st.selectbox(label= "Latitude and Longitude or Postal",options=["Select Option",'PostalCode','Local Authority'])
if selection=='PostalCode':
    postal_codr_values=(Home.df['postcode'].unique())
    postal_code=st.selectbox("Select Postal Code or type down",postal_codr_values)
    df4=Home.df[Home.df['postcode']==postal_code]
    df4['lat']=df4['latitude'].astype('float64')
    df4['lon']=df4['longitude'].astype('float64')
    df4=df4[['lat','lon']]
    st.map(df4)
if selection=='Local Authority':
    local_authority_values=(Home.df['local_authority'].unique())
    local_authority=st.selectbox("Select Local Authority or type down",local_authority_values)
    df4=Home.df[Home.df['local_authority']==local_authority]
    df4['lat']=df4['latitude'].astype('float64')
    df4['lon']=df4['longitude'].astype('float64')
    df4=df4[['lat','lon']]
    st.map(df4)
    