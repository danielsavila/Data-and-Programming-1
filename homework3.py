# PPHA 30537
# Spring 2024
# Homework 3

# Daniel Avila

# Daniel Avila
# danielsavila

# Due date: Sunday May 5th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

#NOTE: All of the plots the questions ask for should be saved and committed to
# your repo under the name "q1_1_plot.png" (for 1.1), "q1_2_plot.png" (for 1.2),
# etc. using fig.savefig. If a question calls for more than one plot, name them
# "q1_1a_plot.png", "q1_1b_plot.png",  etc.

# Question 1.1: With the x and y values below, create a plot using only Matplotlib.
# You should plot y1 as a scatter plot and y2 as a line, using different colors
# and a legend.  You can name the data simply "y1" and "y2".  Make sure the
# axis tick labels are legible.  Add a title that reads "HW3 Q1.1".

# found this to be very helpful: https://matplotlib.org/stable/users/explain/quick_start.html
# this code was for the set_major_formatter lines: https://matplotlib.org/stable/gallery/text_labels_and_annotations/date.html

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
import matplotlib.dates as mdates
import statsmodels.api as sm

x = pd.date_range(start='1990/1/1', end='1991/12/1', freq='MS')
y1 = np.random.normal(10, 2, len(x))
y2 = [np.sin(v)+10 for v in range(len(x))]

fig, axs = plt.subplots(2, 1)
ax = axs[0]
ax.scatter(x, y1, color = "red", label = "random data")
ax.set_xlabel("Date")
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
ax.set_ylabel("Value")

ax = axs[1]
ax.plot(x, y2, label = "sine data")
ax.set_xlabel("Date")
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
# ax.set_xscale("linear")
ax.set_ylabel("Value")
fig.legend(loc = "outside upper right")

ax.set_title("HW3 Q1.1", loc = "center", y = 2.4)
plt.show()


# Question 1.2: Using only Matplotlib, reproduce the figure in this repo named
# question_2_figure.png.


redx = [i for i in range(10, 20)]
redy = redx[::-1]
bluex = redx
bluey = redx

fig, ax = plt.subplots()
ax.plot(redx, redy, color = "Red", label = "Red")
ax.plot(bluex, bluey, color = "Blue", label = "Blue")
ax.legend(loc = "center left")
ax.set_title("X marks the spot")
plt.show()


# Question 1.3: Load the mpg.csv file that is in this repo, and create a
# plot that tests the following hypothesis: a car with an engine that has
# a higher displacement (i.e. is bigger) will get worse gas mileage than
# one that has a smaller displacement.  Test the same hypothesis for mpg
# against horsepower and weight.

os.getcwd()
base_path = str(os.getcwd()) + "/"
file_loc = os.path.join(base_path, "mpg.csv")

data = pd.read_csv(file_loc)
data.columns

# the below regression tells us that, after controlling for acceleration and model year,
# a one point increase in displacement (not sure what units are here) equates to a .05 decrease in mpg.
#i.e. our regression is telling us that heavier engines are worse for mpg. note that this
# is highly statistically significant.
data = sm.add_constant(data)
data = data.dropna()
dis_model = sm.OLS(endog = data["mpg"], exog = data[["const", "displacement", "acceleration", "model_year"]])
dis_result = dis_model.fit()
dis_result.summary()

#plotting mpg to displacement
fig, ax = plt.subplots()
ax.scatter(data["mpg"], data["displacement"], label = "mpg to displacement")
ax.legend()
plt.show()


# the below regression tells us that, after controlling for acceleration and model year,
# a one unit increase in horsepower gave us a .002 increase in mpg, and a 1 pound(?) increase
# in car weight gave us a .006 decrease in mpg. Only the weight of the engine is statistically significant. 
hw_model = sm.OLS(endog = data["mpg"], exog = data[["const", "horsepower", "weight", "acceleration", "model_year"]])
hw_result = hw_model.fit()
hw_result.summary()

#plotting mpg to weight
fig, ax = plt.subplots()
ax.scatter(data["mpg"], data["horsepower"], color = "red", label = "mpg to horsepower")
ax.legend()
plt.show()

#plotting mpg to horsepower
fig, ax = plt.subplots()
ax.scatter(data["mpg"], data["weight"], color = "green", label = "mpg to weight")
ax.legend()
plt.show()

# Question 1.4: Continuing with the data from question 1.3, create a scatter plot 
# with mpg on the y-axis and cylinders on the x-axis.  Explain what is wrong 
# with this plot with a 1-2 line comment.  Now create a box plot using Seaborn
# that uses cylinders as the groupings on the x-axis, and mpg as the values
# up the y-axis.

