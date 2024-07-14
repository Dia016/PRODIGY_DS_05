#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# In[4]:


import pandas as pd
# Load the dataset
data = pd.read_csv("C:/Users/Admin/Downloads/BigML_Dataset_5fde1fade84f94757d00135a.csv")
data.head()


# In[5]:


print(data.isnull().sum())


# In[6]:


print(data.describe())


# In[9]:


data.columns


# In[10]:


columns_to_drop = ['Alcohol Results', 'Drug Involvement']
data = data.drop(columns=columns_to_drop)


# In[11]:


data = data.dropna(subset=['Crash Date', 'Atmospheric Condition', 'Roadway'])


# In[12]:


data['Crash Date'] = pd.to_datetime(data['Crash Date'])


# In[13]:


data['Year'] = data['Crash Date'].dt.year
data['Month'] = data['Crash Date'].dt.month
data['Day'] = data['Crash Date'].dt.day
data['Hour'] = data['Crash Date'].dt.hour
data['Day_of_Week'] = data['Crash Date'].dt.dayofweek


# In[17]:


get_ipython().system('pip install folium')
import folium


# In[18]:


m = folium.Map(location=[39.8283, -98.5795], zoom_start=4) 


# In[20]:


plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='Hour')
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Accidents')
plt.show()


# In[21]:


plt.figure(figsize=(12, 6))
sns.countplot(data=data, y='Atmospheric Condition', order=data['Atmospheric Condition'].value_counts().index)
plt.title('Weather Conditions During Accidents')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Condition')
plt.show()


# In[22]:


plt.figure(figsize=(12, 6))
sns.countplot(data=data, y='Roadway', order=data['Roadway'].value_counts().index)
plt.title('Road Conditions During Accidents')
plt.xlabel('Number of Accidents')
plt.ylabel('Road Condition')
plt.show()


# In[23]:


plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='Day_of_Week')
plt.title('Accidents by Day of the Week')
plt.xlabel('Day of Week')
plt.ylabel('Number of Accidents')
plt.xticks(ticks=[0, 1, 2, 3, 4, 5, 6], labels=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.show()


# In[46]:


plt.figure(figsize=(18, 10))
sns.countplot(data=data, x='Injury Severity', order=data['Injury Severity'].value_counts().index)
plt.title('Injury Severity in Accidents')
plt.xlabel('Injury Severity')
plt.ylabel('Number of Accidents')
plt.show()


# In[25]:


corr_matrix = data.corr()
plt.figure(figsize=(15, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# In[45]:


plt.figure(figsize=(20, 10))
sns.countplot(data=data, x='Injury Severity', order=data['Injury Severity'].value_counts().index)
plt.title('Injury Severity in Accidents')
plt.xlabel('Injury Severity')
plt.ylabel('Number of Accidents')
plt.show()


# In[27]:


monthly_accidents = data.resample('M', on='Crash Date').size()
plt.figure(figsize=(12, 6))
monthly_accidents.plot()
plt.title('Monthly Accidents Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Accidents')
plt.show()


# In[28]:


plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='Day_of_Week')
plt.title('Accidents by Day of the Week')
plt.xlabel('Day of Week')
plt.ylabel('Number of Accidents')
plt.xticks(ticks=[0, 1, 2, 3, 4, 5, 6], labels=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.show()


# In[32]:


plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='Gender')
plt.title('Accidents by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Accidents')
plt.show()


# In[48]:


plt.figure(figsize=(20, 12))
sns.countplot(data=data, x='Race', order=data['Race'].value_counts().index)
plt.title('Accidents by Race')
plt.xlabel('Race')
plt.ylabel('Number of Accidents')
plt.show()


# In[34]:


plt.figure(figsize=(12, 6))
sns.histplot(data=data, x='Age', bins=20)
plt.title('Distribution of Age in Accidents')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[ ]:




