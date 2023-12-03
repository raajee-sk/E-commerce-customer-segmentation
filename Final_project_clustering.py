#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
# ============================================       /     STREAMLIT DASHBOARD      /       ================================================= #
# Comfiguring Streamlit GUI 
st.set_page_config(layout='wide')
# Title
st.header(':violet[E-commerce Customer Segmentation]')
df=pd.read_csv(r"C:\Users\SKAN\Desktop\Raajee\final_project\clustered_customer_data.csv")

col1,col2,col3,col4,col5=st.columns(5)
with col1:
 Gender=st.text_input(':blue[Gender (Note: Male : 1, Female : 0)] ','0')
 Orders=st.text_input(':blue[Orders]','0')
 Jordan=st.text_input(':blue[Jordan]','0')
 Gatorade=st.text_input(':blue[Gatorade]','0')
 Samsung=st.text_input(':blue[Samsung]','0')
 Asus=st.text_input(':blue[Asus]','0')
 Udis=st.text_input(':blue[Udis]','0')
 Mondelez_International=st.text_input(':blue[Mondelez International]','0')
 Wrangler=st.text_input(':blue[Wrangler]','0')
 
with col2:
 Vans=st.text_input(':blue[Vans]','0')
 Fila=st.text_input(':blue[Fila] ','0')
 Brooks=st.text_input(':blue[Brooks]','0')
 Hm=st.text_input(':blue[H&M]','0')
 Dairy_Queen=st.text_input(':blue[Dairy Queen]','0')
 Fendi=st.text_input(':blue[Fendi]','0')
 Hewlett_Packard=st.text_input(':blue[Hewlett Packard]','0')
 Pladis=st.text_input(':blue[Pladis]','0')
 Asics=st.text_input(':blue[Asics]','0')
 

with col3:
 Siemens=st.text_input(':blue[Siemens]','0')
 Burberry=st.text_input(':blue[Burberry]','0')
 Jm=st.text_input(':blue[J.M. Smucker] ','0')
 Pop_Chips=st.text_input(':blue[Pop Chips]','0')
 Juniper=st.text_input(':blue[Juniper]','0')
 Huawei=st.text_input(':blue[Huawei]','0')
 Compaq=st.text_input(':blue[Compaq]','0')
 Ibm=st.text_input(':blue[IBM]','0')
 Mi=st.text_input(':blue[Mi]','0')
 
with col4:
 Lg=st.text_input(':blue[LG]','0')
 Dior=st.text_input(':blue[Dior]','0')
 Scabal=st.text_input(':blue[Scabal] ','0')
 Tommy_Hilfiger=st.text_input(':blue[Tommy Hilfiger]','0')
 Hollister=st.text_input(':blue[Hollister]','0')
 Forever_21=st.text_input(':blue[Forever 21]','0')
 Colavita=st.text_input(':blue[Colavita]','0')
 Microsoft=st.text_input(':blue[Microsoft]','0')
 Jiffy_mix=st.text_input(':blue[Jiffy mix]','0')
 Kraft=st.text_input(':blue[Kraft]','0')
c=st.button("Enter") 
if c:
    import pickle
    with open(r'C:\Users\SKAN\Desktop\Raajee\final_project\cmodel.pkl', 'rb') as file:
        plc=pickle.load( file) 

    sample=[[int(Gender),int(Orders),int(Jordan),int(Gatorade),int(Samsung),int(Asus),int(Udis),int(Mondelez_International),int(Wrangler),int(Vans),int(Fila),int(Brooks),int(Hm),int(Dairy_Queen),int(Fendi),int(Hewlett_Packard),int(Pladis),int(Asics),int(Siemens),int(Jm),int(Pop_Chips),int(Juniper),int(Huawei),int(Compaq),int(Ibm),int(Burberry),int(Mi),int(Lg),int(Dior),int(Scabal),int(Tommy_Hilfiger),int(Hollister),int(Forever_21),int(Colavita),int(Microsoft),int(Jiffy_mix),int(Kraft)]]
    array=np.array(sample)
    result=plc.predict(array)
    
    if result==0:
       st.markdown(
    f"<h1 style='color:#ff6666; font-size: 24px;'>This Customer Belongs To Cluster 0.</h1>",
    unsafe_allow_html=True,)
       st.markdown(
    f"<h1 style='color:#ff6666; font-size: 20px;'>They are more frequent buyers.They also have higher preferences for most of the brands, especially for luxury and fashion brands. They are interested in high-quality and stylish products.They are mostly Male.</h1>",
    unsafe_allow_html=True,)
    else: 
      st.markdown(
    f"<h1 style='color:#ff6666; font-size: 24px;'>This Customer Belongs To Cluster 1.</h1>",
    unsafe_allow_html=True,) 
      st.markdown(
    f"<h1 style='color:#ff6666; font-size: 20px;'>They are less frequent buyers.They also have lower preferences for most of the brands, except for some technology and food brands.They are interested in practical and functional products.They have a more balanced mix of male and female customers.</h1>",
    unsafe_allow_html=True,) 
      
       
       
        

