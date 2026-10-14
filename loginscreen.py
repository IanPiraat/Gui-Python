from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("430x500")
window.title("Login Pass")
window.configure(bg="#5CADFF")
USERNAME = "Ian"
PASSWORD = "12345"

def check_login():
    global USERNAME
    global PASSWORD

    un = user_entry.get()
    ps = password_entry.get()
    if un == USERNAME :
        if ps == PASSWORD :
            messagebox.showinfo("SUCCES","you logged in")   
        else :
            messagebox.showerror("Passwordwrong","you failed to log in")
    else : 
        messagebox.showerror("UsernameWrong","you failed to log in")    

username = Label(window,text="Username",fg="red",bg="white",font=("arial",20,"bold"))
username.place(x=20,y=250)
#username.grid(row=1,column=1,padx=10,pady=10)
#username.pack()
password = Label(window,text="Password",fg="blue",bg ="white",font=("arial",20,"bold"))
password.place(x=20,y=300)

user_entry = Entry(bg="white",fg="red",font=("arial",20,"bold"),width=10)
user_entry.place(x=200,y=250)

password_entry = Entry(bg="white",fg="blue",font=("arial",20,"bold"),width=10)
password_entry.place(x=200,y=300)


login_btm = Button(window,bg="green",fg="black",text="Login?",width=15,height=2,font=("arial",8,"bold"),command=check_login)
login_btm.place(x=50,y=450)

cancel_btm = Button(window,bg="Red",fg="black",text="CANCEL",width=15,height=2,font=("arial",8,"bold"),command=exit)
cancel_btm.place(x=250,y=450)



window.mainloop()
