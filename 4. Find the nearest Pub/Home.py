import streamlit as st 
import pandas as pd 
import numpy as np 
import seaborn as sns



st.set_page_config(page_title='Home',page_icon='house',layout="centered")

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



df=pd.read_csv('open_pubs.csv')
df=df.replace('\\N',np.NaN)
df=df.dropna()
st.title("\t Welcome to Pub finder")

df.columns=['fsa_id','name','address','postcode','easting','northing','latitude','longitude','local_authority']
df[['latitude', 'longitude']]=df[['latitude', 'longitude']].apply(pd.to_numeric, axis = 1)
total = df['name'].count()

local_authority=df['local_authority'].unique()
local_authority_count = local_authority.shape[0]
st.code(f"Here totally {total} Pubs are available. Number of Local Authorities: {local_authority_count}")
map_val=df[['latitude', 'longitude']]


st.subheader('For Educational Purpose only:')
selected=st.selectbox(label='Explore the data',options=['default','Statiscal Analysis','View the data','Plots'])
if selected=='default':
    st.map(map_val)
if selected=='Statiscal Analysis':
    selected2=st.radio(label='Type of statistical Analysis',options=['Description','Info'])
    if selected2=='Description':
        st.table(df.describe())
    if selected2=='Info':
        st.code(df.dtypes)
if selected=='View the data':
    st.dataframe(df)
if selected=='Plots':
    plot=sns.pairplot(df)
    st.pyplot(plot)