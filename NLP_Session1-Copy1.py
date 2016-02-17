
# coding: utf-8

# # WOMEN WHO CODE - DATA ANALYTICS WITH PYTHON (INTERMEDIATE)
# 
# ## Introduction

# In[2]:

import nltk


# nltk.download()
# 
# Download the NLTK Book Collection (30 compressed files about 100Mb disk space) to complete the exercises

# In[3]:

from nltk.book import *


# ## SEARCHING TEXT 

# There are many ways to examine the context of a text.
# A CONCORDANCE  view show us every occurrence of a given word.
# CONCORDANCE permits us to see words in context.
# 
# Look for the word "monstrous" in Moby Dick

# In[3]:

text1.concordance("monstrous")


# CONCORDANCE permits us to see words in context such as *the_pictures* and *the_size*

# What other words appear in a similar range of contexts?
# Use SIMILAR to find out.

# In[5]:

text1.similar("monstrous")


# In[6]:

text2.similar("monstrous")


# Observe that we get different results for different texts.
# Austen uses "monstrous" in a very different way than Melville.
# Austen is positive and Melville negative.

# **COMMON_CONTEXTS** allow us to examine just the contexts that are shared by two or more words, such as *montrous* and *very*

# In[7]:

text2.common_contexts(["monstrous", "very"])


# ## Exercise: 
# 
# Pick another pair of words and test similar() and common_texts() in both texts. 

# ## Determine a word distribution
# 
# We can determine the location of a word in a text (how many words from the beginning it appears.) This is a positional information can be displayed using a **dispersion plot**.
# 
# Let's use the U.S. Presidential Inaugural Addresses to create a dispersion plot. First install and import Numpy and Matplotlib packages to produce the graph.

# In[8]:

import numpy as np


# In[9]:

import matplotlib as mpl


# In[10]:

p = text4.dispersion_plot(["citizens","democracy", "freedom", "America"])


# In[11]:

p


# ## Counting Vocabulary
# 
# Let's find the length of a text from start to finish, in terms of the words and punstuation symbols that appear. We are going to apply len to the book of Genesis:

# In[15]:

len(text3)


# Genesis has 44,764 words and punctuation symbols or **tokens**
# 
# A **TOKEN** is the technical name for a sequence of characters (hairy, his, :) that we want to treat as group.
# 
# **How many distinct words does the book of Genesis contain?**
# 
# The vocabulary of a text is the **SET** of tokens that it uses (duplicates are collapsed together)

# set(text3)
# 
# sorted(set(text3))
# 
# Note: All capitalized words precede lowercase words.

# In[16]:

len(sorted(set(text3)))


# Although the book of Genesis has 44,764 tokens, this book has only 2,789 distinct words or words types.
# a **word type** is the form of spelling of the word independently of its specific occurrences in a text - that is, the word considered as a unique item of vocabulary.
# This count will include punctuation symbols, so we can generally call these unique items **types** instead of word types.

# Calculate the lexical richness of the text. The next example shows us that each word is used 16 times on average (use floating-point division):

# In[17]:

len(text3) / len(set(text3))


# We can count how often a word occurs in a text, and compute what percentage of the text is taken up by a specific word:

# In[18]:

text3.count("smote")


# In[19]:

100 * text4.count('a') / len(text4)


# ## Exercise:
# 
# How many times does the word *lol* appears in text5?

# Because counting words and calculating *lexical diversity* and *percentage* are very common we can a function to do that.

# In[20]:

def lexical_diversity(text):
    return len(text) / len(set(text))


# In[21]:

def percentage(count, total):
    return 100 * count / total


# In[22]:

lexical_diversity(text3)


# In[23]:

lexical_diversity(text5)


# In[24]:

percentage(text4.count('a'), len(text4))


# ### Examples of Lexical diversity by Genre
# 
# 1. skill and hobbies (6.9)
# 2. humor (4.3)
# 3. fiction: science (4.5)
# 4. press: reportage (7.0)
# 5. fiction: romance (8.3)
# 6. religion (6.2)
# 

# ## Python: Texts as Lists of Words
# 
# A text is a sequence of symbols
# Here is how we represent in Python the opening sentence of *Moby Dick*

# In[25]:

sent1 = ['Call', 'me', 'Ishmael', '.']


# In[26]:

len(sent1)


# In[27]:

lexical_diversity(sent1)


# In[28]:

sent2


# ## Exercise:
# 
# Make up two sentences of your own and apply set(), sorted(), len() and ex.count()

# ## Concatenation
# 
# In Python you can use addition operation on lists. Adding two lists creates a new one with everything in the first list followed by everything in the second list.

# In[29]:

sent4 + sent1


# To add a new element to the list use append() 

# In[30]:

sent1.append("Some")
sent1


# ## Indexing Lists
# 
# We can identify the elements of a Python list by the order of occurrence in the list.
# The element that represents this position is the item's **index**.

# In[31]:

text4.index('awaken')


# ### Slicing
# 
# Python permits to access sublists, extracting manageable pieces of language from large texts.

# In[32]:

text5[16715:16735]


# Some other subtleties of indexes:

# In[33]:

sent = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10']


# In[34]:

sent[0]


# In[35]:

sent[9]


# In[36]:

sent[1:9]


# ### Computing with Language: Simple Statistics
# 
# Check the following code

# In[37]:

saying = ['After', 'all', 'is', 'said', 'and', 'done', 'more', 'is', 'said', 'than', 'done']
tokens = set(saying)
tokens


# In[38]:

tokens = sorted(set(saying))
tokens


# In[39]:

tokens[-2:]


# You can use a word as a string

# In[40]:

name = 'Monty'
name[0]


# In[41]:

name[4]


# In[42]:

name * 2


# In[43]:

name + '!'


# You can join words of a list to make a single string, or split a string into a list.

# In[44]:

' '.join(['Monty', 'Python'])


# In[45]:

'Monty Python'. split()


# ### Frequency distributions
# 
# A Frequency Distribution tells us the frequency of each vocabulary item in the text.
# Let's use the FreqDist to find the 50 most frequent words in *Moby Dick*

# In[46]:

fdist1 = FreqDist(text1)
fdist1


# Now use the expression *keys* to get a list of all the distinct types in the text.

# In[47]:

vocabulary1 = fdist1.keys()


# In[48]:

vocabulary1


# In[49]:

len(vocabulary1)


# In[50]:

fdist1['whale']


# In[4]:

fdist1 = FreqDist(text1)


# In[5]:

fdist1['bass']


# In[9]:

fdist1.plot(50, cumulative=True)


# In[7]:

fdist5 = FreqDist(text5)


# In[8]:

sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)

