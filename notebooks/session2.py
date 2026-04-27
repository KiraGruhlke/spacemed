# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python [conda env:conda_envs-gpulab-2025-2]
#     language: python
#     name: conda-env-conda_envs-gpulab-2025-2-py
# ---

# %%
#hello

# %% [markdown]
# # Session2
# We are going to use notebooks for some python
# * basic types
# * flow control

# %%
1+1 #shift+enter to run

# %%
1/2

# %%
a=12 #define the variable "a"

# %%
a

# %%
a*2.5

# %%
type(a) #what kind of variable is "a"

# %%
# ?a #get all information on "a"

# %%
aString="hello, 'world'" #create a string, use each way of quotation marks, but stay consistent

# %%
print(aString)

# %%
aMultiLine="""
Hello world!
It is not sunny today."""
#how to create a multiline string

# %%
print(aMultiLine)

# %%
aString.capitalize()

# %%
aString.upper()

# %%
aString.split()

# %%
aString.split("l") #split on each "l"

# %%
aString.replace("hello", "hi") #replace for one time

# %%
aString

# %%
aString=aString.replace("hello", "hi") #keep the replacement

# %%
aString

# %%
float(1)

# %%
a=1

# %%
b=1.2

# %%
c=str(a+b) #transform a variable to a different kind to be able to add them

# %%
c+b #transforming the variable is not possible -> I cannot add

# %%
aString*2

# %%
aString + aString

# %%
name="Kira"
age=28

# %%
print("{0} is {1} years old".format (name, age)) #use this for larger datasets

# %%
pi=3.14159265

# %%
print(pi)

# %%
print("The value of pi is {:.3f}".format(pi)) #:.3f means to show the first three decimals

# %%
print(f"The value of pi is {pi:.3f}")

# %%
aList=[] #initialize a new empty list called 'aList'

# %%
aList.append(10) #add the number 10 to the end of my list

 # %%
 len(aList) #show me the number of items in this list

# %%
aList.append("hello") #lists are heterogeneous, so I can also add a word

# %%
aList.append(True) #adds a Boolean value to the end of my list

# %%
aList[2]="world" #replace the item currently at position 2 with "world"

# %%
del aList[0] #removes the item at the very first position (python starts with 0) from my list

# %%
aList #show the list

# %%
aList.remove("hello")

# %%
aList

# %%
anotherList=["Hello", "world", "Hello"]

# %%
anotherList.remove("Hello")

# %%
anotherList

# %%
aTupe=(1,"Hello", "world") #other than a list, a Tupe cannot be changed after it is created

# %%
aTupe

# %%
aTupe[0]="wibble" #I try to delete the first item, which doesn't work since it is a Tupe

# %%
numbers=[1,2,3,4,5,6]

# %% [markdown]
# This is slicing.

# %%
# here we are reversing a list
numbers[::-1]

 # %%
 aDict={} #initialize an empty dictionary

# %%
aDict['first'] = "world" # the key 'first' is created and "world" is put in it

# %%
aDict["first"]

# %%
aDict[-1]=100

# %%
aDict

# %%
planets={"earth":1, "jupiter":317.8, "mars":0.107} #initialize dictionary with keys with content

# %%
planets

# %%
p="jupiter"

# %%
print(f"The mass of planet {p} is {planets[p]} earth masses")

# %%
del aDict ["first"] #delete the key "first"

# %%
from pprint import pprint #pprint is a function to print content in a readable manner

# %%
pprint(planets)

# %%
for i in range(10):
    print(i)

# %%
aList=["Moon", "Mars", "Jupiter"]

# %%
for x in aList:
    print(x, len(x))

# %%
for p in planets:
    print(p)

# %% [markdown]
# Create a for loop to print each planet automatically:

# %%
for p in planets:
    print(f"The mass of planet {p} is {planets[p]} earth masses")

# %%
p="earth"

# %% [markdown]
# How to create an if loop:

# %%
if planets[p]>1:
    print (f"{p} has a larger mass than the earth.")
elif planets[p]<1:
    print(f"{p} has a smaller mass than the earth.")
else:
    print(f"{p} has the same mass as the earth.")

# %%
How to integrate the if loop into the for loop to automatically run it on all content:

# %%
for p in planets:
    if planets[p]>1:
        print (f"{p} has a larger mass than the earth.")
    elif planets[p]<1:
        print(f"{p} has a smaller mass than the earth.")
    else:
        print(f"{p} has the same mass as the earth.")
