import random
import time
import pygame

class Ball:

    x = None  
    y = None  
    speed_x = None 
    speed_y = None  
    radius = None 
    color = None 

    def __init__(self, x, y, speed_x, speed_y, radius, color):
       
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        
     
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius)


    def move(self, screen):
  
        self.x += self.speed_x
        self.y += self.speed_y

    
        if self.x > W - self.radius or self.x < self.radius:
            self.speed_x = -self.speed_x


        if self.y > H - self.radius or self.y < self.radius:
            self.speed_y = -self.speed_y


        time.sleep(0.001)
        self.draw(screen)


class Player:

    radius = None
    color = None
    x = 1000
    y = 1000

    def __init__(self, radius, color):
        
        
        self.radius = radius
        self.color = color

    def move(self, screen):
 
        

        if pygame.mouse.get_focused():
            x, y = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            mouse = pygame.mouse.get_pressed()
            imp = pygame.image.load("../GUI_material/rocket_back.jpg").convert()
            imp = pygame.transform.scale(imp, (40, 40))
            screen.blit(imp, (x,y))

            self.x = x
            self.y = y


def create_ball(screen):
   
    x = random.randint(0, W)
    y = random.randint(0, H)
    speed_x = random.randint(-speed, speed)
    speed_y = random.randint(-speed, speed)
    r = 10
    
    b = Ball(x, y, speed_x, speed_y, r, ball_color)
    balls.append(b)
    b.draw(screen)

def show_text(screen, pos, text, txt_color, bg_color, font_size=30):
    cur_font = pygame.font.SysFont("SimHei", font_size)  
    text_fmt = cur_font.render(text, True, txt_color, bg_color)  
    screen.blit(text_fmt, pos)  

def close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

green = (0, 255, 0)
blue = (0, 0, 128)

close_gap = 9
balls = []
speed = 10
ball_color = '#E9E10A'
backgroud_color = '#608FB7'
text_color = '#D9BBB8'

W = 1200
H = 1200


def main():
    
    ball_nums = 30
    pygame.init()
    screen = pygame.display.set_mode((W,H))
    pygame.display.set_caption('Survival Game')

    for i in range(0, ball_nums):
       create_ball(screen)

    player = Player(8, 'red')
    text_time = "TIME:%.3d" % (time.perf_counter())

    is_loop = True
    while is_loop:

        screen.fill(backgroud_color)

        player.move(screen)
        text_time = "TIME:%.3d" % (time.perf_counter())

        for ball in balls:
            ball.move(screen)
            if abs(player.x - ball.x + 20) < close_gap and abs(player.y - ball.y+20) < close_gap:
                is_loop = False
                show_text(screen, (W/2-50, 40), text_time,  text_color, backgroud_color,  font_size=30)
                show_text(screen, (W/2 - 140, H/2-200), "Game over!",  '#C2ACB4', backgroud_color, font_size=80)
                show_text(screen, (W/2 - 140, H/2 ), "Try again, don't give up",  '#C2ACB4', backgroud_color, font_size=40)
                pygame.display.update()
                time.sleep(2)
                close()
                break      
       
        show_text(screen, (W/2-50, 40), text_time,  text_color, backgroud_color,  font_size=30)
        pygame.display.update()

        close()


        
        


if __name__ == '__main__':
    main()