import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 500))
background = pygame.image.load("bgspace.jpg")
background = pygame.transform.scale(background, (1000, 500))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background, (0, 0))
    pygame.display.flip()
pygame.quit()