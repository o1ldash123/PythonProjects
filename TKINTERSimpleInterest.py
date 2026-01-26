#declarations
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Simpler interest calculator')

#gui
root.geometry('400x400')
TopicLabel = Label( root , fg = 'white', text = 'Simple Interest Calculator' , bg ='black')
explain = Label(root , text = 'Enter the values below to calculate simple interest')

TopicLabel.pack(pady = 10 , padx = 5)
explain.pack(pady = 5 , padx = 5)
principalLABEL = Label(root , text = 'Principal amount')
principalLABEL.pack(pady = 5 , padx = 5)
principalEntry = Entry(root)
principalEntry.pack(pady = 5 , padx = 5)
rateLABEL = Label(root , text = 'Rate of interest')
rateLABEL.pack(pady = 5 , padx = 5)
rateEntry = Entry(root)
rateEntry.pack(pady = 5 , padx = 5)
timeLABEL = Label(root , text = 'Time in years')
timeLABEL.pack(pady = 5 , padx = 5)
timeEntry = Entry(root)
timeEntry.pack(pady = 5 , padx = 5)
calculateButton = Button(root , text = 'Calculate Simple Interest' , command = lambda : calculateSIMPLEINTEREST() ,  bg = 'blue' , fg = 'white')
calculateButton.pack(pady = 20 , padx = 5)
def calculateSIMPLEINTEREST():
    try :
        P = float(principalEntry.get())
        R = float(rateEntry.get())
        T = float(timeEntry.get())
        SI = (P * R * T) / 100
        messagebox.showinfo('Simple Interest' , f'The simple interest is {SI}$')
    except ValueError:
        messagebox.showerror('Input error' , 'Please enter valid numeric values')
root.mainloop()


