
# coding: utf-8

# # Introduction to Pandas Data Structures
# 
# 
# Pandas is the primary library for Data Analytics in Python.
# Pandas is a software library written for the Python programming language for data manipulation and analysis.
# In particular, it offers data structures and operations for manipulating numerical tables and time series. 
# Pandas is free software released under the three-clause BSD license.
# 
# Developer Wes McKinney started working on Pandas in 2008 while at AQR Capital Management out of the need for a high performance, flexible tool to perform quantitative analysis on financial data. Before leaving AQR he was able to convince management to allow him to Open Source the library.
# 
# Another AQR employee, Chang She, joined the effort in 2012 as the second major contributor to the library. Around the same time, the library became popular in the Python community, and many more contributors joined the project. The project is considered one of the most vital and active data analysis libraries for Python.
# 

# ## Pandas functionality:
# 
# 1.DataFrame object for data manipulation with integrated indexing
# 2.Tools for reading and writing data between in-memory data structures and different file formats
# 3.Data alignment and integrated handling of missing data
# 4.Reshaping and pivoting of data sets
# 5.Label-based slicing, fancy indexing, and subsetting of large data sets
# 6.Data structure column insertion and deletion
# 7.Group by engine allowing split-apply-combine operations on data sets
# 8.Data set merging and joining
# 9.Hierarchical axis indexing to work with high-dimensional data in a lower-dimensional data structure
# 10. Time series-functionality: date range generation and frequency conversion, moving window statistics, moving window linear regressions, date shifting and lagging

# ## Session 1: Series and Dataframes
# 
# ### Series
# 
# A series is a one-dimensional array like object containing an array of data ( of any NumPy data type) and an associated array of data labels, called its index. The simplest Series is formed from only an array of data.
# 

# In[7]:

from pandas import Series


# In[19]:

from pandas import DataFrame


# In[8]:

import pandas as pd


# In[29]:

import numpy as np


# ## Let's create an Series object (obj)

# In[9]:

obj = Series([4, 7, -5, 3])


# In[10]:

obj


# The Series representation shows the index on the left and the values on the right.
# If no index was specified, a default one consisting of integers 0 through N-1 (where N is the length of the data) is created.
# 
# You can get the array representation and index object of the Series via its values and index attributes.

# In[11]:

obj.values


# In[12]:

obj.index


# To create an index that identifies each data point:

# In[14]:

obj2 = Series([4, 7, -5, 3])


# In[15]:

obj2.index = (['d', 'b', 'a', 'c'])


# In[18]:

obj2


# In[20]:

obj2.index


# Compared with a regular NumPy array, you can use values in the index when selecting single values or a set a values:

# In[21]:

obj2['a']


# In[22]:

obj2['d'] = 6


# In[23]:

obj2[['c', 'a', 'd']]


# You can perform NumPy operations, such as filtering with a boolean array, scalar multiplication or applying math functions. The index-value link will be preserved:

# In[24]:

obj2[obj2 >0] 


# In[25]:

obj2 * 2 


# In[30]:

np.exp(obj2)


# Series can be substituted into many functions that expect a dict:

# In[31]:

'b' in obj2


# In[32]:

'e' in obj2


# You can create a Series from a dict:

# In[34]:

sdata = {'Ohio':35000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}


# In[35]:

obj3 = Series(sdata)


# In[36]:

obj3


# When only passing a dict, the index in the resulting Series will have the dict's keys is sorted order:

# In[37]:

states = ['California', 'Ohio', 'Oregon', 'Texas']


# In[38]:

obj4 = Series(sdata, index=states)


# In[39]:

obj4


# Since no value was found for 'California', it appears as a NaN (not a number) which is considered in pandas  to mark  missing  or NA values.
# 
# Functions isnull and notnull are used in pandas to detect missing data.

# In[40]:

pd.isnull(obj4)


# In[41]:

pd.notnull(obj4)


# In[42]:

obj4.isnull()


# Series automatically aligns differently-indexed data in arithmetric operations:

# In[43]:

obj3


# In[44]:

obj4


# In[45]:

obj3 + obj4


# Data alignment features are addressed as a separate topic.

