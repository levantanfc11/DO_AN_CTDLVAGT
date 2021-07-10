#!/usr/bin/env python
# coding: utf-8

# In[1]:


def giaithua(n):
    if n==0:
        return 1
    else:
        return (n * giaithua(n-1))
n = int(input("Nhập số cần tính giai thừa: "))
print("Giai thừa của số n là: ",giaithua(n))


# In[ ]:




