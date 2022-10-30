import cv2
import hand_translate as ht
import time
import numpy as np
import pyautogui
from utils import Utils
import csv
from collections import Counter


class Translate:
    def __init__(self,model_path = '../Model/snake.sav', scaler_path = '../Scaler/snake.bin',diy_meaning_path = '../JSON/snake.json'):
        # image of each slice 
        self.image=None
        self.current_label = 0
        self.text = []
        self.buffer = []
        self.model_path = model_path
        self.scaler_path = scaler_path
        self.diy_meaning_path = diy_meaning_path

    def add_row_to_csv(self, csv_file_name, array):
        with open(csv_file_name,'a',encoding='utf8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(array)

    def reform_coordinate(self,landmark):
        val = []
        for coord in landmark:
            val.append(coord[1])
            val.append(coord[2])
        return val
    
    def reform_and_norm_coordinate(self,landmark):
        base_x = landmark[0][1]
        base_y = landmark[0][2]
        val = []
        for coord in landmark:
            val.append(coord[1]-base_x)
            val.append(coord[2]-base_y)
        return val

    def top_frequency(self, array):
        return Counter(array).most_common(1)[0][0]

    def translate_start(self):

        handprocess = ht.HandProcess(self.model_path, self.scaler_path, self.diy_meaning_path)
        utils = Utils()
        
        fpsTime = time.time()
        cap = cv2.VideoCapture(0)

       
        resize_w, resize_h = pyautogui.size() 
        start_recording = False
   
    
        while cap.isOpened():
            success, self.image = cap.read()

            try:
                success, self.image = cap.read()
            except:
                print('No camera detected')

            self.image = cv2.resize(self.image, (resize_w, resize_h))
           

            # Processing for each slice
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.image = cv2.flip(self.image, 1)
            self.image = handprocess.processOneHand(self.image)
            self.image,key_point = handprocess.detected_hand(self.image,drawKeyFinger=True)
            
 
            if key_point:

                action = handprocess.plot_model_result()
                print('Action is: ', action)

                if action == 'left':
                    pyautogui.press('left')
                elif action == 'right':
                    pyautogui.press('right')
                elif action == 'up':
                    pyautogui.press('up')
                elif action == 'down':
                    pyautogui.press('down')

            self.image.flags.writeable = True
            self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
            if start_recording:        
                self.image = utils.addText(self.image, "Gluttonous Snake Game" ,  (10, 30), textColor=(0, 255, 0), textSize=70)
            
            self.image = cv2.resize(self.image, (resize_w//6, resize_h//6))
            cv2.imshow('Snake controller', self.image)
            
            if cv2.waitKey(5) & 0xFF == 27:
                break

        cap.release()





start_time = time.time()
# csv_path = str(sys.argv[1])
# recording = int(sys.argv[2])
# time_lag = int(sys.argv[3])
# gestures_num = int(sys.argv[4])
# print('Saving csv path is: ', csv_path)
# model_path = str(sys.argv[1])
# scaler_path = str(sys.argv[2])
# meaning_path = str(sys.argv[3])
ts = Translate()
ts.translate_start()
