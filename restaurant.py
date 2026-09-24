import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset('tips')
print(df.head())
print(df.info())
df=df.dropna()

#barplot
sns.barplot(x='day',y='total_bill',hue='sex',data=df)
plt.title("Average Total bill per day. By gender:")
plt.xlabel("Day")
plt.ylabel("Average Bill")
plt.show()

#countplot
sns.countplot(x='day',hue='sex',data=df)
plt.title("Number of dinners per day by gender:")
plt.xlabel("Day")
plt.ylabel("Count")
plt.show()

#boxplot,stripplot,swarmplot
sns.boxplot(x='day',y='total_bill',data=df)
plt.title("Spread of total bill per day:")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

sns.stripplot(x='day',y='total_bill',data=df,jitter=True)
plt.title("Every bill amount per day using strip plot:")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

sns.swarmplot(x='day',y='total_bill',data=df)
plt.title("Every bill amount per day using swarm plot")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

#jointplot

sns.jointplot(x='total_bill',y='tip',data=df)
plt.suptitle("Total bill vs Tip",y=1.02)
plt.show()

#kde plot
sns.jointplot(x='total_bill',y='tip',data=df,type='kde')
plt.suptitle("Total bill vs Tip - KDE joint plot",y=1.02)
plt.show()

#pairplot

g=sns.pairplot(df[['total_bill','tip','size']])
g.fig.plt.suptitle("pair plot - bill tip and party size",y=1.02)
g.fig.subplots_adjust(top=0.95)
plt.show()

#pointplot
sns.pointplot(x='day',y='total_bill',hue='sex',data=df)
plt.title("average bill per day by gender : ")
plt.xlabel("day")
plt.ylabel("average bill")
plt.show()

#implot
sns.Implot(x='total_bill',y='tip',data=df)
plt.title("Total Bill vs tip")
plt.show()