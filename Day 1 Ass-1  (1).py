#!/usr/bin/env python
# coding: utf-8

# In[9]:


# assignment No1 
# day2 02/08/2020


# # # DATA STRUCUTURES

# # INTEGER
# 
# 

# In[4]:


a=11
b=7


# In[5]:


a+b


# In[6]:


type(a)


# # FLOAT
# #DECIMAL NO

# In[17]:


x=78.9
r=9.44


# In[18]:


x-r


# In[19]:


type(r)


# # STRING -->> used to store characters

# In[25]:


name= "Messi"


# In[26]:


name2 = "lionel"


# In[29]:


# for CONCAT 
name2 + name


# In[30]:


type (name)


# # ADVANCED DATA STRUCTURES
# 
# 

# # LIST
# #used for oredered sequence of data
# #its a container which can hold multiple data types

# In[34]:


lst = ["Beckham", 7,40,"PSG"]


# In[35]:


lst


# In[36]:


# to retrive particular data from the list
lst [0]


# In[37]:


lst.append([20,3,200,37])


# In[38]:


lst


# In[39]:


# for retriving the sub lst
lst[4][3]


# In[41]:


#for inserting an element in specified index of list
lst.insert(4,"British")


# In[42]:


lst


# In[43]:


#for removing an element
lst.remove(40)


# In[44]:


lst


# In[45]:


#pop is usedlto eliminate the last element if the index value is not specified
lst.pop()


# In[46]:


lst


# In[47]:


# to copy the list
lst.copy()


# In[48]:


#list gets empty by using
lst.clear()


# In[49]:


lst


# # DICTIONARY DATA TYPE
# #ITS AN UNORDERED KEY VALUE PAIRS 
# #ITS AN OBJ IF DICT CLASS

# In[53]:


dit={"name":"Cristiano","no":"7","country":"Portugal","age":"30"}


# In[55]:


dit.get("name")


# In[54]:


dit


# In[58]:


dit.keys()


# In[59]:


dit.copy()


# In[61]:


dit.popitem()


# In[63]:


dit.pop("no")


# In[65]:


dit.update()


# In[66]:


dit


# # SETS
# # USED FOR STORING UNIQUE VALUES
# #MAJORLY USED FOR OPERATIONS LIKE 'UNION''DISJOINT''COMMOM'

# In[68]:


st={"ronaldo","benzema",7,9}


# In[69]:


st


# In[75]:


st.issuperset("benzema")


# In[77]:


#TUPLE
#THESE ARE THE ORDERED IMMUTABLE COLLECTION OF DATA


# In[78]:


tup=("Real Matrid","Juventus","Man united",7,17,28)


# In[79]:


tup.count("Man united")


# In[80]:


tup.index(17)


# # BOOLEAN
# #ITS BASIC DATA TYPE USED FOR TRUE AND FALSE

# In[2]:


ab= "true"
xy= 200
ab=0
gh=0.99


# In[88]:


print(bool(200))


# In[89]:


print(bool(62))


# In[90]:


print (bool(ab))


# In[3]:


print(bool(gh))


# In[10]:


mk=input("enter the value")
print(mk)


# In[ ]:




