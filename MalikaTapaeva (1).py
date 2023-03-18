#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
my_series = pd.Series([5, 6, 7, 8, 9, 10])
my_series[3]


# In[8]:


my_series2=pd.Series([5, 6, 7, 8, 9,], index=[ 'a', 'b', 'c', 'd', 'e'])
my_series2[['a', 'b', 'e']]


# In[12]:


import pandas as pd
my_series3=pd.Series({'РОССИЯ':'Москва', 'Германия':'Берлин', 'UK':'Лондан', 'USA':'Вашенктон'})
my_series3['РОССИЯ']


# In[15]:


import pandas as pd
df= pd.DataFrame({
    'Продукты': ['Хлеб', 'Булка', 'Кефир', 'Сыр', 'Шоколад'],
    'Кол-во': [1, 2, 1, 0.2, 1],
    'Цена': [32, 15, 70, 450, 75]
})
df['Стоимость']=df['Кол-во']*df['Цена']
df


# In[21]:


import pandas as pd
df= pd.DataFrame({
    'Класс':[ '8А','8Б','8B', '8Г', '8K'],
    'Кол-во учеников':[11, 12, 13, 14, 15]
})
df['Кол-во съедяных яблок']=df['Кол-во учеников']*3
df


# In[ ]:




