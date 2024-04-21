#NAMES

import pandas as pd

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'

df = pd.read_csv(url_to_csv)

df

# 1) Create a groupby object using "clarity" and "color" as the keys

groupby_clarity_color = df.groupby(by = ["clarity", "color"])

# 2) Display the describe() output JUST for group color=E, clarity=SI2
groupby_clarity_color.get_group(("SI2", "E")).round(2)

#sanity check
df.loc[(df["clarity"] == "SI2") & (df["color"] == "E")]



# 3) Display the max value for price in each group
groupby_clarity_color["price"].max()


# 4) Display the min value for price in each group
groupby_clarity_color["price"].min()


# 5) Write four different functions:
#    - one that works with map on the values in a column

def triple_it(dataframe, colname):
    for colname in dataframe:
        column = dataframe[colname]
        new_column = column.map(lambda x: x*3)
        dataframe["new_column"] = new_column
        return dataframe

triple_it(df, "price")


#    - one that works with apply on the values in a row

def multiply_row(dataframe, row, choose_number):
    for cell in dataframe.iloc[row]:
        if type(row[cell]) == str:
            continue
        else:
            new_row = dataframe.apply(lambda row : dataframe.iloc[cell] * choose_number, axis = 0)
        dataframe[len(dataframe) + 1] = new_row
    return dataframe.tail()

multiply_row(df, 3, 1)
    
    
#    - one that works with apply on the values in a column

def multiply_column(dataframe, column, choose_number):
    for cell in dataframe.loc[[column]]:
        if type(column(cell)) == str:
            continue
        else:
            new_column = dataframe.apply(lambda column : dataframe.iloc[cell] * choose_number, axis = 1)
        dataframe[len(dataframe) + 1] = new_column
        return(dataframe.tail())

multiply_column(df, "price", 8)
        
        
#    - one that works with apply on a groupby object

def gruppy(grouped_df, column):
    new_df = grouped_df.apply(lambda row: row[column] * 15)
    return new_df

gruppy(groupby_clarity_color, "price")

# 6) Display only the maximum price for each clarity.
groupby_clarity = df.groupby(by = ["clarity"])
groupby_clarity["price"].max()



# 7) Stretch goal! Which clarity of diamond has the diamond that is
#    the largest outlier in size (carats) from the mean for that group?
