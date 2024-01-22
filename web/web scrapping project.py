#!/usr/bin/env python
# coding: utf-8

# In[7]:


from bs4 import BeautifulSoup
import requests


# In[6]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[8]:


soup.find('table')


# In[9]:


soup.find_all('table')[1]


# In[10]:


soup.find('table', class_ = 'wikitable sortable' )


# In[15]:


table = soup.find_all('table')[1]


# In[16]:


world_titles = table.find_all('th')


# In[17]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[18]:


import pandas as pd


# In[19]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[20]:


column_data = table.find_all('tr')


# In[22]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[23]:


df


# In[24]:


df.to_csv(r'/Users/anitachung/Desktop/web/Companies.csv', index = False)

