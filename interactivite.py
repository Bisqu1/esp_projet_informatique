import pygame
from pygame import MOUSEWHEEL, MOUSEBUTTONDOWN

import loi_physique
import random

#Variable équation puissance théorique central hydro
# P= densite * gravite * debit * hauteur * rendement
rendement=5
densite=4
gravite=3
debit=2
hauteur=1

#print(loi_physique.equation(rendement,densite,gravite,debit,hauteur,))


#parametre affichage
pygame.init()
screen_width= 1280
screen_height= 720
screen=pygame.display.set_mode([screen_width, screen_height])

clock = pygame.time.Clock()
running = True
centre_pos = (random.randrange(screen_width), random.randrange(screen_height))
rayon= random.randint(20,50)
dt = 0
rectangle= pygame.Rect(random.randrange(screen_width),random.randrange(screen_height), random.randint(20,100),random.randint(20,100) )
couleur= (random.randrange(255),random.randrange(255), random.randrange(255))
#boucle affichage
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #evenement clique souris
        elif event.type == MOUSEBUTTONDOWN:
            print(event)

            #cliquer sur objet
            if event.button == 1:
                if rectangle.collidepoint(event.pos):
                    couleur= "red"
        #detecte mouvement souris
        elif event.type == pygame.MOUSEMOTION:
            souris_pos= pygame.mouse.get_pos()
            print(souris_pos)



    #visuel
    screen.fill("purple")
    pygame.draw.rect(screen, couleur,rectangle )

    #interactivite


    pygame.display.flip()

    dt = clock.tick(60)/1000
pygame.quit()