#!/usr/bin/env python
# coding: utf-8

# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

# In[5]:


def divisible_by_5_7(n):
    for i in range(n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

n = int(input("Enter the vlaue of n : "))
result = ",".join(str(i) for i in divisible_by_5_7(n))
print(result)


# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
# Example:
# If the following n is given as input to the program:
# 10
# Then, the output of the program should be:
# 0,2,4,6,8,10
# 

# In[7]:


def even_number(n):
    for i in range (0, n+1, 2):
        yield i
        
n = int(input("enter the value of n:, "))
result = ",".join(str(i) for i in even_number(n))
print(result)


# 3.The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
# 

# In[9]:


n = int(input("Enter the value of n, "))
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci [-2]) for i in range (2, n+1)]
result =",".join(str(i)for i in fibonacci[:n+1])
print(result)


# 4.Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
# 

# In[10]:


email = input("Enter an email address: ")
username = email.split("@")[0]
print("The user name is:", username)


# 5.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# In[30]:


class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init_(self, lenght):
        self.lenght = lenght
    def area(self):
        return self.lenght**2       


# In[34]:


square = (5)
print("the area of the square is:",square)


# In[ ]:




