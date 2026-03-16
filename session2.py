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
1+1

# %%
1/2

# %%
a=12

# %%
a

# %%
a*2.5

# %%
type(a)

# %%
# ?a

# %%
aString="hello, 'world'"

# %%
print(aString)

# %%
aMultiLine="""
Hello world!
It is not sunny today."""

# %%
print(aMultiLine)

# %%
aString.capitalize()

# %%
aString.upper()

# %%
aString.split()

# %%
aString.split("l")

# %%
aString.replace("hello", "hi")

# %%
aString

# %%
aString=aString.replace("hello", "hi")

# %%
aString

# %%
float(1)

# %%
a=1

# %%
b=1.2

# %%
c=str(a+b)

# %%
c+b

# %%
aString*2

# %%
aString + aString

# %%
name="Kira"
age=28

# %%
print("{0} is {1} years old".format (name, age))

# %%
pi=3.14159265

# %%
print(pi)

# %%
print("The value of pi is {:.3f}".format(pi))

# %%
print(f"The value of pi is {pi:.3f}")

# %%
aList=[]

# %%
aList.append(10)

# %%
len(aList)

# %%
aList.append("hello")

# %%
aList.append(True)

# %%
aList[2]="world"

# %%
del aList[0]

# %%
aList

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
aTupe=(1,"Hello", "world")

# %%
aTupe

# %%
aTupe[0]="wibble"

# %%
numbers=[1,2,3,4,5,6]

# %% [markdown]
# This is slicing.

# %%
# here we are reversing a list
numbers[::-1]

# %%
aDict={}

# %%
aDict['first'] = "world"

# %%
aDict["first"]

# %%
aDict[-1]=100

# %%
aDict

# %%
planets={"earth":1, "jupiter":317.8, "mars":0.107}

# %%
planets

# %%
p="jupiter"

# %%
print(f"The mass of planet {p} is {planets[p]} earth masses")

# %%
del aDict ["first"]

# %%
from pprint import pprint

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

# %%
for p in planets:
    print(f"The mass of planet {p} is {planets[p]} earth masses")

# %%
p="earth"

# %%
if planets[p]>1:
    print (f"{p} has a larger mass than the earth.")
elif planets[p]<1:
    print(f"{p} has a smaller mass than the earth.")
else:
    print(f"{p} has the same mass as the earth.")

# %%
for p in planets:
    if planets[p]>1:
        print (f"{p} has a larger mass than the earth.")
    elif planets[p]<1:
        print(f"{p} has a smaller mass than the earth.")
    else:
        print(f"{p} has the same mass as the earth.")

# %%
