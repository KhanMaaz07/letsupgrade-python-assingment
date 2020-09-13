#!/usr/bin/env python
# coding: utf-8

# In[1]:


# assignment No 1     {day 3}


# In[2]:


# you all are pilots, & we have to land a plane, the altitiude required to land a plane is 1000ft. if its less than that ask the pilot to land
#if its more than 1000ft but less than 5000ft ask the pilot to reduce the altitude to 1000ft.
#if its more than 5000ft then ask the pilot to try again later


# In[4]:


# taking the variable for altitude
at=int(input("inter the altitude"))
#ptint("at is  "at)


# In[5]:


if (at<=1000):
    print("its safe to land the plane")
elif (at>1000 and at<5000):
    print("reduce the altitude to 1000ft")
else:
    print ("try later")
    


# In[ ]:




