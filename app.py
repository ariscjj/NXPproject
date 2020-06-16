# This is the GUI
# This is the backend (does the math)
from tkinter import *
import tkinter as tk
from tkinter import ttk
from model import save

#L is label 
#E is entry
#B is button 
#C is Checkbox 

root = tk.Tk()
root.geometry('1300x700')
#Create Tab Control
TAB_CONTROL = ttk.Notebook(root)
#Tab1- Control
TAB1 = Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='Control')
#Tab2 - Measure
TAB2 = Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Measure')
TAB_CONTROL.pack(expand=1, fill="both")

COLUMNSPAN=2

#Transaction Setting
transL=Label(TAB1, text="Transaction Setting")
transL.grid(row=0, columnspan=6, sticky=W)

addressL=Label(TAB1, text="Address (Dec)")
addressL.grid(row=1, sticky=E)
addressE=Entry(TAB1)
addressE.grid(row=1,column=1,columnspan=COLUMNSPAN)

burstL=Label(TAB1, text="Burst Length (Dec)")
burstL.grid(row=2, sticky=E)
burstE=Entry(TAB1)
burstE.grid(row=2,column=1,columnspan=COLUMNSPAN)
burstB=Button(TAB1, text="random")
burstB.grid(row=2,column=3)

hexL=Label(TAB1, text="Write Data (Hex)")
hexL.grid(row=3, sticky=E)
hexE=Entry(TAB1)
hexE.grid(row=3,column=1,columnspan=COLUMNSPAN)
hexB=Button(TAB1, text="random")
hexB.grid(row=3,column=3)


#Save As Box
# This takes in X and returns Y
SMALLPAD=10
LARGEPAD=50
LARGECOLSPAN=2

saveL=Label(TAB1, text="Save As")
saveL.grid(row=0, column=6,columnspan=LARGECOLSPAN,padx = SMALLPAD,sticky=W)
saveE=Entry(TAB1)
saveE.grid(row=1,column=6,padx = SMALLPAD,sticky=E)

txtL=Label(TAB1, text=".txt")
txtL.grid(row=1, column=7,sticky=W)
saveB=Button(TAB1, text="Save",command=save)
saveB.grid(row=2,column=6,sticky=N+E+S+W,padx = LARGEPAD)

#Burned?
burnedL=Label(TAB1, text="Burned?")
burnedL.grid(row=0, column=7, sticky=E)
burnedE=Entry(TAB1)
burnedE.grid(row=0,column=8,sticky=W)


clickF=Label(TAB1, text="Click Freq (Khx)")
clickF.grid(row=1, column=8, sticky=S)
clickE=Entry(TAB1)
clickE.grid(row=2,column=8)

voltageL=Label(TAB1, text="Voltage (V)")
voltageL.grid(row=3, column=8)
voltageE=Entry(TAB1)
voltageE.grid(row=4,column=8, sticky=N)

#Row of checkbuttons
cengC = Checkbutton(TAB1, text="CENG_MODE")
cengC.grid(row=6,column=8,columnspan=2, sticky=W)
burnC = Checkbutton(TAB1, text="BURN_MODE")
burnC.grid(row=7,column=8,columnspan=2, sticky=W)
iengC=Checkbutton(TAB1, text= "IENG_MODE")
iengC.grid(row=8,column=8,columnspan=2, sticky=W)
txC=Checkbutton(TAB1, text= "TX enable")
txC.grid(row=9,column=8,columnspan=2, sticky=W)

# Buttons for T_trim, t_trim, and Runcik 
tTrimB = Button(TAB1, text="T_trim")
tTrimB.grid(row=7,column=7,sticky=N+E+S+W,padx = LARGEPAD)
iTrimB = Button(TAB1, text="I_trim")
iTrimB.grid(row=8,column=7,sticky=N+E+S+W,padx = LARGEPAD)
runcikB = Button(TAB1, text="Runcik")
runcikB.grid(row=9,column=7,sticky=N+E+S+W,padx = LARGEPAD)

#dataLoop 
dataLoopL = Label(TAB1, text="Data Range/Loop")
dataLoopL.grid(row=11,column=5, columnspan=LARGECOLSPAN, sticky=N+E+S,pady=SMALLPAD)
dataLoopE= Entry(TAB1)
dataLoopE.grid(row=11,column=7,sticky=N+E+S+W,pady=SMALLPAD)
measiB = Button(TAB1, text="measi")
measiB.grid(row=11,column=8,sticky=N+W+S,padx = LARGEPAD,pady=SMALLPAD)

# Switch between SPI and I2C 
var = tk.StringVar()
switch=tk.Checkbutton(TAB1, onvalue="I2C", offvalue="SPI", width=4, indicatoron=False,variable=var, textvariable=var,)
switch.grid(row=5,column=6)
var.set("I2C")

#Row of Buttons 
resetB=Button(TAB1, text="Reset")
resetB.grid(row=13,column=1,sticky=N+E+S+W,padx = SMALLPAD)

writeB=Button(TAB1, text="Write")
writeB.grid(row=13,column=2,sticky=N+E+S+W,padx = SMALLPAD)

shmooB=Button(TAB1, text="Shmoo")
shmooB.grid(row=13,column=3,sticky=N+E+S+W,padx = SMALLPAD)

tsenB=Button(TAB1, text="Tsen")
tsenB.grid(row=13,column=4,sticky=N+E+S+W,padx = SMALLPAD)

burnB=Button(TAB1, text="Burn")
burnB.grid(row=13,column=5,sticky=N+E+S+W,padx = SMALLPAD)


#Log Info
logL=Label(TAB1, text="Log")
logL.grid(row=14,column=0,sticky=N+E+S,padx = LARGEPAD)
clearB=Button(TAB1, text="Clear")
clearB.grid(row=15,column=0,sticky=N+E,padx = LARGEPAD)

#Output Box
outputL=Label(TAB1,bg="white",text="yes!")
outputL.grid(row=15,column=1,rowspan=5,columnspan=8,sticky=S+N+E+W)
TAB1.rowconfigure(15,minsize=100)


#Calling Main()
root.mainloop()

































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












