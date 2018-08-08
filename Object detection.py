import cv2
import sys
import numpy as np
capture = cv2.VideoCapture(0)

f,img1=capture.read()
imgray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)



while(True):

	
    
 r,img2=capture.read()
 imgray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
 diff=cv2.subtract(imgray1,imgray2)
 th,thresholded=cv2.threshold(diff,40,255,cv2.THRESH_BINARY)
 blur=cv2.GaussianBlur(thresholded,(9,9),0)
 th1,thresholded2=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
 edged=cv2.Canny(thresholded2,50,200)
 ,contours, = cv2.findContours(thresholded2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
 if len(contours)>=1:
  cnt=contours[0]
  (x,y),radius = cv2.minEnclosingCircle(cnt)
  center = (int(x),int(y))
  radius = int(radius)
  img= cv2.circle(img2,center,radius+6,(0,255,0),2)
  print (x,y)

 imgray1=imgray2
 
 
 cv2.imshow('main',diff)
 if cv2.waitKey(1) & 0xFF == ord('q'):
        break     

capture.release()
