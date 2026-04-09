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
pyplot.plot(time, absorption)
pyplot.xlabel("time [s]")

# %%
