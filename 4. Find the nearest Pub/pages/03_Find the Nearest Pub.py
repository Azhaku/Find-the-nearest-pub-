import streamlit as st 
import numpy as np
import pandas as pd
import Home


st.set_page_config(page_title='Nearest Pubs',page_icon ='🍹')
st.subheader('Find the Nearest Pub')


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


#Euclidian distance

def distance(x1,y1,x2,y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** ( 1 / 2)

#Store a closest lat_log_values in list
def Nearest(lat_log_values,lat_log,k):
    n=len(lat_log_values)
    my_list=[]
    all_values=[]
    for i in range(n):
        my_list.append({'Distances' : distance(lat_log_values[i][0],lat_log_values[i][1],lat_log[0],lat_log[1]),'Iteration':i})
    #sort a lat_log_values
    my_list= sorted(my_list, key=lambda l:l['Distances'])
    #store it in a new list
    for i in range(k):
        value=[]
        value.append(lat_log_values[my_list[i]["Iteration"]][0])
        value.append(lat_log_values[my_list[i]["Iteration"]][1])
        all_values.append(value)
    #creating a dataframe
    df2=pd.DataFrame(all_values,columns=['latitude','longitude'])
    st.subheader('The closest pubs near your location:')
    st.map(df2)
    
    
df1=Home.df[['latitude', 'longitude']] 
lat_log_values=df1.values.tolist()
selection = st.selectbox('Latitude and Longitude or Postal',options=["Select Option",'Postal','Latitude and Longitude'])
k=5
if selection=='Postal':
    postal_code=st.sidebar.text_input("Enter Postal Code")
    df2= Home.df.loc[Home.df['postcode']==postal_code]
    lat=df2['latitude'].values.astype(float)
    log=df2['longitude'].values.astype(float)
    lat_log=[lat,log]
    Nearest(lat_log_values, lat_log, k)
elif selection=='Latitude and Longitude':
    lat = st.sidebar.number_input('Enter the latitude')
    log = st.sidebar.number_input('Enter the longitude')
    lat_log=[lat,log]
    Nearest(lat_log_values, lat_log, k)
else:
    pass
