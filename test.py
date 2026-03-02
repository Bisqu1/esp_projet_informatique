##############################################################################################################
# Crée par Mathis Robinet, Rayen Rouz, Alexis Paiement
# Crée le 2026-02-17
# 420-ESP-MA INTÉGRATION DES ACQUIS EN SCIENCES DE LA NATURE - PROJET EN INFORMATIQUE: Simulation d'une central hydroélectrique
# interactivite
##############################################################################################################
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor, QPixmap, QPen, QBrush
import sys
import loi_physique
from PySide6.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QSlider,
    QDoubleSpinBox,
    QPushButton
)



class Interface(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simulation Centrale Hydroélectrique')
        self.setGeometry(100, 100, 1200, 800)

        # Layout principal — haut et bas
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(0, 0, 0, 0)  # pas de marges
        layout_principal.setSpacing(0)

        # ---- ZONE VISUELLE (haut 60%) ----
        self.zone_visuelle = ZoneVisuelle()
        layout_principal.addWidget(self.zone_visuelle, stretch=7)

        # ---- ZONE CONTROLES (bas 40%) ----
        zone_bas = QtWidgets.QWidget()
        layout_bas = QtWidgets.QVBoxLayout(zone_bas)

        # Ligne Q
        ligne_Q = QHBoxLayout()
        self.label_Q = QtWidgets.QLabel("Débit Q:")
        self.slider_Q = QtWidgets.QSlider(Qt.Horizontal)
        self.slider_Q.setRange(0, 500)
        self.slider_Q.setValue(100)
        self.spinbox_Q = QtWidgets.QDoubleSpinBox()
        self.spinbox_Q.setRange(0, 500)
        self.spinbox_Q.setValue(100)
        self.spinbox_Q.setSuffix(" m³/s")
        ligne_Q.addWidget(self.label_Q)
        ligne_Q.addWidget(self.slider_Q)
        ligne_Q.addWidget(self.spinbox_Q)
        layout_bas.addLayout(ligne_Q)

        # Ligne h
        ligne_h = QHBoxLayout()
        self.label_h = QtWidgets.QLabel("Hauteur h:")
        self.slider_h = QtWidgets.QSlider(Qt.Horizontal)
        self.slider_h.setRange(0, 300)
        self.slider_h.setValue(50)
        self.spinbox_h = QtWidgets.QDoubleSpinBox()
        self.spinbox_h.setRange(0, 300)
        self.spinbox_h.setValue(50)
        self.spinbox_h.setSuffix(" m")
        ligne_h.addWidget(self.label_h)
        ligne_h.addWidget(self.slider_h)
        ligne_h.addWidget(self.spinbox_h)
        layout_bas.addLayout(ligne_h)

        # Ligne eta
        ligne_eta = QHBoxLayout()
        self.label_eta = QtWidgets.QLabel("Rendement η:")
        self.slider_eta = QtWidgets.QSlider(Qt.Horizontal)
        self.slider_eta.setRange(0, 100)
        self.slider_eta.setValue(90)
        self.spinbox_eta = QtWidgets.QDoubleSpinBox()
        self.spinbox_eta.setRange(0.0, 1.0)
        self.spinbox_eta.setValue(0.90)
        self.spinbox_eta.setSingleStep(0.01)
        self.spinbox_eta.setSuffix(" η")
        ligne_eta.addWidget(self.label_eta)
        ligne_eta.addWidget(self.slider_eta)
        ligne_eta.addWidget(self.spinbox_eta)
        layout_bas.addLayout(ligne_eta)

        # Ligne résultat + bouton
        ligne_bas = QHBoxLayout()
        self.label_resultat = QtWidgets.QLabel("Puissance: -- MW")
        self.button = QtWidgets.QPushButton("Début")
        ligne_bas.addWidget(self.label_resultat)
        ligne_bas.addStretch()
        ligne_bas.addWidget(self.button)
        layout_bas.addLayout(ligne_bas)

        layout_principal.addWidget(zone_bas, stretch=4)  # 40%

        ## SYNCHRONISATIONS
        #self.slider_Q.valueChanged.connect(self.spinbox_Q.setValue)
        #self.spinbox_Q.valueChanged.connect(lambda v: self.slider_Q.setValue(int(v)))
        #self.slider_h.valueChanged.connect(self.spinbox_h.setValue)
        #self.spinbox_h.valueChanged.connect(lambda v: self.slider_h.setValue(int(v)))
        #self.slider_eta.valueChanged.connect(lambda v: self.spinbox_eta.setValue(v / 100))
        #self.spinbox_eta.valueChanged.connect(lambda v: self.slider_eta.setValue(int(v * 100)))

        # CONNEXIONS CALCUL
        self.slider_Q.valueChanged.connect(self.afficher_puissance)
        self.slider_h.valueChanged.connect(self.afficher_puissance)
        self.slider_eta.valueChanged.connect(self.afficher_puissance)
        self.button.clicked.connect(self.afficher_puissance)


    #appelée qunad on clicque le bouton
    def bouton_click(self):
        valeur= self.spinbox_Q.value()
        print(f"Simulation lancée avec un débit de {valeur} m³/s")
        self.afficher_puissance(valeur)

    def afficher_puissance(self, Q: float):
        Q= self.slider_Q.value()
        h= self.slider_h.value()
        eta= self.slider_eta.value()/100    #pour reconvertir en pourcentage

        P = loi_physique.calculer_puissance(Q,h,eta)
        self.label_resultat.setText(f"Puissance: {P } MW")

class ZoneVisuelle(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)
        w = self.width()
        h = self.height()

        # Ciel
        painter.setBrush(QColor(135, 206, 235))
        painter.setPen(Qt.NoPen)
        painter.drawRect(0, 0, w, h)

        # Sol
        painter.setBrush(QColor(34, 139, 34))
        painter.drawRect(0, int(h * 0.7), w, int(h * 0.3))

        # Rivière
        painter.setBrush(QColor(0, 100, 200))
        painter.drawRect(int(w * 0.2), int(h * 0.6), int(w * 0.6), int(h * 0.15))

        # Barrage
        painter.setBrush(QColor(120, 120, 120))
        painter.drawRect(int(w * 0.45), int(h * 0.4), int(w * 0.08), int(h * 0.25))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Interface()
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