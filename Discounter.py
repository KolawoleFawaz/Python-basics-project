#!/usr/bin/env python
# coding: utf-8

# In[57]:


def discount(price):
    if price >= 500:
        discount1 = price * 0.5
        print(f"Discount price is {discount1}")
        
    elif price >=200 and price <500:
        discount2 = price * 0.7
        print(f"Discount price is {discount2}")
        
    elif price <200:
        discount3 = price * 0.9
        print(f"Discount price is {discount3}")
    


# In[61]:


discount(200)


# In[ ]:





# In[ ]:





# In[ ]:




