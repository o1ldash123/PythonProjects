import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

csvFile = pd.read_csv('Company Sales Data.csv')
Profit = np.array(csvFile['total_profit'])
months =np.array(csvFile['month_number'])
faceCream = np.array(csvFile['facecream'])
faceWash = np.array(csvFile['facewash'])
toothpaste = np.array(csvFile['toothpaste'])
bathingSoap = np.array(csvFile['bathingsoap'])
shampoo = np.array(csvFile['shampoo'])
moisturizer = np.array(csvFile['moisturizer'])

def lineplot() :
 print('This is the line plot of profit data')
 plt.plot(months,Profit, linestyle = 'dotted' , marker = 'o' , color = 'red' , linewidth = 3 , markerfacecolor = 'black')
 plt.xlabel('Months')
 plt.ylabel('Profit ($)')
 plt.title('Monthly profit ')
 plt.show()
lineplot()
def multiLinePlot() :
 print('This is the multi line plot of sales data of different products')
 plt.plot(  faceCream , color = 'red' , label = 'faceCream'  , marker = 'o' , linewidth = 3)
 plt.plot(  faceWash , color = 'blue' , label = 'faceWash ' , marker = 'o' , linewidth = 3 )
 plt.plot( toothpaste , color = 'green' , label = 'toothpaste' , marker = 'o' , linewidth = 3)
 plt.plot(bathingSoap , color = 'cyan' , label = 'bathingSoap' , marker = 'o' , linewidth = 3)
 plt.plot(shampoo , color = 'magenta' , label = 'shampoo', marker = 'o' , linewidth = 3)
 plt.plot(moisturizer , color = 'yellow' , label = 'moisturizer', marker = 'o' , linewidth = 3)
 plt.xlabel('Months')
 plt.ylabel('Sales units in number')
 plt.title('Sales data')
 plt.legend()
 plt.show()
multiLinePlot()
def barPlot() :
 print('This is the bar graph to compare the results of face wash and face cream')
 plt.bar(faceWash ,months , color = 'cyan' , label = 'Face wash' , linewidth = 200)
 plt.bar(faceCream ,months , color = 'magenta' , label = 'FaceCream'  , linewidth = 200)
 plt.xlabel('Months')
 plt.ylabel('Sales units in number')
 plt.legend()
 plt.title('Face wash vs Face cream')
 plt.show()
barPlot()
 
