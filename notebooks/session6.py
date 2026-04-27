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
# This is the notebook of session 6 of the SpaceMed Digital Literacy course 2026. 
# In this notebook data from a pulse oxymetry sensor is analyzed and plotted: Peaks are detected and based on these heart rate (in this case = pulse rate) is calculated und plotted.

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
time, absorption =spacemed.read_pulse ("../data/pulse_data.csv") # call the function and open the according dataset, so it can run

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
# transform lists into arrays
absorption = numpy.array(absorption)
time = numpy.array(time)

# %%
peaks = spacemed.find_peaks ("../data/pulse_data.csv",w=50) #call the function to detect peaks

# %%
print (spacemed.find_peaks(absorption, 50)) # print results

# %%
peaks = spacemed.find_peaks(absorption, 50) # define naming to make plot work

# %%
pyplot.plot(absorption)
pyplot.plot(peaks, absorption[peaks], "ro")

# %%
peaks = spacemed.find_peaks(absorption, 50)

# %%
peaks = numpy.array(peaks)
time = numpy.array(time)

# %%
heart_rate = spacemed.calc_heart_rate (time, peaks) # call the function to calculate heart rate

# %%
print (heart_rate) # print results

# %%
pyplot.plot(heart_rate)
