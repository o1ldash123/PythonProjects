import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
IrisDataSet = pd.read_csv('Iris Dataset.csv')

sns.barplot(x='Species', y='SepalLengthCm', data=IrisDataSet)
print('This is a bar plot showing the average sepal length for each species of iris')
plt.show()
sns.countplot(x='Species', data=IrisDataSet)
print('This is a count plot showing the number of samples for each species of iris')
plt.show()
sns.boxplot(x='Species', y='SepalWidthCm', data=IrisDataSet)
print('This is a box plot showing the distribution of sepal width for each species of iris')
plt.show()
sns.swarmplot(x = 'Species' , y = 'SepalWidthCm' , data = IrisDataSet)
print('This is a swarm plot showing the distribution of sepal width for each species of iris')
plt.show()

sns.displot(IrisDataSet['SepalWidthCm'], kde = True)
print('This is a distribution plot showing the distribution of sepal width across all iris samples')
plt.show()
sns.jointplot(x = 'SepalWidthCm' , data = IrisDataSet )
print('This is a joint plot showing the relationship between sepal width and sepal length across all iris samples')
plt.show()
sns.pairplot(IrisDataSet, hue = 'Species')
print('This is a pair plot showing the relationships between all pairs of features for each species of iris')
plt.show()


