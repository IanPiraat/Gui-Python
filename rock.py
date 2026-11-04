from tkinter import *
window = Tk()
window.geometry("750x500")
window.title("rock paper scissors")
window.configure(bg="white")

RockText_label = Label(window,text="Rock Paper Scissors",fg="black",bg="white",font=("arial",45,"bold"))
OptionText_label = Label(window,text="Your Options",fg="black",bg="white",font=("arial",15,"bold"))
ScoreText_label = Label(window,text="Score:",fg="black",bg="white",font=("arial",15,"bold"))
WinText_label = Label(window,text="{} Won!",fg="black",bg="white",font=("arial",15,"bold"))
SelectedBot_label = Label(window,text="Computer selected:{}   computer score:{}",fg="black",bg="white",font=("arial",15,"bold"))
SelectedPlayer_label = Label(window,text="you selected:{}     player score:{}",fg="black",bg="white",font=("arial",15,"bold"))




RockButton_button = Button(window,text="Rock",fg="black",bg="white",font=("arial",20,"bold"))
PaperButton_button = Button(window,text="Paper",fg="black",bg="white",font=("arial",20,"bold"))
ScissorsButton_button = Button(window,text="Scissors",fg="black",bg="white",font=("arial",20,"bold"))






RockText_label.place(x=75,y=50)
OptionText_label.place(x=90,y=200)
ScoreText_label.place(x=90,y=350)

RockButton_button.place(x=100,y=240)
PaperButton_button.place(x=225,y=240)
ScissorsButton_button.place(x=350,y=240)







window.mainloop()