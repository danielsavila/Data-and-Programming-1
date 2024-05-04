# Daniel Avila

import pandas as pd
import pandas_datareader.data as web
import statsmodels.api as sm
import matplotlib.pyplot as plt

series = {'CPMNACSCAB1GQDE':'GDPGermany',
          'LRUNTTTTDEQ156S':'EMPGermany',
          'CPMNACSCAB1GQPL':'GDPPoland',
          'LRUNTTTTPLQ156S':'EMPPoland'}
df = web.DataReader(list(series.keys()), 'fred', start='1995-01-01', end='2019-10-01')

df = df.rename(series, axis=1)

df

# 1)
# This data is from lecture 18.  Explore it using plots and summary
# statistics. What is wrong with the employment data from Poland? 
# Then, apply an HP filter from the statsmodels library, and filter 
# all four series.  Plot the cycles, trends, and original values to
# see what is happening when you filter.

df = df.reset_index()
df = df.dropna(how = "any")
gdp_germany = df["GDPGermany"]
emp_germany = df["EMPGermany"]
gdp_poland = df["GDPPoland"]
emp_poland = df["EMPPoland"]
date = df["DATE"]

# GDP Germany plot
fig, ax = plt.subplots()
ax.plot(date, gdp_germany)
plt.show()

# GDP Poland plot
fig, ax = plt.subplots()
ax.plot(date, gdp_poland)
plt.show()

# employment Germany plot
fig, ax = plt.subplots()
ax.plot(date, emp_germany)
plt.show()

# employment Poland plot
fig, ax = plt.subplots()
ax.plot(date, emp_poland)
plt.show()


# the employment data from poland has either missing data or a jump at the ~1998 - 2000 date
#implementing the HP filter

#GDP Germany cycle and trend
ggdp_cycle, ggdp_trend = sm.tsa.filters.hpfilter(gdp_germany, lamb = 1600)

plt.plot(ggdp_cycle)
plt.show()
plt.plot(ggdp_trend)
plt.show()

#GDP Poland cycle and trend
pgdp_cycle, pgdp_trend = sm.tsa.filters.hpfilter(gdp_poland, lamb = 1600)

plt.plot(pgdp_cycle)
plt.show()
plt.plot(pgdp_trend)
plt.show()

# employment Germany cycle and trend
gemp_cycle, gemp_trend = sm.tsa.filters.hpfilter(emp_germany, lamb = 1600)

plt.plot(gemp_cycle)
plt.show()
plt.plot(gemp_trend)
plt.show()


#employment Poland cycle and trend
pemp_cycle, pemp_trend = sm.tsa.filters.hpfilter(emp_poland, lamb = 1600)

plt.plot(pemp_cycle)
plt.show()
plt.plot(pemp_trend)
plt.show()

# 2)
# The code from the lecture includes a function that implements the
# Hamilton filter, though we did not go over the code in detail.
# Copy that function over and try to understand most of what it is
# doing (you may have to test it in pieces) and then apply it to
# this data. Modify your plots from question 1 to compare the results
# of the Hamilton and HP filters to the unfiltered values.

import numpy as np
def hamilton_filter(data, h=8, p=4):
    def _shift(orig_series, n):
        #implements efficient (positive) shifting for non-Series dtypes
        new_series = np.empty_like(orig_series)
        new_series[:n] = np.NaN
        new_series[n:] = orig_series[:-n]
        return new_series

    new_cols = [_shift(data, s) for s in range(h, h+p)]

    exog = sm.add_constant(np.array(new_cols).transpose())
    model = sm.GLM(endog=data, exog=exog, missing='drop')
    res = model.fit()

    trend = res.fittedvalues
    rand = data - _shift(data, h)
    cycle = res.resid_pearson
    return cycle, trend, rand

g_cycle, g_trend, _ = hamilton_filter(gdp_germany)
p_cycle, p_trend, _ = hamilton_filter(gdp_poland)

fig, axs = plt.subplots(2, 1, figsize=(12,6))
axs[0].plot(g_cycle.index, g_cycle, 'b-', label='Germany')
axs[0].plot(g_cycle.index, p_cycle, 'r-', label='Poland')
axs[1].plot(g_trend.index, g_trend, 'b-')
axs[1].plot(g_trend.index, p_trend, 'r-')
axs[0].set_ylabel('Cycle')
axs[1].set_ylabel('Trend')
fig.legend(loc='upper center', ncols=2)
plt.show()

g_cycle.name = 'Germany_hamilton'
p_cycle.name = 'Poland_hamilton'

model = sm.OLS(g_cycle, sm.add_constant(p_cycle))
result = model.fit()
result.summary()



