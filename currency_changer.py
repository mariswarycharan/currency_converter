from locale import currency
import requests
from forex_python.converter import CurrencyRates




from msilib.schema import ComboBox
from optparse import Values
from tkinter.ttk import Combobox
from turtle import color, width

from tkinter import *
from tkinter.font import BOLD, ITALIC


from pyparsing import col

# from matplotlib.ft2font import BOLD

list = []

root = Tk()
my_dist = {"USD":1.0722,"JPY":136.05,"BGN":1.9558,"CZK":24.7,"DKK":7.4392,"GBP":0.84875,
           "HUF":392.83,"PLN":4.5858,"RON":4.9427,"SEK":10.5293,"CHF":1.0258,"ISK":137.9,
           "NOK":10.179,"HRK":7.5379,"TRY":17.582,"AUD":1.4995,"BRL":5.0959,"CAD":1.3661,
           "CNY":7.1831,"HKD":8.4165,"IDR":15583.97,"INR":83.1915,"KRW":1343.63,"MXN":21.136,
           "MYR":4.6952,"NZD":1.6426,"PHP":56.02,"SGD":1.4679,"THB":36.589,"ZAR":16.746}
for i in my_dist:
    list.append(i)



root.title("currency convertor")
root.configure(background="#33ccff")
title = Label(root,text="currency convertor",font = ("C:/Users/USER/Downloads/poppins/Poppins-Medium.otf",40,BOLD,ITALIC), foreground="red",background="black",padx=10,pady=20)
title.grid(row=1,column=2)

l1 = Label(root,padx=220,background="#33ccff")
l1.grid(row=1,column=1)

# "----------------------------------left-----------------------------------------"

l_mon_l = Label(root,text="currency_from",font = ("C:/Users/USER/Downloads/poppins/Poppins-Medium.otf",40,ITALIC),padx=10,pady=30,background="#33ccff")
l_mon_l.grid(row=2,column=1)


currencybox = Combobox(root,width=20,font = ("C:/Users/USER/Downloads/poppins/Poppins-Medium.otf",20,ITALIC), foreground="red",background="black")
currencybox['values'] = list
currencybox.grid(row = 3,column = 1)
currencybox.set("currency")
currencybox.current()

l1 = Label(root,padx=220,pady=10,background="#33ccff")
l1.grid(row=4,column=1)

from_money = Label(root,font = ("C:/Users/USER/Downloads/poppins/Poppins-Medium.otf",30,ITALIC),background="red",padx=10,borderwidth=10)
from_money.grid(row=5,column=1)

photo_translate = PhotoImage(file="C:\\Users\\USER\\Downloads\\money.png")
l_ima = Label(root,image=photo_translate)
l_ima.grid(row=2,column=2,rowspan=4)



def main_left():
    global get_left
    get_left = currencybox.get()
    from_money.configure(text=get_left)
    from_money.after(1,main_left)
    
main_left()


text_box_left = Text(root,width=8,height=2,font = ("C:/Users/USER/Downloads/poppins/Poppins-Medium.otf",30,ITALIC))
text_box_left.grid(row=6,column=1)

input_mon = str(text_box_left.get(1.0,END))

# "----------------------------------right-----------------------------------------"
l1 = Label(root,text="currency_from",font = ("C:/Users/USER/Downloads/poppins/Poppins-Medium.otf",40,ITALIC),padx=10,pady=30,background="#33ccff")
l1.grid(row=2,column=3)


currencybox_r = Combobox(root,width=20, font = ("C:/Users/USER/Downloads/poppins/Poppins-Medium.otf",20,ITALIC),foreground="red",background="black")
currencybox_r['values'] = list
currencybox_r.grid(row = 3,column = 3)
currencybox_r.set("currency")
currencybox_r.current()

l1 = Label(root,pady=10,background="#33ccff")
l1.grid(row=4,column=3)

to_money = Label(root,padx=10,font = ("C:/Users/USER/Downloads/poppins/Poppins-Medium.otf",30,ITALIC),background="red",borderwidth=10)
to_money.grid(row=5,column=3)


def main_right():
    
    global get_right
    get_right = currencybox_r.get()
    to_money.configure(text=get_right)
    to_money.after(1,main_right)

    
main_right()



text_box_right = Text(root,width=20,height=2,font = ("C:/Users/USER/Downloads/poppins/Poppins-Medium.otf",30,ITALIC))
text_box_right.grid(row=6,column=3)

result_lan = text_box_right.get(1.0,END)


text_result = Text(root,width=50,height=2,font = ("C:/Users/USER/Downloads/poppins/Poppins-Medium.otf",30,ITALIC),foreground="#6960EC")
text_result.grid(row=9,column=1,columnspan=40)

def main():
    
    global input_money,get_left,get_right
    
    input_money = text_box_left.get(1.0,END)    
    print(get_left)
    print(get_right)
    print(input_money)
    
    c = CurrencyRates()
    result = c.convert(get_left,get_right,int(input_money))

    # print(translation)
    text_box_right.insert(END,result)
    
    text = str(input_money),get_left,"=",result,get_right
    
    text_result.insert(END,text)
# main()

button_curency = Button(root,padx=110,text="convert", foreground="red",background="#33ff33",font = ("C:/Users/USER/Downloads/poppins/Poppins-Medium.otf",20,ITALIC),pady=10,command=main)
button_curency.grid(row=6,column=2)

def remove():
    text_box_right.delete(1.0,END)


button_remove = Button(root,padx=100,text="clean all",font = ("C:/Users/USER/Downloads/poppins/Poppins-Medium.otf",20,ITALIC), pady=10,foreground="red",background="#33ff33",command=remove)
button_remove.grid(row=7,column=2)


l_result = Label(root,pady=10,text="RESULT",font = ("C:/Users/USER/Downloads/poppins/Poppins-Medium.otf",40,ITALIC),background="#FF6700")
l_result.grid(row=8,column=2)







root.mainloop()