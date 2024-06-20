import seaborn as sns
from matplotlib import pyplot as plt
sns.set_style("darkgrid")
flowers_df=sns.load_dataset("iris")
print(flowers_df)
print(flowers_df.species.unique())
sns.scatterplot(x=flowers_df.petal_length,y=flowers_df.petal_width,hue=flowers_df.species,s=20)
plt.show()