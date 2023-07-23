import matplotlib.pyplot as plt
import pyautogui
import cv2
import numpy as np
import psutil
import time
from matplotlib.widgets import Slider, Button
import random

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def detectlinesmethod():
    #pyautogui.screenshot("screen.png")

    img = cv2.imread("scren.png")
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gray.png", imggray)
    imggaus=cv2.GaussianBlur(imggray,(5,5),0)
    cv2.imwrite("gaus.png",imggaus)
    f, imgcanny = cv2.threshold(imggaus, 240, 255,cv2.ADAPTIVE_THRESH_MEAN_C)
    cv2.imwrite("canny.png", imgcanny)
    cizgiler = cv2.HoughLinesP(imgcanny, 1, np.pi/180, 1, maxLineGap=5,minLineLength=5)

    for line in cizgiler:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 2)
        
    
    cv2.imwrite("houghlines5.jpg", img)
    #cv2.imshow("imgcanny.jpg", imgcanny)
    #cv2.imshow("gray",imggray)
    
    
# while checkIfProcessRunning("eurotrucks2.exe") == False:
#     checkIfProcessRunning("eurotrucks2.exe")
# else:
#     while True:
#         main()
detectlinesmethod()
cv2.waitKey(0)
cv2.destroyAllWindows()
exit()    