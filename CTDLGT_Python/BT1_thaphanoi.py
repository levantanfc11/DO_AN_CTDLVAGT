#!/usr/bin/env python
# coding: utf-8

# In[1]:


dia = int(input("Nhập số lượng đĩa:"))
def baitoanthaphanoi (dia, A, B, C):
    if dia == 1:
        print('Đĩa ',dia,'di chuyển',A,'=>>',C)
        return
    baitoanthaphanoi(dia-1,A,C,B)
    print('Đĩa ',dia,'di chuyển',A,'=>>',C)
    baitoanthaphanoi(dia-1,B,A,C)
baitoanthaphanoi(dia, "A", "B", "C")


# In[ ]:




