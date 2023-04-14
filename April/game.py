import pygame
pygame.init()
pygame.mixer.music.load('music_1.mp3')
pygame.mixer.music.play(-1)


screen=pygame.display.set_mode((600,400))
pygame.display.set_caption('my game')
img=pygame.image.load('../Berezen/icon2.png')
pygame.display.set_icon(img)

Black=(0,0,0)
Yellow=(255,255,0)
BG=(255,255,0)

x=10
clock=pygame.time.Clock()
fl_pause = False
while True:
    while x<50:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    fl_pause = not fl_pause
                    if fl_pause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
        pygame.display.update()

        clock.tick(60)
        screen.fill(BG)
        x += 1
        font = pygame.font.SysFont('arial', x)
        follow = font.render("1", 1, Black,Yellow )
        screen.blit(follow,(250,250))
        pygame.display.update()

    while x>10:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
        clock.tick(60)
        screen.fill(BG)
        x -= 1
        font = pygame.font.SysFont('arial', x)
        follow = font.render("1", 1, Black, Yellow)
        screen.blit(follow, (250, 250))
        pygame.display.update()