from tkinter import *
from time import strftime

window = Tk()
window.geometry("500x500")
window.title("")
window.configure(bg="white")
def update_time():
    current_time = strftime("%H:%M:%S %p")
    Clocktext_label.config(text=current_time)
    Clocktext_label.config(fg="red")
    Clocktext_label.after(1000,update_time)


Clocktext_label = Label(window,text="2",fg="black",bg ="white",font=("arial",50,"bold"))



Clocktext_label.place(x=60,y=225)
update_time()


window.mainloop()
