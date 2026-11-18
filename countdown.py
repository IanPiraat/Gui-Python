from tkinter import *
from tkinter import messagebox
import time
window = Tk()
window.geometry("500x500")
window.title("Countdown")
window.configure(bg="#5CADFF")
hours = StringVar()
minutes = StringVar()
seconds = StringVar()
hours.set("00")
minutes.set("00")
seconds.set("00") 

Stopwatchtext_label = Label(window,text="Stopwatch",bg="#5cadff",fg="black",font=("arial",45,"bold"))
Stopwatchtext_label.place(x=100,y=100)

HourCounter_Entry = Entry(window,textvariable=hours,bg="black",fg="white",font=("arial",40,"bold"),width=2)
MinutesCounter_Entry = Entry(window,textvariable=minutes,bg="black",fg="white",font=("arial",40,"bold"),width=2)
SecondsCounter_Entry = Entry(window,textvariable=seconds,bg="black",fg="white",font=("arial",40,"bold"),width=2)


def countdown() :
    try :
        total_seconds = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
    except :
        messagebox.showerror("Error","Conversion Failed")
    h = 0
    s = 0
    m = 0
    while total_seconds >= 0 :
        m,s = divmod(total_seconds,60)
        if m>60 :
            h,m = divmod(m,60)
        hours.set("{:02d}".format(h))
        seconds.set("{:02d}".format(s))
        minutes.set("{:02d}".format(m))
        window.update()    
        time.sleep(1)
        total_seconds -= 1
    else :
        messagebox.showinfo("Countdown Done","The countdown finished")    

            
        
        
StartButton_Button = Button(window,text="START COUNTDOWN",fg="black",bg="white",font=("arial",30,"bold"),command=countdown)


HourCounter_Entry.place(x=125,y=250)
MinutesCounter_Entry.place(x=225,y=250)
SecondsCounter_Entry.place(x=325,y=250)
StartButton_Button.place(x=25,y=350)





window.mainloop()