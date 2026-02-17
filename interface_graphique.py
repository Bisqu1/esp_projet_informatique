import pygame

##crée une fenêtre


pygame.init()
screen = pygame.display.set_mode((1280,640))
##clock = pygame.Clock()


## boucle de running

running = True

while running:

    ##dessins


    pygame.draw.rect(screen, color = "green", rect = (100, 200, 50, 50))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    ##clock.tick(60)


pygame.quit()

## dessins

