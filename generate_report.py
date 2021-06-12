# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:04:40 2020

@author: Laraib
"""
 
import csv



# --------------- READING_REGISTERED_STUDENTS_IN_A_LIST --------------- #
def reading_reg_students():
    regstudents =[]
    with open("RegisteredStudents.csv", "r", newline="") as file:
        content = csv.reader(file)
        next(content, None) #skips header
        for c in content:
            regstudents.append(c[0])
    return regstudents
#reading_reg_students()


# --------------- CHECKING_IF_THE_LIST_NAMES_EXIST_IN_CSV_FILE_OR_NOT --------------- #
def checking_attendance_file(regstudents, sheetname, u):
    csvfile = "./Instructors/" + u + "/"+ sheetname
    regstudents2 =[]
    with open(csvfile, "r", newline="") as file:
        content = csv.reader(file)
        next(content, None) #skips header
        for c in content:
            if c[0] in regstudents:
                regstudents2.append(c[0])     
    return regstudents2
#regstudents = ['1', '2', '3']
#checking_attendance_file(regstudents)


# --------------- COUNTING_ENTRIES_IN_ATTENDANCE_SHEET --------------- #
def counting_entries(regnum ,sheetname, u):
    csvfile = "./Instructors/" + u + "/"+ sheetname
    count = 0
    with open(csvfile, "r", newline="") as file:
        content = csv.reader(file)
        next(content, None) #skips header
        for c in content:
            if(regnum == c[0]):
                count +=1
    return count



'''
regstudents = reading_reg_students()
#print(type(regstudents))
print(regstudents)

regstudents2 = checking_attendance_file(regstudents)
#print(type(regstudents2))
print(regstudents2)

regstudentsset = set(regstudents2) #eliminating duplicates using set
#print(type(regstudentsset))
print(regstudentsset)

regstudentlist = list(regstudentsset) #type-casting from set back to list
#print(type(regstudentlist))
regstudentlist.sort() #sorting list in ascending order
print(regstudentlist)


length = len(regstudentlist)


total = 32
for i in range(0,length):
    count = counting_entries(regstudentlist[i])
    percentage = int ( (count/total) * 100 )
    print(f"Reg Number-{regstudentlist[i]} has {percentage}% attendance.")
    if percentage >= 75:
        print(f"Reg Number-{regstudentlist[i]} is eligible for final exams.")
    else:
        print(f"Reg Number-{regstudentlist[i]} is not eligible for final exams.")
    print()
'''








