#template
from tkinter import *
import calendar
window = Tk()
window.geometry("800x500")
window.title("Calendar")
window.config(bg="#041322")

def show_calender() :
    year = int(dateBT.get()) 

    window2 = Tk()
    window2.geometry("2000x1300")
    window2.title("Calender2")
    window2.config(bg="#041322")
    content = calendar.calendar(year)
    text = Label(window2,text="{}".format(content),fg="white",bg="#041322",font=("arial",18,"bold"),bd=5)
    text.place(x=0,y=250)
    


    window2.mainloop()


#labels
calender = Label(window,text="CALENDAR",fg="white",bg="#041322",font=("arial",60,"bold"))
dateBT = Entry(window,text="2026",fg="white",bg ="#041322",font=("arial",12,"bold"),bd=5,)
showBT = Button(window,text="Show",fg="white",bg ="#041322",font=("arial",33,"bold"),bd=5,relief="solid",command=show_calender)



#hover event
def hover(event):
    showBT.config(fg="white",bg ="#E4E9EE")
def unhover(event) :
    showBT.config(fg="white",bg ="#041322")

showBT.bind("<Enter>", hover)
showBT.bind("<Leave>", unhover)


#place
calender.place(x=190,y=150)
dateBT.place(x=225,y=280)
showBT.place(x=450,y=250)


#mainloop
window.mainloop()