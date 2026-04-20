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

# %% [markdown]
# # Rocket Equation
# At time $t_0$ to rocket starts to expel gas at a
# _constant mass flow rate_ $R$ meassured in kg/s
# and _exhaust velocity relative to the rocket_
# $v_e$ in m/s.
# $$
# \frac{dv}{dt} = -\frac{F}{m(t)} = -\frac{Rv_e}{m(t)}
# $$

# %%
# in between the $$ in Markdown, there is a maths-term
# backslash frac gives a fraction

# %% [markdown]
# # Notes Session 6

# %%
def sum_prod(a,b,c=1):
    return c*(a+b)


# %%
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


# %% [markdown]
# ## Open the files and read it, so it is usable

# %%
# input = name of the file, output = time and absorption
# now this cell is a function in itself
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
# # Python Arrays

# %%
a=numpy.arange(10)+1

# %%
a.shape

# %%
a.dtype

# %%
a.nbytes

# %%
b=numpy.array([[1,2,3],[4,5,6]])

# %%
b.shape

# %%
b.T @ b

# %%
a.T@ a # @= Vektorprodukt

# %%
a

# %%
numpy.max(a) # tells the biggest number

# %%
numpy.argmax(a) # tells the maximum position (starting at 0)

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
subset = absorption # now the subset is the whole data set. to practice you can e.g. choose the subset until 1000

# %%
peaks = []
for i in range (len(subset)): # the window moves along the dataset
    start = max(i-w, 0) # the point before is lower (i-w), 0 to include start of data
    end = min(i+w, len(subset)) # len(subset) to include the end of data
    window = subset[start:end]
    max_pos = numpy.argmax(window) + start # gives us the position inside the window, where the maximum is
    if i == max_pos:
        peaks.append(i)
print(peaks)

# %%
pyplot.plot(subset)
pyplot.plot(peaks, subset[peaks], "ro")

# %%
time_peaks = time[peaks]

# %%
delta_t = time_peaks[1:] -time_peaks[:-1]

# %%
hr = 60/ delta_t

# %%
pyplot.plot(hr)

# %% [markdown]
# ### Connotations

# %% [markdown]
# #### Graph with peaks

# %%
test = numpy.arange(20)

# %%
test

# %%
s= test[5:10] # create a subset

# %%
s

# %% [markdown]
# => the index of numbers in our window does change and not match the index in the whole array, so we need to add the lower bound of our subset (+ start in max_pos above)

# %% [markdown]
# #### Graph heart rate

# %%
peaks # to get a list of peaks

# %%
time[peaks] #create an array of time

# %%
tp=time[peaks]

# %%
tp[1:]-tp[:-1] # = delta t

# %% [markdown]
#
