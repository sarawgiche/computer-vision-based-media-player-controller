import numpy as np
import serial
import time
import sys
import cv2
import pyautogui

#arduino = serial.Serial('COM1',9600)
#time.sleep(2)
#print("Connection to arduino...")


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
count =0

while 1:
    ret, img = cap.read()
    cv2.resizeWindow('img', 500,500)
    #cv2.line(img,(500,250),(0,250),(0,255,0),1)
    #cv2.line(img,(250,0),(250,500),(0,255,0),1)
    #cv2.circle(img, (250, 250), 5, (255, 255, 255), -1)
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
        roi_gray  = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        arr = {y:y+h, x:x+w}
        print (arr)

        print ('X :' +str(x))
        print ('Y :'+str(y))
        print ('x+w :' +str(x+w))
        print ('y+h :' +str(y+h))

        xx = int(x+(x+h))/2
        yy = int(y+(y+w))/2

        print (xx)
        print (yy)

        center = (xx,yy)

        print("Center of Rectangle is :", center)
        #data = "X{0:.0f}Y{1:.0f}Z".format(xx, yy)
        #print ("output = '" +data+ "'")
        #arduino.write(data.encode())


    cv2.imshow('img',img)
    if xx>=305 and xx<=325 and yy>=230 and yy<=245 and count==1  :#callibrate it
        pyautogui.press('space')
        count=0

    elif xx>=350 and xx<=365 and yy>=220 and yy<=235 and count==0:#calibrate it
        pyautogui.press('space')
        count=1



    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
