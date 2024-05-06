#Daniel Avila

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')
sns.scatterplot(x='sepal_length', y='petal_length',
                data=df, hue='species')
plt.show()

# Recreate this plot in Matplotlib, without using Seaborn!
# Then try adding some of your own customizations to the 
# plot using MatPlotLib methods

df.head()

x = df["sepal_length"]
y = df["petal_length"]

fig, ax = plt.subplots()

flower_groups = df.groupby("species")
colors = {"setosa":"blue", "versicolor":"orange", "virginica":"green"}

for key, group in flower_groups:
    group.plot(x = "sepal_length", y = "petal_length",
               ax = ax,
               kind = "scatter",
               color = colors[key],
               label = key)

ax.legend().set_title("species")

plt.show()
