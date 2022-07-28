import matplotlib.pyplot as plt
from cv2 import threshold
import pyautogui
import cv2
import numpy as np
import psutil
import time

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def detectlinesmethod():
    pyautogui.screenshot("screen.png")

    img = cv2.imread("screen.png")

    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gray.png", imggray)
    ret, threshold = cv2.threshold(imggray, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite("threshold.png", threshold)
    cizgiler = cv2.HoughLinesP(threshold, 1, np.pi/180, 30, maxLineGap=10)

    for line in cizgiler:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)

    cv2.imwrite("houghlines5.jpg", img)
    cv2.imshow("houghlines5.jpg", img)
    time.sleep(3)

def detectLineCollision():
    pyautogui.screenshot("screen.png")
    img = cv2.imread("screen.png")
    
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    plt.imshow(imgrgb)
    plt.show()
# while checkIfProcessRunning("eurotrucks2.exe") == False:
#     checkIfProcessRunning("eurotrucks2.exe")
# else:
#     while True:
#         main()
detectLineCollision()
cv2.waitKey()
cv2.destroyAllWindows()    