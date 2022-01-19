#!/usr/bin/env python
# coding: utf-8

# In[6]:


#This simple Python program calculates the approx. time you have left on this earth based on the life expectancy of your country.
#It shows you how many years, months, or days you have left.
#The months and days are calculated based on the fact that there are 12 months or (usually) 365 days in one year.

life_exp = int(input("What's life expectancy in your country? "))
age = int(input("How old are you now? "))

print(f"\nYou have approx. {life_exp - age} years left.")
print(f"That's {(life_exp - age) * 12} months, or {(life_exp - age) * 365} days.")
print("Do your best each day!")


# In[ ]:





# In[ ]:




