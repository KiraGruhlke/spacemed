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
#     display_name: Python [conda env:conda_envs-compute-conda]
#     language: python
#     name: conda-env-conda_envs-compute-conda-py
# ---

# %% [markdown]
# # Reading a Data File and plotting

# %% [markdown]
# ## Import needed files

# %%
import numpy # import needed files first
from matplotlib import pyplot #import from matplotlib the function for this code

# %% [markdown]
# ## Open the files and read it, so it is usable

# %%
#create lists
time= []
absorption=[]

# %%
dataFile=open("data/pulse_data.csv")

# %%
# !pwd #where am I

# %%
dataFile.readline() # if we run this, we read a line and then discard it, so jump to the next line
for line in dataFile.readlines() : # now the for loop starts with the second line
    line=line.split(",") #split at the comma
    time.append(float(line[0])) # 0 = before the comma; float because it would have been a string and you cannot plot strings, but floats
    absorption.append(float(line[1])) # 1 = after the comma
# if I reexecude the loop later, I might already be in the wrong line of the file

# %%
print(len(time), len(absorption)) # how many items do I have in it (length)

# %%
for i in range (10): # print the first 10 items
    print(time[i], absorption[i])

# %% [markdown]
# ## Random plot

# %%
x=numpy.random.normal(size=(500,)) #select 500 normally distributed random data points
y=numpy.random.normal(size=(500,))

# %%
pyplot.plot(x,y,"or") # plot them in red
pyplot.xlabel("x-achsis") # label the x-achsis
pyplot.ylabel("y-achsis") #label the y-achsis
pyplot.title("random points") # give a title

# %% [markdown]
# ## Plot the PPG

# %%
pyplot.plot(time, absorption) #plot the lists, the first named list is gonna be placed on the x-achsis
pyplot.xlabel("time") # label the x-achsis
pyplot.ylabel("absorption") #label the y-achsis
pyplot.title("PPG") # give a title
