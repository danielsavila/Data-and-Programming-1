# PPHA 30537
# Spring 2024
# Homework 4

# Daniel Avila

# Daniel Avila
# danielsavila

# Due date: Sunday May 12th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

# Question 1: Explore the data APIs available from Pandas DataReader. Pick
# any two countries, and then 
#   a) Find two time series for each place
#      - The time series should have some overlap, though it does not have to
#        be perfectly aligned.
#      - At least one should be from the World Bank, and at least one should
#        not be from the World Bank.
#      - At least one should have a frequency that does not match the others,
#        e.g. annual, quarterly, monthly.
#      - You do not have to make four distinct downloads if it's more appropriate
#        to do a group of them, e.g. by passing two series titles to FRED.

# https://fred.stlouisfed.org/series/FPCPITOTLZGPOL
# https://data.worldbank.org/indicator/NY.GDP.PCAP.CD?locations=PL
# https://fred.stlouisfed.org/series/DEXMXUS

#   b) Adjust the data so that all four are at the same frequency (you'll have
#      to look this up), then do any necessary merge and reshaping to put
#      them together into one long (tidy) format dataframe.

import pandas_datareader.data as web
from pandas_datareader import wb
import datetime
import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
import numpy as np

#used documentation to get data https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-fred

fred_mexico_code = "DEXMXUS"
source = "fred"
fred_poland_code = "FPCPITOTLZGPOL"
wb_indicator = "NY.GDP.PCAP.CD"
wb_countries = ["PL", "MX"]

path = os.getcwd()

fred_mexico = web.DataReader(name = fred_mexico_code, 
                             data_source = source, 
                             start = datetime.date(1995, 1, 1),
                             end = datetime. date(2022, 12, 31)) #daily data

fred_poland = web.DataReader(fred_poland_code,
                             data_source = source,
                             start = datetime.date(1975, 1, 1),
                             end = datetime.date(2022, 12, 31)) # annual data

world_bank = wb.download(indicator = wb_indicator, country = wb_countries,
                           start = datetime.date(1990, 1, 1),
                           end = datetime.date(2022, 12, 31)) # annual data

world_bank = world_bank.reset_index()
world_bank["year"] = pd.to_datetime(world_bank["year"])
world_bank["year"] = world_bank["year"].dt.year
world_bank

wbpol = world_bank[world_bank["country"] == "Poland"]
wbpol = wbpol.rename(columns = {"NY.GDP.PCAP.CD": "wb_pl_gdp_per_cap"})
wbpol = wbpol.drop("country", axis = "columns")
wbpol

wbmex = world_bank[world_bank['country'] == "Mexico"]
wbmex = wbmex.rename(columns = {"NY.GDP.PCAP.CD": "wb_mx_gdp_per_cap"})
wbmex = wbmex.drop("country", axis = "columns")
wbmex

fred_mexico = fred_mexico.resample("1y").mean()
fred_mexico = fred_mexico.reset_index()
fred_mexico["year"] = fred_mexico["DATE"].dt.year
fred_mexico = fred_mexico.rename(columns = {"DEXMXUS": "fmex"})
fred_mexico = fred_mexico.drop("DATE", axis = "columns")
fred_mexico


fred_poland = fred_poland.reset_index()
fred_poland["year"] = fred_poland["DATE"].dt.year
fred_poland = fred_poland.drop("DATE", axis = "columns")
fred_poland = fred_poland.rename(columns = {"FPCPITOTLZGPOL": "fpol"})
fred_poland

data = wbpol.merge(wbmex, how = "outer", on = "year", indicator = True)
data = data.drop("_merge", axis = "columns")
data = data.merge(fred_mexico, how = "outer", on = "year", indicator = True)
data = data.drop("_merge", axis = "columns")
data = data.merge(fred_poland, how = "outer", on = "year", indicator = True)
data.head()

#was checking throughout above in the merge steps, so left the data.drop step here, just deleted the 
#printing of data on every step

#   c) Finally, go back and change your earlier code so that the
#      countries and dates are set in variables at the top of the file. Your
#      final result for parts a and b should allow you to (hypothetically) 
#      modify these values easily so that your code would download the data
#      and merge for different countries and dates.
#      - You do not have to leave your code from any previous way you did it
#        in the file. If you did it this way from the start, congrats!
#      - You do not have to account for the validity of all the possible 
#        countries and dates, e.g. if you downloaded the US and Canada for 
#        1990-2000, you can ignore the fact that maybe this data for some
#        other two countries aren't available at these dates.

#   d) Clean up any column names and values so that the data is consistent
#      and clear, e.g. don't leave some columns named in all caps and others
#      in all lower-case, or some with unclear names, or a column of mixed 
#      strings and integers. Write the dataframe you've created out to a 
#      file named q1.csv, and commit it to your repo.

data.columns
path

data.to_csv("q1.csv", na_rep = "NA")

# Question 2: On the following Harris School website:
# https://harris.uchicago.edu/academics/design-your-path/certificates/certificate-data-analytics
# There is a list of six bullet points under "Required courses" and 12
# bullet points under "Elective courses". Using requests and BeautifulSoup: 
#   - Collect the text of each of these bullet points
#   - Add each bullet point to the csv_doc list below as strings (following 
#     the columns already specified). The first string that gets added should be 
#     approximately in the form of: 
#     'required,PPHA 30535 or PPHA 30537 Data and Programming for Public Policy I'

#   - Hint: recall that \n is the new-line character in text

#   - You do not have to clean up the text of each bullet point, or split the details out
#     of it, like the course code and course description, but it's a good exercise to
#     think about.

#   - Using context management, write the data out to a file named q2.csv

#   - Finally, import Pandas and test loading q2.csv with the read_csv function.
#     Use asserts to test that the dataframe has 18 rows and two columns.

url = "https://harris.uchicago.edu/academics/design-your-path/specializations/specialization-data-analytics"
response = requests.get(url)
data = response.content
    
soup = BeautifulSoup(data, "lxml")
"Required courses" in soup.text
"PPHA 30545" in soup.text

ul42 = soup.find_all("ul")[42].find_all("li")
ul43 = soup.find_all("ul")[43].find_all("li")
ul44 = soup.find_all("ul")[44].find_all("li")
ul42

required = []
for row in soup.find_all("ul")[42:44]:
    li_tags = row.find_all("li")
    required.append([val.text for val in li_tags])

elective = []
for row in soup.find_all("ul")[44:45]:
    li_tags = row.find_all("li")
    elective.append([val.text for val in li_tags])

required
elective

# for this list comprehension https://stackoverflow.com/questions/25674169/how-does-the-list-comprehension-to-flatten-a-python-list-work
flattened_required = [i for x in required for i in x]
flattened_elective = [i for x in elective for i in x]

required_list = [["required", i] for i in flattened_required]
elective_list = [["elective", i] for i in flattened_elective]
required_list
elective_list


dataframe = pd.DataFrame(columns = "type, description")
q2 = "q2.csv"
csv_doc = ['type,description']

csv_doc = csv_doc + required_list + elective_list
with open(q2) as file:
    writer = csv.writer("q2.csv")
    writer.writerow(["type, description"])
    for row in csv_doc:
        writer.writerow(row)

test_data = pd.read_csv("q2.csv")

test_data
