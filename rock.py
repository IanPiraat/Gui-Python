from tkinter import *
import random
import pygame
pygame.mixer.init()

window = Tk()
window.geometry("750x500")
window.title("rock paper scissors")
window.configure(bg="white")
computerscore = 0
playerscore = 0
OptionList = ["rock","paper","scissors"]

ComputerChoice = None
UserChoice = None
WinScenario = None

select=pygame.mixer.Sound("Sounds/select.wav")
lose=pygame.mixer.Sound("Sounds/lose.wav")
win=pygame.mixer.Sound("Sounds/correct.wav")


RockText_label = Label(window,text="Rock Paper Scissors",fg="black",bg="white",font=("arial",45,"bold"))
OptionText_label = Label(window,text="Your Options",fg="black",bg="white",font=("arial",15,"bold"))
ScoreText_label = Label(window,text="Score:",fg="black",bg="white",font=("arial",15,"bold"))
SelectedBot_label = Label(window,text=f"Computer selected:{ComputerChoice}   computer score:{computerscore}",fg="black",bg="white",font=("arial",15,"bold"))
SelectedPlayer_label = Label(window,text=f"you selected:{UserChoice}     player score:{playerscore}",fg="black",bg="white",font=("arial",15,"bold"))



WinText_label = Label(window,text=f"press a button to start.",fg="black",bg="white",font=("arial",15,"bold"))

def Gameplay(UserChoice) :
    global computerscore,playerscore,WinScenario
    print("")
    select.play()
    ComputerChoice = random.choice(OptionList)
    
    






    ComputerChoice = random.choice(OptionList)
    print(ComputerChoice)
    # computer
    if ComputerChoice == UserChoice :
        WinScenario = "Tie"


    if ComputerChoice == "paper" and UserChoice == "rock" :
        WinScenario = "Computer"
        computerscore += 1
        lose.play()

    if ComputerChoice == "rock" and UserChoice == "scissors" :
        WinScenario = "Computer"
        computerscore += 1
        lose.play()

    if ComputerChoice == "scissors" and UserChoice == "paper" :
        WinScenario == "Computer"  
        computerscore += 1
        lose.play()           
    #User
    if UserChoice == ComputerChoice :
        WinScenario = "Tie"
        

    if UserChoice == "paper" and ComputerChoice == "rock" :
        WinScenario = "User"
        playerscore += 1
        win.play()

    if UserChoice == "rock" and ComputerChoice == "scissors" :
        WinScenario = "User"
        playerscore += 1
        win.play()

    if UserChoice == "scissors" and UserChoice == "paper" :
        WinScenario = "User"
        playerscore += 1
        win.play()

    
               
    
    WinText_label.config(text=f"{WinScenario} Won!")    
    SelectedPlayer_label.config(text=f"Player Selected {UserChoice}, player score ={playerscore}")
    

    SelectedBot_label.config(text=f"Computer selected {ComputerChoice}, computer score ={computerscore}")



RockButton_button = Button(window,text="Rock",fg="black",bg="white",font=("arial",20,"bold"),command = lambda:Gameplay("rock"))
PaperButton_button = Button(window,text="Paper",fg="black",bg="white",font=("arial",20,"bold"),command = lambda:Gameplay("paper"))
ScissorsButton_button = Button(window,text="Scissors",fg="black",bg="white",font=("arial",20,"bold"),command = lambda:Gameplay("scissors"))
ExitButton_button = Button(window,text="Exit?",fg="black",bg="white",font=("arial",20,"bold"),command=exit)


      


ExitButton_button.place(x=325,y=440)
SelectedBot_label.place(x=150,y=380)
SelectedPlayer_label.place(x=150,y=405)
RockText_label.place(x=75,y=50)
OptionText_label.place(x=90,y=200)
ScoreText_label.place(x=90,y=350)
WinText_label.place(x=200,y=150) 
RockButton_button.place(x=100,y=240)
PaperButton_button.place(x=225,y=240)
ScissorsButton_button.place(x=350,y=240)







window.mainloop()