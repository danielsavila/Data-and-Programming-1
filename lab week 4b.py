#NAMES

#For the following questions, load the iris.csv dataset into a Pandas
#DataFrame. Make sure you set up an absolute path as described in 
#lecture, and if you're working with others, you should each update
#it to work on your computer.

import pandas as pd
import os

PATH = r"C:\Users\AVILA\OneDrive\Documents\GitHub\Data-and-Programming-1"
file_path = os.path.join(PATH, "iris.csv")

iris = pd.get_csv("iris.csv")

#1. Explore the data.  How many categories of flowers are there? 

iris.shape
iris.describe()
iris["species"].unique()
## there are 3 different types of flowers in the datset, setosa, versicolor, and virginica.

# What are the mean and median values, and the standard deviation?

iris["sepal_length"].mean()
iris["sepal_width"].mean()
iris["petal_length"].mean()
iris["petal_width"].mean()

iris["sepal_length"].median()
iris["sepal_width"].median()
iris["petal_length"].median()
iris["petal_width"].median()

iris["sepal_length"].std()
iris["sepal_width"].std()
iris["petal_length"].std()
iris["petal_width"].std()


# How would you find the mean values per type of flower?  

iris[iris["species"] == "setosa"].mean()
iris[iris["species"] == "versicolor"].mean()
iris[iris["species"] == "veriginica"].mean()

# Right now you can implement this with subsetting; next week we will cover how to
#   do this using groupby.


#2. Locate the max value across all four measures.  Use loc to display
#   just the rows that contain those values.
max_sepal_length = iris["sepal_length"].max()
max_sepal_width = iris["sepal_width"].max()
max_petal_length = iris["petal_length"].max()
max_petal_width = iris["petal_width"].max()

iris.loc[iris["sepal_length"] == max_sepal_length]
iris.loc[iris["sepal_width"] == max_sepal_width]
iris.loc[iris["petal_length"] == max_petal_length]
iris.loc[iris["petal_width"] == max_petal_width]
                       

#3. How many of observations for each species of iris is in the data?
iris.loc[iris["species"] == "virginica"].shape
iris.loc[iris["species"] == "setosa"].shape
iris.loc[iris["species"] == "versicolor"].shape

#50 of each species

#4. Using one line of code, divide each value by the mean for that measure,
#   and assign the result to four new columns.  How is this different from 
#   a zscore?  How would you make this a zscore instead?  What's the problem
#   with doing this without accounting for the values in the species column?

iris.apply(lambda iris[i]: (iris[i] / iris[:,i]i.mean())

#5. Create a new column named "petal_area" which is equal to the length
#   times the width.  Note that this isn't really the area of the petal, since
#   petals presumably aren't rectangles.


#6. Subset the data to a new variable that is a dataframe with only virginica 
#   flowers.  Now add a new column to this subset that is equal to 1 if the 
#   sepal_length is greater than the mean sepal_length, else 0.  Did you get a
#   SettingWithCopyWarning message?  Modify your copying to do away with the 
#   warning.  Hint: You can create this with apply, or with map if you also
#   create a global variable holding the mean.

