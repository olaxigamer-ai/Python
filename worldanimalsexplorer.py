import matplotlib.pyplot as plt
import seaborn as sns

df= sns.load_dataset('penguins')
df=df.dropna()
print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()

print("species",df['species'].unique())
print("island",df['island'].unique())

#histogram
sns.histplot(data=df,x='body_mass_g',bins=20,color='steelblue')
plt.title("Distribution of penguin body mass:")
plt.xlabel("Body Mass in grams")
plt.ylabel("Count")
plt.show()

#kde plot (Curve)
sns.kdeplot(data=df,x='flipper_length_mm',hue='species',fill=True)
plt.title("Flipper Length shape by species")
plt.xlabel("flipper length in mm")
plt.show()

sns.histplot(data=df,x='flipper_length_mm',kde=True,color='coral')
plt.title("Flipper Length shape by species using histogram by making kde true:")
plt.xlabel("flipper length in mm")
plt.ylabel("count")
plt.show()

#scatter plot
sns.scatterplot(data=df,x='flipper_length_mm',y='body_mass_g',hue='species')
plt.title("Flipper Length vs body mass by species")
plt.xlabel("flipper length in mm")
plt.ylabel("body mass in grams")
plt.show()

#heat map
corr=df.corr(numeric_only=True)
print("Correlation Table: ")
print(corr)
print()
sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap - penguin measurement:")
plt.show()