import pygame
pygame.init()

screen=pygame.display.set_mode((600,400))
pygame.display.set_caption('my game')
img=pygame.image.load('icon2.png')
pygame.display.set_icon(img)
font=pygame.font.SysFont('arial',32)
Yellow=(255,255,255)
Blue=(0,0,0)
BG=(0,0,0)
follow=font.render("1",1,Yellow,Blue)
follow2=font.render("2",1,Yellow,Blue)
follow3=font.render("3",1,Yellow,Blue)
follow4=font.render("4",1,Yellow,Blue)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
    screen.fill(BG)
    screen.blit(follow,(0,0))
    screen.blit(follow2,(580, 0))
    screen.blit(follow3,(580,370))
    screen.blit(follow4,(0, 370))


    pygame.display.update()