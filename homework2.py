# PPHA 30537
# Spring 2024
# Homework 2

# Daniel Avila
# danielsavila

# Due date: Sunday April 21st before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.  Using functions for organization will be rewarded.

##################

# To answer these questions, you will use the csv document included in
# your repo.  In nst-est2022-alldata.csv: SUMLEV is the level of aggregation,
# where 10 is the whole US, and other values represent smaller geographies. 
# REGION is the fips code for the US region. STATE is the fips code for the 
# US state.  The other values are as per the data dictionary at:
# https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2022/NST-EST2022-ALLDATA.pdf
# Note that each question will build on the modified dataframe from the
# question before.  Make sure the SettingWithCopyWarning is not raised.

# PART 1: Macro Data Exploration


import pandas as pd
import os


# Question 1.1: Load the population estimates file into a dataframe. Specify
# an absolute path using the Python os library to join filenames, so that
# anyone who clones your homework repo only needs to update one for all
# loading to work.

PATH = r"C:\Users\AVILA\OneDrive\Documents\GitHub\Data-and-Programming-1"
file_path = os.path.join(PATH, "NST-EST2022-ALLDATA.csv")
census = pd.read_csv(file_path)

# Question 1.2: Your data only includes fips codes for states (STATE).  Use 
# the us library to crosswalk fips codes to state abbreviations.  Drop the
# fips codes

# all code below was influenced by what I found at this link: https://pypi.org/project/us/
# when I was running this dictionary, the state.fips was returning as a string,
# so in order to get the mapping to work, needed to convert to int in the variable                                                        
import us as us
fips_to_abbr = {int(state.fips): state.abbr for state in us.states.STATES_AND_TERRITORIES}
fips_to_abbr
census["STATE"] = census["STATE"].map(fips_to_abbr)                   
census["STATE"].head(30)

 # Question 1.3: Then show code doing some basic exploration of the
# dataframe; imagine you are an intern and are handed a dataset that your
# boss isn't familiar with, and asks you to summarize for them.  Do not 
# create plots or use groupby; we will do that in future homeworks.  
# Show the relevant exploration output with print() statements.

# used this code to find duplicates https://www.statology.org/pandas-find-duplicates/
duplicated_states = census[census.duplicated(["STATE"])]                
duplicated_states["STATE"]
print("There are", len(duplicated_states["STATE"]), "NaN objects (unknown entries) in the STATE column")
print("There are", len(census["STATE"].unique()) - 1, "'states' in our data, one of which is Puerto Rico.")
# adding a column of the duplicated states to the census datset and filtering out duplicates
census["duplicates"] = census.duplicated(["STATE"])
census["duplicates"].head(30)
filtered_census = census[census["duplicates"] == False]
# when I filtered in the above step, it left behind one value of NaN at index position 0
# drop method citation https://www.statology.org/pandas-drop-row-by-index/
filtered_census = filtered_census.drop(index = 0)
print(filtered_census.shape)
print(filtered_census.columns)

# Question 1.4: Subset the data so that only observations for individual
# US states remain, and only state abbreviations and data for the population
# estimates in 2020-2022 remain.  The dataframe should now have 4 columns.

filtered_census["STATE"].unique
# dropping Puerto Rico
filtered_census = filtered_census.drop(index = 65)
filtered_census.head()
pop_filtered_census = filtered_census.loc[:, ["STATE", "POPESTIMATE2020", "POPESTIMATE2021", "POPESTIMATE2022"]]

# Question 1.5: Show only the 10 largest states by 2021 population estimates,
# in decending order.

# found sort_values method as a response in this link 
#https://stackoverflow.com/questions/16958499/sort-pandas-dataframe-and-print-highest-n-values
print(pop_filtered_census.sort_values('POPESTIMATE2021', ascending = False).head(10))


# Question 1.6: Create a new column, POPCHANGE, that is equal to the change in
# population from 2020 to 2022.  How many states gained and how many lost
# population between these estimates?

pop_filtered_census["POPCHANGE"] = pop_filtered_census["POPESTIMATE2022"] - pop_filtered_census["POPESTIMATE2020"]
print(pop_filtered_census["POPCHANGE"])

# Question 1.7: Show all the states that had an estimated change in either
# direction of smaller than 1000 people. 

pop_filtered_census[(pop_filtered_census["POPCHANGE"] > 1000) | (pop_filtered_census["POPCHANGE"] < -1000)]

# Question 1.8: Show the states that had a population growth or loss of 
# greater than one standard deviation.  Do not create a new column in your
# dataframe.  Sort the result by decending order of the magnitude of 
# POPCHANGE.

import statistics as stats
pop_filtered_census[pop_filtered_census["POPCHANGE"] > stats.stdev(pop_filtered_census["POPCHANGE"])]

#PART 2: Data manipulation

# Question 2.1: Reshape the data from wide to long, using the wide_to_long function,
# making sure you reset the index to the default values if any of your data is located 
# in the index.  What happened to the POPCHANGE column, and why should it be dropped?
# Explain in a brief (1-2 line) comment.

