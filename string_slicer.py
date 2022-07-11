#!/usr/bin/env python
# coding: utf-8

# In[27]:


def slice(strings):
    result = ""
    
    for x in range(len(strings)):
        if x % 2 == 0:
            result+= strings[x]
    return result
slice("fawaz")
    
    


# In[ ]:




