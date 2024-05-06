#Daniel Avila

import matplotlib.pyplot as plt
import pandas as pd
import datetime

# Load the file UNRATE.csv, which shows the seasonally-adjusted US unemployment
# rate, monthly, from 2000 to present. 
data = pd.read_csv("UNRATE.csv")
data["DATE"] = pd.to_datetime(data["DATE"])
data.head()

#  Create a line plot, with vertical
# lines to mark recessions:
#   March 2001 - November 2001
#   December 2007 - June 2009
#   February 2020 - April 2020

x = data["DATE"]
y = data["UNRATE"]
dates = pd.to_datetime([pd.Timestamp("2000-03-01"),
                        pd.Timestamp("2000-11-01"),
                        pd.Timestamp("2007-12-01"),
                        pd.Timestamp("2009-06-01"),
                        pd.Timestamp("2020-02-01"),
                        pd.Timestamp('2020-04-01')])
fig, ax = plt.subplots()
for i in dates:
    ax.axvline(i, color = "k", linestyle = ":")

ax.plot(x, y, "-b", label ="recession start and end dates")


# Next continue to clean up the figure, adding a title, axis labels, shading the area
# that designates recessions, and any other changes that come to mind. If you manually
# copy-pasted the code for each recession line, try instead to put them in containers
# and use a for-loop.

ax.legend(loc = "best")

plt.show()

