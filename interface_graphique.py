import pygame

##crée une fenêtre


pygame.init()
screen = pygame.display.set_mode(640,640)
clock = pygame.time.Clock()


## boucle de running
running = True
while running:
    for event in pygame.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()