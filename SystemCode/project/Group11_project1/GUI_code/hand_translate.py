
import cv2
import mediapipe as mp
import time
import math
import numpy as np
from utils import Utils
import pickle
import json
from joblib import dump, load


class HandProcess:

    def __init__(self,model_path = '../Model/hello.sav', scaler_path = '../Scaler/hello.bin',diy_meaning_path = '../JSON/hello.json'):
      
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False,
                                         min_detection_confidence=0.7,
                                         min_tracking_confidence=0.5,
                                         max_num_hands=2)

        self.landmark_list = []
        self.model = pickle.load(open(model_path, 'rb'))
        self.scaler = load(scaler_path)
        self.diy_meaning = self.read_json(diy_meaning_path)
        print('diy_meaning is: ',self.diy_meaning)
        self.action_labels = {
            'none': 'Finger detected',
            'left': 'Left',
            'right': 'Right',
            'up': 'Up',
            'down': 'Down',
            'Keep moving': 'Keep moving',
            'Damn':'Damn!!!',
            'move':'Finger detected'

        }
        self.action_deteted = ''
        



    

    def getFingerXY(self,index):
        return (self.landmark_list[index][1],self.landmark_list[index][2])


    # display current recording gesture label.
    def updateText(self, action):
        self.action_deteted = action
    
    def read_json(self, path):
            with open(path, "r") as f:
                data = json.load(f)

            return data

    def load_diy_meaning(self, path):
        json_result = self.read_json(path)
        self.diy_meaning = json_result

    def plot_model_result(self):
        result = self.predictPositionByModel()
        # print('trans result is:  ',result)
        trans_result = self.diy_meaning[str(result+1)]
        # print('trans result is:  ',trans_result)
        self.action_deteted = str(trans_result)
        return trans_result

    def get_position(self):
        key_point = self.getFingerXY(0)
        return key_point

    def control_mouse(self,img):
        upList = self.checkFingersUp()
        

        if len(upList) == 0:
            return img,None
        
        key_point = self.getFingerXY(8)
    
        # if (upList == [0,1,0,0,0]):
        #     self.action_deteted = 'Finger detected'
         
        
        self.action_deteted = 'Finger detected'
        
        return img,key_point


    # check finger position
    def detected_hand(self,img,drawKeyFinger=True):
        upList = self.checkFingersUp()
        
        if len(upList) == 0:
            return img,None
    
        key_point = self.getFingerXY(0)
      
        return img,key_point

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

    def single_inference(self, model, data):
        
        data = np.expand_dims(data,0)
        data = self.scaler.transform(data)
        model_output = int(model.predict(data)[0])
        return model_output
        
    def predictPositionByModel(self):
        landmark = self.landmark_list
        positions = self.reform_and_norm_coordinate(landmark)
        
        prediction_result = self.single_inference(self.model, positions[0:41])

        return prediction_result


    def checkFingersUp(self):

        fingerTipIndexs = [4,8,12,16,20]
        upList = []
        if len(self.landmark_list) == 0:
            return upList
        if self.landmark_list[fingerTipIndexs[0]][1] < self.landmark_list[fingerTipIndexs[0]-1][1]:
            upList.append(1)
        else:
            upList.append(0)
        for i in range(1,5):
            if self.landmark_list[fingerTipIndexs[i]][2] < self.landmark_list[fingerTipIndexs[i]-2][2]:
                upList.append(1)
            else:
                upList.append(0)
        
        return upList


    def processOneHand(self,img,drawBox=True,drawLandmarks=True):
        utils = Utils()

        results = self.hands.process(img)
        self.landmark_list = []
        
        if results.multi_hand_landmarks:
            
            for hand_index,hand_landmarks in enumerate(results.multi_hand_landmarks):
                
                if drawLandmarks:
                    self.mp_drawing.draw_landmarks(
                        img,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_drawing_styles.get_default_hand_landmarks_style(),
                        self.mp_drawing_styles.get_default_hand_connections_style())

                
                for landmark_id, finger_axis in enumerate(hand_landmarks.landmark):
                    h,w,c = img.shape
                    p_x,p_y = math.ceil(finger_axis.x * w), math.ceil(finger_axis.y * h)

                    self.landmark_list.append([
                        landmark_id, p_x, p_y,
                        finger_axis.z
                    ])

                if drawBox:
                    x_min,x_max =  min(self.landmark_list,key=lambda i : i[1])[1], max(self.landmark_list,key=lambda i : i[1])[1]
                    y_min,y_max =  min(self.landmark_list,key=lambda i : i[2])[2], max(self.landmark_list,key=lambda i : i[2])[2]

                    # img = cv2.rectangle(img,(x_min-30,y_min-30),(x_max+30,y_max+30),(0, 255, 0),2)
                    img = utils.addText(img, self.action_deteted,  (x_min-20,y_min-120), textColor=(255, 0, 255), textSize=60)
                        
        return img
