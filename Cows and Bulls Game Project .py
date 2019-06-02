#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random

random_number = str(random.randrange ( 1000 , 10000 ))
print(random_number)

dict_digits = {'digit_1':random_number[0],'digit_2':random_number[1],'digit_3':random_number[2],'digit_4':random_number[3]}

usr_num = '1035'
usr_separate = {'digit1':usr_num[0],'digit2':usr_num[1],'digit3':usr_num[2],'digit4':usr_num[3]}
cows_bulls = [0,0]
for every_digit in usr_separate and dict_digits:
    x = usr_separate.get(every_digit)
    y = dict_digits.get(every_digit)
    
    if dict_digits('digit_1') == usr_separate('digit2') or usr_separate('digit3') or usr_separate('digit4'):
        cows_bulls[1]+=1
            
    while cows_bulls[0] < 4:
        
        if x==y:
            cows_bulls[0]+=1
        elif x!=y:
            cows_bulls[1]+=1
            

        


# In[ ]:




