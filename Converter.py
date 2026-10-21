from tkinter import *
window = Tk()
window.geometry("800x800")
window.title("")
window.configure(bg="white")

#labels
convert_label = Label(window,text="MONEY CONVERTER",fg="black",bg="white",font=("arial",45,"bold"))
topframe = Frame(window,bg="black",width=600,height=200)

amount_entry = Entry(topframe) 
#,bg="white",fg="red",text=

amount_label = Label(topframe,bg="black",fg="white",text="test")
#placing
convert_label.place(x=100,y=100)

topframe.place(x=100,y=200)
amount_label.place(x=50,y=50)
amount_entry.place(x=50,y=50)







window.mainloop()