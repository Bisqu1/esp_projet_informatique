##############################################################################################################
# Crée par Mathis Robinet, Rayen Rouz, Alexis Paiement
# Crée le 2026-02-17
# 420-ESP-MA INTÉGRATION DES ACQUIS EN SCIENCES DE LA NATURE - PROJET EN INFORMATIQUE: Simulation d'une central hydroélectrique
# interactivite.py
##############################################################################################################
from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor, QPixmap, QPen, QBrush, QPixmap

from matplotlib.ticker import AutoMinorLocator
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import os
import csv
import sys

import numpy as np

from loi_physique import calculs_physique
from partie_physique import AnalyseDonnees


class Interface(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.analyse = AnalyseDonnees()  # créer obj
        self.calculs = calculs_physique()
        self.initUI()
        self.P = 9

        #apelle fonction pour afficher image de départ
        self.create_image()

        #apelle la fonction pour permettre la modification d'image dans le code
        #cette fonction est necessaire pour le fonctionnement du code
        self.update()

    def initUI(self):

    # ============= FENÊTRE =========== #
        self.setWindowTitle('Simulation Central Hydroélectrique')  #titre
        self.setGeometry(100, 100, 1200, 800)  #position,dimension fenêtre
        #1200,570
    # ============ LAYOUT ============ #
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

            # -----zone Modif données(partie gauche de la zone interactive)-----
        self.panneau_Igauche = QtWidgets.QWidget()
        self.layout_gauche = QtWidgets.QVBoxLayout(self.panneau_Igauche)  # crée layout vertical pour empiler les lignes
        self.layout_interactive.addWidget(self.panneau_Igauche, stretch=1)  #prend 50% de la zone interactive

            #-----zone autre chose interactive a ajouter plutard( partie droite de la zone interactive)-------
        self.panneau_Idroit = QtWidgets.QWidget()
        self.panneau_Idroit.setStyleSheet("background-color: lightgrey;")  #temporaire pour differencier zone gauche de droite
        self.layout_droite = QtWidgets.QVBoxLayout(self.panneau_Idroit)
        self.layout_interactive.addWidget(self.panneau_Idroit, stretch=1)  #prend 50% de la zone interactive

        self.layout_droite.addWidget(self.analyse)


    # ========== WIDGETS ========== #


        #----DÉBIT (Q)-----#
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

        #---------HAUTEUR (h)----------#
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

        #-----RENDEMENT (eta)----#
        self.ligne_eta= QtWidgets.QHBoxLayout()

        self.label_eta= QtWidgets.QLabel("Rendement (η):")

        self.slider_eta = QtWidgets.QSlider(Qt.Horizontal)
        self.slider_eta.setRange(60,90)
        self.slider_eta.setValue(90)

        self.spinbox_eta= QtWidgets.QDoubleSpinBox()
        self.spinbox_eta.setRange(0.6,0.9)
        self.spinbox_eta.setValue(0.90)
        self.spinbox_eta.setSingleStep(0.01)

        self.ligne_eta.addWidget(self.label_eta)
        self.ligne_eta.addWidget(self.slider_eta)
        self.ligne_eta.addWidget(self.spinbox_eta)
        self.layout_gauche.addLayout(self.ligne_eta)

        #-----CONSOMMATION ÉNREGETIQUE MAISON (C)----#
        self.ligne_conso = QtWidgets.QHBoxLayout()

        self.label_conso = QtWidgets.QLabel("Consommation (C):")

        self.slider_conso = QtWidgets.QSlider(Qt.Horizontal)
        self.slider_conso.setRange(1, 2000)
        self.slider_conso.setValue(500)

        self.spinbox_conso = QtWidgets.QDoubleSpinBox()
        self.spinbox_conso.setRange(1,2000 )
        self.spinbox_conso.setValue(500)
        self.spinbox_conso.setSingleStep(50)

        self.ligne_conso.addWidget(self.label_conso)
        self.ligne_conso.addWidget(self.slider_conso)
        self.ligne_conso.addWidget(self.spinbox_conso)
        self.layout_gauche.addLayout(self.ligne_conso)
        self.spinbox_conso.setSuffix(" MW")

        #-----LONGUEUR DES CABLES (L)----#
        self.ligne_L = QtWidgets.QHBoxLayout()

        self.label_L = QtWidgets.QLabel("longueur cables (L): ")

        self.slider_L = QtWidgets.QSlider(Qt.Horizontal)
        self.slider_L.setRange(30, 90)
        self.slider_L.setValue(50)

        self.spinbox_L = QtWidgets.QDoubleSpinBox()
        self.spinbox_L.setRange(30, 90)
        self.spinbox_L.setValue(50)
        self.spinbox_L.setSingleStep(1)

        self.ligne_L.addWidget(self.label_L)
        self.ligne_L.addWidget(self.slider_L)
        self.ligne_L.addWidget(self.spinbox_L)
        self.layout_gauche.addLayout(self.ligne_L)
        self.spinbox_L.setSuffix(" km")

        #-----Tension (U)----#
        self.ligne_U = QtWidgets.QHBoxLayout()

        self.label_U = QtWidgets.QLabel("Tension des lignes (U): ")

        self.slider_U = QtWidgets.QSlider(Qt.Horizontal)
        self.slider_U.setRange(100, 1000)
        self.slider_U.setValue(745)

        self.spinbox_U = QtWidgets.QDoubleSpinBox()
        self.spinbox_U.setRange(100, 1000)
        self.spinbox_U.setValue(745)
        self.spinbox_U.setSingleStep(10)

        self.ligne_U.addWidget(self.label_U)
        self.ligne_U.addWidget(self.slider_U)
        self.ligne_U.addWidget(self.spinbox_U)
        self.layout_gauche.addLayout(self.ligne_U)
        self.spinbox_U.setSuffix(" kV")

    # =============== CONNEXION ================ #
        # ----CONNEXION spinbox avec slider----- pour que quand valeur de slider change, celle de spin box aussi et vice versa
            #---- connexion Q spinbox avec slider --------#
        self.slider_Q.valueChanged.connect(self.spinbox_Q.setValue)  #quand VALEUR DE SLIDER change setValue de spinbox avec nouvelle valeur de slider
        self.spinbox_Q.valueChanged.connect(self.slider_Q.setValue)  #quand VALEUR DE SPINBOX change setValue de slider avec nouvelle valeur de spinbox

            #---- connexion h spinbox avec slider --------#
        self.slider_h.valueChanged.connect(self.spinbox_h.setValue)
        self.spinbox_h.valueChanged.connect(self.slider_h.setValue)

            #----- connexion eta spinbox avec slider --------#
        self.slider_eta.valueChanged.connect(lambda v: self.spinbox_eta.setValue(v / 100))  #quand valeur slider change (entier`[0,100]) divise par 100 pour setValue de spinbox en decimal
        self.spinbox_eta.valueChanged.connect(lambda v: self.slider_eta.setValue(int(v * 100)))  #spinbox change (decimal, [0,1]) multiplie par 100 pour setValue de slider en entier

            #------ connexion conso spinbox avec slider -------#
        self.slider_conso.valueChanged.connect(self.spinbox_conso.setValue)
        self.spinbox_conso.valueChanged.connect(self.slider_conso.setValue)
            #------ connexion longueur cables spinbox avec slider -------#
        self.slider_L.valueChanged.connect(self.spinbox_L.setValue)
        self.spinbox_L.valueChanged.connect(self.slider_L.setValue)

        #------ connexion tension spinbox avec slider --------#
        self.slider_U.valueChanged.connect(self.spinbox_U.setValue)
        self.spinbox_U.valueChanged.connect(self.slider_U.setValue)





    # ============== LABEL RESULTAT =================#
        self.ligne_resultat= QtWidgets.QHBoxLayout()
        self.label_resultat = QtWidgets.QLabel("Puissance: MW")  #creation widget label pour afficher résulat puissance
        self.button = QtWidgets.QPushButton("Début")
        self.button.clicked.connect(self.bouton_click)  #quand le bouton est cliquer apelle fonction qui calcule puissance
        self.ligne_resultat.addWidget(self.label_resultat)
        self.ligne_resultat.addStretch()  #Ajout d'un espace a la ligne (layout)
        self.ligne_resultat.addWidget(self.button)  #pour que le bouton soit a droite
        self.layout_gauche.addLayout(self.ligne_resultat)
        #self.ligne_evaluation = QtWidgets.QHBoxLayout()
        #self.layout_gauche.addLayout(self.ligne_evaluation)
        #self.label_evaluation = QtWidgets.QLabel()
        #self.ligne_evaluation.addWidget(self.label_evaluation)
        self.ligne_perte =QtWidgets.QHBoxLayout()

        self.label_perte = QtWidgets.QLabel("Perte de puissance: MW")
        self.ligne_perte.addWidget(self.label_perte)
        self.layout_gauche.addLayout(self.ligne_perte)




    # ============== LABEL AVERTISSEMENTS =================#
        self.label_avertissement = QtWidgets.QLabel("")
        self.label_avertissement.setWordWrap(True)

        self.label_avertissement.setStyleSheet("""
                            QLabel {
                                color: red;
                                background-color: #fff3cd;
                                border: 1px solid black;
                                border-radius: 2px;
                                max-height: 3em;
                                min-height: 1em;
                                padding: 2px 4px;
                            }
                        """)
        self.label_avertissement.hide()  # caché par défaut

        #self.ligne_avertissement = QtWidgets.QHBoxLayout()
        #self.layout_gauche.addLayout(self.ligne_avertissement)
        #self.ligne_avertissement.addWidget(self.label_avertissement)
        self.label_avertissement.hide()
        self.layout_gauche.addWidget(self.label_avertissement)


        self.label_avertissement.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)



    # ---- CONNEXION CALCUL---- #
        self.slider_Q.valueChanged.connect(lambda: self.clear_text( puissance=True, evaluation=True, perte=True))  #lambda ignore valeur envoyé par slider quand valueChanged, car s'attend a bool
        self.slider_eta.valueChanged.connect(lambda: self.clear_text( puissance=True, evaluation=True, perte=True))
        self.slider_h.valueChanged.connect(lambda: self.clear_text( puissance=True, evaluation=True, perte=True))

        self.slider_conso.valueChanged.connect(lambda: self.clear_text(evaluation=True))
        self.slider_L.valueChanged.connect(lambda: self.clear_text(perte=True))
        #if self.slider_Q.valueChanged:
        #    self.label_resultat.clear()

        # self.slider_h.valueChanged.connect(self.afficher_puissance)  #quand valeurs des sliders change apelle fonction qui recalcule puissance
        # self.slider_eta.valueChanged.connect(self.afficher_puissance)

    # ==== appelée quand on clicque le bouton ===== #
    def bouton_click(self):
        self.afficher_puissance()
        print(f"Simulation a été lancée avec un  débit de {self.Q} m³/s, une hauteur de {self.h} m et un rendement de {self.eta}, ce qui donne une puissance de {self.P: .2f} MW .")
        self.afficher_perte()
        self.analyse.run_centrale(self.P,self.perte)


        # sert à appeler la fonction quand on clique sur le bouton
        self.update_image()

        self.analyse.afficher_graphique(self.consommation, self.perte)








    # ========== AFFICHAGE IMAGE ========== #
    def create_image(self):
        self.image_label = QLabel(self)
        self.layout_visuelle.addWidget(self.image_label)
        self.image_label.setScaledContents(True)
        pixmap = QPixmap("image/imagebarrage_lumiere0.png")
        self.image_label.setPixmap(pixmap)


    # ========== Remplacer l'image  ========== #
    # fonction qui, si appelée, va remplacer l'image par celle appropriée
    # pour le niveau de puissance.
    def update_image(self):



        # chaîne qui determine quel image prendre selon leur proportion avec la puissance
        if self.P < self.consommation * 0.10:
            chemin = QPixmap("image/imagebarrage_lumiere0.png")

        elif self.P < self.consommation * 0.20 :
            chemin = QPixmap("image/imagebarrage_lumiere1.png")

        elif self.P < self.consommation * 0.30 :
            chemin = QPixmap("image/imagebarrage_lumiere2.png")

        elif self.P < self.consommation * 0.40 :
            chemin = QPixmap("image/imagebarrage_lumiere3.png")

        elif self.P < self.consommation * 0.50 :
            chemin = QPixmap("image/imagebarrage_lumiere4.png")

        elif self.P < self.consommation * 0.60 :
            chemin = QPixmap("image/imagebarrage_lumiere5.png")

        elif self.P < self.consommation * 0.70 :
            chemin = QPixmap("image/imagebarrage_lumiere6.png")

        elif self.P < self.consommation * 0.80 :
            chemin = QPixmap("image/imagebarrage_lumiere7.png")

        elif self.P < self.consommation * 0.90 :
            chemin = QPixmap("image/imagebarrage_lumiere8.png")

        elif self.P < self.consommation :
            chemin = QPixmap("image/imagebarrage_lumiere9.png")

        else :
            chemin = QPixmap("image/imagebarrage_lumiere10.png")

        pixmap = QPixmap(chemin)

        # if else, si l'image est null ou ne peut pas être affichée retourne du texte,
        # sinon change l'image en accord avec notre chaîne if, elif. ... précédente
        if pixmap.isNull():
            self.image_label.setText("l'image n'a pas été trouvée ou n'a pas pu être affichée")
        else :
            self.image_label.setPixmap(pixmap)

    # ====== supprime le texte de ces labels ======= #
    def clear_text(self, puissance=False, evaluation= False, perte= False):
        if puissance:
            self.label_resultat.setText("Puissance: --- MW")
        #self.label_evaluation.setText("---")
        if evaluation:
            self.label_avertissement.setText("---")
            #self.label_avertissement.hide()
        if perte:
            self.label_perte.setText("Perte puissance: --- MW")


    # ====== affichage de la puissance ======= #
    def afficher_puissance(self):
        #utilise valeur du slider x
        self.Q= self.slider_Q.value()
        self.h= self.slider_h.value()
        self.eta= self.slider_eta.value()/100  #divise par 100 pour reconvertir en decimal

        self.P = self.calculs.calculer_puissance(self.Q,self.h,self.eta)/1_000_000  #diviser par 1million pour convertir en mega watts
        self.label_resultat.setText(f"Puissance: {self.P:.2f} MW")  #modifie label resultat en ajoutant valeur puissance
        self.verifier_realisme()

    # ======= vérification du réalisme des valeurs ======= #
    def verifier_realisme(self):
        avertissements = []

        # prend la valeur de la consommation et la retourne en float pour la chaîne
        self.consommation = self.slider_conso.value()

        # Limites pour une centrale de village (72 MW)
        if self.Q > 400:
            avertissements.append(f"⚠️ Débit trop élevé ({self.Q} m³/s), un village à typiquement besoin de moins de 400 m³/s de débit.")
        if self.Q < 10:
            avertissements.append(f"⚠️ Débit trop faible ({self.Q} m³/s), production négligeable.")

        if self.h > 200:
            avertissements.append(f"⚠️ Hauteur de chute très élevée ({self.h} m), rare pour un village.")
        if self.h < 2:
            avertissements.append(f"⚠️ Hauteur de chute trop faible ({self.h} m), irréaliste.")

        if self.P > self.consommation:
            avertissements.append(f"⚠️ Puissance de {self.P:.1f} MW dépasse les besoins du village de {self.P- self.consommation:.1f} MW.")
        elif self.P < self.consommation and (self.Q > 0 and self.h > 0):
            avertissements.append(
                f"⚠️ Puissance de {self.P:.1f} MW est insuffisante pour un village, il lui manque {self.consommation-self.P:.1f} MW.")

        if avertissements:
            self.label_avertissement.setText("\n".join(avertissements))
            self.label_avertissement.show()
        else:
            self.label_avertissement.hide()
            
    # ====== affichage de la perte de puissance ======= #
    def afficher_perte(self):
        self.U = self.spinbox_U.value()
        self.L= self.spinbox_L.value()


        self.perte = self.calculs.calculer_pertes(self.calculs.puissance_W, self.L, self.U)
        self.label_perte.setText(f"Perte puissance: {self.perte:.2f} MW")  #modifie label resultat en ajoutant valeur puissance




# system exit
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Interface()
    widget.show()
    sys.exit(app.exec())


