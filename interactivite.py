import pygame
import loi_physique
rendement=5
densite=4
gravite=3
debit=2
hauteur=1

print(loi_physique.equation(rendement,densite,gravite,debit,hauteur,))


#parametre affichage
pygame.init()
screen_width= 900
screen_height= 400
screen=pygame.display.set_mode([screen_width, screen_height])
#clock = pygame.time.Clock()
running = True
centre_pos = (screen_width/2, screen_height/2)
#dt = 0


#boucle affichage


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #
    screen.fill("purple")
    pygame.draw.circle(screen, "green",centre_pos,100 )

    pygame.display.flip()
    #dt = clock.tick(60)/1000
pygame.quit()