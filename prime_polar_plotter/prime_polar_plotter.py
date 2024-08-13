import pygame
import math


scale = int(input("Enter scaling factor\nThe bigger the number the more you zoom out (200 is pretty good)"))# downscaling

pygame.init()


width,height = 1000,600
screen = pygame.display.set_mode((width,height))

running = True

centrex,centrey = (width//2, height//2)
white = (255,255,255)
cyan = (112, 243, 255)
font_size = 20
font = pygame.font.SysFont(None, font_size)
ls = []
def plot(r,theta,color):
    x = centrex + int(r * math.sin(theta))
    y = centrey + int(r* math.cos(theta))
    pygame.draw.circle(screen,color,(x,y),1)
    
def plot_line(r,theta):
    x = centrex + int(r * math.sin(theta))
    y = centrey + int(r* math.cos(theta))
    pygame.draw.line(screen,cyan,(centrex,centrey),(x,y),2)

def ls_stuff(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

kk = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    plot(0,0,white)
    kk += 1
    if (ls_stuff(kk)):
        ls.append(kk)
    text = font.render('Prime: '+ str(kk), True, (255,255,255))
    text_rect = text.get_rect(center=(width- 200, height -100))
    screen.blit(text, text_rect)

    for j in ls:
        plot(j/scale,j,white)
    pygame.display.flip()

    plot(j/scale,j,cyan)
    

pygame.quit()