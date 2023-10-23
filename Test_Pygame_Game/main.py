import pygame
import sys

pygame.init()

size=(510,510)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game field')
width = heigth = 40
margin=10
red = (255,0,0)
white=(255,255,255)
mas = [[0]*10 for i in range(10)]
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(f'x={x_mouse} y={y_mouse}')
            column = x_mouse//(margin+width)
            row = y_mouse//(margin+heigth)
            mas[row][column]= mas[row][column]^1
    for col in range(10):
        for row in range(10):
            if mas[row][col]==1:
                color= red
            else:
                color= white
            x= col*width+(col+1)*margin
            y=row*heigth+(row+1)*margin
            pygame.draw.rect(screen,color,(x,y,width,heigth))
    pygame.display.update()

