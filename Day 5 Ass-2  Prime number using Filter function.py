#!/usr/bin/env python
# coding: utf-8

# In[5]:


def Prime():
    lower = 1
    upper = 2500
    print("Prime numbers between", lower, "and", upper, "are:")
    
for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break 
            else:
                print(num)
                 
                    
fltrObj=filter(Prime, range(2500)
               print("Prime numbers ")
              ## print("Prime numbers ", list(fltrObj))


# In[ ]:




