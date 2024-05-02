#Daniel Avila

import pandas as pd
import numpy as np 
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'
df = pd.read_csv(url_to_csv)


# 1) Explore the data & produce some basic summary stats  
df
df[["price","carat", "depth", "x", "y"]].mean()
cut_groupby = df.groupby(["clarity"])
mean = cut_groupby[["price","carat", "depth", "table", "x", "y", "z"]].mean()
mean


# 2) Run a regression of price (y) on carat (x), including an 
#    intercept term.  Report the estimates of the intercept & slope 
#    coefficients using each of the following methods:
#        a) NumPy
#        b) statsmodels (smf) 
#        c) statsmodels (sm)
#        d) scikit-learn (LinearRegression)  
#           Hint:  scikit-learn only works with array-like objects.    
#    Confirm that all four methods produce the same estimates.

price = np.array(df["price"])
carat = np.array(df["carat"])

# Numpy
m, b = np.polyfit(carat, price, deg = 1)
np_line = np.poly1d((m, b))
fig, ax = plt.subplots()
ax.plot(carat, price, 'ro')
ax.plot(carat, np_line(carat), 'k--')
plt.show()
print(np_line.coefficients)

# smf
df["intercept"] = 1
model = smf.ols("price ~ carat", data = df)
result = model.fit()
result.summary()

print(result.params)

# sm
model_sm = sm.OLS(endog = df["price"], exog = df[["carat", "intercept"]])
result_sm = model_sm.fit()
result_sm.summary()

print(result_sm.params)

#scikit learn
model_sci = LinearRegression(fit_intercept = True)
carat2d = np.array(carat.reshape(-1, 1))

results_sci = model_sci.fit(carat2d, price)
print(model_sci.coef_, model_sci.intercept_)

#all four methods are producing the same slope and intercept

# 3) Run a regression of price (y) on carat, the natual logarithm of depth  
#    (log(depth)), and a quadratic polynomial of table (i.e., include table & 
#    table**2 as regressors).  Estimate the model parameters using any Python
#    method you choose, and display the estimates.  

df["log_depth"] = np.log(df["depth"])
logdepth = pd.DataFrame(df["log_depth"])
logdepth = logdepth.T

df["table_sq"] = np.square(df["table"])
table_sq = pd.DataFrame(df["table_sq"])
table_sq = table_sq.T

model_big = sm.OLS(endog = price, exog = df[["log_depth", "table_sq", "table"]])
results_model_big = model_big.fit()
print(results_model_big.summary())


# 4) Run a regression of price (y) on carat and cut.  Estimate the model 
#    parameters using any Python method you choose, and display the estimates.  

cut = np.array(df["cut"])
cut
# cut_model = sm.OLS(endog = price, exog = cut)
# cant run this model because the values in df["cut"] are strings so this regression wouldnt make any sense.

# 5) Run a regression of price (y) on whatever predictors (and functions of 
#    those predictors you want).  Try to find the specification with the best
#    fit (as measured by the largest R-squared).  Note that this type of data
#    mining is econometric blasphemy, but is the foundation of machine
#    learning.  Fit the model using any Python method you choose, and display 
#    only the R-squared from each model.  We'll see who can come up with the 
#    best fit by the end of lab.  

rbest = sm.OLS(endog = price, exog = df[["table", "table_sq", "depth", "log_depth", "z", "y", "x", "carat"]])
rbest.fit().summary()
