#!/usr/bin/env python
# coding: utf-8

# In[3]:


##print the first armstrong no in the range of 1042000 to 702648265 and exit the loop as soon as the no is encounterd.


# In[11]:



lower = 1042000
upper = 702648265

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
        break

   if num == sum:
       print("the first Armstong no is-----",num)


# In[ ]:




