# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:28:13 2020

@author: Laraib
"""

import cv2
import os
import numpy as np
from PIL import Image
#importing student_csv_methods.py
import student_csv_methods




# --------------- ACQUIRING_IMAGES --------------- #
def take_imgs_opencv(regnum,name):
    if not os.path.exists('./dataset'):
        os.makedirs('./dataset')

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    cap = cv2.VideoCapture(0)
    
    sampleNum = 0
    
    while sampleNum < 20:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            sampleNum = sampleNum + 1
            cv2.imwrite("dataset/" + name + "." + regnum + "." + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.waitKey(100)
        cv2.imshow('Acquiring Images', img)
        cv2.waitKey(1)    
        '''
        if sampleNum > 20:
            break
        '''   
    cap.release()
    cv2.destroyAllWindows()
    return True 
#take_imgs_opencv('1', 'Student 1')




# --------------- TRANING_MODEL --------------- #
def train_through_dataset():
    flag = True
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path = 'dataset'
    if not os.path.exists('./recognizer'):
        os.makedirs('./recognizer')
    
    try:
        Ids, face = getImagesWithID(path)
        recognizer.train(face, Ids)
        recognizer.save('recognizer/trainingData.yml')
        cv2.destroyAllWindows()
    except:
        #print("ERROR!")
        flag = False  
    return flag
    
def getImagesWithID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    face = []
    ids = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        face.append(faceNp)
        ids.append(ID)
        cv2.imshow("Training Model", faceNp)
        cv2.waitKey(1000)
    return np.array(ids), face
#train_through_dataset()




# --------------- RECOGNIZING_FACE --------------- #
def auto_attendance(sheetname, u):  
    fname = "recognizer/trainingData.yml"
    if not os.path.isfile(fname):
        flag = False
        #print("Please train the model first")
        #exit(0)
    else:
        flag = True
        faces_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(fname)
        while True:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faces_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
                ids, conf = recognizer.predict(gray[y:y + h, x:x + w])
                #print(ids)
                #accessing student name from RegisteredStudents.csv given the id
                ids = str(ids)
                name = student_csv_methods.return_name(ids)

                if conf < 50: 
                    cv2.putText(img, name, (x + 2, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 255, 0), 2)
                else:
                    cv2.putText(img, 'No Match', (x + 2, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
             
            cv2.imshow('Recognizing Face', img)
            if(cv2.waitKey(10) & 0xFF==ord('q')):
                break
            
        cap.release()
        cv2.destroyAllWindows()
        #mark attendance in a csv file storing current date and time against name and reg
        if student_csv_methods.mark_auto_attendance(ids,name,sheetname,u):
            print("Attendance Marked!")
            attendance = True
        if attendance:
            #csv = "Instructors\mona\StudentAttendance.csv"
            csvfile = "Instructors\\" + u + "\\" + sheetname
            student_csv_methods.open_attendance_sheet(csvfile)
    return flag
#auto_attendance()





















    