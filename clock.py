from tkinter import *
import random
from time import strftime


window = Tk()
window.geometry("500x500")
window.title("")
window.configure(bg="white")

Digital_label = Label(window,text="My digital clock",fg="black",bg="white",font=("arial",48,"bold"))
Clocktext_label = Label(window,text="2",fg="black",bg="white",font=("arial",50,"bold"))

def update_time():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r2 = random.randint(0, 255)
    g2 = random.randint(0, 255)
    b2 = random.randint(0, 255)
    finalcolor = "#{:02x}{:02x}{:02x}".format(r, g, b)
    finalcolor2 = "#{:02x}{:02x}{:02x}".format(r2, g2, b2)
    window.configure(bg=finalcolor)
    Digital_label.configure(bg=finalcolor)
    Clocktext_label.configure(bg=finalcolor)
    current_time = strftime("%H:%M:%S %p")
    Clocktext_label.configure(text=current_time, fg=finalcolor2)
    Clocktext_label.after(1000, update_time)

Digital_label.place(x=5,y=100)
Clocktext_label.place(x=50,y=225)
update_time()


window.mainloop()
