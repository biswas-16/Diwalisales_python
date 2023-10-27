#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install numpy')


# In[2]:


get_ipython().system('pip install seaborn')


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df = pd.read_csv('Diwali Sales Data.csv', encoding = 'unicode_escape')


# In[5]:


df.shape


# In[6]:


df.head()


# In[7]:


df.info()


# # EXPLORATORY DATA ANALYSIS EDA
# 

# In[9]:


ax = sns.countplot(x='Gender',data=df)

for bar in ax.containers:
    ax.bar_label(bar)


# In[10]:


df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[17]:


sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Gender',y='Amount' , data = sales_gen)


# From the above graph we can see that most of the buyers are female and the purchasing power of female is more than male.

# # AGE

# In[19]:


sns.countplot(data=df,x='Age Group', hue='Gender')


# In[20]:


ax=sns.countplot(data=df,x='Age Group', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[25]:


sales_age=df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Age Group',y='Amount' ,  data = sales_age)


# From the above graph we can see that most of the buyers are between the age group 26-35.

# # STATE

# In[35]:


sale_state=df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(16,10)})
sns.barplot(x='State',y='Orders',data=sale_state)


# From the above graph we can see that most of the orders are placed from Uttarpradesh.

# # PRODUCT CATEGORY

# In[44]:


sns.set(rc={'figure.figsize':(30,10)})
ax=sns.countplot(data=df,x='Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)


# The above graph shows the category of product with highest number of sales.

# In[56]:


sale_product=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by= 'Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,10)})
sns.barplot(data=sale_product,x='Product_Category',y='Amount')


# In the above graph we could see that maximum amount is spent on Fooding.

# # TOP SELLING PRODUCT

# In[57]:


sale_product=df.groupby(['Product_ID'],as_index=False)['Amount'].sum().sort_values(by= 'Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,10)})
sns.barplot(data=sale_product,x='Product_ID',y='Amount')


# Product Id P00265242 is the top selling product.

# In[ ]:




