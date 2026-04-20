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
#     display_name: Python [conda env:.conda-spacemed26]
#     language: python
#     name: conda-env-.conda-spacemed26-py
# ---

# %% [raw]
# title: "Session 6"
# author: Kira Gruhlke
# format:
#   html:
#     code-fold: true
#   pdf:
#     echo: false
#     pdf-engine: pdflatex
#     toc: true
#     number-depth: 2
#     number-sections: true
#     papersize: a4
#     documentclass: article
# jupyter: python3

# %%
# the first cell provides metadata (raw cell)

# %%
# automatically reload any packages that have changes
# %load_ext autoreload
# %autoreload 2

# %% [markdown]
# # Notes Session 6

# %%
# create a new function (def) called sum_prod
# tell it what to do and to return the result
def sum_prod(a,b,c=1):
    return c*(a+b)


# %%
# example
sum_prod(c=1, a=2, b=2)

# %%
name="Kira"
age="28"

# %%
print (name, age, sep=" is ")

# %% [markdown]
# # Reading a Data file and plotting
# *Copy from session 4 to use for session 6*

# %% [markdown]
# ## Import needed files

# %%
import numpy # import needed files first
from matplotlib import pyplot #import from matplotlib the function for this code

# %%
import spacemed

# %%
spacemed.__version__


# %% [markdown]
# ## Create a function to open and look at the data

# %%
# input = name of the file, output = time and absorption
# now this cell is a function in itself
# check connotations on the function itself in session4
def read_pulse (fname):
    dataFile = open(fname)
    time= []
    absorption=[]
    dataFile.readline()
    for line in dataFile.readlines() :
        line=line.split(",")
        time.append(float(line[0]))
        absorption.append(float(line[1]))
    return time, absorption


# %%
time, absorption =read_pulse ("../data/pulse_data.csv") # call the function and open the according dataset, so it can run

# %% [markdown]
# ## Basic Plot

# %%
#| label: fig-dataset
#| fig-cap: "Measurements from an oxymetry sensor as a
#| function of time for 3 cycles"
pyplot.plot(time, absorption)
pyplot.xlabel("time [s]")

# %% [markdown]
# ## Calculate pulse rate

# %% [markdown]
# $$H = \frac{T}{\Delta T_{\text{peaks}}}$$

# %%
absorption = numpy.array(absorption)
time = numpy.array(time)

# %%
w=50 # w = window (compare a point to the points around)

# %%
data = absorption # now the subset is the whole data set. to practice you can e.g. choose the subset until 1000


# %%
def find_peaks (data, w):
    peaks = []
    for i in range (len(data)): # the window moves along the dataset
        start = max(i-w, 0) # the point before is lower (i-w), 0 to include start of data
        end = min(i+w, len(data)) # len(subset) to include the end of data
        window = data[start:end]
        max_pos = numpy.argmax(window) + start # gives us the position inside the window, where the maximum is
        if i == max_pos:
            peaks.append(i)
    return peaks


# %%
print (find_peaks(absorption, 50)) # call the function

# %%
peaks = find_peaks(absorption, 50) # define naming to make plot work

# %%
pyplot.plot(data)
pyplot.plot(peaks, data[peaks], "ro")


# %%
def calc_heart_rate (time, peaks):
        time_peaks = time[peaks]
        delta_t = time_peaks[1:] -time_peaks[:-1]
        hr = 60/ delta_t
        return hr


# %%
print (calc_heart_rate(time, peaks)) # call the function

# %%
hr = calc_heart_rate(time, peaks) # define naming to make plot work

# %%
pyplot.plot(hr)