fig, ax = plt.subplots()
ax.scatter(data["cylinders"], data["mpg"], label = "cylinders to mpg")
ax.legend()
plt.show()

# this is similar to being long to wide instead of wide to long, we have multiple observations of
# mpg for each increase in cylinders, so we cant tell where "clustering" of observations occurs in this graph.

#referenced this: https://seaborn.pydata.org/generated/seaborn.boxplot.html
sns.boxplot(data = data, x = data["cylinders"], y = data["mpg"])
plt.show()

# Question 1.5: Continuing with the data from question 1.3, create a two-by-two 
# grid of subplots, where each one has mpg on the y-axis and one of 
# displacement, horsepower, weight, and acceleration on the x-axis.  To clean 
# up this plot:
#   - Remove the y-axis tick labels (the values) on the right two subplots - 
#     the scale of the ticks will already be aligned because the mpg values 
#     are the same in all axis.  
#   - Add a title to the figure (not the subplots) that reads "Changes in MPG"
#   - Add a y-label to the figure (not the subplots) that says "mpg"
#   - Add an x-label to each subplot for the x values
# Finally, use the savefig method to save this figure to your repo.  If any
# labels or values overlap other chart elements, go back and adjust spacing.

#again used this: https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_constrained_layout.html#sphx-glr-gallery-subplots-axes-and-figures-demo-constrained-layout-py
# and for saving figs to a location/file naming: https://stackoverflow.com/questions/11373610/save-matplotlib-file-to-a-directory

fig, axs = plt.subplots(2, 2, layout = 'constrained')
ax = axs[0, 0]
ax.scatter(data["displacement"], data["mpg"], color = "red", label = "displacement")
ax.set_xlabel("displacement")

ax = axs[1, 0]
ax.scatter(data["horsepower"], data["mpg"], color = "blue", label = "horsepower")
ax.set_xlabel("horsepower")

ax = axs[0, 1]
ax.scatter(data["weight"], data["mpg"], color = "orange", label = "weight")
ax.set_yticks([])
ax.set_xlabel("weight")

ax = axs[1, 1]
ax.scatter(data["acceleration"], data["mpg"], color = "purple", label =  "acceleration")
ax.set_yticks([])
ax.set_xlabel("acceleration")

fig.suptitle("Changes in MPG")
fig.text(0, .5, "mpg", ha = "center")
fig.savefig(base_path + "/firstfig.png")
plt.show()

# Question 1.6: Are cars from the USA, Japan, or Europe the least fuel
# efficient, on average?  Answer this with a plot and a one-line comment.
data.columns
sns.boxplot(data = data, x = data["origin"], y = data["mpg"])
plt.show()
#japanese cars are the most fuel effecient, they have the highest average, the highest ourliers, and the highest minimum fuel economy.


# Question 1.7: Using Seaborn, create a scatter plot of mpg versus displacement,
# while showing dots as different colors depending on the country of origin.
# Explain in a one-line comment what this plot says about the results of 
# question 1.6.

groupby = data.groupby("origin")
groupby.head()
sns.scatterplot(data = data, x = data["displacement"], y = data["mpg"], hue = "origin")
plt.show()

# Question 2: The file unemp.csv contains the monthly seasonally-adjusted unemployment
# rates for US states from January 2020 to December 2022. Load it as a dataframe, as well
# as the data from the policy_uncertainty.xlsx file from homework 2 (you do not have to make
# any of the changes to this data that were part of HW2, unless you need to in order to 
# answer the following questions).


import us

unemp = pd.read_csv("unemp.csv")
policyunc = pd.read_excel("policy_uncertainty.xlsx")


policyunc["state"] = policyunc["state"].map(us.states.mapping("name", "abbr"), na_action = "ignore")
policyunc["day"] = 1
policyunc.columns = policyunc.columns.str.lower()
policyunc["date"] = pd.to_datetime(policyunc[["year", "month", "day"]])
policyunc.head()
unemp.head()
unemp.columns = unemp.columns.str.lower()
unemp["date"] = pd.to_datetime(unemp["date"])

#    2.1: Merge both dataframes together
merged_df = unemp.merge(policyunc, how = "inner", right_on = ["state", "date"], left_on = ["state", "date"], validate = "one_to_one", indicator = True )
merged_df["_merge"].unique()
#did this as an inner merge because if I had NaN values with a left, right, our outer merge, I would 
# end up removing those columns anyway. So figured I would only use the ones ethat were inner merged.

