import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CSV = pd.read_csv('IMDB Dataset.csv')
print("The head tail , info and null values of the dataset are shown below along with rows 41 to 75:")
print(CSV.head(3))
print(CSV.tail(3))
print(CSV.info())
print(CSV.isnull())
print(CSV.iloc[41:76])
#HIGHEST RATED MOVIE
print('information about the highest rated movie is shown below:')
print(CSV.where(CSV['No_of_Votes'] == CSV['No_of_Votes'].max()).info())
print(CSV.info())

print()
print('The average IMDB rating for movies in the dataset is shown below:')
sns.boxplot(x = 'IMDB_Rating' , y = 'Runtime' , data = CSV)
plt.show()
print('This is a box plot showing the distribution of runtime for each IMDB rating across all movies in the dataset')
plt.plot(CSV['Runtime'] , CSV['IMDB_Rating'] , 'o')
plt.show()
print('This is a scatter plot showing the relationship between runtime and IMDB rating across all movies in the dataset')
sns.displot(x = 'IMDB_Rating', y = 'Runtime', data = CSV)
plt.show()
print('This is a distribution plot showing the relationship between IMDB rating and runtime across all movies in the dataset')
print('The count of movies for each rating is shown below(i didnt put the specific movies because they were too many):')
sns.countplot(x = 'IMDB_Rating', data = CSV)
plt.show()




