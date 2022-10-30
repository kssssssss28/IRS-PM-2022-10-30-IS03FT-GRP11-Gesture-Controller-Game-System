import tkinter as tk
from PIL import Image, ImageTk
import GUI_Main as main



class About_Us(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller
        self.controller.title('MetaMedAI')
        self.controller.state('normal')
        

        self.controller.geometry('{}x{}'.format(main.width, main.height)) #页面大小
        self.controller.maxsize(1600,680)
        parent.pack_propagate(0)

        
        welcome_bg_color = "#2D2D2D"
        canvas_about = tk.Canvas(
            self, bg=welcome_bg_color, height=main.height, width=main.width,
            bd=0, highlightthickness=0, relief="ridge")
        canvas_about.place(x=0, y=0)

        

        global bg_img
        bg_img = ImageTk.PhotoImage(Image.open('../GUI_material/bg5.png'))
        kk = canvas_about.create_image(0, 0, image=bg_img)


        thickness = 60
        length = main.width
        rec_x_ = 0
        rec_y_ = 0
        canvas_about.create_rectangle(rec_x_, rec_y_, rec_x_ + length, rec_y_ + thickness, fill="#FFFFFF", outline="")

        # logo image
        global logo
        logo = tk.PhotoImage(file="../GUI_material/nus_logo.png")
        logo_img = canvas_about.create_image(200, 30, image=logo)


        def enter_home_page(event):                  
            controller.show_frame('Welcome_Page')
        
        def enter_about_us(event):                  
            controller.show_frame('About_Us')

        def enter_instruction(event):                  
            controller.show_frame('Instruction')


        label_inter = 120
        start_x = 1190
        bar_y = 29
        
        text_color = '#000000'
        
        home_page=canvas_about.create_text(start_x, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='home_page')
        canvas_about.tag_bind(home_page, '<ButtonPress-1>', enter_home_page)   
        canvas_about.insert(home_page,1,"Home page")

        about_us=canvas_about.create_text(start_x + label_inter+20, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='about_us_')
        canvas_about.tag_bind(about_us, '<ButtonPress-1>', enter_about_us)   
        canvas_about.insert(about_us,1,"About us")


        instruction=canvas_about.create_text(start_x + label_inter*2+20, bar_y,font=("Arial-BoldMT", 17),anchor="nw",fill = text_color,tags='instruction')
        canvas_about.tag_bind(instruction, '<ButtonPress-1>', enter_instruction)   
        canvas_about.insert(instruction,1,"Description")
        
        output_x = 540
        output_y = 180

        # canvas_about.create_rectangle(output_x, output_y, output_x + 1030, output_y + 450, fill='#747474', outline="")
        
        
        ltc_head = 'LUO TIANCHEN: '

        ks_head = 'KUANG SHAN: '

        xx_head = 'XIANG XU: '

        ltc_line1 = ' Collected 10k+ hands features from self-recording video, responsible for feature pre-processing '
        ltc_line2 = ' Trained gestures classification model to control the gluttonous snake game'
        ltc_line3 = ' Responsible for GUI implement and combining model inference results with GUI and games'


        ks_line1 = ' Implemented Survival game and combined hand gesture controller with the game '
        ks_line2 = ' Responsible for system design, code structure construction and camera invoking'
        ks_line3 = ' Responsible for backend and Graphic User Interface implement'

        xx_line1 = ' Implemented Intellectual Q&A game and implemented hand position analysis code'
        xx_line2 = ' Responsible for background removal algorithm and its result with OpenCV interface'
        xx_line3 = ' Construct Q&A SQL database and made visual based interactive game'

        t1_x = 650

        t1_y = 190

        author_inter = 160
        ty_inter = 38

        '''
        Dear future ISS students, if you are reading my comments here, a kindly reminder:

        Be careful when choosing your teammates for projects 
        Be careful when choosing your teammates for projects
        Be careful when choosing your teammates for projects

        I made this stup*d system within 5 days because of my teammate cannot do anything and didn't tell us until 48 hours before due date.
        Be careful and check their coding and AI knowledge ability before build your team.
        '''


        canvas_about.create_text(t1_x, t1_y, anchor='w',text=ltc_head,font=('Arial-BoldMT', 22),fill = '#FFFFFF')
        canvas_about.create_text(t1_x, t1_y + author_inter, anchor='w',text=ks_head,font=('Arial-BoldMT', 22),fill = '#FFFFFF')
        canvas_about.create_text(t1_x, t1_y + author_inter*2, anchor='w',text=xx_head,font=('Arial-BoldMT', 22),fill = '#FFFFFF')


        canvas_about.create_text(t1_x, t1_y + ty_inter, anchor='w',text=ltc_line1,font=('bold', 22),fill = '#FFFFFF')
        canvas_about.create_text(t1_x, t1_y + ty_inter*2, anchor='w',text=ltc_line2,font=('bold', 22),fill = '#FFFFFF')
        canvas_about.create_text(t1_x, t1_y + ty_inter*3, anchor='w',text=ltc_line3,font=('bold', 22),fill = '#FFFFFF')

        canvas_about.create_text(t1_x, t1_y + ty_inter+ author_inter, anchor='w',text=ks_line1,font=('bold', 22),fill = '#FFFFFF')
        canvas_about.create_text(t1_x, t1_y + ty_inter*2+ author_inter, anchor='w',text=ks_line2,font=('bold', 22),fill = '#FFFFFF')
        canvas_about.create_text(t1_x, t1_y + ty_inter*3+ author_inter, anchor='w',text=ks_line3,font=('bold', 22),fill = '#FFFFFF')

        canvas_about.create_text(t1_x, t1_y + ty_inter+ author_inter*2, anchor='w',text=xx_line1,font=('bold', 22),fill = '#FFFFFF')
        canvas_about.create_text(t1_x, t1_y + ty_inter*2+ author_inter*2, anchor='w',text=xx_line2,font=('bold', 22),fill = '#FFFFFF')
        canvas_about.create_text(t1_x, t1_y + ty_inter*3+ author_inter*2, anchor='w',text=xx_line3,font=('bold', 22),fill = '#FFFFFF')
        

        txt_y = 100
        line_txt_y_inter = 50

        members_line_x = 140
        move_right = 20

        workers_txt=canvas_about.create_text(130, txt_y,font=("Arial-BoldMT", int(35.0)),anchor="nw",fill = '#6FACB5')
        canvas_about.insert(workers_txt,1,"Group Members\n")

        canvas_about.create_line(members_line_x-5+ move_right, txt_y + line_txt_y_inter, 353+ move_right, txt_y + line_txt_y_inter, fill='#6FACB5')

        company_txt = canvas_about.create_text(910, txt_y,font=("Arial-BoldMT", int(35.0)),anchor="nw",fill = '#6FACB5')
        canvas_about.insert(company_txt,1,"Our contribution\n")

        canvas_about.create_line(945, txt_y + line_txt_y_inter, 1162, txt_y + line_txt_y_inter, fill='#6FACB5')

        photo_width = 120
        photo_height = 160

        row1_x = 130
        row1_y = 255
        row2_y = 500
        x_inter = 220

        ltc = 'LUO TIANCHEN'
        xx = 'XIANG XU'
        ks = 'KUANG SHAN'
        tsq = 'TONG SHIQIN'

        move_left = 40
        canvas_about.create_text(100+ move_right-move_left, 365, anchor='w',text=ltc,font=("Arial-BoldMT", 21),fill = '#FFFFFF')
        canvas_about.create_text(320+ move_right-move_left, 365, anchor='w',text=ks,font=('Arial-BoldMT', 21),fill = '#FFFFFF')
        canvas_about.create_text(100+ move_right-move_left+20, 610, anchor='w',text=xx,font=('Arial-BoldMT', 21),fill = '#FFFFFF')
        canvas_about.create_text(320+ move_right-move_left, 610, anchor='w',text=tsq,font=('Arial-BoldMT', 21),fill = '#FFFFFF')
        

        global ltc_img
        ltc_img = ImageTk.PhotoImage(Image.open('../GUI_material/ltc_img.png').resize((photo_width,photo_height)))
        canvas_about.create_image(row1_x+ move_right, row1_y, image=ltc_img)

        global ks_img
        ks_img = ImageTk.PhotoImage(Image.open('../GUI_material/ks_img.png').resize((photo_width,photo_height)))
        canvas_about.create_image(row1_x + x_inter+ move_right, row1_y, image=ks_img)

        global xx_img
        xx_img = ImageTk.PhotoImage(Image.open('../GUI_material/xx_img.png').resize((photo_width,photo_height)))
        canvas_about.create_image(row1_x+ move_right, row2_y, image=xx_img)

        global tsq_img
        tsq_img = ImageTk.PhotoImage(Image.open('../GUI_material/tsq_img.png').resize((photo_width,photo_height)))
        canvas_about.create_image(row1_x + x_inter+ move_right, row2_y, image=tsq_img)

        

        

        
    
        

      
        
        
          
