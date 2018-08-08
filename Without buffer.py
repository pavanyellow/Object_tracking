import cv2
import sys
import numpy as np
capture = cv2.VideoCapture(0)




while(True):
 r,img1=capture.read()
 imgray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
	
  
 r,img2=capture.read()
 imgray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
 diff=cv2.subtract(imgray1,imgray2)
 th,thresholded=cv2.threshold(diff,40,255,cv2.THRESH_BINARY)
 blur=cv2.GaussianBlur(thresholded,(9,9),0)
 th,thresholded2=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
 edged=cv2.Canny(thresholded2,50,200)
 c,contours,v = cv2.findContours(thresholded2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
 if len(contours)>=1:
  cnt=contours[0]
  x,y,w,h = cv2.boundingRect(cnt)
  img = cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)

 
 
 
 cv2.imshow('window',img2)
 if cv2.waitKey(1) & 0xFF == ord('q'):
        break     

capture.release()