# Both Series object itself and its index have a **name** attribute, which integrates with other key areas of Pandas functionality.

# In[46]:

obj4.name = 'population'


# In[47]:

obj4.index.name = 'state'


# In[48]:

obj4


# A Series's index can be altered in place by assignment:

# In[49]:

obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']


# In[50]:

obj


# ### DataFrame
# 
# 1. A DataFrame represents a tabular, spreadsheet-like data structure containing an ordered collection of columns, each of which can be a different value type (numeric, string, boolean, etc.). 
# 2. The DataFrame has both a row and a column index
# 3. A DataFrame can be thought of as a dict of Series (one for all sharing the same index)

# A DataFrame can be created from a dict of equal-length lists or NumPy arrays:

# In[51]:

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)


# The resulting DataFrame will have its index assigned automatically as with Series, and the columns are placed in sorted order:

# In[52]:

frame


# You can specify a sequence of columns:

# In[53]:

DataFrame(data, columns=['year', 'state', 'pop'])


# As with Series, if you pass a column that isn't contained in data, it will appear with NA values in the result:

# In[54]:

frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index =['one', 'two', 'three', 'four', 'five'])


# In[55]:

frame2


# In[56]:

frame2.columns


# A column is a DataFrame can be retrieved as a Series either by dict-like notation or by an attribute:

# In[57]:

frame2['state']


# In[58]:

frame2.year


# Note that the returned Series have the same index as the DataFrame, and their name attribute has been appropiately set.
# Rows can also be retrieved by position or name by a couple of methods, such as the ix indexing field:

# In[59]:

frame2.ix['three']


# Columns can be modified by assignment. For example, the empty 'debt column could be assigned a scalar value or an array of values:

# In[60]:

frame2['debt'] = 16.5


# In[61]:

frame2


# In[62]:

frame2['debt'] = np.arange(5.)


# In[63]:

frame2


# When assigning lists or arrays to a column, the value's length must match the length of a DataFrame.
# If you assign a Series, it will be instead conformed exactly to the DataFrame's index, inserting missing valures in any holes:

# In[64]:

val = Series([-1.2, -1.5, -1.7], index = ['two', 'four', 'five'])


# In[65]:

frame2['debt'] = val 


# In[66]:

frame2


# Assigning a column that doesn't exist creates a new column.     
# The **del** keyword will delete columns as with a dict:

# In[67]:

frame2['eastern'] = frame2.state = 'Ohio'


# In[68]:

frame2


# In[69]:

del frame2['eastern']


# In[70]:

frame2


# In[71]:

frame2.columns


# Another common form of data is a nested dict of dicts format:

# In[72]:

pop = {'Nevada': {2001:2.4, 2002:2.9}, 'Ohio': {2000:1.5, 2001:1.7, 2002:3.6}}


# If passed to DataFrame, it will interpret the outer dict keys as the columns and the inner keys as the row indices:

# In[73]:

frame3 = DataFrame(pop)


# In[74]:

frame3


# You can transpose the result:

# In[76]:

frame3.T


# The keys in the inner dicts are unioned and sorted to form the index in the result. This doesn't happen if an explicit index is specified:

# In[77]:

DataFrame(pop, index = [2001, 2002, 2003])


# Dicts of Series are treated much in the same way:

# In[78]:

pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}


# In[79]:

DataFrame(pdata)


# In[80]:

frame3['Ohio']


# In[81]:

frame3['Ohio'][:-1]


# If a DataFrame's index and columns have their name attributes set, these will also be displayed:

# In[82]:

frame3.index.name = 'year'; frame3.columns.name = 'state'


# In[83]:

frame3


# Like Series, the values attribute returns the data contained in the DataFrame as a 2D narray:

# In[84]:

frame3.values


# If the DataFrame's columns are different dtypes, the dtype of the values array will be chosen to accomodate all ofvthe columns:

# In[85]:

frame2.values


# Exercise:
# Create a DataFrame for a group of students in a Running Club with name, age, zipcode, phone. Dataframe name should be "Run_Club", and specify the index feature as 'name'. Transpose the dataFrame
