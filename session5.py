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

# %% [markdown]
# # Session 5 - Pandas

# %%
import pandas

# %%
station_ids = pandas.read_csv("data/Niederschlag_1981-2010_Stationsliste.txt",
                              encoding="iso-8859-1", delimiter=" *; *", #star to include any number of spaces
                             index_col="Stations_id", engine="python") #read the file

# %%
station_ids #show an overview

# %%
station_ids.columns #tell us which columns are there

# %%
station_ids.info() #get information; brackets to display it nicely

# %%
station_ids.head() #show first five lines

# %%
station_ids.tail() #show last five lines

# %%
station_ids.drop (station_ids.columns [-1], axis=1, inplace=True) #delete the last column (columns=-1, lines=0)

# %%
station_ids.columns # run to check the working of prior line

# %%
station_ids.info()

# %%
station_ids.head()

# %%
station_ids.iloc[2,0] #iloc: use the index 2,0 (see loading of data, which made the station-id-column usable as an index)

# %%
station_ids.iloc[:5] #slice 5 out of it

# %%
station_ids.loc[:1:3]

# %%
station_ids.loc[3,"Stationsname"]

# %%
station_ids.loc[3:6,"Stationsname"] # after slicing 5 is missing nows

# %%
station_ids.loc["geogr. Breite":"geogr. Laenge"]

# %%
station_ids["Bundesland"]

# %%
station_ids.Bundesland #for names without space also possible

# %%
station_ids.groupby("Bundesland").count().sort_values("Stationsname")
# split dataset into groups (Bundesland), count the members of each group and sort by name

# %%
mask=station_ids.Bundesland=="Bayern" #when "Bayern" is true or false

# %%
station_ids[mask]

# %%
bayern=station_ids[mask] # start a new subgroup assigned as bayern

# %%
station_ids.Bundesland.iloc[-1]

# %%
bayern.loc[17] #show position 17

# %% [markdown]
# ## Precipitation Data (exercise Alexanderplatz and follow up)
# get a list of stations in Berlin  
# figure out the station ID of Berlin Alexanderplatz  
# load the 30 year mean precipitation data "data/Niederschlag 1981-2010.txt"  
# only keep the columns with the monthly means

# %%
precip_ref = pandas.read_csv("data/Niederschlag_1981-2010.txt", # get all precipitation
                              encoding="iso-8859-1", delimiter=" *; *",
                             index_col="Stations_id", engine="python")

# %%
precip_ref = precip_ref.loc[:,"Jan.":"Dez."] #get monthly mean precipitation

# %%
precip_ref.loc[399] # monthly mean precipitation on Berlin Alexanderplatz (ID=399)

# %%
precip_ref.loc[399].plot.bar()

# %%
precip = pandas.read_csv("data/produkt_precipitation_399_akt.txt",
                              encoding="iso-8859-1", delimiter=" *; *",
                              engine="python")

# %%
precip.head()

# %%
precip["date_time"]=pandas.to_datetime(precip.MESS_DATUM, format="%Y%m%d%H")
#take the column and convert the numbers into the given data format (we overwrite the column)

# %%
precip_alex=precip[["date_time", "NIEDERSCHLAGSHOEHE"]]

# %%
precip_alex=precip_alex.rename(columns={"date_time" : "date",
                                        "NIEDERSCHLAGSHOEHE" : "precipitation"})
# rename the columns and overwrite the previous precip_alex

# %%
precip_alex=precip_alex.set_index("date")

# %%
precip_alex.plot()

# %%
monthly = precip_alex.resample("ME").sum() # ME=monthly

# %%
monthly.describe()

# %%
precip_ref.loc[399]

# %%
monthly.groupby(monthly.index.month).describe() #for each year groups our data by month 

# %%
monthly.plot()

# %%
refs=pandas.DataFrame({"precipitation":precip_ref.loc[399].to_list()*12},
                      index=pandas.date_range("2015-01-01", "2026-12-31", freq="ME"))
# create a new DataFrame with only one column: precipitation
# from climate data grab Alexanderplatz and convert it to a list, repeat this 12 times

# %%
refs

# %%
monthly["climate"] = refs # create a new column: climate

# %%
monthly

# %%
monthly.plot()

# %%
monthly["anomaly"]=monthly.precipitation - monthly.climate
#to just get the defference between the general mean precipitation and the mean precipitation on Alexanderplatz

# %%
monthly.anomaly.plot()
# many spikes in minus-area, so Berlin is dryer

# %%