# refrenced documentation
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.wide_to_long.html
pop_filtered_census_w2l = pd.wide_to_long(pop_filtered_census, stubnames = "POPESTIMATE", i = "STATE", j = "year")
pop_filtered_census_w2l[pop_filtered_census_w2l["POPCHANGE"] == 660]
pop_filtered_census_w2l = pop_filtered_census_w2l.drop("POPCHANGE", axis = 1)
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html
pop_filtered_census_w2l = pop_filtered_census_w2l.reset_index()
pop_filtered_census_w2l
# we need to drop the POPCHANGE column because it is taking the value that we calculated previously, and now adding it as a cell for 
# year 2020, 2021, and 2022. However what we calculated is only the change from 2020 to 2022, so the 2021 and 2020 values are incorrect.

# Question 2.2: Repeat the reshaping using the melt method.  Clean up the result so
# that it is the same as the result from 2.1 (without the POPCHANGE column).

# referenced documentation
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html
pop_filtered_census_melt = pd.melt(pop_filtered_census, id_vars = "STATE", value_vars = ["POPESTIMATE2020", "POPESTIMATE2021", "POPESTIMATE2022"], var_name = "year")
pop_filtered_census_melt["year"] = pop_filtered_census_melt["year"].str.strip("POPESTIMATE")
pop_filtered_census_melt

# Question 2.3: Open the state-visits.xlsx file in Excel, and fill in the VISITED
# column with a dummy variable for whether you've visited a state or not.  If you
# haven't been to many states, then filling in a random selection of them
# is fine too.  Save your changes.  Then load the xlsx file as a dataframe in
# Python, and merge the VISITED column into your original wide-form population 
# dataframe, only keeping values that appear in both dataframes.  Are any 
# observations dropped from this?  Show code where you investigate your merge, 
# and display any observations that weren't in both dataframes.

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
file_path2 = os.path.join(PATH, "state-visits.xlsx")
statevisit = pd.read_excel(file_path2)
statevisit
merged_df = census.merge(statevisit, how = "outer", on = "STATE", validate = "many_to_one", indicator = True)
merged_df["_merge"].unique()
non_both = merged_df[(merged_df["_merge"] == "left_only") | (merged_df["_merge"] == "right_only")]
non_both
# non_both contains the 15 observations in the census dataset that were not states, AND 3 values from the statevisit dataset that consisted of 
# PR, DC, and Guam. So what is happening is that the first 15 observations from census are not being matched to the statevisit dataset,
# and 3 of the observations in the statevisit dataset are not being matched to the census dataset.
# In total, across both datasets, we had 18 observations which were not matched. 
filt_merge_df = merged_df[merged_df["_merge"] == "both"]
filt_merge_df
# filt_merge_df contains just the observations that existed in both the census and statevisit datasets.



# Question 2.4: The file policy_uncertainty.xlsx contains monthly measures of 
# economic policy uncertainty for each state, beginning in different years for
# each state but ending in 2022 for all states.  The EPU_National column esimates
# uncertainty from national sources, EPU_State from state, and EPU_Composite 
# from both (EPU-N, EPU-S, EPU-C).  Load it as a dataframe, then calculate 
# the mean EPU-C value for each state/year, leaving only columns for state, 
# year, and EPU_Composite, with each row being a unique state-year combination.

file_path3 = os.path.join(PATH, "policy_uncertainty.xlsx")
pol_uncertainty = pd.read_excel(file_path3)

pol_uncertainty.tail()
pol_uncertainty["EPUC_mean"] = pol_uncertainty.groupby(["state", "year"])["EPU_Composite"].transform(lambda x: x.mean()).round(2)

# documentation referenced on the transform function and indexing groupby
#https://stackoverflow.com/questions/45797633/looping-over-groups-in-a-grouped-dataframe
#https://pbpython.com/pandas_transform.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transform.html


# Question 2.5 Reshape the EPU data into wide format so that each row is unique 
# by state, and the columns represent the EPU-C values for the years 2022, 
# 2021, and 2020. 



# Question 2.6) Finally, merge this data into your merged data from question 2.3, 
# making sure the merge does what you expect.


# Question 2.7: Using groupby on the VISITED column in the dataframe resulting 
# from the previous question, answer the following questions and show how you  
# calculated them: a) what is the single smallest state by 2022 population  
# that you have visited, and not visited?  b) what are the three largest states  
# by 2022 population you have visited, and the three largest states by 2022 
# population you have not visited? c) do states you have visited or states you  
# have not visited have a higher average EPU-C value in 2022?


# Question 2.8: Transforming data to have mean zero and unit standard deviation
# is often called "standardization", or a "zscore".  The basic formula to 
# apply to any given value is: (value - mean) / std
# Return to the long-form EPU data you created in step 2.4 and then, using groupby
# and a function you write, transform the data so that the values for EPU-C
# have mean zero and unit standard deviation for each state.  Add these values
# to a new column named EPU_C_zscore.
