#!/usr/bin/env python
# coding: utf-8

# 13 example

# In[6]:


s1 = '  abc  '

print(f'String =\'{s1}\'')

print(f'After Removing Leading Whitespaces String =\'{s1.lstrip()}\'')

print(f'After Removing Trailing Whitespaces String =\'{s1.rstrip()}\'')

print(f'After Trimming Whitespaces String =\'{s1.strip()}\'')


# 14) Write a python program to represent a user entered number in expanded form. For eg: user_input = 2345 Output = (2x10^3) + (3x10^2) + (4x10^1) + (5x10^0)

# In[1]:


def expand(num):
    n = str(num) # convert number to string
    output = []
    for i, digit in enumerate(n):
         output.append("(" + digit + "x10^" + str(len(n)-i-1) + ")")
    return " + ".join(output)


# In[3]:


n=int(input("Enter a number: "))
expand(n)


# In[ ]:





# 15) Write a python program to determine whether the number entered by the user is an Armstrong number or not?

# In[5]:


num = int(input("Enter a number: "))  
sum = 0  
temp = num  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number") 


# In[ ]:




