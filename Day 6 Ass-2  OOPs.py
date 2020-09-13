#!/usr/bin/env python
# coding: utf-8

# In[17]:


import math
#creating a class viz Cone

class Cone:
    def __init__(self, Radius, Height):
        self.Radius = Radius
        self.Height = Height
    
## defining the methods

def Volume():
    pi=22/7
    height = float(input('Height of Cone: '))
    radian = float(input('Radius of Cone: '))
    volume = pi * radian * radian * height/3
    print("Volume is: ", volume)

def Suf_Area():
    pi=22/7
    height = float(input('Height of Cone: '))
    radian = float(input('Radius of Cone: '))
    base = (pi*radian*radian)
    #side = (pi*radian*radian) + (pi*radian) (height*height) + (radian*radian) * (0.5)
    print("base of Cone is: ", base)

    
V=Volume()
S=Suf_Area()


# In[ ]:




