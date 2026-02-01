from tkinter import *
def passwordCheck(password) :
    if len(password)  < 8 and len(password) > 6:
        return "Medium"   
    elif len(password)  > 12:
        return "Very Strong" 
    elif len(password) >= 5 :
        return "Weak"
    elif len(password) > 8 :
        return "Strong"
    else :
        return "Very Weak"
Window = Tk()
Window.title("Password Strength Checker")
Window.geometry("400x400")
label = Label(Window , text = "Password strength checker" , font = ('Arial' , 15))
label.pack(pady = 30 , padx = 30)
entry = Entry(Window , width = 30)
entry.pack(pady = 0 , padx = 10)
result = Label(Window , text = "  " , font = ('Arial' , 15))
result.pack(pady = 0 , padx = 10)
checkButton = Button(Window , text = "Check Password" , command =lambda: check() , bg = '#0000F0' , fg = '#FFFFFF' , width = 25)
checkButton.pack(pady = 20 , padx = 10)
def check() :
    color = 'black'
    if strength == "Very Weak" or strength == "Weak" :
        color = 'red'
    elif strength == "Medium" :
        color = 'orange'
    else :
        color = 'green'
    pwd = entry.get()
    strength = passwordCheck(pwd)
    result.config(text = f"Password Strength : {strength}"  , fg = color)
Window.mainloop()