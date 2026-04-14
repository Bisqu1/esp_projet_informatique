##############################################################################################################
# Crée par Mathis Robinet, Rayen Rouz, Alexis Paiement
# Crée le 2026-02-17
# 420-ESP-MA INTÉGRATION DES ACQUIS EN SCIENCES DE LA NATURE - PROJET EN INFORMATIQUE: Simulation d'une central hydroélectrique
# interactivite
##############################################################################################################
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor, QPixmap, QPen, QBrush, QPixmap, Qt
import sys
from partie_physique import Graphique
from matplotlib.ticker import AutoMinorLocator
import loi_physique
import partie_physique
import numpy
import matplotlib.pyplot as plt
import os
import csv
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
#from visuel import ZoneVisuelle

#--------AVEC LAYOUT ---------

class Interface(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.affichage_image("image/imagebarragetest1.png")
    def initUI(self):

    #=============FENÊTRE ===========
        self.setWindowTitle('Simulation Central Hydroélectrique')  #titre
        self.setGeometry(100, 100, 1200, 800)  #position,dimension fenêtre

    #============LAYOUT============
        #-----LAYOUT PRINCIPAL--------
        self.layout_principal= QtWidgets.QVBoxLayout(self)  #crée un layout verticale(V) (Q(V/H)Box)

        #-------ZONE VISUELLE-------
        self.zone_visuelle = QtWidgets.QWidget()  #crée zone ou tout le visuelle va être (haut)
        self.zone_visuelle.setStyleSheet("background-color: lightblue;")
        self.layout_visuelle= QtWidgets.QVBoxLayout(self.zone_visuelle)
        self.layout_principal.addWidget(self.zone_visuelle, stretch=7)  #ajoute la zone au layout principal qui prend de 70% de la hauteur du layout principal

        #---------ZONE INTERACTIVE--------
        self.zone_interactive= QtWidgets.QWidget()  #crée zone ou tout interactif va etre (bas)
        self.layout_interactive= QtWidgets.QHBoxLayout(self.zone_interactive)  #crée layout horizontal a l'interieur de zone_interactive
        self.layout_principal.addWidget(self.zone_interactive, stretch=3)  # ajoute la zone au layout principal en prennant 30% du layout principal

            # -----zone Modif donne(partie gauche de la zone interactive)-----
        self.panneau_Igauche = QtWidgets.QWidget()
        self.layout_gauche = QtWidgets.QVBoxLayout(self.panneau_Igauche)  # crée layout vertical pour empiler les lignes
        self.layout_interactive.addWidget(self.panneau_Igauche, stretch=1)  #prend 50% de la zone interactive

            #-----zone autre chose interactive a ajouter plutard( partie droite de la zone interactive)-------
        self.panneau_Idroit = QtWidgets.QWidget()
        self.panneau_Idroit.setStyleSheet("background-color: lightgrey;")  #temporaire pour differencier zone gauche de droite
        self.graphique = Graphique()
        self.layout_droite = QtWidgets.QVBoxLayout(self.panneau_Idroit)
        self.layout_interactive.addWidget(self.panneau_Idroit, stretch=1)  #prend 50% de la zone interactive
        #self.fig,self.ax = plt.subplots()
        #self.canvas = FigureCanvas(self.fig)
        #self.layout_droite.addWidget(self.canvas)
        self.layout_droite.addWidget(self.graphique)


    #==========WIDGETS==========


        #----DÉBIT (Q)-----
        self.ligne_Q= QtWidgets.QHBoxLayout()  #crée layout horizontal qui va contenir toutes interactions avec  débit

        self.label_Q =QtWidgets.QLabel("débit (Q):")  #creation widget label

        self.slider_Q = QtWidgets.QSlider(Qt.Horizontal)  #creation widget slider horizontal
        self.slider_Q.setRange(0,500)  #valeur max et min
        self.slider_Q.setValue(200)  #valeur depart


        self.spinbox_Q = QtWidgets.QSpinBox()  #creation widget doublespinbox
        self.spinbox_Q.setSuffix(" m³/s ")  # suffix(unité de mesure) de la valeur de doublespinbox
        self.spinbox_Q.setRange(0, 500)
        self.spinbox_Q.setValue(100)
        self.spinbox_Q.setSingleStep(5)  #Bond

        #ajoute les 3 widgets sur la ligne de gauche a droit
        self.ligne_Q.addWidget(self.label_Q)
        self.ligne_Q.addWidget(self.slider_Q)
        self.ligne_Q.addWidget(self.spinbox_Q)
        self.layout_gauche.addLayout(self.ligne_Q)  #ajoute ligne compltète(Q) a la zone au layout interactive

        #----HAUTEUR (h)----------
        self.ligne_h= QtWidgets.QHBoxLayout()

        self.label_h = QtWidgets.QLabel("hauteur (h):")

        self.slider_h = QtWidgets.QSlider(Qt.Horizontal)
        self.slider_h.setRange(0,300)
        self.slider_h.setValue(50)

        self.spinbox_h = QtWidgets.QSpinBox()
        self.spinbox_h.setRange(0, 300)
        self.spinbox_h.setValue(50)
        self.spinbox_h.setSuffix(" m")

        self.ligne_h.addWidget(self.label_h)
        self.ligne_h.addWidget(self.slider_h)
        self.ligne_h.addWidget(self.spinbox_h)
        self.layout_gauche.addLayout(self.ligne_h)

        #-----RENDEMENT (eta)----
        self.ligne_eta= QtWidgets.QHBoxLayout()

        self.label_eta= QtWidgets.QLabel("Rendement (η):")

        self.slider_eta = QtWidgets.QSlider(Qt.Horizontal)
        self.slider_eta.setRange(0,100)
        self.slider_eta.setValue(90)

        self.spinbox_eta= QtWidgets.QDoubleSpinBox()
        self.spinbox_eta.setRange(0.0,1.0)
        self.spinbox_eta.setValue(0.90)
        self.spinbox_eta.setSingleStep(0.01)

        self.ligne_eta.addWidget(self.label_eta)
        self.ligne_eta.addWidget(self.slider_eta)
        self.ligne_eta.addWidget(self.spinbox_eta)
        self.layout_gauche.addLayout(self.ligne_eta)

    #===============CONNEXION================
        # ----CONNEXION spinbox avec slider----- pour que quand valeur de slider change, celle de spin box aussi et vice versa
            #---- connexion Q spinbox avec slider --------
        self.slider_Q.valueChanged.connect(self.spinbox_Q.setValue)  #quand VALEUR DE SLIDER change setValue de spinbox avec nouvelle valeur de slider
        self.spinbox_Q.valueChanged.connect(self.slider_Q.setValue)  #quand VALEUR DE SPINBOX change setValue de slider avec nouvelle valeur de spinbox

            #---- connexion h spinbox avec slider --------
        self.slider_h.valueChanged.connect(self.spinbox_h.setValue)
        self.spinbox_h.valueChanged.connect(self.slider_h.setValue)

            #---- connexion eta spinbox avec slider --------
        self.slider_eta.valueChanged.connect(lambda v: self.spinbox_eta.setValue(v / 100))  #quand valeur slider change (entier`[0,100]) divise par 100 pour setValue de spinbox en decimal
        self.spinbox_eta.valueChanged.connect(lambda v: self.slider_eta.setValue(int(v * 100)))  #spinbox change (decimal, [0,1]) multiplie par 100 pour setValue de slider en entier



        # ---- CONNEXION CALCUL----
        self.slider_Q.valueChanged.connect(self.afficher_puissance)
        self.slider_h.valueChanged.connect(self.afficher_puissance)  #quand valeurs des sliders change apelle fonction qui recalcule puissance
        self.slider_eta.valueChanged.connect(self.afficher_puissance)

    # ==============LABEL RESULTAT=================
        self.ligne_bas= QtWidgets.QHBoxLayout()
        self.label_resultat = QtWidgets.QLabel("Puissance: MW")  #creation widget label pour afficher résulat puissance
        self.button = QtWidgets.QPushButton("Début")
        self.button.clicked.connect(self.bouton_click)  #quand le bouton est cliquer apelle fonction qui calcule puissance
        self.ligne_bas.addWidget(self.label_resultat)
        self.ligne_bas.addStretch()  #Ajout d'un espace a la ligne (layout)
        self.ligne_bas.addWidget(self.button)  #pour que le bouton soit a droite
        self.layout_gauche.addLayout(self.ligne_bas)

    # ========== AFFICHAGE IMAGE ==========
    def affichage_image(self,image_path):
        self.image_label = QLabel(self)
        self.layout_visuelle.addWidget(self.image_label)
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

    #appelée quand on clicque le bouton
    def bouton_click(self):

        self.afficher_puissance()
        print(f"Simulation a été lancée avec un  débit de {self.Q} m³/s, une hauteur de {self.h} m et un randement de {self.eta}, ce qui donne une puissance de {self.P:.2f} .")

        #print(powers)
        self.graphique.run_centrale(self.Q, self.h, self.eta)
        #self.figure = partie_physique.run_centrale(Q, h, eta)
        #self.canvas = FigureCanvas(self.figure)
        #self.layout_droite.addWidget(self.canvas)
        #print(self.y)


    def afficher_puissance(self):
        #utilise valeur du slider x
        self.Q= self.slider_Q.value()
        self.h= self.slider_h.value()
        self.eta= self.slider_eta.value()/100  #divise par 100 pour reconvertir en decimal

        self.P = loi_physique.calculer_puissance(self.Q,self.h,self.eta)/1_000_000
        self.label_resultat.setText(f"Puissance: {self.P:.2f} MW")  #modifie label resultat en ajoutant valeur puissance

    #def afficher_graphique(self,powers):
    #    x = list(range(1, len(powers) + 1))
    #    self.ax.clear()
    #    self.ax.scatter(x, [val for val in powers],s=10,color='steelblue', zorder=3)
    #    self.ax.set_xlabel("Numéro de run")
    #    self.ax.set_ylabel("Puissance (MW)")
    #    self.ax.set_title("Puissance par run")
    #    self.ax.minorticks_on()
    #    self.ax.set_xticks(x)
    #    self.y = np.arange(0,max(powers), 200)
    #    self.ax.set_yticks(self.y)
    #    #self.xaxis.set_minor_locator(AutoMinorLocator())
    #    self.ax.grid( color="grey", linestyle="-", linewidth=.5, alpha=0.6)
    #    self.fig.tight_layout()
    #    self.canvas.draw()  # rafraîchit le canvas Qt




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Interface()
    widget.show()
    sys.exit(app.exec())
#


##############################################################################################################
# Crée par Mathis Robinet, Rayen Rouz, Alexis Paiement
# Crée le 2026-02-17
#420-ESP-MA INTÉGRATION DES ACQUIS EN SCIENCES DE LA NATURE - PROJET EN INFORMATIQUE: Simulation d'une central hydroélectrique
##############################################################################################################
import numpy
import matplotlib.pyplot as plt
import csv
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


from matplotlib.backends.backend_template import FigureCanvas

import loi_physique
import os



class Graphique(FigureCanvasQTAgg):
    def __init__(self):
        # ======= FIGURE ========
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)

        # ======DONNÉES =======
        self.filename = "scatter_power.csv"
        self.powers = []


    def run_centrale(self,Q, h, eta, g=9.81, rho=1000):
        P = loi_physique.calculer_puissance(Q,h,eta,g,rho)/1000000

        if len(self.powers) >= 10:
                del self.powers[0]  # supprime la plus vieille valeur
        self.powers.append(P)  # ajoute toujours le nouveau p
        self.sauvegarder_csv(P)
        self.afficher_graphique()

    def sauvegarder_csv(self,P):
        with open("scatter_power.csv", 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for power_val in self.powers:
                writer.writerow([power_val])

    def afficher_graphique(self):
        if not self.powers:
            return
        x = list(range(1, len(self.powers) + 1))
        self.ax.clear()
        self.ax.scatter(x, self.powers, s=10, color='steelblue', zorder=3)
        self.ax.set_xlabel("Numéro de run")
        self.ax.set_ylabel("Puissance (MW)")
        self.ax.set_title("Puissance par run")
        self.ax.minorticks_on()
        self.ax.set_xticks(x)
        self.y = np.arange(0, max(self.powers), 200)
        self.ax.set_yticks(self.y)
        # self.xaxis.set_minor_locator(AutoMinorLocator())
        self.ax.grid(color="grey", linestyle="-", linewidth=.5, alpha=0.6)
        self.fig.tight_layout()
        self.draw()  # rafraîchit le canvas Qt

