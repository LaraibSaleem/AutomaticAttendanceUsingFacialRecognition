# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:11:30 2020

@author: Laraib
"""




# --------------- ARBITRARY_NO_OF_BUTTONS --------------- #
import tkinter as tk
from tkinter import *
import att_sheet_methods
from functools import partial





'''
def get_btn_txt(fileno):
    fileno = int(fileno)
    print(buttons[fileno]['text'])
'''




def get_btn_txt(n):
    btnpressed = (buttons[n])
    print(btnpressed['text'])


master = Tk()
buttons = []

listoffiles = att_sheet_methods.return_listoffiles("mona")
length = len(listoffiles)

for i in range(length):
    fileno = str(i+1)
    filename = listoffiles[i]
    fullname = fileno+"."+" " +filename
    button = tk.Button(master, text = fullname, command=partial(get_btn_txt, i), fg="white", bg="dim gray",
                        width=25, activebackground="Red", font=('calibri', 15, 'bold'))
    button.pack()
    buttons.append(button)
master.mainloop()




'''
# --------------- GETTING_TEXT_OF_A_BUTTON_PRESSED--------------- #
from tkinter import *
from functools import partial

win = Tk()
button_identities = []

def change(n):
    # function to get the index and the identity (bname)
    print(n)
    bname = (button_identities[n])
    bname.configure(text = "clicked")

for i in range(5):
    # creating the buttons, assigning a unique argument (i) to run the function (change)
    button = Button(win, width=10, text=str(i), command=partial(change, i))
    button.pack()
    # add the button's identity to a list:
    button_identities.append(button)

# just to show what happens:
print(button_identities)

win.mainloop()
'''





