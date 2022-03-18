#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Hello World')


# In[2]:


import calendar


# In[3]:


cal = calendar.month(2019,7)


# In[4]:


print(cal)


# In[5]:


import math


# In[6]:


result = math.sqrt(49)


# In[7]:


print(result)


# In[8]:


import random


# In[9]:


number = random.randint(1,100)


# In[10]:


print(number)


# In[14]:


movies = ['aladin','star wars','harry potter','lord of the rings']


# In[15]:


watch = random.choice(movies)


# In[16]:


print(watch)


# In[17]:


random.shuffle(movies)

print(movies)
# In[18]:


print(movies)


# In[1]:


name = "Brad"
groupOfNames = ["Juan", "Snorri","Andre"]


# In[2]:


type(name)


# In[3]:


type(list)


# In[4]:


n = 5


# In[5]:


print(n)


# In[6]:


listA = [1,2,3,4,5,6]


# In[7]:


print(listA)


# In[8]:


type(listA)


# In[ ]:


print(listaA[0])


# In[10]:


print(listA[0])


# In[11]:


listA[0] = 7


# In[12]:


print(listA[0])


# In[13]:


print(listA)


# In[14]:


listB = [True,"Star Wars",5]


# In[15]:


print(listB)


# In[16]:


type(listB)


# In[17]:


child1_birth = ("Julia","Lucile Packard Hospital", "Standford","California","07/29/2019","09:42")


# In[18]:


child2_birth = ("Juan", "San Roque Hospital", "Cordoba", "Cordoba", "07/03/1995", "00:01")


# In[ ]:


type(chil1_birth)


# In[20]:


type(child1_birth)


# In[ ]:


type(chile2_birth)


# In[22]:


type(child2_birth)


# In[23]:


print(child1_birth)


# In[24]:


print(child2_birth)


# In[25]:


print(child1_birth[0])


# In[ ]:


child2_birth[0] = "Snorri"


# In[27]:


raining = input("Is it raining? (yes/no)")
if raining == yes:
    print("You need an umbrella")


# In[28]:


raining = input("Is it raining? (yes/no)")
if raining == "yes":
    print("You need an umbrella")


# In[ ]:


print(raining)


# In[31]:


n = input("Choose and integer between -10 and 10 and enter it here:")
n = int(n)
if n < 5:
    print("The integer you choose is lees than 5.")


# In[32]:


def minimum(x,y):
    if x < y:
        return x
    else: return y


# In[33]:


result = minimum(2,5)
print(result)


# In[35]:


result = minimum(-2,-5)
print(result)


# In[36]:


result = minimum(7,7)
print(result)


# In[37]:


result = minimum(3,3.1)
print(result)


# In[2]:


raining2 = input("Is it raning? (yes/no)")
umbrella = input("Do you have an umbrella? (yes/no)")
if raining2 == "yes" and umbrella == "yes":
    print("Don't forget your umbrella")
elif raining2 == "yes" and umbrella == "no":
    print("Wear a waterproof jacket then")


# In[3]:


x = input("Enter a number here: ")
x = float(x)
if x < 2:
    print("the number is less than 2")
elif x < 6:
    print("the number is less than 6")
elif x < 8:
    print("the number is less than 8")
elif x < 10:
    print("the number is less than 10")


# In[4]:


x = 1
print(float(x))


# In[5]:


x = 1.5
print(int(x))


# In[6]:


x = input("Enter a number here: ")
x = float(x)
if x < 2:
    print("the number is less than 2")
if x < 6:
    print("the number is less than 6")
if x < 8:
    print("the number is less than 8")
if x < 10:
    print("the number is less than 10")


# In[7]:


def abs_val(num):
    if num < 0:
        return -1 * num
    elif num == 0:
        return 0
    else:
        return num


# In[8]:


result = abs_val(-4)
print(result)


# In[9]:


result = abs_val(0)
print(result)


# In[10]:


result = abs_val(78.3)
print(result)


# In[11]:


#Hangman game
word = "serendipitous"
vowels = ["a","e","i","o","u"]
vowelCount = 0


# In[12]:


for i in range(4):
    print(i)


# In[13]:


for i in range(1,8,2):
    print(i)


# In[18]:


for v in vowels:
    print(v)


# In[19]:


length = len(vowels)
print(length)


# In[21]:


i = 0
while i < length:
    print(vowels[i])
    i += 1


# In[22]:


class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def bark(self):
        print("woof woof")


# In[23]:


fido = Dog("Fido",2)


# In[24]:


fido.bark()


# In[25]:


print(fido.name)


# In[26]:


print(fido.age)


# In[27]:


print(fido)


# In[30]:


fido.age +=1 


# In[31]:


print(fido.age)

