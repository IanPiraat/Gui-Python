from tkinter import *
import random
window = Tk()
window.geometry("750x500")
window.title("rock paper scissors")
window.configure(bg="white")
computerscore = 0
playerscore = 0

OptionList = ["rock","paper","scissors"]





RockText_label = Label(window,text="Rock Paper Scissors",fg="black",bg="white",font=("arial",45,"bold"))
OptionText_label = Label(window,text="Your Options",fg="black",bg="white",font=("arial",15,"bold"))
ScoreText_label = Label(window,text="Score:",fg="black",bg="white",font=("arial",15,"bold"))
WinText_label = Label(window,text=f"{} Won!",fg="black",bg="white",font=("arial",15,"bold"))
SelectedBot_label = Label(window,text=f"Computer selected:{}   computer score:{}",fg="black",bg="white",font=("arial",15,"bold"))
SelectedPlayer_label = Label(window,text=f"you selected:{}     player score:{}",fg="black",bg="white",font=("arial",15,"bold"))


RockButton_button = Button(window,text="Rock",fg="black",bg="white",font=("arial",20,"bold"))
PaperButton_button = Button(window,text="Paper",fg="black",bg="white",font=("arial",20,"bold"))
ScissorsButton_button = Button(window,text="Scissors",fg="black",bg="white",font=("arial",20,"bold"))

WinScenario = None
def Gameplay(UserChoice) :
    print("")
    ComputerChoice = random.choice(OptionList)
    
    SelectedPlayer_label.config(text=f"Player Selected{UserChoice}")

    SelectedBot_label.config(text=f"Computer selected{ComputerChoice}")







    # computer
    if ComputerChoice == UserChoice :
        WinScenario = "tie"

    if ComputerChoice == "paper" and UserChoice == "rock" :
        WinScenario = "computer"

    if ComputerChoice == "rock" and UserChoice == "scissors" :
        WinScenario = "computer"

    if ComputerChoice == "scissors" and UserChoice == "paper" :
        WinScenario == "computer"             
    #User
    if UserChoice == ComputerChoice :
        WinScenario = "tie"

    if UserChoice == "paper" and ComputerChoice == "rock" :
        WinScenario = "user"

    if UserChoice == "rock" and ComputerChoice == "scissors" :
        WinScenario = "User"

    if UserChoice == "scissors" and UserChoice == "paper" :
        WinScenario = "User"
                



        





RockText_label.place(x=75,y=50)
OptionText_label.place(x=90,y=200)
ScoreText_label.place(x=90,y=350)

RockButton_button.place(x=100,y=240)
PaperButton_button.place(x=225,y=240)
ScissorsButton_button.place(x=350,y=240)







window.mainloop()