#    2.2: Calculate the log-first-difference (LFD) of the EPU-C data
merged_df.columns
merged_df = merged_df.drop(["year", "month", "day"], axis = 1)

#need to create a new dataframe so that I can get the log first difference of each state seperately
# without using the last value of ex. Alabama being used to calculate the first value of Arkansas

ldf_df = pd.DataFrame(data = None, columns = merged_df.columns)
states_abbr = merged_df["state"].unique()
for abbr in states_abbr:
    holding_df = merged_df[merged_df["state"] == abbr]
    holding_df["epu_composite"] = np.log(holding_df.loc[:, "epu_composite"]) - np.log(holding_df.loc[:, "epu_composite"].shift())
    ldf_df = pd.concat([ldf_df, holding_df], axis = 0, ignore_index = True)

ldf_df.head(50)

#    2.2: Select five states and create one Matplotlib figure that shows the unemployment rate
#         and the LFD of EPU-C over time for each state. Save the figure and commit it with 
#         your code.

illinois = ldf_df[ldf_df["state"] == "IL"]
michigan = ldf_df[ldf_df["state"] == "MI"]
wisconsin = ldf_df[ldf_df["state"] == "WI"]
vermont = ldf_df[ldf_df["state"] == "VT"]
kentucky = ldf_df[ldf_df["state"] == "KY"]

illinois.columns
illinois["epu_composite"]


fig, axs = plt.subplots(5, 2, layout = "constrained", figsize = (10, 5))

ax = axs[0, 0]
ax.plot(illinois["date"], illinois["epu_composite"], color = "red", label = "illinois")
ax.set_xticks([])
ax.set_ylabel("illinois")

ax = axs[0,1]
ax.plot(illinois["date"], illinois["unemp_rate"], color = "black")
ax.set_xticks([])

ax = axs[1,0]
ax.plot(michigan["date"], michigan["epu_composite"], color = "blue", label = "michigan")
ax.set_xticks([])
ax.set_ylabel("michigan")

ax = axs[1,1]
ax.plot(michigan["date"], michigan["unemp_rate"], color = "black")
ax.set_xticks([])

ax = axs[2,0]
ax.plot(wisconsin["date"], wisconsin["epu_composite"], color = "orange", label = "wisconsin")
ax.set_xticks([])
ax.set_ylabel("wisconsin")

ax = axs[2,1]
ax.plot(wisconsin["date"], wisconsin["unemp_rate"], color = "black")
ax.set_xticks([])

ax = axs[3,0]
ax.plot(vermont["date"], vermont["epu_composite"], color = "purple", label = "vermont")
ax.set_xticks([])
ax.set_ylabel("vermont")

ax = axs[3,1]
ax.plot(vermont["date"], vermont["unemp_rate"], color = "black")
ax.set_xticks([])

ax = axs[4,0]
ax.plot(kentucky["date"], kentucky["epu_composite"], color = "green", label = "kentucky")
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
ax.set_ylabel("kentucky")

ax = axs[4,1]
ax.plot(kentucky["date"], kentucky["unemp_rate"], color = "black")
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))

fig.savefig(base_path + "/secondfig.png")
plt.show()


#    2.3: Using statsmodels, regress the unemployment rate on the LFD of EPU-C and fixed
#         effects for states. Include an intercept.

#creating fixed effects for states
for abbr in states_abbr:
    ldf_df[abbr] = 0
    ldf_df[abbr] = ldf_df["state"].apply(lambda x: 1 if x == abbr else 0)


ldf_df.tail(50)
ldf_df = sm.add_constant(ldf_df)
ldf_df = ldf_df.dropna()

exog_var = list(ldf_df.columns)
exog_var.remove("date")
exog_var.remove("state")
exog_var.remove("unemp_rate")
exog_var.remove("_merge")

states_model = sm.OLS(endog = ldf_df["unemp_rate"], exog = ldf_df[exog_var])
states_result = states_model.fit()

#    2.4: Print the summary of the results, and write a 1-3 line comment explaining the basic
#         interpretation of the results (e.g. coefficient, p-value, r-squared), the way you 
#         might in an abstract.

states_result.summary()
# After controlling for fixed effects, our results are that economic policy uncertainty has a negative effect on unemployment. 
# A 1% increase in composite economic policy uncertainty leads to a -.012734 percent increase in unemployment. (unemployment rate is already in percentages)
# Our results are highly statistically significant, and our regression has an Adj. R-Squared of .629 which indicates a high degree of variability in unemployment is explained by our exog variables. 