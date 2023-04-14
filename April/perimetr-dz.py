import pygame

pygame.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
x = 50
y = 50
size = 50
speed = 0.5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if x < screen_width - size and y == 50:
        x += speed
    elif x == screen_width - size and y < screen_height - size:
        y += speed
    elif y == screen_height - size and x > 50:
        x -= speed
    elif x == 50 and y > 50:
        y -= speed
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, size, size))
    pygame.display.flip()
pygame.quit()

