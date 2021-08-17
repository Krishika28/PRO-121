import numpy as np
import cv2 

video = cv2.VideoCapture(0)
image = cv2.imread('White.jpg')

while(True):
    ret, frame = video.read()
    
    print(frame)
    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 
  
 # hsv value   
    u_black = np.array([170, 111, 255]) 
    l_black = np.array([0, 0, 160]) 
  
    mask = cv2.inRange(frame, l_black, u_black) 
    res = cv2.bitwise_and(frame, frame, mask = mask) 
  
    f = frame - res 
    f = np.where(f == 0, image, f) 
    cv2.imshow('Output', frame)
    cv2.imshow('Mask', f)
    
    if(cv2.waitKey(1) & 0xFF==ord('Q')):
        break

video.release() 
cv2.destroyAllWindows()