import cv2
import time
import numpy as np
import pyautogui
from utils import Utils
import autopy
import hand_translate as ht


class ControlMouse:
    def __init__(self):
        

        self.image=None
    

    def move(self):
        handprocess = ht.HandProcess()
        screenWidth, screenHeight = pyautogui.size() 

        cap = cv2.VideoCapture(0)
        resize_w = 1280
        resize_h = 720

        frameMargin = 100
        stepX, stepY = 0, 0
        smoothening = 5


        while cap.isOpened():
      
            try:
                success, self.image = cap.read()
            except:
                print('No camera detected')

            self.image = cv2.resize(self.image, (resize_w, resize_h))
            self.image.flags.writeable = False
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.image = cv2.flip(self.image, 1)
            self.image = handprocess.processOneHand(self.image)
            self.image,key_point =  handprocess.control_mouse(self.image)
            action = handprocess.action_deteted

            if key_point:
        
                destinationX = np.interp(key_point[0], (frameMargin, resize_w - frameMargin), (0, screenWidth))
                destinationY = np.interp(key_point[1], (frameMargin, resize_h - frameMargin), (0, screenHeight))
                
                destinationX = stepX + (destinationX - stepX) / smoothening
                destinationY = stepY + (destinationY - stepY) / smoothening
            

                if action == 'Finger detected':
                 
                    autopy.mouse.move(destinationX, destinationY)

                stepX, stepY = destinationX, destinationY

            self.image.flags.writeable = True
            self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
            
            
            scale = 4
            self.image = cv2.resize(self.image, (resize_w//scale, resize_h//scale))
            cv2.imshow('Control the mouse', self.image)
            
            if cv2.waitKey(5) & 0xFF == 27:
                break
        cap.release()



control = ControlMouse()
control.move()