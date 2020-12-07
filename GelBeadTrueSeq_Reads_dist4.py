#!/usr/bin/env python
# coding: utf-8

# In[1]:


# To process data.
import pandas as pd
import numpy as np
# To plot.
from pylab import *
from plotnine import *


# In[2]:


# Loading data
dist4 = pd.read_table("barnyard01.split.txt___DF___SampleN_assigned_duplicates_dropped_dist4.tab")
dist4.head(3)


# In[3]:


# To build df_gsr_drop
df_gsr = dist4.groupby(['GelBead_TrueSeq', 'SampleN'])['umi_seq'].count().reset_index(name = "Reads")
df_gsr_sort = df_gsr.sort_values(by=['Reads'],ascending=False)
df_gsr_drop = df_gsr_sort.drop_duplicates(['GelBead_TrueSeq'])#done


# In[4]:


df_gsr_drop.head(5)


# In[5]:


# geom_point. Reorder GelBead_TrueSeq by Reads.
(ggplot(df_gsr_drop, aes(x = 'reorder(GelBead_TrueSeq,Reads)', y = 'log10(Reads)', color = 'factor(SampleN)' ) )
+ geom_point(aes(size = 'Reads'))
+ scale_alpha_continuous(range=(1,100))
+ labs(x='GelBead_TrueSeq', y='log10(Reads)', title = "GelBead_Reads_dist4")
+ theme_bw()
+ theme(panel_grid=element_blank(), axis_text_x = element_blank(), axis_ticks_major_x=element_blank())
)

