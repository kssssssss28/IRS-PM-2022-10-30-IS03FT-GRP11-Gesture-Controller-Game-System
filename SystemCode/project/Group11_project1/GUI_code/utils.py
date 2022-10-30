from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import json
import os
import csv

class Utils:
    def __init__(self):
        pass

    def create_folder(path):
        if not os.path.exists(path):
            os.makedirs(path)

    def add_row_to_csv(self, csv_file_name, array):
        with open(csv_file_name,'a',encoding='utf8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(array)

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
 
    def addText(self,image_array, text, position, textColor=(0, 255, 0), textSize=30):
        if (isinstance(image_array, np.ndarray)):  
            rgb_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
            image_array = Image.fromarray(rgb_array)
        
        draw = ImageDraw.Draw(image_array)
        arial_font = ImageFont.truetype("../fonts/arial.ttf", 60, encoding="utf-8")
        draw.text(position, text, textColor,arial_font)
        bgr = cv2.cvtColor(np.asarray(image_array), cv2.COLOR_RGB2BGR)
        return bgr

    def write_json(path, dict):
        with open(path,"w") as f:         
            json.dump(dict,f,indent=2)

    def isRegister(username,users_folders):
        return username in users_folders

    def read_json(path):
        with open(path, "r") as f:
            data = json.load(f)
        return data