#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
from access_parser import AccessParser as ap
import streamlit as st


# In[14]:


bd_file = ap("Streamlit101.accdb")
tbl = bd_file.parse_table("Cliente")
df = pd.DataFrame(tbl)
st.write(df)


# In[ ]:




