#Project: Final
#Author: Josh Millikan
#Date: 12/4/2021
#Summary: Take currencys and convert them into U.S dollars



#Import GUI
from tkinter import *
from tkinter import ttk



#Layout GUI
converter = Tk()
converter.title("Unit Converter")
converter.geometry("600x400")

#Define Exchange Rates
OPTIONS = {
    "Australian Dollar": 1.428272,
    "Brazilian Real":5.653287,
    "British Pound":0.755661,
    "Chinese Yuan":6.376348,
    "Euro":0.883871,
    "HongKong Dollar":7.794734,
    "Indonesian Rupiah":0.004864,
    "Japanese Yen":112.780631,
        }

#Define Mainloop
def ok():
    price = dollars.get()
    answer = variable1.get()
    DICT = OPTIONS.get(answer,None)
    converted = float(DICT)*float(price)
    result.delete(1.0,END)
    result.insert(INSERT,"Price in ",INSERT,answer,INSERT," = ",INSERT,converted)
appName = Label(converter,text="Josh's Currency Converter",font=("arial",25,"bold","underline"),fg="dark red")
appName.place(x=150, y=10)

#Layout buttons and text options
result = Text(converter,height=5,width=50,font=("arial",10,"bold"),bd=5)
result.place(x=125, y=60)

unitedStates = Label(converter,text="Value in U.S Dollars:",font=("arial",10,"bold"),fg="red")
unitedStates.place(x=30, y=165)

dollars = Entry(converter,font=("arial",20))
dollars.place(x=200, y=160)

choice = Label(converter,text="Choice:",font=("arial",10,"bold"),fg="red")
choice.place(x=30, y=220)

variable1 = StringVar(converter)
variable1.set(None)
option = OptionMenu(converter,variable1,*OPTIONS)
option.place(x=100 , y=210,width=100, height=40)

button = Button(converter,text="Convert",fg="green",font=("arial",20),bg="powder blue",command=ok)
button.place(x=200, y=210,height=40,width=150)





converter.mainloop()
