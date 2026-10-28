from tkinter import *

window = Tk()
window.geometry("800x800")
window.title("")
window.configure(bg="white")

#labels
convert_label = Label(window,text="MONEY CONVERTER",fg="black",bg="white",font=("arial",45,"bold"))
topframe = Frame(window,bg="black",width=600,height=200)
bottomframe = Frame(window,bg="red",width=600,height=200)
currencylist = ["GBP", "USD","EU","JPY","CNY","RON"]
currency_conversion_data = {
    # USD
    "USD:EUR": 0.87,
    "USD:JPY": 147.2,
    "USD:GBP": 0.75,
    "USD:CNY": 7.18,
    "USD:RON": 4.42,

    # EUR
    "EUR:USD": 1.15,
    "EUR:JPY": 169.2,
    "EUR:GBP": 0.86,
    "EUR:CNY": 8.25,
    "EUR:RON": 5.08,

    # GBP
    "GBP:USD": 1.33,
    "GBP:EUR": 1.16,
    "GBP:JPY": 196.3,
    "GBP:CNY": 9.55,
    "GBP:RON": 5.85,

    # JPY
    "JPY:USD": 0.0068,
    "JPY:EUR": 0.0059,
    "JPY:GBP": 0.0051,
    "JPY:CNY": 0.0488,
    "JPY:RON": 0.030,

    # CNY
    "CNY:USD": 0.139,
    "CNY:EUR": 0.121,
    "CNY:GBP": 0.105,
    "CNY:JPY": 20.45,
    "CNY:RON": 0.615,

    # RON
    "RON:USD": 0.226,
    "RON:EUR": 0.197,
    "RON:GBP": 0.171,
    "RON:JPY": 33.33,
    "RON:CNY": 1.626,
}

def conversion() :
    try:
      if amount_entry_value.get().isdigit():
         fromvalue = float(amount_entry_value)
      from_cur = currency_choice.get()
      to_cur = currency_choice2.get()
    except:
       print("error")

#,bg="white",fg="red",text=
amount_entry_value = StringVar(value="1")
amount_entry = Entry(topframe,textvariable=amount_entry_value,font=("arial",13,"bold"))
amount_entry2_value = StringVar(value="1.19")
amount_entry2 = Entry(bottomframe,textvariable=amount_entry2_value,font=("arial",13,"bold"))
amount_label1 = Label(topframe,bg="black",fg="white",text="i have.......",font=("arial",20,"bold"))
amount_label2 = Label(bottomframe,bg="red",fg="white",text="i get.......",font=("arial",20,"bold"))
currency_choice = StringVar(value="Euro")
currency_dropdown = OptionMenu(topframe, currency_choice,*currencylist)
currency_choice2 = StringVar(value="british pound")
currency_dropdown2 = OptionMenu(bottomframe, currency_choice2,*currencylist)
currency_dropdown2.config(font=("arial",20,"bold"),bg="#4BE837")
currency_dropdown.config(font=("arial",20,"bold"),bg="#309423")
currency_dropdown["menu"].config(fg="green")
currency_dropdown2["menu"].config(fg="green")
currency_swap = Button(text="💱swap💱",font=("arial",20,"bold"))
#placing
currency_swap.place(x=330,y=425)
convert_label.place(x=100,y=75)
bottomframe.place(x=100,y=500)
topframe.place(x=100,y=200)
topframe.place(x=100,y=200)
amount_label1.place(x=50,y=25)
amount_label2.place(x=50,y=25)
currency_dropdown.place(x=250,y=80)
amount_entry.place(x=50,y=110)
currency_dropdown2.place(x=250,y=80)
amount_entry2.place(x=50,y=110)







window.mainloop()