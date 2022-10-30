
from matplotlib.figure import Figure
from matplotlib.colors import colorConverter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import tkinter as tk


from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import font as tkFont
from subprocess import Popen, PIPE, call
from subprocess import call
import GUI_Main as main
import os
import json



class Register(tk.Frame):

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
        data_set_dir = '../User_info'

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

        def enter_home():                  
            controller.show_frame('Welcome_Page')
        
        def enter_about_us(event):                  
            controller.show_frame('About_Us')
            
        def enter_function(event):                  
            controller.show_frame('Functions')

        def enter_instruction(event):                  
            controller.show_frame('Instruction')

        

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



        # user name and register 

        register_x = 640
        register_y = 200
        register_y_inter = 70

        entry_width = 37
        # entry_left_move = 150

        user_name_var = tk.StringVar()
        user_name_var.set('user_name')
        user_name_entry = tk.Entry(self, width=entry_width, textvariable=user_name_var, validate='key')
        user_name_entry.place(x=register_x, y=register_y)
        
        password_var = tk.StringVar()
        password_var.set('password')
        password_entry = tk.Entry(self, width=entry_width, textvariable=password_var, validate='key')
        password_entry.place(x=register_x, y=register_y+register_y_inter)

        repeat_password_var = tk.StringVar()
        repeat_password_var.set('repeat password')
        repeat_password_entry = tk.Entry(self, width=entry_width, textvariable=repeat_password_var, validate='key')
        repeat_password_entry.place(x=register_x, y=register_y+register_y_inter*2)


            

        

        def create_folder(path):
            if not os.path.exists(path):
                os.makedirs(path)


        def create_json(user_name, password):
            dict_ = {}
            
            dict_['username'] = user_name
            dict_['password'] = password

            file_name = str(user_name) + '.json'
            
            sub_folder = os.path.join(data_set_dir,user_name)
            json_path = os.path.join(sub_folder, file_name)

            with open(json_path,"w") as f:
                json.dump(dict_,f,indent=2)


        def confirm():
            user_name = user_name_var.get()
            password = password_var.get()

            if repeat_password_var.get() == password_var.get():
                create_folder(os.path.join(data_set_dir,user_name))
                create_json(user_name, password)
                messagebox.showinfo('Success','Account created successfully')

                enter_home()
            else:
                messagebox.showinfo('Hinter','Check your password, it must be same')



        global confirm_btn_img
        confirm_btn_img = tk.PhotoImage(file="../GUI_material/empty_func.png")
        
        confirm_btn = tk.Button(self,
                             image=confirm_btn_img, borderwidth=0, highlightthickness=0,
                             command=confirm, relief="flat", text="Confirm", 
                             fg = 'white',compound="center",font=("Arial-BoldMT", int(17)))
        confirm_btn.place(x=register_x+120, y=register_y+register_y_inter*3)
        confirm_btn.place(width=124, height=38)

        label_x = 740
        label_y = 100

        config_label = tk.Label(self,
            text='Register', bg= bg_color,
            fg="white", font=("Arial-BoldMT", int(29)))

        config_label.place(x=label_x, y=label_y)

       

        

        



        
        
       
        


        
        