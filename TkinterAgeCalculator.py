from tkinter import *
from datetime import date as dt
window = Tk()
window.title("Age Calculator")
window.geometry("400x400")
#Widgets
Titlelabel = Label(window, text="Age Calculator", font=("Arial", 24) , bg ="lightblue")
Titlelabel.pack(pady=20)
label1 = Label(window, text="Enter your birth year:")
label1.pack(pady=10)
birthYearEntry = Entry(window)
birthYearEntry.pack(pady=5)
birthMonthLabel = Label(window, text="Enter your birth month (1-12):")
birthMonthLabel.pack(pady=10)
birthDateEntry = Entry(window)
birthDateEntry.pack(pady=5)
def submitResult():
    currentYEAR = dt.today().year
    currentMONTH = dt.today().month
    birthYEAR = int(birthYearEntry.get())
    birthMONTH = int(birthDateEntry.get())
    age = currentYEAR - birthYEAR
    if currentMONTH < birthMONTH:
        age -= 1
    resultLabel = Label(window, text=f"Your age is: {age} years old")
    resultLabel.pack(pady=20)
    
BDbutton = Button(window, text="submit" , command = submitResult)
BDbutton.pack(pady=20)

window.mainloop()
