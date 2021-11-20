#!/usr/bin/env python
# coding: utf-8

# ### Program to find the factorial of a number

# In[34]:


import math

def factorial(n):
    return(math.factorial(n))

num = 10

print ("Factorial of", num, "is",factorial(num))


# ### Program to find the whether a number is prime or composite

# In[35]:


num = int(input("Enter a num"))

if num > 1 :
    for i in range (2,num):
        if (num % i)==0:
            print (num, "is not a prime number")
            break
            
    else:
        print (num,"is a prime number")
elif num == 0 or 1 :
    print (num, "is neither a prime number nor compostite number")
    
else:
    print (num, "is a composite number")


# ### Program for Palindrome String

# In[36]:


my_string = "level"

rev_string = reversed(my_string)


if list (my_string) == list(rev_string):
    print ("The string is Palindrome")
else:
    print ("The string is not Palindrome")


# ### Program to get third side of right angled traingle from other two

# In[37]:


def pythagoras(opp_side,adj_side,hypt):
        if opp_side == str("x"):
            return ("Opposite_Side = " + str(((hypt**2) - (adj_side**2))**0.5))
        elif adj_side == str("x"):
            return ("Adjacent_Side = " + str(((hypt**2) - (opp_side**2))**0.5))
        elif hypt == str("x"):
            return ("Hypotenous = " + str(((opp_side**2) + (adj_side**2))**0.5))
        else:
            return "All inputs are correct!"
        
print (pythagoras(5,12,'x'))
print (pythagoras(12,'x',13))
print (pythagoras('x',5,13))
print (pythagoras(5,12,13))


# ### Program to print the frequency of each of the characters present in a given string

# In[38]:


from collections import Counter

test_string  = 'Kurkure'

res = Counter(test_string)

print ("Frequency of all charecters present in the string is ", (res))


# In[ ]:




