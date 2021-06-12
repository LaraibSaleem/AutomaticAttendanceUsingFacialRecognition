# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:48:28 2020

@author: Laraib
"""


#for GUI
import tkinter as tk
from tkinter import *
#for generating a beep sound
import winsound
#for meesage box displayed when exiting windows
from tkinter import messagebox
from functools import partial #for uniqueness of buttons created in a loop for displaying attendance sheets
import csv #for check_reg() only
#importing db.py
import db
#importing student_csv_methods.py
import student_csv_methods
#importing opencv_methods.py
import opencv_methods
#importing generate_report.py
import generate_report

import os #signup - making directory at the system with username
import att_sheet_methods

from PIL import Image, ImageTk #for Images (Logo etc)

from tkinter import font





# --------------- LOG_OUT_INSTRUCCTOR --------------- #
def log_out_inst():
    instwindow.destroy()
    main_window()
      
# --------------- PASSWORD_CHANGE_SUCCESSFUL --------------- #
def pw_change_successful():
    global pwchangesuccessful
    pwchangesuccessful = tk.Tk()
    pwchangesuccessful.geometry('330x100')
    pwchangesuccessful.iconbitmap('project_images/AMS.ico')
    pwchangesuccessful.title('Success')
    pwchangesuccessful.configure(background='gainsboro')
    Label(pwchangesuccessful, text='Password changed successfully',
          fg='green', bg='gainsboro', font=('calibri', 16, ' bold ')).pack()
    Button(pwchangesuccessful, text='OK', command=exit_pw_change_successful, fg="green", bg="gainsboro", width=9, height=1,
          activebackground="Green", font=('calibri', 15, ' bold ')).place(x=110, y=50)
    pwchangesuccessful.resizable(width=False, height=False)
    pwchangesuccessful.mainloop()
          
def exit_pw_change_successful():
    pwchangesuccessful.destroy()


# --------------- EX_NEW_PASS_CANNOT_BE_SAME_ERROR --------------- #
def ex_new_pass_error():
    global enpasserror
    enpasserror = tk.Tk()
    enpasserror.geometry('400x100')
    enpasserror.iconbitmap('project_images/AMS.ico')
    enpasserror.title('Warning!')
    enpasserror.configure(background='gainsboro')
    Label(enpasserror, text='Existing & new password cannot be same.', fg='red', bg='gainsboro',
                      font=('calibri', 16, ' bold ')).pack()
    Button(enpasserror, text='OK', command=exit_ex_new_pass_error, fg="red", bg="gainsboro", width=9, height=1,
                         activebackground="Red", font=('calibri', 15, ' bold ')).place(x=150, y=50)
    enpasserror.resizable(width=False, height=False)
    enpasserror.mainloop()
    
def exit_ex_new_pass_error():
    enpasserror.destroy()


# --------------- UNAME_DOES_NOT_EXIST_ERROR --------------- #
def uname_exis_error():
    global unameexiserror
    unameexiserror = tk.Tk()
    unameexiserror.geometry('310x100')
    unameexiserror.iconbitmap('project_images/AMS.ico')
    unameexiserror.title('Warning!')
    unameexiserror.configure(background='gainsboro')
    Label(unameexiserror, text='Username does not exist.', fg='red', bg='gainsboro',
                      font=('calibri', 16, ' bold ')).pack()
    Button(unameexiserror, text='OK', command=exit_uname_exis_error, fg="red", bg="gainsboro", width=9, height=1,
                         activebackground="Red", font=('calibri', 15, ' bold ')).place(x=90, y=50)
    unameexiserror.resizable(width=False, height=False)
    unameexiserror.mainloop()
      
def exit_uname_exis_error():
    unameexiserror.destroy()
    #not working!
    '''
    #destroy change password window in first
    destroy_changepasswindow()

def destroy_changepasswindow():
    changepasswindow.destroy()
    '''

# --------------- CLEARING_FIELDS_FOR_CHANGE_PASSWORD --------------- #
def clear_change_pass ():
    changepasstxt1.delete(first=0, last=30)
    changepasstxt2.delete(first=0, last=30)
    changepasstxt3.delete(first=0, last=30)


    
# --------------- CHANGE_PASSWORD_INSTRUCCTOR_(FUNCTION) --------------- # 
def change_pass():
    if(not(changepasstxt1.get()=="" or changepasstxt2.get() == "" or changepasstxt3.get() == "")):
        u = changepasstxt1.get()
        if db.check_uname(u):
            p1 = changepasstxt2.get()
            if(db.sign_in(u,p1) == 'instructor'):
                p2 = changepasstxt3.get()
                if not p1 == p2:
                    db.change_password(u,p2)
                    #print("Password changed successfully")
                    pw_change_successful() 
                else:
                    error_sound()
                    #print("Existing & New Password cannot be same")
                    ex_new_pass_error()
            else:
                error_sound()
                #print("Invalid Credentials")
                signin_error() #error screen for invalid credentials, defined for sign in
        else:
            error_sound()
            #print("Username does not exist")
            uname_exis_error()
    else:
        print("Fields are empty")
        error_sound()
        #empty_fields_error()
        #input fields empty error
        #please fill all fields
        
    

    
# --------------- CHANGE_PASSWORD_INSTRUCCTOR_(WINDOW)--------------- #    
def change_pass_inst():
    global changepasswindow
    changepasswindow = tk.Tk()
    changepasswindow.title("Change Password")
    changepasswindow.iconbitmap('project_images/AMS.ico')
    changepasswindow.geometry('1260x700')
    changepasswindow.configure(background='gainsboro')
    
    changepasslabel = tk.Label(changepasswindow, text="Change Password", width=50, fg="black", bg="gainsboro", height=2, font=('calibri', 25, ' bold '))
    changepasslabel.place(x=285, y=100)
    
    global changepasstxt1
    changepasslbl1 = tk.Label(changepasswindow, text="Enter Username", width=30, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
    changepasslbl1.place(x=200, y=200)
    changepasstxt1 = tk.Entry(changepasswindow, width=20, fg="black", font=('calibri', 20))
    changepasstxt1.place(x=550, y=210)
    
    global changepasstxt2
    changepasslbl2 = tk.Label(changepasswindow, text="Enter Existing Password", width=30, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
    changepasslbl2.place(x=200, y=300)
    changepasstxt2 = tk.Entry(changepasswindow, width=20, fg="black", font=('calibri', 20))
    changepasstxt2.place(x=550, y=310)
    
    global changepasstxt3
    changepasslbl3 = tk.Label(changepasswindow, text="Enter New Password", width=30, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
    changepasslbl3.place(x=200, y=400)
    changepasstxt3 = tk.Entry(changepasswindow, width=20, fg="black", font=('calibri', 20))
    changepasstxt3.place(x=550, y=410)
    
    #button for change password
    changepass = tk.Button(changepasswindow, text="Change", command=change_pass, fg="white", bg="dim gray",
                        width=10, activebackground="Red", font=('calibri', 15, ' bold '))
    changepass.place(x=700, y=500)
    
    #button for clearing text fields - signin
    clear_changepass = tk.Button(changepasswindow, text="Clear", command=clear_change_pass, fg="white", bg="dim gray",
                        width=5, activebackground="Red", font=('calibri', 15, ' bold '))
    clear_changepass.place(x=900, y=500)
    
    changepasswindow.mainloop()










# --------------- SHEET_CREATED_SUCCESSFUL --------------- #
def sheet_created_successful():
    global sheetcreatedsuccessful
    sheetcreatedsuccessful = tk.Tk()
    sheetcreatedsuccessful.geometry('330x100')
    sheetcreatedsuccessful.iconbitmap('project_images/AMS.ico')
    sheetcreatedsuccessful.title('Success')
    sheetcreatedsuccessful.configure(background='gainsboro')
    Label(sheetcreatedsuccessful, text='Sheet created successfully',
          fg='green', bg='gainsboro', font=('calibri', 16, ' bold ')).pack()
    Button(sheetcreatedsuccessful, text='OK', command=exit_sheet_created_successful, fg="green", bg="gainsboro", width=9, height=1,
          activebackground="Green", font=('calibri', 15, ' bold ')).place(x=110, y=50)
    sheetcreatedsuccessful.resizable(width=False, height=False)
    sheetcreatedsuccessful.mainloop()
          
def exit_sheet_created_successful():
    sheetcreatedsuccessful.destroy()




# --------------- SHEET_CREATION_ERROR --------------- #
def sheet_creation_error():
    global sheetcreationerror
    sheetcreationerror = tk.Tk()
    sheetcreationerror.geometry('360x100')
    sheetcreationerror.iconbitmap('project_images/AMS.ico')
    sheetcreationerror.title('Warning!')
    sheetcreationerror.configure(background='gainsboro')
    Label(sheetcreationerror, text='There was an error creating sheet.', fg='red', bg='gainsboro',
                      font=('calibri', 16, ' bold ')).pack()
    Button(sheetcreationerror, text='OK', command=exit_sheet_creation_error, fg="red", bg="gainsboro", width=9, height=1,
                         activebackground="Red", font=('calibri', 15, ' bold ')).place(x=115, y=50)
    sheetcreationerror.resizable(width=False, height=False)
    sheetcreationerror.mainloop()
      
def exit_sheet_creation_error():
    sheetcreationerror.destroy()






# --------------- SHEET_NAME_ALREADY_EXISTS_ERROR --------------- #
def sheetname_exis_error():
    global sheetnameexiserror
    sheetnameexiserror = tk.Tk()
    sheetnameexiserror.geometry('310x100')
    sheetnameexiserror.iconbitmap('project_images/AMS.ico')
    sheetnameexiserror.title('Warning!')
    sheetnameexiserror.configure(background='gainsboro')
    Label(sheetnameexiserror, text='Sheet name already in use.', fg='red', bg='gainsboro',
                      font=('calibri', 16, ' bold ')).pack()
    Button(sheetnameexiserror, text='OK', command=exit_sheetname_exis_error, fg="red", bg="gainsboro", width=9, height=1,
                         activebackground="Red", font=('calibri', 15, ' bold ')).place(x=90, y=50)
    sheetnameexiserror.resizable(width=False, height=False)
    sheetnameexiserror.mainloop()
      
def exit_sheetname_exis_error():
    sheetnameexiserror.destroy()





# --------------- CREATING_NEW_ATTENDANCE_SHEETS --------------- #
def create_sheets_func():
    if(not(unametxt.get() =="" or filetxt.get() == "")):
        username = unametxt.get()
        if db.check_uname(username): 
            filename = filetxt.get()
            filenamelower = filename.lower()
            #print(filenamelower)
            if att_sheet_methods.check_filename(username,filenamelower):
                error_sound()
                #print("Sheet name already exists")
                sheetname_exis_error()
            else:
                if att_sheet_methods.create_sheets(username,filename):
                    #print("File created Successfully")
                    sheet_created_successful()
                else:
                    error_sound()
                    #print("File DID NOT create Successfully")
                    sheet_creation_error()
        else:
            error_sound()
            #print("Username doesnot exist")
            uname_exis_error()
    else:
        error_sound()
        print("Fields are empty")
        #empty_fields_error()
        #input fields empty error
        #please fill all fields



# --------------- CLEARING_UNAME_FILENAME_OF_CREATE_SHEETS --------------- #    
def clear_sheets_func():
    unametxt.delete(first=0, last=30)
    filetxt.delete(first=0, last=30)



def create_sheets():
    createsheetstwindow = tk.Tk()
    createsheetstwindow.title("Create Attendance Sheets")
    createsheetstwindow.iconbitmap('project_images/AMS.ico')
    createsheetstwindow.geometry('1260x700')
    createsheetstwindow.configure(background='gainsboro')
    
    createsheetstlbl = tk.Label(createsheetstwindow, text="Create New Attendance Sheets", width=50, fg="black", bg="gainsboro", height=2, font=('calibri', 25, ' bold '))
    createsheetstlbl.place(x=285, y=100)
    
    #label & text box for user name
    global unametxt
    unamelbl = tk.Label(createsheetstwindow, text="Enter Username", width=20, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
    unamelbl.place(x=200, y=200)
    unametxt = tk.Entry(createsheetstwindow, width=20, fg="black", font=('calibri', 20))
    unametxt.place(x=550, y=210)
    
    
    #label & text box for csv file name
    global filetxt
    filelbl = tk.Label(createsheetstwindow, text="Enter Sheet Name", width=20, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
    filelbl.place(x=200, y=300)
    filetxt = tk.Entry(createsheetstwindow, width=20, fg="black", font=('calibri', 20))
    filetxt.place(x=550, y=310)    

    
    #button for creation of file
    createsheetstbtn = tk.Button(createsheetstwindow, text="Create", command=create_sheets_func, fg="white", bg="dim gray",
                        width=10, activebackground="Red", font=('calibri', 15, ' bold '))
    createsheetstbtn.place(x=700, y=400)
    
    
    #button for cleaing text fields
    clear_sheets = tk.Button(createsheetstwindow, text="Clear", command=clear_sheets_func, fg="white", bg="dim gray",
                        width=10, activebackground="Red", font=('calibri', 15, ' bold '))
    clear_sheets.place(x=900, y=400)
    
    createsheetstwindow.mainloop()










# ---------------GENERATE_ATTENDANCE_REPORT_OF_EXISTING_SHEETS_(SEPARATE_FOR_EVERY_INSTRUCTOR) --------------- #


# --------------- GENERATE_ATTENDANCE_REPORT --------------- #
def generate_attendance_report(sheetname, u):
    generatereportwindow = tk.Tk()
    generatereportwindow.title("Generate Attendance Report")
    generatereportwindow.iconbitmap('project_images/AMS.ico')
    generatereportwindow.geometry('1260x700')
    generatereportwindow.configure(background='gainsboro')
    
    regstudents = generate_report.reading_reg_students()
    #print(type(regstudents))
    #print(regstudents)
    
    regstudents2 = generate_report.checking_attendance_file(regstudents, sheetname, u)
    #print(type(regstudents2))
    #print(regstudents2)
    
    regstudentsset = set(regstudents2) #eliminating duplicates using set
    #print(type(regstudentsset))
    #print(regstudentsset)
    
    regstudentlist = list(regstudentsset) #type-casting from set back to list
    #print(type(regstudentlist))
    regstudentlist.sort() #sorting list in ascending order
    #print(regstudentlist)
    
    
    length = len(regstudentlist)   
    total = 32
    
    '''
    generatereportlabel = tk.Label(generatereportwindow, text="Attendance Report", width=50, fg="black", bg="gainsboro", height=2, font=('calibri', 25, ' bold '))
    generatereportlabel.place(x=285, y=100)
    '''
   
    #displaying attendance report on window
    
    Label1 = Label(generatereportwindow, text="Registration No", width=27, height=2, font=('calibri', 15, ' bold '))
    Label1.grid(row=0, column=0)
    Label2 = Label(generatereportwindow, text="Name", width=27, height=2, font=('calibri', 15, ' bold '))
    Label2.grid(row=0, column=1)
    Label3 = Label(generatereportwindow, text="Attendance (in No.)", width=27, height=2, font=('calibri', 15, ' bold '))
    Label3.grid(row=0, column=2)
    Label1 = Label(generatereportwindow, text="Attendance (in %age)", width=27, height=2, font=('calibri', 15, ' bold '))
    Label1.grid(row=0, column=3)
    Label1 = Label(generatereportwindow, text="Eligibilty for finals", width=27, height=2, font=('calibri', 15, ' bold '))
    Label1.grid(row=0, column=4)
    
    
    
    for i in range(0,length):
        Label(generatereportwindow, text = regstudentlist[i], width=27, height=2, font=('calibri', 15, ' bold ')).grid(row=i+1, column=0)
        
        name = student_csv_methods.return_name(regstudentlist[i]) #getting names to reg no
        
        Label(generatereportwindow, text = name, width=27, height=2, font=('calibri', 15, ' bold ')).grid(row=i+1, column=1)
        
        count = generate_report.counting_entries(regstudentlist[i], sheetname, u) #getting count of no of presents
        
        Label(generatereportwindow, text = count, width=27, height=2, font=('calibri', 15, ' bold ')).grid(row=i+1, column=2)
        
        percentage = int ( (count/total) * 100 ) #getting percentage of presents
        
        Label(generatereportwindow, text = percentage, width=27, height=2, font=('calibri', 15, ' bold ')).grid(row=i+1, column=3)
        
        if percentage >= 75: #eligility for finals
            Label(generatereportwindow, text = "Eligible", width=27, height=2, font=('calibri', 15, ' bold ')).grid(row=i+1, column=4)
        else:
            Label(generatereportwindow, text = "Not Eligible", width=27, height=2, font=('calibri', 15, ' bold ')).grid(row=i+1, column=4)
            
   
    #displaying attendance report on console
    
    '''
    for i in range(0,length):
        count = generate_report.counting_entries(regstudentlist[i])
        percentage = int ( (count/total) * 100 )
        print(f"Reg Number-{regstudentlist[i]} has {percentage}% attendance.")
        if percentage >= 75:
            print(f"Reg Number-{regstudentlist[i]} is eligible for final exams.")
        else:
            print(f"Reg Number-{regstudentlist[i]} is not eligible for final exams.")
        print()
    '''
        
    generatereportwindow.mainloop()
    

# --------------- PASSING_SHEET_NAME_FOR_GENERATE_ATTENDANCE_REPORT --------------- #
def gen_rep_get_btn_txt(n, u):
    btnpressed = (buttons[n])
    #print(btnpressed['text'])
    sheetname = btnpressed['text']
    #global sheetname_uname_manual
    #sheetname_uname_manual = [sheetname, u]
    #print(sheetname_uname_manual)
    generate_attendance_report(sheetname, u)


# --------------- SELECT_SHEET_FOR_GENERATE_REPORT_FUNCTION --------------- #
def select_sheet_gen_rep_func():
    if not unametxt.get()=="":
        u = unametxt.get()
        if db.check_uname(u):
            listoffiles = att_sheet_methods.return_listoffiles(u)
            length = len(listoffiles)
            if  length == 0:
                error_sound()
                #print("You don't have any Attendance Sheet.")
                no_att_sheet_error() # already defined in auto attendance
            else:
                #print(f"You have {length} Attendance Sheet(s).")
                
                #create a window for buttons
                btnswindow = tk.Tk()
                btnswindow.title("Attendance Sheets")
                btnswindow.iconbitmap('project_images/AMS.ico')
                btnswindow.configure(background='gainsboro')
                
                global buttons 
                buttons = []
                for i in range(length):
                    #fileno = str(i+1)
                    filename = listoffiles[i]
                    #fullname = fileno+"."+" " +filename
                    button = tk.Button(btnswindow, text = filename, command=partial(gen_rep_get_btn_txt, i, u), fg="white", bg="dim gray",
                                        width=25, activebackground="Red", font=('calibri', 15, 'bold'))
                    #button.place(x=550, y=i+200)
                    button.pack()
                    buttons.append(button)
                
                btnswindow.resizable(width=False, height=False)
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
        
    
# --------------- SELECT_SHEET_FOR_GENERATE_REPORT_WINDOW --------------- #
def select_sheet_gen_rep():
    global selectsheetgenrepwindow
    selectsheetgenrepwindow = tk.Tk()
    selectsheetgenrepwindow.title("Select Attendance Sheet")
    selectsheetgenrepwindow.iconbitmap('project_images/AMS.ico')
    selectsheetgenrepwindow.geometry('1260x700')
    selectsheetgenrepwindow.configure(background='gainsboro')
    
    selectsheetgenreplbl = tk.Label(selectsheetgenrepwindow, text="Select Sheet for Report Generation", width=75, fg="black", bg="gainsboro", height=2, font=('calibri', 25, ' bold '))
    selectsheetgenreplbl.place(x=100, y=100)
    
    #label & text box for user name
    global unametxt
    unamelbl = tk.Label(selectsheetgenrepwindow, text="Enter Username", width=20, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
    unamelbl.place(x=200, y=200)
    unametxt = tk.Entry(selectsheetgenrepwindow, width=20, fg="black", font=('calibri', 20))
    unametxt.place(x=550, y=210)

    
    #button for creation of file
    selectsheetgenrepbtn = tk.Button(selectsheetgenrepwindow, text="Next", command=select_sheet_gen_rep_func, fg="white", bg="dim gray",
                        width=10, activebackground="Red", font=('calibri', 15, ' bold '))
    selectsheetgenrepbtn.place(x=550, y=300)
    
    
    #button for cleaing text field
    clear_select_sheet = tk.Button(selectsheetgenrepwindow, text="Clear", command=clear_sheet_func, fg="white", bg="dim gray",
                        width=10, activebackground="Red", font=('calibri', 15, ' bold '))
    clear_select_sheet.place(x=750, y=300)
    

    selectsheetgenrepwindow.mainloop()
















# --------------- MANUAL_ATTENDANCE_ON_EXISTING_SHEETS_(SEPARATE_FOR_EVERY_INSTRUCTOR) --------------- #



# --------------- SREG_EXISTENCE_ERROR_FOR_SREG_CHECK_OF_MANUAL_ATTENDANCE --------------- #
def s_reg_exstnc_error_manual():
    global sregerrormanualE
    sregerrormanualE = tk.Tk()
    sregerrormanualE.geometry('330x100')
    sregerrormanualE.iconbitmap('project_images/AMS.ico')
    sregerrormanualE.title('Warning!')
    sregerrormanualE.configure(background='gainsboro')
    Label(sregerrormanualE, text='Student is not registered', fg='red', bg='gainsboro',
                      font=('calibri', 16, ' bold ')).pack()
    Button(sregerrormanualE, text='OK', command=exit_s_reg_exstnc_error_manual, fg="red", bg="gainsboro", width=9, height=1,
                         activebackground="Red", font=('calibri', 15, ' bold ')).place(x=90, y=50)
    sregerrormanualE.resizable(width=False, height=False)
    sregerrormanualE.mainloop()
    
def exit_s_reg_exstnc_error_manual():
    sregerrormanualE.destroy()



# --------------- SREG_CHECK_FOR_MANUAL_ATTENDANCE --------------- #
def s_reg():
    if(not(sregtxtmanual.get()=="")):
        try:
            sregtxtmanualvalue = int(sregtxtmanual.get())
            sregtxtmanualvalue = str(sregtxtmanualvalue)
            if(student_csv_methods.checking_reg(sregtxtmanualvalue)):
                name = student_csv_methods.return_name(sregtxtmanualvalue)
                #get_sheetname_&_uname
                sheetname = sheetname_uname_manual[0]
                #print(sheetname)
                u = sheetname_uname_manual[1]
                #print(u)
                if student_csv_methods.mark_auto_attendance(sregtxtmanualvalue, name, sheetname, u):
                    manualattendancewindow.destroy()
                    csvfile = "Instructors\\" + u + "\\" + sheetname
                    student_csv_methods.open_attendance_sheet(csvfile)
            else:
                error_sound()
                s_reg_exstnc_error_manual()
        except:
            #input integer error
            error_sound() 
            s_reg_input_error() #only numbers are allowed, defined for take_imgs
    else:
        print("Fields are empty")
        error_sound()
        #empty_fields_error()
        #input fields empty error
        #please fill all fields


# --------------- CLEARING_SREG_FOR_MANUAL_ATTENDANCE --------------- #
def clear_student_reg():
    sregtxtmanual.delete(first=0, last=30)


# --------------- TAKE MANUAL ATTENDANCE --------------- #
def take_manual_attendance():
    global manualattendancewindow
    manualattendancewindow = tk.Tk()
    manualattendancewindow.title("Manual Attendance")
    manualattendancewindow.iconbitmap('project_images/AMS.ico')
    manualattendancewindow.geometry('1260x700')
    manualattendancewindow.configure(background='gainsboro')
    
    manualattendancelabel = tk.Label(manualattendancewindow, text="Take Manual Attendance", width=50, fg="black", bg="gainsboro", height=2, font=('calibri', 25, ' bold '))
    manualattendancelabel.place(x=285, y=100)
    
    #label and text box for student reg no
    global sregtxtmanual
    sreglblmanual = tk.Label(manualattendancewindow, text="Enter Student Reg no", width=30, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
    sreglblmanual.place(x=200, y=300)
    sregtxtmanual = tk.Entry(manualattendancewindow, width=20, fg="black", font=('calibri', 20))
    sregtxtmanual.place(x=550, y=310)
    
    #button for checking reg if registered or not
    startimgs = tk.Button(manualattendancewindow, text="Mark Attendance", command=s_reg, fg="white", bg="dim gray",
                        width=15, activebackground="Red", font=('calibri', 15, ' bold '))
    startimgs.place(x=700, y=400)
    
    #button for clearing text fields
    clear_sreg = tk.Button(manualattendancewindow, text="Clear", command=clear_student_reg, fg="white", bg="dim gray",
                        width=5, activebackground="Red", font=('calibri', 15, ' bold '))
    clear_sreg.place(x=900, y=400)
    
    manualattendancewindow.mainloop()



# --------------- PASSING_SHEET_NAME_FOR_MANUAL_ATTENDANCE --------------- #
def man_get_btn_txt(n, u):
    btnpressed = (buttons[n])
    #print(btnpressed['text'])
    sheetname = btnpressed['text']
    global sheetname_uname_manual
    sheetname_uname_manual = [sheetname, u]
    #print(sheetname_uname_manual)
    take_manual_attendance()
            

# --------------- SELECT_SHEET_FOR_MANUAL_ATTENDANCE_FUNCTION --------------- #
def select_sheet_man_att_func():
    if not unametxt.get()=="":
        u = unametxt.get()
        if db.check_uname(u):
            listoffiles = att_sheet_methods.return_listoffiles(u)
            length = len(listoffiles)
            if  length == 0:
                error_sound()
                #print("You don't have any Attendance Sheet.")
                no_att_sheet_error() # already defined in auto attendance
            else:
                #print(f"You have {length} Attendance Sheet(s).")
                
                #create a window for buttons
                btnswindow = tk.Tk()
                btnswindow.title("Attendance Sheets")
                btnswindow.iconbitmap('project_images/AMS.ico')
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
                    
                btnswindow.resizable(width=False, height=False)
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
        

# --------------- SELECT_SHEET_FOR_MANUAL_ATTENDANCE_FUNCTION --------------- #
def select_sheet_man_att():
    global selectsheetmanattwindow
    selectsheetmanattwindow = tk.Tk()
    selectsheetmanattwindow.title("Select Attendance Sheet")
    selectsheetmanattwindow.iconbitmap('project_images/AMS.ico')
    selectsheetmanattwindow.geometry('1260x700')
    selectsheetmanattwindow.configure(background='gainsboro')
    
    selectsheetmanattlbl = tk.Label(selectsheetmanattwindow, text="Select Sheet for Manual Attendance", width=75, fg="black", bg="gainsboro", height=2, font=('calibri', 25, ' bold '))
    selectsheetmanattlbl.place(x=100, y=100)
    
    #label & text box for user name 
    global unametxt
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


















# --------------- AUTO_ATTENDANCE_ON_EXISTING_SHEETS_(SEPARATE_FOR_EVERY_INSTRUCTOR) --------------- #



# --------------- TRAINER_FILE_EXISTENCE_ERROR_FOR_TAKE_AUTO_ATTENDANCE --------------- #
def take_auto_attendance_error():
    global autoattendanceerror
    autoattendanceerror = tk.Tk()
    autoattendanceerror.geometry('330x100')
    autoattendanceerror.iconbitmap('project_images/AMS.ico')
    autoattendanceerror.title('Warning!')
    autoattendanceerror.configure(background='gainsboro')
    Label(autoattendanceerror, text='Error! First train model.', fg='red', bg='gainsboro',
                      font=('calibri', 16, ' bold ')).pack()
    Button(autoattendanceerror, text='OK', command=exit_take_auto_attendance_error, fg="red", bg="gainsboro", width=9, height=1,
                         activebackground="Red", font=('calibri', 15, ' bold ')).place(x=90, y=50)
    autoattendanceerror.resizable(width=False, height=False)
    autoattendanceerror.mainloop() 
    
def exit_take_auto_attendance_error():
    autoattendanceerror.destroy()


# --------------- TAKE_AUTO_ATTENDANCE --------------- #
def take_auto_attendance(sheetname, u):
    #opencv_methods.auto_attendance()
    if(not(opencv_methods.auto_attendance(sheetname, u))):
       #print("Trainer file DOES NOT exists")
       error_sound()
       take_auto_attendance_error()
    else:
        print("Trainer file exists")



# --------------- PASSING_SHEET_NAME_FOR_AUTO_ATTENDANCE_(take_auto_attendance(sheetname, u)) --------------- #
def auto_get_btn_txt(n, u):
    btnpressed = (buttons[n])
    #print(btnpressed['text'])
    sheetname = btnpressed['text']
    take_auto_attendance(sheetname, u)
  
        

# --------------- NO_ATT_SHEET_ERROR_FOR_AUTO_+_MANUAL_+_REPORT --------------- #              
def no_att_sheet_error():
    global noattsheeterror
    noattsheeterror = tk.Tk()
    noattsheeterror.geometry('350x100')
    noattsheeterror.iconbitmap('project_images/AMS.ico')
    noattsheeterror.title('Warning!')
    noattsheeterror.configure(background='gainsboro')
    Label(noattsheeterror, text="You don't have any Attendance Sheet.", fg='red', bg='gainsboro',
                      font=('calibri', 16, ' bold ')).pack()
    Button(noattsheeterror, text='OK', command=exit_no_att_sheet_error, fg="red", bg="gainsboro", width=9, height=1,
                         activebackground="Red", font=('calibri', 15, ' bold ')).place(x=120, y=50)
    noattsheeterror.resizable(width=False, height=False)
    noattsheeterror.mainloop() 
    
def exit_no_att_sheet_error():
    noattsheeterror.destroy()




# --------------- SELECT_SHEET_FOR_AUTO_ATTENDANCE_FUNCTION --------------- #
def select_sheet_auto_att_func():
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
                btnswindow.iconbitmap('project_images/AMS.ico')
                btnswindow.configure(background='gainsboro')
                
                global buttons 
                buttons = []
                for i in range(length):
                    #fileno = str(i+1)
                    filename = listoffiles[i]
                    #fullname = fileno+"."+" " +filename
                    button = tk.Button(btnswindow, text = filename, command=partial(auto_get_btn_txt, i, u), fg="white", bg="dim gray",
                                        width=25, activebackground="Red", font=('calibri', 15, 'bold'))
                    #button.place(x=550, y=i+200)
                    button.pack()
                    buttons.append(button)
                
                btnswindow.resizable(width=False, height=False)
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



# --------------- CLEARING_UNAME_FIELD_FOR_AUTO_+_MANUAL_+_REPORT --------------- #
def clear_sheet_func():
    unametxt.delete(first=0, last=30)




# --------------- SELECT_SHEET_FOR_AUTO_ATTENDANCE_WINDOW --------------- #
def select_sheet_auto_att():
    global selectsheetautoattwindow
    selectsheetautoattwindow = tk.Tk()
    selectsheetautoattwindow.title("Select Attendance Sheet")
    selectsheetautoattwindow.iconbitmap('project_images/AMS.ico')
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














# --------------- ON_CLOSING_INSTRUCTOR_PANEL_WINDOW --------------- #        
def on_closing_instwindow():
    error_sound()
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        instwindow.destroy()



# --------------- INSTRUCTOR_PANEL_WINDOW --------------- #
def instructor_panel():
    window.destroy()
    
    global instwindow
    instwindow = tk.Tk()
    instwindow.title("Instructor Panel")
    instwindow.iconbitmap('project_images/AMS.ico')
    instwindow.geometry('1260x700')
    instwindow.configure(background='gainsboro')
    
    instlabel = tk.Label(instwindow, text="Welcome to the Instructor Panel", width=50, fg="black", bg="gainsboro", height=2, font=('calibri', 25, ' bold '))
    instlabel.place(x=285, y=150)
    
    
    #undelining main heading (Panel Name)
    f = font.Font(instlabel, instlabel.cget("font"))
    f.configure(underline=True)
    instlabel.configure(font=f)
    
    
    #logo Label
    logo = Image.open("project_images/fyp-logo-1.png") 
    logo = logo.resize((210, 210), Image.ANTIALIAS)
    logo1 = ImageTk.PhotoImage(logo)
    logolabel = tk.Label(image=logo1, bg="gainsboro").place(x=115,y=25)
    
    
    checkreg = tk.Button(instwindow, text="Check Registerations", command=check_reg, fg="white", bg="dim gray", width=20, height=3,
                   activebackground="Red", font=('calibri', 15, ' bold '))
    checkreg.place(x=100, y=350)
    
    takeautoattendance = tk.Button(instwindow, text="Take Auto Attendance", command=select_sheet_auto_att, fg="white", bg="dim gray", width=20, height=3,
                        activebackground="Red", font=('calibri', 15, ' bold '))
    takeautoattendance.place(x=400, y=350)
    
    takemanualattendance = tk.Button(instwindow, text="Take Manual Attendance", fg="white", command=select_sheet_man_att, bg="dim gray", width=22, height=3,
                         activebackground="Red", font=('calibri', 15, ' bold '))
    takemanualattendance.place(x=700, y=350)
    
    generatereport = tk.Button(instwindow, text="Generate Attendance Report", fg="white", command=select_sheet_gen_rep, bg="dim gray", width=25, height=3,
                         activebackground="Red", font=('calibri', 15, ' bold '))
    generatereport.place(x=1000, y=350)
    
    
    createsheets = tk.Button(instwindow, text="Create Attendance Sheets", command=create_sheets, fg="white", bg="dim gray", width=25, height=3,
                             activebackground="Red", font=('calibri', 15, ' bold '))
    createsheets.place(x=550, y=475)
    
    
    #instructor_image label
    instlogo = Image.open("project_images/inst_1.png") 
    instlogo = instlogo.resize((100, 100), Image.ANTIALIAS)
    instlogo1 = ImageTk.PhotoImage(instlogo)
    instlogolabel = tk.Label(image=instlogo1, bg="gainsboro").place(x=1225,y=35)
    
    
    
    changepassinst = tk.Button(instwindow, text="Change Password", fg="white", command=change_pass_inst, bg="dim gray", width=18, 
                         activebackground="Red", font=('calibri', 10, ' bold '))
    changepassinst.place(x=1190, y=140)
    
    
    
    logoutinst = tk.Button(instwindow, text="Log Out", fg="white", command=log_out_inst, bg="dim gray", width=18, 
                         activebackground="Red", font=('calibri', 10, ' bold '))
    logoutinst.place(x=1190, y=175)
    
    
    #copyrights label
    proj_cr = tk.Label(instwindow, text="Copyright © 2020, All Rights Reserved.", width=140, fg="white", bg="dim gray", height=2, font=('calibri', 15, ' bold '))
    proj_cr.place(x=0, y=651)
    

    instwindow.protocol("WM_DELETE_WINDOW", on_closing_instwindow)
    instwindow.mainloop()
























# --------------- LOG_OUT_ADMIN --------------- #
def log_out_admin():
    adminwindow.destroy()
    main_window()



# --------------- TRAIN_MODEL_SUCCESSFULL_SCREEN --------------- #
def train_model_successful():
    global trainmodelsuccessful
    trainmodelsuccessful = tk.Tk()
    trainmodelsuccessful.geometry('600x100')
    trainmodelsuccessful.iconbitmap('project_images/AMS.ico')
    trainmodelsuccessful.title('Success')
    trainmodelsuccessful.configure(background='gainsboro')
    Label(trainmodelsuccessful, text='Model is successfully trained for the provided dataset.',
          fg='green', bg='gainsboro', font=('calibri', 16, ' bold ')).pack()
    Button(trainmodelsuccessful, text='OK', command=exit_train_model_successful, fg="green", bg="gainsboro", width=9, height=1,
          activebackground="Green", font=('calibri', 15, ' bold ')).place(x=215, y=50)
    trainmodelsuccessful.resizable(width=False, height=False)
    trainmodelsuccessful.mainloop()
          
def exit_train_model_successful():
    trainmodelsuccessful.destroy()





# --------------- TRAIN_MODEL_ERROR_SCREEN --------------- #
def train_model_error():
    global trainmodelerror
    trainmodelerror = tk.Tk()
    trainmodelerror.geometry('330x100')
    trainmodelerror.iconbitmap('project_images/AMS.ico')
    trainmodelerror.title('Warning!')
    trainmodelerror.configure(background='gainsboro')
    Label(trainmodelerror, text='Error! First take images.', fg='red', bg='gainsboro',
                      font=('calibri', 16, ' bold ')).pack()
    Button(trainmodelerror, text='OK', command=exit_train_model_error, fg="red", bg="gainsboro", width=9, height=1,
                         activebackground="Red", font=('calibri', 15, ' bold ')).place(x=90, y=50)
    trainmodelerror.resizable(width=False, height=False)
    trainmodelerror.mainloop() 
    
def exit_train_model_error():
    trainmodelerror.destroy()




# --------------- TRAIN_MODEL --------------- #
def train_model():
    if(opencv_methods.train_through_dataset()):
        #print("Successfully trained model")
        train_model_successful()
        #suucessfull training screen
    else:
        #print("Error in training the model")
        #error in training screen
        error_sound()
        train_model_error()








# --------------- TAKE_IMAGES_SUCCESSFULL_SCREEN --------------- #
def take_imgs_successful():
    global takeimgssuccessful
    takeimgssuccessful = tk.Tk()
    takeimgssuccessful.geometry('600x100')
    takeimgssuccessful.iconbitmap('project_images/AMS.ico')
    takeimgssuccessful.title('Success')
    takeimgssuccessful.configure(background='gainsboro')
    Label(takeimgssuccessful, text='Student registered successfully. Now train the model.',
          fg='green', bg='gainsboro', font=('calibri', 16, ' bold ')).pack()
    Button(takeimgssuccessful, text='OK', command=exit_take_imgs_successful, fg="green", bg="gainsboro", width=9, height=1,
          activebackground="Green", font=('calibri', 15, ' bold ')).place(x=215, y=50)
    takeimgssuccessful.resizable(width=False, height=False)
    takeimgssuccessful.mainloop()
      
def exit_take_imgs_successful():
    takeimgssuccessful.destroy()




# --------------- SREG_INPUT_ERROR_FOR_SREG_CHECK_OF_TAKE_IMAGES_(USED_MULTIPLE_TIMES) --------------- # 
def s_reg_input_error():
    global sregerrorI
    sregerrorI = tk.Tk()
    sregerrorI.geometry('330x100')
    sregerrorI.iconbitmap('project_images/AMS.ico')
    sregerrorI.title('Warning!')
    sregerrorI.configure(background='gainsboro')
    Label(sregerrorI, text='Only numbers are allowed in Reg No.', fg='red', bg='gainsboro',
                      font=('calibri', 16, ' bold ')).pack()
    Button(sregerrorI, text='OK', command=exit_s_reg_input_error, fg="red", bg="gainsboro", width=9, height=1,
                         activebackground="Red", font=('calibri', 15, ' bold ')).place(x=90, y=50)
    sregerrorI.resizable(width=False, height=False)
    sregerrorI.mainloop()
    
def exit_s_reg_input_error():
    sregerrorI.destroy()





# --------------- SREG_EXISTENCE_ERROR_FOR_SREG_CHECK_OF_TAKE_IMAGES --------------- # 
def s_reg_exstnc_error():
    global sregerrorE
    sregerrorE = tk.Tk()
    sregerrorE.geometry('330x100')
    sregerrorE.iconbitmap('project_images/AMS.ico')
    sregerrorE.title('Warning!')
    sregerrorE.configure(background='gainsboro')
    Label(sregerrorE, text='Student is Already Registered', fg='red', bg='gainsboro',
                      font=('calibri', 16, ' bold ')).pack()
    Button(sregerrorE, text='OK', command=exit_s_reg_exstnc_error, fg="red", bg="gainsboro", width=9, height=1,
                         activebackground="Red", font=('calibri', 15, ' bold ')).place(x=90, y=50)
    sregerrorE.resizable(width=False, height=False)
    sregerrorE.mainloop()
    
def exit_s_reg_exstnc_error():
    sregerrorE.destroy()





# --------------- SREG_CHECK_FOR_TAKE_IMAGES --------------- # 
def s_reg_check():
    if(not(sregtxt.get()=="" or snametxt.get() == "")):
        try:
            sreg = int(sregtxt.get())
            sreg=str(sreg)
            if(student_csv_methods.checking_reg(sreg)):
                error_sound()
                s_reg_exstnc_error()
            else:
                #print("Student does not exist in csv file")
                sname = snametxt.get()
                #take images
                if(opencv_methods.take_imgs_opencv(sreg,sname)):
                    #registeration of student
                    student_csv_methods.registering_reg(sreg,sname)
                    #print("Student registered")
                    take_imgs_successful()
                    #screen to tell successful registrartion of student
                    #now train the model for the student
                        #ok to exit the screen
                else:
                    error_sound()
                    print("error in taking imgs")
        except:
            #input integer error
            error_sound() 
            s_reg_input_error()
    else:
        print("Fields are empty")
        error_sound()
        #empty_fields_error()
        #input fields empty error
        #please fill all fields





# --------------- CLEARING_SNAME_&_SREG_FOR_TAKE_IMAGES --------------- #    
def clear_student_credentials():
    snametxt.delete(first=0, last=30)
    sregtxt.delete(first=0, last=30)
    



# --------------- TAKE_IMAGES --------------- #
def take_imgs():
    takeimgswindow = tk.Tk()
    takeimgswindow.title("Take Images")
    takeimgswindow.iconbitmap('project_images/AMS.ico')
    takeimgswindow.geometry('1260x700')
    takeimgswindow.configure(background='gainsboro')
    
    takeimgslabel = tk.Label(takeimgswindow, text="Register student & Take Images", width=50, fg="black", bg="gainsboro", height=2, font=('calibri', 25, ' bold '))
    takeimgslabel.place(x=285, y=100)
    
    #label & text box for studentname
    global snametxt
    snamelbl = tk.Label(takeimgswindow, text="Enter Student Name", width=30, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
    snamelbl.place(x=200, y=200)
    snametxt = tk.Entry(takeimgswindow, width=20,  fg="black", font=('calibri', 20))
    snametxt.place(x=550, y=210)
    
    #label & text box for studentregno
    global sregtxt
    sreglbl = tk.Label(takeimgswindow, text="Enter Student Reg no", width=30, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
    sreglbl.place(x=200, y=300)
    sregtxt = tk.Entry(takeimgswindow, width=20, fg="black", font=('calibri', 20))
    sregtxt.place(x=550, y=310)
    
    #button for check
    startimgs = tk.Button(takeimgswindow, text="Start", command=s_reg_check, fg="white", bg="dim gray",
                        width=10, activebackground="Red", font=('calibri', 15, ' bold '))
    startimgs.place(x=700, y=400)
    
    #button for clearing text fields
    clear_sfields = tk.Button(takeimgswindow, text="Clear", command=clear_student_credentials, fg="white", bg="dim gray",
                        width=5, activebackground="Red", font=('calibri', 15, ' bold '))
    clear_sfields.place(x=900, y=400)
    
    takeimgswindow.mainloop()





# --------------- ON_CLOSING_ADMIN_PANEL_WINDOW --------------- #
def on_closing_adminwindow():
    error_sound()
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        adminwindow.destroy()




# --------------- ADMIN__PANEL_WINDOW --------------- # 
def admin_panel():
    window.destroy()
    
    global adminwindow
    adminwindow = tk.Tk()
    adminwindow.title("Admin Panel")
    adminwindow.iconbitmap('project_images/AMS.ico')
    adminwindow.geometry('1260x700')
    adminwindow.configure(background='gainsboro')
    
    
    #logo Label
    logo = Image.open("project_images/fyp-logo-1.png") 
    logo = logo.resize((210, 210), Image.ANTIALIAS)
    logo1 = ImageTk.PhotoImage(logo)
    logolabel = tk.Label(image=logo1, bg="gainsboro").place(x=115,y=25)
    
    
    adminlabel = tk.Label(adminwindow, text="Welcome to the Admin Panel", width=50, fg="black", bg="gainsboro", height=2, font=('calibri', 25, ' bold '))
    adminlabel.place(x=285, y=100)
    
    #undelining main heading (Panel Name)
    f = font.Font(adminlabel, adminlabel.cget("font"))
    f.configure(underline=True)
    adminlabel.configure(font=f)    
    
    
    checkreg = tk.Button(adminwindow, text="Check Registerations", command=check_reg, fg="white", bg="dim gray", width=20, height=3,
                   activebackground="Red", font=('calibri', 15, ' bold '))
    checkreg.place(x=300, y=300)
    
    takeimgs = tk.Button(adminwindow, text="Take Images", command=take_imgs, fg="white", bg="dim gray", width=20, height=3,
                        activebackground="Red", font=('calibri', 15, ' bold '))
    takeimgs.place(x=600, y=300)
    
    trainmodel = tk.Button(adminwindow, text="Train Model", fg="white", command=train_model, bg="dim gray", width=20, height=3,
                         activebackground="Red", font=('calibri', 15, ' bold '))
    trainmodel.place(x=900, y=300)
    
    
    #admin_image label
    admlogo = Image.open("project_images/adm_1.png") 
    admlogo = admlogo.resize((100, 100), Image.ANTIALIAS)
    admlogo1 = ImageTk.PhotoImage(admlogo)
    admlogolabel = tk.Label(image=admlogo1, bg="gainsboro").place(x=1200,y=40)
    
    
    logoutadmin = tk.Button(adminwindow, text="Log Out", fg="white", command=log_out_admin, bg="dim gray", width=9, 
                         activebackground="Red", font=('calibri', 10, ' bold '))
    logoutadmin.place(x=1215, y=140)
    
    
    #copyrights label
    proj_cr = tk.Label(adminwindow, text="Copyright © 2020, All Rights Reserved.", width=140, fg="white", bg="dim gray", height=2, font=('calibri', 15, ' bold '))
    proj_cr.place(x=0, y=651)
    
    
    adminwindow.protocol("WM_DELETE_WINDOW", on_closing_adminwindow)
    adminwindow.mainloop()






















# --------------- SEARCH_BY_REG_NO ---------------- #
def search_by_reg():
    if not searchbyregtxt.get() == "":
        try:
            searchbyregvalue = int(searchbyregtxt.get())
            searchbyregvalue = str(searchbyregvalue)
            if student_csv_methods.checking_reg(searchbyregvalue):
                name = student_csv_methods.return_name(searchbyregvalue) #getting names to reg no
                #print("Student is registered!")
                
                #displaying reg and name on window

                Label1 = Label(checkregwindow, text="Registration No", width=35, height=2, font=('calibri', 15, ' bold '))
                Label1.place(x=550 , y=300)
                Label1 = Label(checkregwindow, text="Name", width=35, height=2, font=('calibri', 15, ' bold '))
                Label1.place(x=850 , y=300)
                
                Label(checkregwindow, text = searchbyregvalue, width=35, height=2, font=('calibri', 15, ' bold ')).place(x=550 , y=350)
                Label(checkregwindow, text = name, width=35, height=2, font=('calibri', 15, ' bold ')).place(x=850 , y=350)
                
                
            else:
                #print("Student is not registered!")
                
                Label1 = Label(checkregwindow, text="Student is not registered yet.", width=65, height=2, font=('calibri', 15, ' bold '))
                Label1.place(x=550 , y=300)
                Label1 = Label(checkregwindow, text="", width=5, height=2, font=('calibri', 15, ' bold '))
                Label1.place(x=1150 , y=300)
                
                Label(checkregwindow, text = "", width=35, height=2, font=('calibri', 15, ' bold ')).place(x=550 , y=350)
                Label(checkregwindow, text = "", width=35, height=2, font=('calibri', 15, ' bold ')).place(x=850 , y=350)
                
        except:
            #input integer error
            error_sound() 
            s_reg_input_error() #only numbers are allowed, defined for take_imgs
    else:
        print("Field is empty")
        error_sound()
        #empty_fields_error()
        #input fields empty error
        #please fill all fields
 
         
        
# --------------- CLEAR_SEARCH_BY_REG_NO ---------------- #        
def clear_search_by_reg():
    searchbyregtxt.delete(first=0, last=30)
    
    

# --------------- CHECK_REGISTRATIONS_(COMMON_FOR_ADMIN_&_INSTRUCTOR) ---------------- #
def check_reg():
    global checkregwindow
    checkregwindow = tk.Tk()
    checkregwindow.title("Registered Students")
    checkregwindow.iconbitmap('project_images/AMS.ico')
    checkregwindow.geometry('1260x700')
    checkregwindow.configure(background='gainsboro')
  
    
    #vertical line separating registered students and search students
    '''
    c = Canvas(checkregwindow, width=1370, height=720, bg='gainsboro', highlightbackground='gainsboro')
    #c.pack()
    c.create_line(685, 150, 685, 570, fill="black", width=2)
    '''
     
    
    '''
    checkreglbl1 = tk.Label(checkregwindow, text="List of Registered Students", width=50, fg="black", bg="gainsboro", height=2, font=('calibri', 25, ' bold '))
    checkreglbl1.place(x=50, y=100)
    '''
    
    
    csvfile = 'RegisteredStudents.csv'
    with open(csvfile, "r", newline="") as file:
        reader = csv.reader(file)
        r = 0
        for col in reader:
            c = 0
            for row in col:
                # i've added some styling
                label = tk.Label(checkregwindow, width=20, height=1, fg="black", font=('calibri', 15, ' bold '),
                                                      bg="gainsboro", text=row, relief=tk.RIDGE)
                label.grid(row=r, column=c)
                c += 1
            r += 1
            
            
     
    '''
    checkreglbl2 = tk.Label(checkregwindow, text="Search from the Provided List", width=50, fg="black", bg="gainsboro", height=2, font=('calibri', 25, ' bold '))
    checkreglbl2.place(x=100, y=100)
    '''
    
    
    
    global searchbyregtxt
    searchbyreglbl = tk.Label(checkregwindow, text="Enter Student Reg no", width=30, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
    searchbyreglbl.place(x=500, y=100)
    searchbyregtxt = tk.Entry(checkregwindow, width=20, fg="black", font=('calibri', 20))
    searchbyregtxt.place(x=850, y=100)
    
    searchbyregbtn = tk.Button(checkregwindow, text="Search by Reg No.", command=search_by_reg, fg="white", bg="dim gray", 
                            width=20, activebackground="Red", font=('calibri', 15, ' bold '))
    searchbyregbtn.place(x=700, y=200)
    
    searchbyregclear = tk.Button(checkregwindow, text="Clear", command=clear_search_by_reg, fg="white", bg="dim gray", 
                            width=5, activebackground="Red", font=('calibri', 15, ' bold '))
    searchbyregclear.place(x=950, y=200)
    
     
    checkregwindow.mainloop()



# --------------- SIGN_IN_ERROR --------------- #      
def signin_error():
    global signinerror
    signinerror = tk.Tk()
    signinerror.geometry('330x100')
    signinerror.iconbitmap('project_images/AMS.ico')
    signinerror.title('Warning!')
    signinerror.configure(background='gainsboro')
    Label(signinerror, text='Please enter valid credentials.', fg='red', bg='gainsboro',
                      font=('calibri', 16, ' bold ')).pack()
    Button(signinerror, text='OK', command=exit_signin_error, fg="red", bg="gainsboro", width=9, height=1,
                         activebackground="Red", font=('calibri', 15, ' bold ')).place(x=120, y=50)
    signinerror.resizable(width=False, height=False)
    signinerror.mainloop()


def exit_signin_error():
    signinerror.destroy()



# --------------- SIGN_IN --------------- #
def sign_in():
    if(not(txt1.get()=="" or txt2.get()=="")):
        uname = txt1.get()
        pw = txt2.get()
        if(db.sign_in(uname,pw)=='admin'):
            #print("Is an Admin")
            admin_panel()
        elif(db.sign_in(uname,pw)=='instructor'):
            #print("Is an Instructor")
            instructor_panel()
        else:
            #print("ERROR!")
            error_sound()
            signin_error()
    else:
        print("Fields are empty")
        error_sound()
        #empty_fields_error()
        #input fields empty error
        #please fill all fields


    
# --------------- SIGN_UP_SUCCESSFUL --------------- #
def signup_successful():
    clear_credentials_signup()
    global signupsuccessful
    signupsuccessful = tk.Tk()
    signupsuccessful.geometry('620x100')
    signupsuccessful.iconbitmap('project_images/AMS.ico')
    signupsuccessful.title('Success')
    signupsuccessful.configure(background='gainsboro')
    Label(signupsuccessful, text='Your account is created suucessfully, now sign in to access your portal.',
          fg='green', bg='gainsboro', font=('calibri', 16, ' bold ')).pack()
    Button(signupsuccessful, text='OK', command=exit_signup_successful, fg="green", bg="gainsboro", width=9, height=1,
          activebackground="Green", font=('calibri', 15, ' bold ')).place(x=235, y=50)
    signupsuccessful.resizable(width=False, height=False)
    signupsuccessful.mainloop()
      
def exit_signup_successful():
    signupsuccessful.destroy()
    


# --------------- SIGN_UP_ERROR --------------- #
def signup_error():
    global signuperror
    signuperror = tk.Tk()
    signuperror.geometry('330x100')
    signuperror.iconbitmap('project_images/AMS.ico')
    signuperror.title('Warning!')
    signuperror.configure(background='gainsboro')
    Label(signuperror, text='Username Already Exists!', fg='red', bg='gainsboro',
                      font=('calibri', 16, ' bold ')).pack()
    Button(signuperror, text='OK', command=exit_signup_error, fg="red", bg="gainsboro", width=9, height=1,
                         activebackground="Red", font=('calibri', 15, ' bold ')).place(x=90, y=50)
    signuperror.resizable(width=False, height=False)
    signuperror.mainloop()


def exit_signup_error():
    signuperror.destroy()    

  
    
# --------------- SIGN_UP --------------- #
def sign_up():
    if(not(txt3.get()=="" or txt4.get()=="")):
        uname = txt3.get()
        if db.check_uname(uname):
            #print("Username already Exists in Database")
            error_sound()
            signup_error()
        else:
            pw = txt4.get()
            if db.sign_up(uname,pw):
               #print("Your account is created, now signin.")
               os.makedirs(f'./Instructors/{uname}')
               signup_successful()          
    else:
        print("Fields are empty")
        error_sound()
        #empty_fields_error()
        #input fields empty error
        #please fill all fields



# --------------- ERROR_SOUND --------------- #
def error_sound(): 
    winsound.Beep(500, 250)
  
    

# --------------- EMPTY_FIELDS_ERROR --------------- #
def empty_fields_error():
    #i think that error sound is enough when fields are empty.
    pass


# --------------- CLEARING_UNAME_&_UPASS - SIGN_UP (txt3, txt4) --------------- #
def clear_credentials_signup():
    txt3.delete(first=0, last=30)
    txt4.delete(first=0, last=30)


# --------------- CLEARING_UNAME_&_UPASS - SIGN_IN (txt1, txt2) --------------- #
def clear_credentials_signin():
    txt1.delete(first=0, last=30)
    txt2.delete(first=0, last=30)



# --------------- ON_CLOSING_MAIN_WINDOW --------------- #
def on_closing():
    error_sound()
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()




# --------------- MAIN_WINDOW --------------- #
def main_window():
    global window
    window = tk.Tk()
    window.title("AAUFR-Automatic Attendance Using Facial Recognition")
    window.iconbitmap('project_images/AMS.ico')
    window.geometry('1260x700')
    window.configure(background='gainsboro')
      
    
    
    #vertical line separating signup & signin
    c = Canvas(window, width=1370, height=720, bg='gainsboro', highlightbackground='gainsboro')
    c.pack()
    c.create_line(685, 300, 685, 610, fill="black", width=2)
    
    
    
    #logo Label
    logo = Image.open("project_images/fyp-logo-2.png") 
    logo = logo.resize((190, 190), Image.ANTIALIAS)
    logo1 = ImageTk.PhotoImage(logo)
    logolabel = tk.Label(image=logo1, bg="gainsboro").place(x=125,y=25)
    
    
    #project-name label
    proj_lbl = tk.Label(window, text="AUTOMATIC ATTENDANCE USING FACIAL RECOGNITION", width=50, fg="black", bg="gainsboro", height=2, font=('calibri', 25, ' bold '))
    proj_lbl.place(x=285, y=80)
    
    #undelining main heading (Project Name)
    f = font.Font(proj_lbl, proj_lbl.cget("font"))
    f.configure(underline=True)
    proj_lbl.configure(font=f)
    
        
    #signup label
    signup_lbl = tk.Label(window, text="Don't have an account? Sign up Here", width=35, fg="black", bg="gainsboro", height=2, font=('calibri', 25, ' bold '))
    signup_lbl.place(x=65, y=225)
    
    
    #label & text box for uname - signup
    global txt3
    lbl3 = tk.Label(window, text="Enter Username", width=20, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
    lbl3.place(x=35, y=350)
    txt3 = tk.Entry(window, width=20,  fg="black", font=('calibri', 20))
    txt3.place(x=285, y=360)
    
    #label & text box for pw - signup
    global txt4
    lbl4 = tk.Label(window, text="Enter Password", width=20, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
    lbl4.place(x=35, y=425)
    txt4 = tk.Entry(window, width=20, show='*',  fg="black", font=('calibri', 20))
    txt4.place(x=285, y=435)
    
    #button for signup - signup
    signup = tk.Button(window, text="Sign up", command=sign_up, fg="white", bg="dim gray",
                        width=10, activebackground="Red", font=('calibri', 15, ' bold '))
    signup.place(x=235, y=525)
    
    #button for clearing text fields - signup
    clear_signup = tk.Button(window, text="Clear", command=clear_credentials_signup, fg="white", bg="dim gray",
                        width=5, activebackground="Red", font=('calibri', 15, ' bold '))
    clear_signup.place(x=435, y=525)
    
    
    
    #signin label
    signin_lbl = tk.Label(window, text="Have an account? Sign in Here", width=30, fg="black", bg="gainsboro", height=2, font=('calibri', 25, ' bold '))
    signin_lbl.place(x=760, y=225)
    
    
    #label & text box for uname - signin
    global txt1
    lbl1 = tk.Label(window, text="Enter Username", width=20, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
    lbl1.place(x=700, y=350)
    txt1 = tk.Entry(window, width=20,  fg="black", font=('calibri', 20))
    txt1.place(x=950, y=360)
    
    #label & text box for pw - signin
    global txt2
    lbl2 = tk.Label(window, text="Enter Password", width=20, fg="black", bg="gainsboro", height=2, font=('calibri', 15, ' bold '))
    lbl2.place(x=700, y=425)
    txt2 = tk.Entry(window, width=20, show='*',  fg="black", font=('calibri', 20))
    txt2.place(x=950, y=435)
    
    #button for signin - signin
    signin = tk.Button(window, text="Sign in", command=sign_in, fg="white", bg="dim gray",
                        width=10, activebackground="Red", font=('calibri', 15, ' bold '))
    signin.place(x=900, y=525)
    
    #button for clearing text fields - signin
    clear_signin = tk.Button(window, text="Clear", command=clear_credentials_signin, fg="white", bg="dim gray",
                        width=5, activebackground="Red", font=('calibri', 15, ' bold '))
    clear_signin.place(x=1100, y=525)
    
    
    #copyrights label
    proj_cr = tk.Label(window, text="Copyright © 2020, All Rights Reserved.", width=140, fg="white", bg="dim gray", height=2, font=('calibri', 15, ' bold '))
    proj_cr.place(x=0, y=651)
    
    
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
   
    
   
main_window()