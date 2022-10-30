
from matplotlib.figure import Figure
from matplotlib.colors import colorConverter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import font as tkFont
from subprocess import call
import GUI_Main as main
import os



class Controller(tk.Frame):

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

        canvas_training = tk.Canvas(
            self, bg=bg_color, height=main.height, width=main.width,
            bd=0, highlightthickness=0)

        canvas_training.place(x=0, y=0)

        thickness = 60
        length = main.width
        rec_x_ = 0
        rec_y_ = 0
        canvas_training.create_rectangle(rec_x_, rec_y_, rec_x_ + length, rec_y_ + thickness, fill="#FFFFFF", outline="")

        # ------------------------ Logo ----------------------------
        
        global logo
        logo = tk.PhotoImage(file="../GUI_material/nus_logo.png")
        logo_img = canvas_training.create_image(200, 30, image=logo)

        #  ------------------------ enter functions ----------------------------
        text_color = '#000000'

        def enter_home_page(event):                  
            controller.show_frame('Welcome_Page')
        
        def enter_about_us(event):                  
            controller.show_frame('About_Us')
            
        def enter_function(event):                  
            controller.show_frame('Functions')

        def enter_instruction(event):                  
            controller.show_frame('Instruction')

        
        # ------------------------ Box img ----------------------------
            
        global box_img
        box_img = ImageTk.PhotoImage(Image.open('../GUI_material/box2.png'))
        kk = canvas_training.create_image(main.box_x, main.box_y, image=box_img)
        l1 = canvas_training.create_line(1230, 102, 1350, 102, fill='#E0E0E0')
        l2 = canvas_training.create_line(1230, 131, 1350, 131, fill='#E0E0E0')
        l3 = canvas_training.create_line(1230, 138+23, 1350, 138+23, fill='#E0E0E0')
        l4 = canvas_training.create_line(1230, 138+23*2+5, 1350, 138+23*2+5, fill='#E0E0E0')
        
        canvas_training.itemconfig(kk, state='hidden')
        canvas_training.itemconfig(l1, state='hidden')
        canvas_training.itemconfig(l2, state='hidden')
        canvas_training.itemconfig(l3, state='hidden')
        canvas_training.itemconfig(l4, state='hidden')
        

        # ------------------------ button img ----------------------------

        label_inter = 120
        start_x = 1090
        bar_y = 24
        
        text_color = '#000000'
        
        home_page=canvas_training.create_text(start_x, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='home_page')
        canvas_training.tag_bind(home_page, '<ButtonPress-1>', enter_home_page)   
        canvas_training.insert(home_page,1,"Home page")

        function=canvas_training.create_text(start_x + label_inter+20, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='about_us_')
        canvas_training.tag_bind(function, '<ButtonPress-1>', enter_function)   
        canvas_training.insert(function,1,"Functions")

        about_us=canvas_training.create_text(start_x + label_inter*2+20, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='about_us_')
        canvas_training.tag_bind(about_us, '<ButtonPress-1>', enter_about_us)   
        canvas_training.insert(about_us,1,"About us")

        instruction=canvas_training.create_text(start_x + label_inter*3+20, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='instruction')
        canvas_training.tag_bind(instruction, '<ButtonPress-1>', enter_instruction)   
        canvas_training.insert(instruction,1,"Description")



        
        
       
        


        
        