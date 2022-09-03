#!/usr/bin/env python
# coding: utf-8

# In[3]:


n=int(input("Enter the number to be check: "))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The entered number by the user is palindrome")
else:
    print("The entered number by the user is not palindrome")


# In[ ]:




