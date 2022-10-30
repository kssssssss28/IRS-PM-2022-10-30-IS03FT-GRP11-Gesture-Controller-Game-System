
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

    def __init__(self,static_image_mode=False,max_num_hands=2,model_path = '../Model/mlp_test.sav'):
        # 参数
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=static_image_mode,
                                         min_detection_confidence=0.7,
                                         min_tracking_confidence=0.5,
                                         max_num_hands=max_num_hands)

        self.landmark_list = []
        self.model = pickle.load(open(model_path, 'rb'))
        self.sc = load('../Scaler/std_scaler.bin')
        self.diy_meaning = {}
        self.action_labels = {
            'none': 'Finger detected',
            'move': 'Finger detected',
    
            'left': 'Left',
            'right': 'Right',
            'up': 'Up',
            'down': 'Down',
            'Keep moving': 'Finger detected',
            'Damn':'Damn!!!'

        }
        self.action_deteted = ''
        self.degree = 0
        self.update = True
        self.prev_fix = 0
        self.width = 2500
        self.height = 1400
        



    def checkHandsIndex(self,handedness):
     
        if len(handedness) == 1:
            handedness_list = [handedness[0].classification[0].label]
        else:
            handedness_list = [handedness[0].classification[0].label,handedness[1].classification[0].label]
        
        return handedness_list
    

    def getDistance(self,pointA,pointB):
        return math.hypot((pointA[0]-pointB[0]),(pointA[1]-pointB[1]))

   
    def getFingerXY(self,index):
        return (self.landmark_list[index][1],self.landmark_list[index][2])

    
    def drawInfo(self,img,action):
        thumbXY,indexXY,middleXY = map(self.getFingerXY,[4,8,12])

        if action == 'move':
            img = cv2.circle(img,indexXY,20,(255,0,255),-1)

        elif action == 'click_single_active':
            middle_point = int(( indexXY[0]+ thumbXY[0])/2),int((  indexXY[1]+ thumbXY[1] )/2)
            img = cv2.circle(img,middle_point,30,(0,255,0),-1)

        elif action == 'click_single_ready':
            img = cv2.circle(img,indexXY,20,(255,0,255),-1)
            img = cv2.circle(img,thumbXY,20,(255,0,255),-1)
            img = cv2.line(img,indexXY,thumbXY,(255,0,255),2)
        

        elif action == 'click_right_active':
            middle_point = int(( indexXY[0]+ middleXY[0])/2),int((  indexXY[1]+ middleXY[1] )/2)
            img = cv2.circle(img,middle_point,30,(0,255,0),-1)

        elif action == 'click_right_ready':
            img = cv2.circle(img,indexXY,20,(255,0,255),-1)
            img = cv2.circle(img,middleXY,20,(255,0,255),-1)
            img = cv2.line(img,indexXY,middleXY,(255,0,255),2)


        return img

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


    # check finger position
    def checkFingerPosition(self,img,drawKeyFinger=True):
        upList = self.checkFingersUp()
        action = 'none'

        if len(upList) == 0:
            return img,action,None
        
        # 侦测距离
        dete_dist = 100

        # palm
        key_point = self.getFingerXY(0)
        finger_x = key_point[0]
        finger_y = key_point[1]
        
        if (finger_x < 600 and finger_y > 250 and finger_y < 1100):
            # action = 'left'
            action = 'Damn'
        
        elif (finger_x > 1800 and finger_y > 250 and finger_y < 1100):
            # action = 'right'
            action = 'Keep moving'
        
        elif (finger_x <1800 and finger_x > 600 and finger_y < 400):
            # action = 'up'
            action = 'Keep moving'

        elif (finger_x <1800 and finger_x > 600 and finger_y > 900):
            # action = 'down'
            action = 'Keep moving'
        

        return img, action, key_point

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
        data = self.sc.transform(data)
        model_output = int(model.predict(data)[0])
        return model_output
        
    def predictPositionByModel(self):
        landmark = self.landmark_list
        positions = self.reform_and_norm_coordinate(landmark)
        
        prediction_result = self.single_inference(self.model, positions[0:41])
        print('Current gesture is: ', prediction_result )

    def control_mouse(self,img):
        upList = self.checkFingersUp()
        action = 'none'

        if len(upList) == 0:
            return img,action,None
        
        key_point = self.getFingerXY(8)
    
        
        if (upList == [0,1,0,0,0]):
            action = 'move'
         
        
        self.action_deteted = self.action_labels[action]
        

        return img,action,key_point

    def compute_degree(self, middle_finger, palm):
        x1,y1 = middle_finger
        x1 = x1 -  palm[0]
        y1 = -(x1 -  palm[1])

        angle= np.arctan2((x1), (y1))
        degree = angle*(180/np.pi)

        return degree



    
 
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



    def GetChoice(self,img,drawKeyFinger=True):
        upList = self.checkFingersUp()
        action = 'none'

        if len(upList) == 0:
            return img,action,None
        
        key_point = self.getFingerXY(8)
        finger_x = key_point[0]
        finger_y = key_point[1]
        
    

        if (finger_x < self.width/2 and finger_y < self.height/2):
            action = 'A'
            self.updateText('Your Choice:' + action)
           
        
        elif (finger_x > self.width/2 and finger_y < self.height/2):
            action = 'B'
            self.updateText('Your Choice:' + action)
 
        
        elif (finger_x < self.width/2 and finger_y > self.height/2):
            action = 'C'
            self.updateText('Your Choice:' + action)

        elif (finger_x > self.width/2 and finger_y > self.height/2):
            action = 'D'
            self.updateText('Your Choice:' + action)
        
        
        return img,action,key_point

        

 
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

