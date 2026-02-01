from tkinter import *
import random
import time
def calculateWinner(you , computer ) :
    message = ' '
    color = ' '
    
    if you == computer :
        message =  'Its a Tie both chose ' + you
    
    if you == "rock" and computer == "scissors" :
        color = 'green'
        message =  'rock beats scissors \n YOU WIN!'
    if you == "scissors" and computer == "paper" :
        color = 'green'
        message =  'scissors beats paper \n YOU WIN!'
    if you == "paper" and computer == "rock" :
        color = 'green'
        message = "paper beats rock \n YOU WIN!"
    
    if computer == "rock" and you == "scissors" :
        color = 'red'
        message =  "rock  beats scissors\n YOU LOSE!"
    if computer == "scissors" and you == "paper" :
        color = 'red'
        message = "scissors beats paper \n YOU LOSE!"
    if computer == "paper" and you == "rock" :
        color = 'red'
        message =  "paper beats rock \n YOU LOSE!"
    top = Toplevel(MAIN)
    top.title("Result")
    top.geometry("300x200")
    result = Label(master =top , text = message , font = ('Arial' , 15) )
    result.pack(pady = 50 , padx = 10)
    ok = Button(master = top , text = "Ok" , command = top.destroy , bg = '#0000F0' , fg = '#FFFFFF' , width = 10)

    ok.pack(pady = 10 , padx = 10)

    

   
def pick(TYPE) :
    return TYPE
def computerPick() :
    options = ['rock' , 'paper' , 'scissors']
    return random.choice(options)
MAIN = Tk()
MAIN.title("Rock Paper Scissors")
MAIN.geometry("400x400")

Topic = Label(MAIN , text = "Rock Paper Scissors" , font = ('Arial' , 20))
explain = Label(MAIN , text = "Choose your option and the computer will compete against you :" , font = ('Arial' , 15))
rock = Button(MAIN , text = 'Rock' , command = lambda : calculateWinner(pick('rock') , computerPick()) , bg = '#0000F0', width= 10 , fg = '#FFFFFF')
paper = Button(MAIN , text = 'Paper' , command = lambda : calculateWinner(pick('paper'), computerPick()), bg = '#00F000' , width= 10 , fg = '#FFFFFF')
scissors = Button(MAIN , text = 'Scissors' , command =  lambda : calculateWinner(pick('scissors') , computerPick() ) , bg = '#F00000' , width = 10 , fg = '#FFFFFF')

Topic.pack(pady = 30 , padx = 10)
rock.pack(padx = 10 , pady = 10)
paper.pack(padx=10 , pady = 10)
scissors.pack(padx = 10 , pady = 10)


MAIN.mainloop()