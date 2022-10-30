import tkinter as tk
import os
from PIL import Image, ImageTk
import GUI_Main as main



class Instruction(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller
        self.controller.title('Gesture Controller')
        self.controller.state('normal')
        

        self.controller.geometry('{}x{}'.format(main.width, main.height)) 
        self.controller.maxsize(1600,680)
        parent.pack_propagate(0)

        
        
        welcome_bg_color = "#2D2D2D"
        canvas_ins = tk.Canvas(
            self, bg=welcome_bg_color, height=main.height, width=main.width,
            bd=0, highlightthickness=0, relief="ridge")
        canvas_ins.place(x=0, y=0)


        global bg_img
        bg_img = ImageTk.PhotoImage(Image.open('../GUI_material/bg5.png'))
        kk = canvas_ins.create_image(0, 0, image=bg_img)

        thickness = 60
        length = main.width
        rec_x_ = 0
        rec_y_ = 0
        canvas_ins.create_rectangle(rec_x_, rec_y_, rec_x_ + length, rec_y_ + thickness, fill="#FFFFFF", outline="")

        # logo
        global logo
        logo = tk.PhotoImage(file="../GUI_material/nus_logo.png")
        logo_img = canvas_ins.create_image(200, 30, image=logo)

        def enter_bpe():
            controller.show_frame('BPE')

        def enter_home_page(event):                  
            controller.show_frame('Welcome_Page')
            
        def enter_about_us(event):                  
            controller.show_frame('About_Us')

        def enter_contact(event):                  
            controller.show_frame('Contact')

        def enter_instruction(event):                  
            controller.show_frame('Instruction')


        label_inter = 120
        start_x = 1190
        bar_y = 29
        
        text_color = '#000000'
        
        home_page=canvas_ins.create_text(start_x, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='home_page')
        canvas_ins.tag_bind(home_page, '<ButtonPress-1>', enter_home_page)   
        canvas_ins.insert(home_page,1,"Home page")

        about_us=canvas_ins.create_text(start_x + label_inter+20, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='about_us_')
        canvas_ins.tag_bind(about_us, '<ButtonPress-1>', enter_about_us)   
        canvas_ins.insert(about_us,1,"About us")


        instruction=canvas_ins.create_text(start_x + label_inter*2+20, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='instruction')
        canvas_ins.tag_bind(instruction, '<ButtonPress-1>', enter_instruction)   
        canvas_ins.insert(instruction,1,"Description")


        font_size = 22

        word_x = 185
        word_y = 120
        inter = 50

        line_x = 50
        line_length = main.width - line_x*2
        line_y = 635
        
        canvas_ins.create_line(line_x, line_y, line_x+line_length, line_y, fill='#C1C1C1')
        txtid9=canvas_ins.create_text(560, line_y + 15,font=("Arial-BoldMT", 14),anchor="nw",fill = '#C1C1C1')
        canvas_ins.insert(txtid9,1,"Copyright © 2022   NUS-ISS Intelligent System Group 11  All Rights Reserved. \n")


        line1=canvas_ins.create_text(word_x, word_y,font=("Arial-BoldMT", font_size),anchor="nw",fill = 'white')
        canvas_ins.insert(line1,1,"Gesture controller game system:\n")



        line2=canvas_ins.create_text(word_x, word_y + inter*1,font=("Arial-BoldMT", font_size),anchor="nw",fill = 'white')
        canvas_ins.insert(line2,1,"In this project, in order to use light weight camera to detect human-hand, we use MediaPipe which is a multimedia \n")
        txtid3=canvas_ins.create_text(word_x, word_y + inter*2,font=("Arial-BoldMT", font_size),anchor="nw",fill = 'white')
        canvas_ins.insert(txtid3,1,"machine learning model application framework developed and open-sourced by Google Research. It is able to \n")
        txtid4=canvas_ins.create_text(word_x, word_y + inter*3,font=("Arial-BoldMT", font_size),anchor="nw",fill = 'white')
        canvas_ins.insert(txtid4,1,"detect and give bound-box for users hands detected by camera and return 21 finger joints location(landmarks)\n")
        txtid5=canvas_ins.create_text(word_x, word_y + inter*4,font=("Arial-BoldMT", font_size),anchor="nw",fill = 'white')
        canvas_ins.insert(txtid5,1,"which can be regarded as gestures features. We made an automatic features collection program by recording landmarks\n")
        txtid10=canvas_ins.create_text(word_x, word_y + inter*5,font=("Arial-BoldMT", font_size),anchor="nw",fill = 'white')
        canvas_ins.insert(txtid10,1,"from each frame captured by camera and save in .csv file for further model training. After cross-validation experiments\n")
        txtid6=canvas_ins.create_text(word_x, word_y + inter*6,font=("Arial-BoldMT", font_size),anchor="nw",fill = 'white')
        canvas_ins.insert(txtid6,1,"and efficiency consideration, eventually, we chose a Neural Network as classification model for gestures interpretation. \n")
        txtid7=canvas_ins.create_text(word_x, word_y + inter*7,font=("Arial-BoldMT", font_size),anchor="nw",fill = 'white')
        canvas_ins.insert(txtid7,1,"The model achieved 99.8%. accuracy in 3000+ test set. We further process the output of our own model and combine its result   \n")
        txtid8=canvas_ins.create_text(word_x, word_y + inter*8,font=("Arial-BoldMT", font_size),anchor="nw",fill = 'white')
        canvas_ins.insert(txtid8,1,"with pygames, as you can see, three games show up, you can play them by using hand gestures.  To improve users interactive  \n")
        txtid9=canvas_ins.create_text(word_x, word_y + inter*9,font=("Arial-BoldMT", font_size),anchor="nw",fill = 'white')
        canvas_ins.insert(txtid9,1,"experience, we used Selfie Segmentation algorithm from CV-Zone to replace background by our intellectual questions. \n")

        
      
      

       

        
