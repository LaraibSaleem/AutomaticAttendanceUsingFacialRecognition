# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:19:18 2020

@author: Laraib
"""
import csv
from datetime import date
from datetime import datetime
import os

'''
def checking_reg(r):
    flag = False
    with open("RegisteredStudents.csv", "r", newline="") as file:
        content = csv.reader(file)
        for c in content:
            if(r == c[0]):
               flag = True 
    return flag   
'''        



# --------------- CHECKING_IF_REG_EXISTS --------------- #
def checking_reg(regnum):
    flag = None
    with open("RegisteredStudents.csv", "r", newline="") as file:
        content = csv.reader(file)
        next(content, None) #skips header
        for c in content:
            if(regnum == c[0]):
                #print("condition satisfied")
                flag = True
            else:
                #print("condition NOT satisfied")
                flag = False
            if(flag):
                break
            #break
    return flag
#checking_reg('2')




# --------------- REGISTERING_NEW_STUDENT --------------- #
def registering_reg(regnum,name):
    flag = None
    with open("RegisteredStudents.csv", "a", newline="") as file:
        content = csv.writer(file)
        try:
            content.writerow([regnum,name])
            #print("Student registered successfully")
            flag = True
        except Exception:
            #print("Student DID NOT register")
            flag = False
    return flag
#registering_reg('4','Student 4')




# --------------- RETURNING_NAME_TO_A_REG --------------- #
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



# --------------- MARKING_ATTENDANCE --------------- #
def mark_auto_attendance(regno,name,sheetname,u):
    flag = None
    today = date.today()
    d = today.strftime("%d-%m-%Y")
    now = datetime.now()
    t = now.strftime("%I:%M %p")
    csvfile = "./Instructors/" + u + "/"+ sheetname
    with open(csvfile, "a", newline="") as file:
        content = csv.writer(file)
        try:
            content.writerow([regno,name,d,t,'p'])
            #print("Attendance Marked Successfully")
            flag = True
        except Exception: 
            #print("Attendance IS NOT Marked Successfully")
            flag = False
    return flag
#mark_auto_attendance('4',"Student 4")




# --------------- OPENING_EXCEL_SHEET --------------- #
def open_attendance_sheet(csvfile):
    os.startfile(csvfile)
#open_attendance_sheet()



'''
def attendance_sheet_making():
    with open("StudentAttendance.csv", "w", newline="") as file:
        content = csv.writer(file)
        content.writerow(["Reg_No","Name", "Date", "Time", "Attendance"])
        print("Attendance sheet made successfully")        
#attendance_sheet_making()    
'''
