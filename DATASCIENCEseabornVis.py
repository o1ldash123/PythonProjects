import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
csvFile = pd.read_csv('Tips Dataset.csv')
print('This is the seaborn visualization of the tips dataset')
print(csvFile.head())
sb.displot(np.array(csvFile['total_bill']), kde = True  , color = 'purple')
sb.jointplot(x = 'total_bill' , y = 'tip' , data = csvFile , color = 'cyan' , hue = 'time')
sb.pairplot(csvFile , hue = 'gender' , palette = 'Set2')
plt.show()

