# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:06:56 2020

@author: Laraib
"""
import os
import csv



# --------------- NEW_SHEET_CREATION --------------- #
def create_sheets(username, filename):
    filename = filename +".csv"
    filename = "Instructors/" + username + '/' + filename
    #print(filename)
    flag = None
    with open(filename, "w", newline="") as file:
        content = csv.writer(file)
        try:
            content.writerow(['Reg_no', 'Name', 'Date', 'Time', 'Attendance'])
            #print("File created successfully")
            flag = True
        except Exception:
            #print("File DID NOT create successfully")
            flag = False
    return flag
#create_sheets("mona", "f16B")





# --------------- CHECKING_FOR_NOT_TO_DUPLICATE_FILE_NAME --------------- #
def check_filename(username, filename):
    flag = None
    filename = filename + ".csv"
    dirName = "./Instructors/" + username
    # Get the list of all files in directory tree at given path
    listOfFiles = os.listdir(dirName)
    #print(len(listOfFiles))
    #rint(listOfFiles)
    #print(filename)
    
    for f in listOfFiles:
        if filename == f.lower():
            flag = True
            #print("File Exists")
        else:
            flag = False
            #print("File Does not Exist")
        if(flag):
                break
    return flag
#check_filename("mona", "f16b.csv")





# --------------- CHECKING_IF_THERE_IS_ANY_FILE_IN_INSTRUCTOR'S_FOLDER_OR_NOT --------------- #
def return_listoffiles(uname):
    dirName = "./Instructors/" + uname
    # Get the list of all files in directory tree at given path
    listOfFiles = os.listdir(dirName)
    return listOfFiles


