# This is the backend (does the math)
from tkinter import *
import tkinter as tk
from tkinter import ttk

root = Tk()
root.geometry('1000x400')
#Create Tab Control
TAB_CONTROL = ttk.Notebook(root)
#Tab1- Control
TAB1 = Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='Control')
#Tab2 - Measure
TAB2 = Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Measure')
TAB_CONTROL.pack(expand=1, fill="both")



#Transaction Setting
Label(TAB1, text="Transaction Setting").grid(row=0, columnspan=6, sticky=W)
Label(TAB1, text="Address (Dec)").grid(row=1, sticky=E)
Label(TAB1, text="Burst Length (Dec)").grid(row=2, sticky=E)
Label(TAB1, text="Write Data (Hex)").grid(row=3, sticky=E)
Entry(TAB1).grid(row=1,column=1,columnspan=2)
Entry(TAB1).grid(row=2,column=1,columnspan=2)
Entry(TAB1).grid(row=3,column=1,columnspan=2)
Button(TAB1, text="random").grid(row=2,column=3)
Button(TAB1, text="random").grid(row=3,column=3)

#Save As Box
Label(TAB1, text="Save As").grid(row=0, column=4,columnspan=2,padx = 20,sticky=W)
Entry(TAB1).grid(row=1,column=4,padx = 20,columnspan=1, sticky=E)
Label(TAB1, text=".txt").grid(row=1, column=4,sticky=E)
Button(TAB1, text="Save").grid(row=2,column=4,sticky=N+E+S+W,padx = 60)

#Burned?
Label(TAB1, text="Burned?").grid(row=0, column=5,columnspan=1, sticky=E)
Entry(TAB1).grid(row=0,column=6,columnspan=1, sticky=W)
Label(TAB1, text=".txt").grid(row=1, column=4,sticky=E)

Label(TAB1, text="Click Freq (Khx)").grid(row=1, column=5,columnspan=2, sticky=S)
Entry(TAB1).grid(row=2,column=5,columnspan=2, padx=80)

Label(TAB1, text="Voltage (V)").grid(row=3, column=5,columnspan=2)
Entry(TAB1).grid(row=4,column=5,columnspan=2, padx=80, sticky=N)


#Row of checkbuttons
Checkbutton(TAB1, text="CENG_MODE").grid(row=6,column=6,columnspan=2, sticky=W)
Checkbutton(TAB1, text="BURN_MODE").grid(row=7,column=6,columnspan=2, sticky=W)
Checkbutton(TAB1, text= "IENG_MODE").grid(row=8,column=6,columnspan=2, sticky=W)
Checkbutton(TAB1, text= "TX enable").grid(row=9,column=6,columnspan=2, sticky=W)
'''
def toggle():
    if var.get() == "ON":
        print("turning on...")
    else:
        print("turning off...")
'''
var = tk.StringVar()
tk.Checkbutton(TAB1, onvalue="ON", offvalue="OFF", width=4, indicatoron=False,variable=var, textvariable=var,
selectcolor="green", background="red").grid(row=5,column=4)


var.set("OFF")





































'''
#Tab Name Labels
Label(TAB1, text="This is Tab 1").grid(column=0, row=0, padx=10, pady=10)
Label(TAB2, text="This is Tab 2").grid(column=0, row=0, padx=10, pady=10)
'''


'''
frame_main = ttk.Frame(TAB1)
Frame1 = tk.Frame(frame_main, bg = "red")
Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)
Frame2 = tk.Frame(frame_main, bg="blue")
Frame2.grid(row = 3, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)
Frame3 = tk.Frame(frame_main, bg="green")
Frame3.grid(row = 0, column = 2, rowspan = 6, columnspan = 3, sticky = W+E+N+S)
'''

'''
topframe = ttk.Frame(frame_main)
topframe.pack(side = TOP)

Label(topframe, text="Address (Dec)").grid(row=0, sticky=E)
Label(topframe, text="Burst Length (Dec)").grid(row=1, sticky=E)
Label(topframe, text="Write Data (Hex)").grid(row=2, sticky=E)
Entry(topframe).grid(row=0,column=1)
Entry(topframe).grid(row=1,column=1)
Entry(topframe).grid(row=2,column=1)
Button(topframe, text="random").grid(row=1,column=2)
Button(topframe, text="random").grid(row=2,column=2)
'''

'''
frame_main = ttk.Frame(TAB1)
topframe = Frame(frame_main)
topframe.pack(side = TOP)

Label(TAB1, text="Address (Dec)").grid(row=0, sticky=E)
Label(TAB1, text="Burst Length (Dec)").grid(row=1, sticky=E)
Label(TAB1, text="Write Data (Hex)").grid(row=2, sticky=E)
Entry(TAB1).grid(row=0,column=1)
Entry(TAB1).grid(row=1,column=1)
Entry(TAB1).grid(row=2,column=1)
Button(TAB1, text="random").grid(row=1,column=2)
Button(TAB1, text="random").grid(row=2,column=2)
'''


'''
topframe = Frame(TAB1)

label1 = Label(topframe, text="Address (Dec)")
label2 = Label(topframe, text="Burst Length (Dec)")
label3 = Label(topframe, text="Write Data (Hex)")
entry1 = Entry(topframe)
entry2 = Entry(topframe)
button2 = Button(topframe, text="random")
button3 = Button(topframe, text="random")

label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)
label3.grid(row=2, sticky=E)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

button2.grid(row=0,column=2)
button2.grid(row=0,column=3)
'''

#Calling Main()
root.mainloop()












root=Tk()