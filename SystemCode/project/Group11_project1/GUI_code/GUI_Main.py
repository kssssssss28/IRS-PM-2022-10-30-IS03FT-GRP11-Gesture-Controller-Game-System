
import tkinter as tk
from tkinter import *
import GUI_AboutUs as us
import GUI_Instruction as ins
import GUI_games as game
import GUI_Register as register
from tkinter import messagebox
import os
import json
from PIL import Image, ImageTk
import numpy as np

# Canvas size
width = 1600
height = 680
box_x = 1290
box_y = 127

def list_dir_without_DS_Store(dir_path):
    list_ = os.listdir(dir_path)
    try:
        list_.remove('.DS_Store')
    except:
        pass
        # raise(NotFoundErr)
    return list_


class IntelligentSystem(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self, width=500, height=250)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_propagate(0)
        container.pack_propagate(0)
        self.frames = {}

        
        for F in (Welcome_Page, us.About_Us,ins.Instruction,game.Games, register.Register):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid_propagate(0) 
            frame.grid(row=0, column=0, sticky="nsew")
            

        self.show_frame("Welcome_Page")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Welcome_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller
        self.controller.title('Gesture Games')
        self.controller.state('normal')
        

        self.controller.geometry('{}x{}'.format(width, height)) 
        self.controller.maxsize(1600,700)
        parent.pack_propagate(0)
        
        
        welcome_bg_color = "#181A27"
        canvas = tk.Canvas(
            self, bg=welcome_bg_color, height=height, width=width,
            bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

      
        data_set_dir = '../User_info'
        # --------------------- Siamese ---------------------

        

        left_x = 100
        left_welcome_y = 200
        left_word = left_welcome_y + 100
        left_inter = 40

        global bg_img
        bg_img = ImageTk.PhotoImage(Image.open('../GUI_material/bg5.png'))
        kk = canvas.create_image(0, 0, image=bg_img)

        thickness = 60
        length = width
        rec_x = 0
        rec_y = 0
        canvas.create_rectangle(rec_x, rec_y, rec_x + length, rec_y + thickness, fill="#FFFFFF", outline="")

        # logo image
        global logo
        logo = tk.PhotoImage(file="../GUI_material/nus_logo.png")
        logo_img = canvas.create_image(200, 30, image=logo)
        

        def enter_home_page(event):                  
            controller.show_frame('Welcome_Page')
        
        def enter_about_us(event):                  
            controller.show_frame('About_Us')

        def enter_game():                  
            controller.show_frame('Games')

        def enter_instruction(event):                  
            controller.show_frame('Instruction')

        def enter_register(event):
            controller.show_frame('Register')



        # -------------------- Upper buttons ------------------------
        label_inter = 120
        start_x = 1190
        bar_y = 29
        
        text_color = '#000000'
        
        home_page=canvas.create_text(start_x, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='home_page')
        canvas.tag_bind(home_page, '<ButtonPress-1>', enter_home_page)   
        canvas.insert(home_page,1,"Home page")

        about_us=canvas.create_text(start_x + label_inter+20, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='about_us_')
        canvas.tag_bind(about_us, '<ButtonPress-1>', enter_about_us)   
        canvas.insert(about_us,1,"About us")


        instruction=canvas.create_text(start_x + label_inter*2+20, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='instruction')
        canvas.tag_bind(instruction, '<ButtonPress-1>', enter_instruction)   
        canvas.insert(instruction,1,"Description")


        txtid1=canvas.create_text(left_x+60, left_word,font=("Arial-BoldMT", 35),anchor="nw",fill = 'white')
        canvas.insert(txtid1,1,"Gluttonous Snake \n\n")
        
        txtid2=canvas.create_text(left_x+65, left_word + 2* left_inter,font=("Arial-BoldMT", 35),anchor="nw",fill = 'white')
        canvas.insert(txtid2,1,"Survival Rocket \n\n")

        txtid3=canvas.create_text(left_x+65, left_word + 4* left_inter,font=("Arial-BoldMT", 35),anchor="nw",fill = 'white')
        canvas.insert(txtid3,1,"Intellectual Q&A\n\n")

        txtid4=canvas.create_text(left_x+10, left_welcome_y-3,font=("Arial-BoldMT", int(50.0)),anchor="nw",fill = '#C4C2C7')
        canvas.insert(txtid4,1," Gesture Games \n")


        '''
        login 
        '''
        login_x = 1130
        login_y = 200
        login=canvas.create_text(1130, 200,font=("Arial-BoldMT", 35),anchor="nw",fill = '#C4C2C7')  
        canvas.insert(login,1,"Log in")
        line_length = 110
        below_pixel = 45
        canvas.create_line(login_x-10, login_y+below_pixel, login_x+line_length, login_y+below_pixel, fill='#C4C2C7')

        # user name
        entry_width = 34
        entry_left_move = 150
        user_name_var = tk.StringVar()
        user_name_var.set('admin')
        user_name_entry = tk.Entry(self, width=entry_width, textvariable=user_name_var, validate='key')
        user_name_entry.place(x=left_x+780+entry_left_move, y=left_word+20)


        
        # password
        password_var = tk.StringVar()
        password_var.set('admin')
        password_entry = tk.Entry(self, width=entry_width, textvariable=password_var, validate='key')
        password_entry.place(x=left_x+780+entry_left_move, y=left_word+90)



        def read_json(path):
            with open(path, "r") as f:
                data = json.load(f)
            return data

        def isRegister(username,users_folders):
            return username in users_folders
        
        def correctPassword(username,password):
            json_name = username +'.json'
            json_file_path = os.path.join(data_set_dir, username,json_name)
            user_info  =read_json(json_file_path)
            correct_password = user_info['password']
            return password == correct_password

       
        user_path = '../Position/user.json'

        def write_json(path, dict):
            with open(path,"w") as f:         
                json.dump(dict,f,indent=2)

        def login_function(event):
            
            username = user_name_var.get()
            password = password_var.get()

            user_data = {}
            user_data['current_user'] = username

            
            if username == 'admin' and password == 'admin':
                write_json(user_path, user_data)
                enter_game()
                
            else:
                users_folders = list_dir_without_DS_Store(data_set_dir)
                registered = isRegister(username,users_folders)

                if not registered:
                    messagebox.showinfo('Invalid User_name','Wrong username. \nIf you have not register, please create your own account')
                else:
                    correct_password = correctPassword(username,password)
                    if correct_password:
                        write_json(user_path, user_data)
                        enter_game()
                    else:
                        messagebox.showinfo('Wrong password','Wrong password. \n')



        btns_x = left_x+990
        
        login_button=canvas.create_text(btns_x, 520,font=("Arial-BoldMT", 23),anchor="nw",fill = 'white',tags='functions')
        canvas.tag_bind(login_button, '<ButtonPress-1>', login_function)   
        canvas.insert(login_button,1,"LOG IN")

        register_button=canvas.create_text(btns_x+120, 520,font=("Arial-BoldMT", 23),anchor="nw",fill = 'white',tags='functions')
        canvas.tag_bind(register_button, '<ButtonPress-1>', enter_register)   
        canvas.insert(register_button,1,"Register")

        
       


        


if __name__ == "__main__":
    print('------------- Welcome to Group 11 project ---------------')
    app = IntelligentSystem()
    app.mainloop()

    
