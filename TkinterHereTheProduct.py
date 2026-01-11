from tkinter import *
# plan
# step one get elements button label  entry
# background color blue

root = Tk()
root.geometry('500x400')
titleLbl = Label(text = 'Product of Two Numbers' , bg = 'blue' , fg = 'white' , font = ('Arial' , 20))
titleLbl.pack()
FirstNumberLabel = Label(text = 'First Number' , bg = 'white')
FirstNumberLabel.pack()
FirstNumber = Entry()
FirstNumber.pack()
SecondNumberLabel = Label(text = 'Second Number' , bg = 'yellow')
SecondNumberLabel.pack()
SecondNum = Entry()
SecondNum.pack()
def product():
    num1 = float(FirstNumber.get())
    num2 = float(SecondNum.get())
    product = num1 * num2
    resultLbl = Label(text = f'The Product is {product}' , bg = 'green' , fg = 'white' , font = ('Arial' , 16))
    resultLbl.pack()
productBtn = Button(text = 'Get Product' , bg = 'red' , fg = 'white' , command = product)
productBtn.pack()
root.mainloop()


