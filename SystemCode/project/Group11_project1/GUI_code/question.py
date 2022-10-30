import cv2
import pymysql
from utils import Utils
import handProcess
import time
import numpy as np
from cvzone.SelfiSegmentationModule import SelfiSegmentation

class Quesiton:
    def __init__(self):
        self.image = None
        self.que_dic = {}
        self.opt_dic = {}
        self.result = ['Wrong!','Correct!']
        self.buffer = ['A','A','A','B','A','A','A','A','A','B','A','A','A','B','A','A','A','A','A','B''A','A','A','B','A','A','A','A','A','B''A','A','A','B','A','A','A']
        self.db = pymysql.connect(host='localhost',
                            user='root',
                            password='12345678',
                            database='questions')


    def load_question(self):
        
        cursor = self.db.cursor()
        sql = 'SELECT * FROM QUESTIONS_tbl'
        cursor.execute(sql)
        questions = cursor.fetchall()
        for i in range(len(questions)):
            self.que_dic[questions[i][1]] = questions[i][6]

        for i in range(len(questions)):
            self.opt_dic[questions[i][1]] = questions[i][2:6]
        
    def check_ans(self, question, guess):
        correct_ans = self.que_dic.get(question)
        if correct_ans == guess:
            return 1
        else:
            return 0 
       
    def generate_questions(self, num=10):
        que_keys = []
        for i in range(num):
            que_keys.append(np.random.choice(list(self.que_dic), replace=False))
        return que_keys

    def add_queue(self, new):
        self.buffer.pop(0)
        self.buffer.append(new)

    def check(self):
        if len(set(self.buffer)) == 1:
            return True
        else:
            return False

    def display_question(self, key):
        utils = Utils()

        self.image = utils.addText(self.image, key,  (10, 30), textColor=(0, 0, 0), textSize=85)
        self.image = utils.addText(self.image, 'A:'+self.opt_dic[key][0],  (200, 350), textColor=(222, 249, 250), textSize=80)
        self.image = utils.addText(self.image, 'B:'+self.opt_dic[key][1],  (1450, 350), textColor=(222, 249, 250), textSize=80)
        self.image = utils.addText(self.image, 'C:'+self.opt_dic[key][2],  (200, 1050), textColor=(222, 249, 250), textSize=80)
        self.image = utils.addText(self.image, 'D:'+self.opt_dic[key][3],  (1450, 1050), textColor=(222, 249, 250), textSize=80)

    def create_bg(self):
        img = np.ones([1400,2500,3],np.uint8)
        img[:120,:,:] = 255
        img[120:700,0:1250,0] = 205 #B
        img[120:700,0:1250,1] = 90 #G
        img[120:700,0:1250,2] = 106 #R

        img[120:700,1250:,0] = 192 #B
        img[120:700,1250:,1] = 190 #G
        img[120:700,1250:,2] = 192 #R

        img[700:,0:1250,0] = 128 #B
        img[700:,0:1250,1] = 142 #G
        img[700:,0:1250,2] = 42 #R

        img[700:,1250:,0] = 20 #B
        img[700:,1250:,1] = 128 #G
        img[700:,1250:,2] = 48 #R

        return img

    def remove_bg(self, img ,w ,h):
        segment = SelfiSegmentation()

        bg_img = self.create_bg()
        bg_img = cv2.resize(bg_img,(w,h))
        self.image = segment.removeBG(img, bg_img, threshold=0.15)
 
    def New_game(self):
        correct_guesses = [0,0,0,0,0,0,0,0,0,0,0]
        handprocess = handProcess.HandProcess(False,1)
        utils = Utils()

        cap = cv2.VideoCapture(0)
        resize_w = 2500
        resize_h = 1400
        play_again = True


        que_keys = self.generate_questions()
        test_time = time.time()
        while cap.isOpened() and play_again == True:
            current_time = time.time()
            _, self.image = cap.read()
            self.image = cv2.resize(self.image, (resize_w, resize_h))
            self.remove_bg(self.image, resize_w, resize_h)
            # Processing for each slice
            self.image.flags.writeable = True

            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

            self.image = cv2.flip(self.image, 1)
            self.image = handprocess.processOneHand(self.image)
            self.image,action,key_point = handprocess.GetChoice(self.image,drawKeyFinger=True)
            self.add_queue(action)
                                                                                                                                                                    
            if current_time - test_time < 10:
                self.display_question(que_keys[0])
                if self.check() and 'none' not in set(self.buffer):
                    add = self.check_ans(que_keys[0],self.buffer[10])
                    correct_guesses[0] = add
                    self.image = utils.addText(self.image, self.result[add],  (1100, 1200), textColor=(0, 0, 255), textSize=80)
                    
            elif 10 < current_time - test_time < 20:
                self.display_question(que_keys[1])
                if self.check() and 'none' not in set(self.buffer):
                    add = self.check_ans(que_keys[1],self.buffer[10])
                    correct_guesses[1] = add
                    self.image = utils.addText(self.image, self.result[add],  (1100, 1200), textColor=(0, 0, 255), textSize=80)
            
            elif 20 < current_time - test_time < 30:
                self.display_question(que_keys[2])
                if self.check() and 'none' not in set(self.buffer):
                    add = self.check_ans(que_keys[2],self.buffer[10])
                    correct_guesses[2] = add
                    self.image = utils.addText(self.image, self.result[add],  (1100, 1200), textColor=(0, 0, 255), textSize=80)

            elif 30 < current_time - test_time < 40:
                self.display_question(que_keys[3])
                if self.check() and 'none' not in set(self.buffer):
                    add = self.check_ans(que_keys[3],self.buffer[10])
                    correct_guesses[3] = add
                    self.image = utils.addText(self.image, self.result[add],  (1100, 1200), textColor=(0, 0, 255), textSize=80)
                
            elif 40 < current_time - test_time < 50:
                self.display_question(que_keys[4])
                if self.check() and 'none' not in set(self.buffer):
                    add = self.check_ans(que_keys[4],self.buffer[10])
                    correct_guesses[4] = add
                    self.image = utils.addText(self.image, self.result[add],  (1100, 1200), textColor=(0, 0, 255), textSize=80)

            elif 50 < current_time - test_time < 60:
                self.display_question(que_keys[5])
                if self.check() and 'none' not in set(self.buffer):
                    add = self.check_ans(que_keys[5],self.buffer[10])
                    correct_guesses[5] = add
                    self.image = utils.addText(self.image, self.result[add],  (1100, 1200), textColor=(0, 0, 255), textSize=80)
            
            elif 60 < current_time - test_time < 70:
                self.display_question(que_keys[6])
                if self.check() and 'none' not in set(self.buffer):
                    add = self.check_ans(que_keys[6],self.buffer[10])
                    correct_guesses[6] = add
                    self.image = utils.addText(self.image, self.result[add],  (1100, 1200), textColor=(0, 0, 255), textSize=80)

            elif 70 < current_time - test_time < 80:
                self.display_question(que_keys[7])
                if self.check() and 'none' not in set(self.buffer):
                    add = self.check_ans(que_keys[7],self.buffer[10])
                    correct_guesses[7] = add
                    self.image = utils.addText(self.image, self.result[add],  (1100, 1200), textColor=(0, 0, 255), textSize=80)
            
            elif 80 < current_time - test_time < 90:
                self.display_question(que_keys[8])
                if self.check() and 'none' not in set(self.buffer):
                    add = self.check_ans(que_keys[8],self.buffer[10])
                    correct_guesses[8] = add
                    self.image = utils.addText(self.image, self.result[add],  (1100, 1200), textColor=(0, 0, 255), textSize=80)
            
            elif 90 < current_time - test_time < 100:
                self.display_question(que_keys[9])
                if self.check() and 'none' not in set(self.buffer):
                    add = self.check_ans(que_keys[9],self.buffer[10])
                    correct_guesses[9] = add
                    self.image = utils.addText(self.image, self.result[add],  (1100, 1200), textColor=(0, 0, 255), textSize=80)
            
            elif 100 < current_time - test_time < 110:
                score = int(sum(correct_guesses) * 10)
                self.image = utils.addText(self.image, 'Your Score is: ' + str(score) + '%',  (1000, 700), textColor=(0, 0, 255), textSize=100)
            
            elif current_time - test_time > 110:
                break


            self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
            self.image = cv2.resize(self.image, (resize_w//2, resize_h//2))

            cv2.imshow('Feature collection stage', self.image)
            if cv2.waitKey(5) & 0xFF == 27:
                break
        cap.release()


    def add_question(self,que,A,B,C,D,ANS):
        cursor = self.db.cursor()
        sql = 'SELECT * FROM QUESTIONS_tbl'
        cursor.execute(sql)
        questions = cursor.fetchall()
        count = len(questions)
        ## defining the Query
        query ="INSERT INTO QUESTIONS_tbl VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (count+1, que, A, B, C, D, ANS)
 
        ## executing the query with values
        cursor.execute(query, values)
        self.db.commit()

 

        
if __name__ == "__main__":
    game = Quesiton()
    game.load_question()
    game.New_game()
