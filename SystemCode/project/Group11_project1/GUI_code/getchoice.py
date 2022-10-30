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