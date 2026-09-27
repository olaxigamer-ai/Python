import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

print(sns.get_dataset_names())
df=sns.load_dataset("penguins")
print(df.head())
print(df.tail())
print(df.isnull().sum())
print(df.describe())
print(df.dtypes)
print(df.info())
print(df.corr(numeric_only=True))

#heat map
sns.heatmap(df.corr(numeric_only=True),annot=True)
plt.title("Heatmap of numeric values and collumns")
plt.show()

#histogram
df.select_dtypes(include=[np.number]).hist(figsize=(12,8))
plt.show()

#boxplot
df.select_dtypes(include=[np.number]).plot(kind="box",figsize=(8,12))
plt.show()

#countplots
sns.countplot(data=df,x='sex')
plt.show()

sns.countplot(data=df,x='island')
plt.show()

sns.countplot(data=df,x='species')
plt.show()

sns.countplot(data=df,x='sex',hue='species')
plt.show()

sns.countplot(data=df,x='island',hue='species')
plt.show()

sns.countplot(data=df,x='island',hue='sex')
plt.show()

#pairplot
sns.pairplot(data=df,hue='species')
plt.show()