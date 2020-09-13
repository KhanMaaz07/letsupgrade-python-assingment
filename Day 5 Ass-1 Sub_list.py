#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Python3 code to demonstrate  
# to check if list is subset of other  
  
# initializing list 
num = input(range(0,10)) 
sub_list = [1, 1, 5] 
  
# printing original lists 
print ("Original list : " + str(num)) 
print ("Original sub list : " + str(sub_list)) 
  
      
# printing result 
for sub_list in range(0,10):
    if (num==sub_list):
        print ("its a Match") 
        break
    else : 
        print ("its Gone.") 
        break

