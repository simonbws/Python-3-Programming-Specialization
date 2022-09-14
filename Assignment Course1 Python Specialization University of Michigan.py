#!/usr/bin/env python
# coding: utf-8

# # Assignment Course 1 - Python Basics, Python 3 Programming Coursera Specialization/ University of Michigan
# 

# # Task1

# In[6]:


scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"


# In[7]:


scores2 = 0

for i in splittedScors:
    if int(i) == 90 or int(i) > 90:
        scores2+=1
print(scores2)


# # Task2

# In[3]:



splittedScors = scores.split()
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"


# In[5]:


org2 = org.split()
acronym = ''
for word in org2:
    if word not in stopwords:
        acronym = acronym + word[0].upper()
print(acronym)


# # Task3

# In[9]:


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"


# In[10]:


sent2=sent.split()

acronym =''

for word in sent2:
    if word not in stopwords:
        acronym=acronym+word[0].upper()+word[1].upper()+'. '
        

acronym=acronym[:-2]

print(acronym)


# # Task4

# In[11]:


p_phrase = "was it a car or a cat I saw"


# In[12]:


r_phrase=''

for char in p_phrase:
    r_phrase=char+r_phrase
    
print(r_phrase)
print(r_phrase==p_phrase)


# # Task5

# In[13]:


inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]


# In[14]:


for temp in inventory:
    temp = temp.split(',')
    str1="The store has{} {}, each for{} USD."
    str1=str1.format(temp[1],temp[0],temp[2])
    print(str1)


# In[ ]:




