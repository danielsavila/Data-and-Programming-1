#DANIEL AVILA

import pandas as pd

#1. It's a puzzle! Load these three dataframes and explore their structure.
#Then combine them so that the result is a single dataframe with the columns 
#"date", "place", "value1", "value2", with the date columns being datetime 
#objects that run from 1/2020 to 10/2021, without modifying any starter code.

data1 = {'date':['2020-1-1', '2020-4-1', '2020-7-1', '2020-10-1'],
         'place1':[39, 17, 20, 88],
         'place2':[55, 88, 19, 42]}

data2 = {'date':['2020-01-01', '2020-04-01', '2020-07-01', '2020-10-01',
                 '2021-01-01', '2021-04-01', '2021-07-01', '2021-10-01'],
         'place1':[1, 4, 7, 2, 5, 8, 11, 13],
         'place2':[2, 5, 8, 6, 6, 9, 13, 15]}

data3 = {'date':['2021-1-1', '2021-4-1', '2021-7-1', '2021-10-1']*2,
         'place':['place1']*4 + ['place2']*4,
         'value1':[33, 43, 53, 34, 35, 46, 47, 48]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

df1.shape
df2.shape
df3.shape

df1["date"] = pd.to_datetime(df1["date"])
df2["date"] = pd.to_datetime(df2["date"])
df3["date"] = pd.to_datetime(df3["date"])
df3

df1_merge = df1.merge(df2, how = "left", on = "date", indicator = True)
df1_merge    

df1_w2l = pd.melt(df1_merge, id_vars = "date", value_vars = ["place1_x", "place2_x", "place1_y", "place2_y"], var_name = "place", value_name = "value1")
df1_w2l

df1_w2l_merge = df1_w2l.merge(df3, how = "outer", on = ["date", "place"], indicator = True)
df1_w2l_merge["place"] = df1_w2l_merge.loc[:, "place"].str.replace("place", "")

assert(len(df1) + len(df2) + len(df3) < 24), "seems to be right!"

df1_w2l_merge


df1_w2l_concat = pd.concat([df1_w2l, df3])
df1_w2l_concat["place"] = df1_w2l_concat.loc[:, "place"].str.replace("place", "")
df1_w2l_concat


# 2. You had to do some merging in part 1. If you did not already, go back and use
# some assert statements to verify that the dataframes did what you expected.




#3. Is the dataframe from part 1 in long or wide format? Write code to convert it
#into the other.

#already did this in the above step. but trying something new in this section

try_again = df1.merge(df2, how = "left", on = "date", indicator = True)
try_again

try_again2 = try_again.merge(df3, how = "outer", on = "date", indicator = True)
try_again2
