# create an application length in inches as input from the user and return the value of that length in centimeters using the Python Tkinter library.\
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Length Converter")
root.geometry("400x300")
label = Label(root, text="Enter length in inches:")
label.pack(pady=10)
entry = Entry(root)
entry.pack(pady=20)
def convert():
  try :
    centimetres = float(entry.get()) * 2.54
    messagebox.showinfo("Result", f"Length in centimeters: {centimetres} cm")
  except ValueError :
    messagebox.showerror("Invalid input", "Please enter a valid number.")

submitBTN = Button(master = root , bg = 'lightgreen' , fg= 'black' , text = 'Convert length' , command = convert )
submitBTN.pack(pady=20)
root.mainloop()
