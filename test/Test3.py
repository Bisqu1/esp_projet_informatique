import sys
from PySide6 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Simulation Centrale Hydroélectrique')
        self.setGeometry(100, 100, 600, 400)

        # --- Widgets ---
        self.button = QtWidgets.QPushButton("Simuler")

        self.doublespinbox = QtWidgets.QDoubleSpinBox()
        self.doublespinbox.setSuffix(" m³/s")
        self.doublespinbox.setRange(0, 500)  # débit min/max
        self.doublespinbox.setValue(100)  # valeur de départ
        self.doublespinbox.setSingleStep(5)  # incrément par flèche

        self.label_resultat = QtWidgets.QLabel("Puissance : MW")

        # --- Layout ---
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.doublespinbox)  # ← manquait!
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label_resultat)

        # --- Connexions ---
        self.button.clicked.connect(self.on_bouton_click)
        self.doublespinbox.valueChanged.connect(self.on_debit_change)

    # Appelé quand la spinbox change
    def on_debit_change(self, valeur: float):
        print(f"Nouveau débit : {valeur} m³/s")
        self.calculer_puissance(valeur)

    # Appelé quand on clique le bouton
    def on_bouton_click(self):
        valeur = self.doublespinbox.value()
        print(f"Simulation lancée avec {valeur} m³/s")
        self.calculer_puissance(valeur)

    # Logique physique centralisée ici
    def calculer_puissance(self, debit: float):
        # P = η * ρ * g * h * Q
        eta = 0.9  # rendement turbine
        rho = 1000  # densité eau (kg/m³)
        g = 9.81  # gravité
        h = 50  # hauteur de chute (m) ← sera un slider plus tard

        puissance_W = eta * rho * g * h * debit
        puissance_MW = puissance_W / 1_000_000

        self.label_resultat.setText(f"Puissance : {puissance_MW:.2f} MW")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())



##Variable équation puissance théorique central hydro (Test)
## P= densite * gravite * debit * hauteur * rendement
#rendement=5
#densite=4
#gravite=3
#debit=2
#hauteur=0
#
##print(loi_physique.equation(rendement,densite,gravite,debit,hauteur,))
#
#
##parametre affichage
#pygame.init()
#screen_width= 1280
#screen_height= 720
#screen=pygame.display.set_mode([screen_width, screen_height])
#
#clock = pygame.time.Clock()
#running = True
#centre_pos = (random.randrange(screen_width), random.randrange(screen_height))
#rayon= random.randint(20,50)
#dt = 0
##rectangle= pygame.Rect(random.randrange(screen_width),random.randrange(screen_height), random.randint(20,100),random.randint(20,100) )
#rectangle= pygame.Rect(screen_width/2,screen_height/2, random.randint(20,100),random.randint(20,100) )
#couleur= (random.randrange(255),random.randrange(255), random.randrange(255))
##boucle affichage
#while running:
#    # poll for events
#    # pygame.QUIT event means the user clicked X to close your window
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#        #evenement clique souris
#        elif event.type == MOUSEBUTTONDOWN:
#            print(event)
#
#            #cliquer sur objet
#            if event.button == 1:
#                if rectangle.collidepoint(event.pos):
#                    couleur= "red"
#        #detecte mouvement souris
#        elif event.type == pygame.MOUSEMOTION:
#            souris_pos= pygame.mouse.get_pos()
#            print(souris_pos)
#
#
#
#    #visuel
#    screen.fill("purple")
#    pygame.draw.rect(screen, couleur,rectangle )
#
#    #interactivite
#
#
#    pygame.display.flip()
#
#    dt = clock.tick(60)/1000
#pygame.quit()