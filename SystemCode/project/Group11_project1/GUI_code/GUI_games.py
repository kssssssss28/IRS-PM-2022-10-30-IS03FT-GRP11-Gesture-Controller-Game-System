
from matplotlib.figure import Figure
from matplotlib.colors import colorConverter
from subprocess import Popen, PIPE, call
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import tkinter as tk
import matplotlib as mpl
from scipy.ndimage import rotate
from tkinter import *
from tkinter import ttk
import time
from PIL import Image, ImageTk
import os
import numpy as np
from tkinter import filedialog
from tkinter import font as tkFont
from subprocess import call
import GUI_Main as main
import matplotlib.pyplot as plt
from tkinter import messagebox



class Games(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#f0efeb', width=1600, height=680)
        self.controller = controller
        self.controller.title('Gesture Controller')
        self.controller.state('normal')
        self.columnconfigure(0, minsize=500, weight=1)
        self.columnconfigure(1, minsize=500, weight=1)
        self.rowconfigure(0, minsize=650, weight=1)
        self.rowconfigure((0, 10), minsize=40, weight=1)
        self.columnconfigure([0, 1, 2, 3, 4], minsize=60, weight=1)
        
    # ------------------ Background -------------------------
        
        bg_color = "#181A27" 

        canvas_game = tk.Canvas(
            self, bg=bg_color, height=main.height, width=main.width,
            bd=0, highlightthickness=0)

        canvas_game.place(x=0, y=0)

        thickness = 60
        length = main.width
        rec_x_ = 0
        rec_y_ = 0
        canvas_game.create_rectangle(rec_x_, rec_y_, rec_x_ + length, rec_y_ + thickness, fill="#FFFFFF", outline="")

        # ------------------------ Logo ----------------------------
        
        
        # logo图像
        global logo
        logo = tk.PhotoImage(file="../GUI_material/nus_logo.png")
        logo_img = canvas_game.create_image(200, 30, image=logo)

        #  ------------------------ enter functions ----------------------------
        text_color = '#000000'

        def enter_home_page(event):                  
            controller.show_frame('Welcome_Page')
        
        def enter_about_us(event):                  
            controller.show_frame('About_Us')

        def enter_instruction(event):                  
            controller.show_frame('Instruction')


  

        label_inter = 120
        start_x = 1090
        bar_y = 24
        
        text_color = '#000000'
        
        home_page=canvas_game.create_text(start_x + label_inter, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='home_page')
        canvas_game.tag_bind(home_page, '<ButtonPress-1>', enter_home_page)   
        canvas_game.insert(home_page,1,"Home page")

        # function=canvas_game.create_text(start_x + label_inter+20, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='about_us_')
        # canvas_game.tag_bind(function, '<ButtonPress-1>', enter_function)   
        # canvas_game.insert(function,1,"Functions")

        about_us=canvas_game.create_text(start_x + label_inter*2+20, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='about_us_')
        canvas_game.tag_bind(about_us, '<ButtonPress-1>', enter_about_us)   
        canvas_game.insert(about_us,1,"About us")

        instruction=canvas_game.create_text(start_x + label_inter*3+20, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='instruction')
        canvas_game.tag_bind(instruction, '<ButtonPress-1>', enter_instruction)   
        canvas_game.insert(instruction,1,"Description")

        #   ------ button -----

        
        btn_y = 130
        btn_x = 50
        btn_font_size = 23
        btn_width = 366
        btn_height = 74
        btn_y_inter = 100
        btn_x_inter = 570

        def snake():
           
            Popen(["python3", "control_snake.py"])
            time.sleep(5)
            Popen(["python3", "snake.py"])
    
        
        global snake_img
        snake_img = tk.PhotoImage(file="../GUI_material/empty.png")
        snake_btn = tk.Button(self,
                             image=snake_img, borderwidth=0, highlightthickness=0,
                             command=snake, relief="flat", text='Gluttonous Snake', 
                             fg = 'white',compound="center",font=("Arial-BoldMT", int(btn_font_size)))
        snake_btn.place(x=btn_x, y=btn_y)
        snake_btn.place(width=btn_width, height=btn_height)
        
        def rocket():
        
            Popen(["python3", "move_mouse.py"])
            time.sleep(5)
            Popen(["python3", "rocket.py"])

        
        global surv_img
        surv_img = tk.PhotoImage(file="../GUI_material/empty.png")
        surv_btn = tk.Button(self,
                             image=surv_img, borderwidth=0, highlightthickness=0,
                             command=rocket, relief="flat", text='Survival', 
                             fg = 'white',compound="center",font=("Arial-BoldMT", int(btn_font_size)))
        surv_btn.place(x=btn_x + btn_x_inter, y=btn_y)
        surv_btn.place(width=btn_width, height=btn_height)


        def questions():
            Popen(["python3", "question.py"])
            
        
        global question_img
        question_img = tk.PhotoImage(file="../GUI_material/empty.png")
        question_btn = tk.Button(self,
                             image=question_img, borderwidth=0, highlightthickness=0,
                             command=questions, relief="flat", text='FAQs', 
                             fg = 'white',compound="center",font=("Arial-BoldMT", int(btn_font_size)))
        question_btn.place(x=btn_x + btn_x_inter*2, y=btn_y)
        question_btn.place(width=btn_width, height=btn_height)


        # --------- icon ---------

        icon_x = 220
        icon_y = 580
        icon_x_inter = 590

        global snake_logo
        snake_logo = tk.PhotoImage(file="../GUI_material/snake_icon.png")
        canvas_game.create_image(icon_x, icon_y, image=snake_logo)

        global rocket_logo
        rocket_logo = tk.PhotoImage(file="../GUI_material/rocket_icon.png")
        canvas_game.create_image(icon_x + icon_x_inter*1, icon_y, image=rocket_logo)

        global qa_logo
        qa_logo = tk.PhotoImage(file="../GUI_material/qa_icon.png")
        canvas_game.create_image(icon_x + icon_x_inter*2, icon_y, image=qa_logo)
        
       
        des_x = 100
        des_y = 240
        des_y_inter = 60
        des_color = 'white'

        snake_description1 = canvas_game.create_text(des_x-30, des_y,font=("Arial-BoldMT", 25),anchor="nw",fill = des_color)
        canvas_game.insert(snake_description1,1,"   Gesture Control Snake \n\n")

        snake_description2 = canvas_game.create_text(des_x-30, des_y+des_y_inter,font=("Arial-BoldMT", 20),anchor="nw",fill = des_color)
        canvas_game.insert(snake_description2,1,"  Use thumb to change directions \n\n")

        snake_description3 = canvas_game.create_text(des_x-20, des_y+des_y_inter*2,font=("Arial-BoldMT", 20),anchor="nw",fill = des_color)
        canvas_game.insert(snake_description3,1," If you don't like these gestures\n\n")

        snake_description4 = canvas_game.create_text(des_x-50, des_y+des_y_inter*3,font=("Arial-BoldMT", 20),anchor="nw",fill = des_color)
        canvas_game.insert(snake_description4,1," You can train your own model easily \n\n")



        rocket_description1 = canvas_game.create_text(des_x + icon_x_inter-35, des_y,font=("Arial-BoldMT", 25),anchor="nw",fill = des_color)
        canvas_game.insert(rocket_description1,1,"   Gesture Move Rocket \n\n")

        rocket_description2 = canvas_game.create_text(des_x-13 + icon_x_inter, des_y+des_y_inter,font=("Arial-BoldMT", 20),anchor="nw",fill = des_color)
        canvas_game.insert(rocket_description2,1,"  Use index finger to move\n\n")

        rocket_description3 = canvas_game.create_text(des_x-33 + icon_x_inter, des_y+des_y_inter*2,font=("Arial-BoldMT", 20),anchor="nw",fill = des_color)
        canvas_game.insert(rocket_description3,1,"  Replace mouse by your hand  \n\n")

        rocket_description4 = canvas_game.create_text(des_x-33 + icon_x_inter, des_y+des_y_inter*3,font=("Arial-BoldMT", 20),anchor="nw",fill = des_color)
        canvas_game.insert(rocket_description4,1," Try to avoid bullet and survive \n\n")

      

        qa_description1 = canvas_game.create_text(des_x + icon_x_inter*2 - 60, des_y,font=("Arial-BoldMT", 25),anchor="nw",fill = des_color)
        canvas_game.insert(qa_description1,1,"   Interesting Q&A Games \n\n")

        qa_description2 = canvas_game.create_text(des_x + icon_x_inter*2 - 70, des_y+des_y_inter,font=("Arial-BoldMT", 20),anchor="nw",fill = des_color)
        canvas_game.insert(qa_description2,1," Some intellectual multiple choices  \n\n")

        qa_description3 = canvas_game.create_text(des_x-20 + icon_x_inter*2 - 40, des_y+des_y_inter*2,font=("Arial-BoldMT", 20),anchor="nw",fill = des_color)
        canvas_game.insert(qa_description3,1," Point the correct answer by hand   \n\n")

        qa_description4 = canvas_game.create_text(des_x + icon_x_inter*2 - 40, des_y+des_y_inter*3,font=("Arial-BoldMT", 20),anchor="nw",fill = des_color)
        canvas_game.insert(qa_description4,1,"     Try to reach best grade!     \n\n")


        
        