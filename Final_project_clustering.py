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
 Gender=st.text_input(':blue[Gender (Note: Male : 1, Female : 0)] ')
 Orders=st.text_input(':blue[Orders]')
 Jordan=st.text_input(':blue[Jordan]')
 Gatorade=st.text_input(':blue[Gatorade]')
 Samsung=st.text_input(':blue[Samsung]')
 Asus=st.text_input(':blue[Asus]')
 Udis=st.text_input(':blue[Udis]')
 Mondelez_International=st.text_input(':blue[Mondelez International]')
 Wrangler=st.text_input(':blue[Wrangler]')
 
with col2:
 Vans=st.text_input(':blue[Vans]')
 Fila=st.text_input(':blue[Fila] ')
 Brooks=st.text_input(':blue[Brooks]')
 Hm=st.text_input(':blue[H&M]','0')
 Dairy_Queen=st.text_input(':blue[Dairy Queen]')
 Fendi=st.text_input(':blue[Fendi]')
 Hewlett_Packard=st.text_input(':blue[Hewlett Packard]')
 Pladis=st.text_input(':blue[Pladis]')
 Asics=st.text_input(':blue[Asics]')
 

with col3:
 Siemens=st.text_input(':blue[Siemens]')
 Burberry=st.text_input(':blue[Burberry]')
 Jm=st.text_input(':blue[J.M. Smucker] ')
 Pop_Chips=st.text_input(':blue[Pop Chips]')
 Juniper=st.text_input(':blue[Juniper]')
 Huawei=st.text_input(':blue[Huawei]')
 Compaq=st.text_input(':blue[Compaq]')
 Ibm=st.text_input(':blue[IBM]')
 Mi=st.text_input(':blue[Mi]')
 
with col4:
 Lg=st.text_input(':blue[LG]')
 Dior=st.text_input(':blue[Dior]')
 Scabal=st.text_input(':blue[Scabal] ')
 Tommy_Hilfiger=st.text_input(':blue[Tommy Hilfiger]')
 Hollister=st.text_input(':blue[Hollister]')
 Forever_21=st.text_input(':blue[Forever 21]')
 Colavita=st.text_input(':blue[Colavita]')
 Microsoft=st.text_input(':blue[Microsoft]')
 Jiffy_mix=st.text_input(':blue[Jiffy mix]')
 Kraft=st.text_input(':blue[Kraft]')
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
    f"<h1 style='color:#ff6666; font-size: 24px;'>This customer belongs to the group that is more interested in luxury and fashion brands.</h1>",
    unsafe_allow_html=True,)
       
    else: 
      st.markdown(
    f"<h1 style='color:#ff6666; font-size: 24px;'>This Customer belongs to the group that is more interested in practical and functional products.</h1>",
    unsafe_allow_html=True,) 
      
       
       
        

