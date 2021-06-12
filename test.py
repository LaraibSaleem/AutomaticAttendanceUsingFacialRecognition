# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:27:22 2020

@author: Laraib
"""

#for GUI
import tkinter as tk
from tkinter import * 
from functools import partial

import att_sheet_methods
import db
import opencv_methods
from PIL import Image, ImageTk #for Images (Logo etc)




from tkinter import font

window = tk.Tk()
window.title("AAUFR-Automatic Attendance Using Facial Recognition")
window.geometry('1260x700')
window.configure(background='gainsboro')

# Create the text within a frame
pref = Label(window, text = "Select Preferences")
# Pack or use grid to place the frame
pref.grid(row = 0, sticky = W)
# font.Font instead of tkFont.Fon
f = font.Font(pref, pref.cget("font"))
f.configure(underline=True)
pref.configure(font=f)

window.mainloop()




# --------------- LOGO --------------- #
window = tk.Tk()
window.title("AAUFR-Automatic Attendance Using Facial Recognition")
window.iconbitmap('AMS.ico')
window.geometry('1260x700')
window.configure(background='gainsboro')

'''
#Logo
img = ImageTk.PhotoImage(Image.open("fyp-logo-1.png"))
panel = Label(window, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
'''

img1  = Image.open("fyp-logo-1.png") 
img1 = img1.resize((250, 250), Image.ANTIALIAS)
photo1=ImageTk.PhotoImage(img1)
lab1=Label(image=photo1).place(x=50,y=50)


img2  = Image.open("fyp-logo-2.png") 
img2 = img2.resize((250, 250), Image.ANTIALIAS)
photo2=ImageTk.PhotoImage(img2)
lab2=Label(image=photo2, bg="gainsboro").place(x=400,y=400)

    
window.mainloop()
















# --------------- MANUAL_ATTENDANCE_ON_EXISTING_SHEETS_(SEPARATE_FOR_EVERY_INSTRUCTOR) --------------- #

def man_get_btn_txt(n, u):
    btnpressed = (buttons[n])
    #print(btnpressed['text'])
    sheetname = btnpressed['text']
    if(not(opencv_methods.auto_attendance(sheetname, u))):
       #print("Trainer file DOES NOT exists")
       error_sound()
       take_auto_attendance_error()
    else:
        print("Trainer file exists")
        
        
# --------------- NO_ATT_SHEET_ERROR_FOR_AUTO_+_MANUAL_+_REPORT --------------- #              
def no_att_sheet_error():
    pass



# --------------- SELECT_SHEET_FOR_AUTO_ATTENDANCE_FUNCTION --------------- #
def select_sheet_man_att_func():
    if not unametxt.get()=="":
        u = unametxt.get()
        if db.check_uname(u):
            listoffiles = att_sheet_methods.return_listoffiles(u)
            length = len(listoffiles)
            if  length == 0:
                error_sound()
                #print("You don't have any Attendance Sheet.")
                no_att_sheet_error()
            else:
                #print(f"You have {length} Attendance Sheet(s).")
                
                #create a window for buttons
                btnswindow = tk.Tk()
                btnswindow.title("Attendance Sheets")
                btnswindow.iconbitmap('AMS.ico')
                btnswindow.configure(background='gainsboro')
                
                global buttons 
                buttons = []
                for i in range(length):
                    #fileno = str(i+1)
                    filename = listoffiles[i]
                    #fullname = fileno+"."+" " +filename
                    button = tk.Button(btnswindow, text = filename, command=partial(man_get_btn_txt, i, u), fg="white", bg="dim gray",
                                        width=25, activebackground="Red", font=('calibri', 15, 'bold'))
                    #button.place(x=550, y=i+200)
                    button.pack()
                    buttons.append(button)
                
                btnswindow.mainloop()
        else:
            error_sound()
            #print("Username doesnot exist")
            uname_exis_error()
    else:
        print("Field is empty")
        error_sound()
        #empty_fields_error()
        #input fields empty error
        #please fill all fields
        




def clear_sheet_func():
    pass




def select_sheet_man_att():
    global selectsheetmanattwindow
    selectsheetmanattwindow = tk.Tk()
    selectsheetmanattwindow.title("Select Attendance Sheet")
    selectsheetmanattwindow.iconbitmap('AMS.ico')
    selectsheetmanattwindow.geometry('1260x700')
    selectsheetmanattwindow.configure(background='gainsboro')
    
    selectsheetmanattlbl = tk.Label(selectsheetmanattwindow, text="Select Sheet for Manual Attendance", width=75, fg="black", bg="gainsboro", height=2, font=('calibri', 25, ' bold '))
    selectsheetmanattlbl.place(x=100, y=100)
    
    #label & text box for user name - unametxt already globalized for auto attendance
    unamelbl = tk.Label(selectsheetmanattwindow, text="Enter Username", width=20, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
    unamelbl.place(x=200, y=200)
    unametxt = tk.Entry(selectsheetmanattwindow, width=20, fg="black", font=('calibri', 20))
    unametxt.place(x=550, y=210)

    
    #button for creation of file
    selectsheetmanattbtn = tk.Button(selectsheetmanattwindow, text="Next", command=select_sheet_man_att_func, fg="white", bg="dim gray",
                        width=10, activebackground="Red", font=('calibri', 15, ' bold '))
    selectsheetmanattbtn.place(x=550, y=300)
    
    
    #button for cleaing text field
    clear_select_sheet = tk.Button(selectsheetmanattwindow, text="Clear", command=clear_sheet_func, fg="white", bg="dim gray",
                        width=10, activebackground="Red", font=('calibri', 15, ' bold '))
    clear_select_sheet.place(x=750, y=300)
    

    selectsheetmanattwindow.mainloop()

#select_sheet_man_att()




















# --------------- AUTO_ATTENDANCE_ON_EXISTING_SHEETS_(SEPARATE_FOR_EVERY_INSTRUCTOR) --------------- #
'''
def auto_get_btn_txt(n, u):
    btnpressed = (buttons[n])
    #print(btnpressed['text'])
    sheetname = btnpressed['text']
    if(not(opencv_methods.auto_attendance(sheetname, u))):
       #print("Trainer file DOES NOT exists")
       error_sound()
       take_auto_attendance_error()
    else:
        print("Trainer file exists")



def select_sheet_auto_att_func():
    if not unametxt.get()=="":
        u = unametxt.get()
        if db.check_uname(u):
            listoffiles = att_sheet_methods.return_listoffiles(u)
            length = len(listoffiles)
            if  length == 0:
                print("You don't have any Attendance Sheet.")
            else:
                print(f"You have {length} Attendance Sheet(s).")
                global buttons 
                buttons = []
                for i in range(length):
                    #fileno = str(i+1)
                    filename = listoffiles[i]
                    #fullname = fileno+"."+" " +filename
                    button = tk.Button(selectsheetautoattwindow, text = filename, command=partial(auto_get_btn_txt, i, u), fg="white", bg="dim gray",
                                        width=25, activebackground="Red", font=('calibri', 15, 'bold'))
                    button.pack()
                    buttons.append(button)
        else:
            #error_sound()
            print("Username doesnot exist")
            #uname_exis_error()
    else:
        print("Field is empty")
        error_sound()
        #empty_fields_error()
        #input fields empty error
        #please fill all fields




def clear_sheet_func():
    unametxt.delete(first=0, last=30)



def select_sheet_auto_att():
    global selectsheetautoattwindow
    selectsheetautoattwindow = tk.Tk()
    selectsheetautoattwindow.title("Create Attendance Sheets")
    selectsheetautoattwindow.iconbitmap('AMS.ico')
    selectsheetautoattwindow.geometry('1260x700')
    selectsheetautoattwindow.configure(background='gainsboro')
    
    selectsheetautoattlbl = tk.Label(selectsheetautoattwindow, text="Select Sheet for Automatic Attendance", width=75, fg="black", bg="gainsboro", height=2, font=('calibri', 25, ' bold '))
    selectsheetautoattlbl.place(x=100, y=100)
    
    #label & text box for user name
    global unametxt
    unamelbl = tk.Label(selectsheetautoattwindow, text="Enter Username", width=20, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
    unamelbl.place(x=200, y=200)
    unametxt = tk.Entry(selectsheetautoattwindow, width=20, fg="black", font=('calibri', 20))
    unametxt.place(x=550, y=210)

    
    #button for creation of file
    selectsheetautoattbtn = tk.Button(selectsheetautoattwindow, text="Next", command=select_sheet_auto_att_func, fg="white", bg="dim gray",
                        width=10, activebackground="Red", font=('calibri', 15, ' bold '))
    selectsheetautoattbtn.place(x=550, y=300)
    
    
    #button for cleaing text field
    clear_select_sheet = tk.Button(selectsheetautoattwindow, text="Clear", command=clear_sheet_func, fg="white", bg="dim gray",
                        width=10, activebackground="Red", font=('calibri', 15, ' bold '))
    clear_select_sheet.place(x=750, y=300)
    

    selectsheetautoattwindow.mainloop()

    
select_sheet_auto_att()
'''






#getting text of a button
'''
import tkinter as tk

master = tk.Tk()
master.geometry("500x500")

def function():
    print(btn['text'])

btn = tk.Button(master, text="Clear", command=function, fg="white", bg="dim gray",
                        width=5, activebackground="Red", font=('calibri', 15, ' bold '))
btn.place(x=0, y=0)
master.mainloop()
'''




'''
print({'1', '1', '1', '1', '1', '1', '2', '3', '4'})
'''



# --------------- OPENING_EXCEL_SHEET --------------- #
'''
def open_attendance_sheet():
     os.startfile("StudentAttendance.csv")
#open_attendance_sheet()
'''


# --------------- RETURNING_NAME_TO_A_REG --------------- #
'''
def return_name(regnum):
    flag = None
    name = ""
    with open("RegisteredStudents.csv", "r", newline="") as file:
        content = csv.reader(file)
        next(content, None) #skips header
        for c in content:
            if(regnum == c[0]):
                #print(c[1])
                flag = True
                name = c[1]
            else:
                #print("condition NOT satisfied")
                flag = False
                name = "No Match in CSV"
            if(flag):
                break
    return name
#return_name('8')



reg = '5'
name = return_name(reg)
if checking_att_sheet(reg):
    print("2nd time attendance")
    mark_auto_attendance_2(reg,name)
else:
    print("1st time attendance")
    mark_auto_attendance_1(reg,name)
'''






# --------------- VERTICAL_LINE_TEST --------------- #
'''
from tkinter import *
master = Tk()
w = Canvas(master, width=200, height=100)
w.pack()
w.create_line(100, 25, 100, 75, fill="#476042", width=3)
mainloop()
'''






'''
import tkinter as tk

app = tk.Tk()
app.geometry("500x500")

def s_reg_check():
    try:
        sreg = int(sregtxt.get())
    except Exception:
        error()
        
def error():
    global sregerror
    sregerror = tk.Tk()
    sregerror.geometry('330x100')
    sregerror.iconbitmap('AMS.ico')
    sregerror.title('Warning!')
    sregerror.configure(background='gainsboro')
    Label(sregerror, text='Student is Already Registered', fg='red', bg='gainsboro',
                      font=('times', 16, ' bold ')).pack()
    Button(sregerror, text='OK', command=exit_error, fg="red", bg="gainsboro", width=9, height=1,
                         activebackground="Red", font=('times', 15, ' bold ')).place(x=90, y=50)
    sregerror.mainloop()
       
    
def exit_error():
    sregerror.destroy()
        

sreglbl = tk.Label(app, text="Enter Student Reg no", width=30, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
sreglbl.place(x=200, y=300)
sregtxt = tk.Entry(app, width=20, fg="black", font=('calibri', 20))
sregtxt.place(x=550, y=310)
tk.Button(app, text="click", command=s_reg_check).pack()

app.mainloop()
'''



# --------------- #switching between frames --------------- #
"""
import tkinter as tk
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go to page one",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Go to page two",
                  command=lambda: master.switch_frame(PageTwo)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
"""