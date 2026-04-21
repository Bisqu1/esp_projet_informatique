##############################################################################################################
# Crée par Mathis Robinet, Rayen Rouz, Alexis Paiement
# Crée le 2026-02-17
# 420-ESP-MA INTÉGRATION DES ACQUIS EN SCIENCES DE LA NATURE - PROJET EN INFORMATIQUE: Simulation d'une central hydroélectrique
#  partie-physique.py
##############################################################################################################
import numpy as np
import matplotlib.pyplot as plt
import csv

from matplotlib.lines import lineStyles

import loi_physique
import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class AnalyseDonnees(FigureCanvasQTAgg):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.ax2 = self.ax.twinx()  #deuxième axe y pour mieux voir perte puissance (trop grande difference d'echelle entre puissance produit et perte
        super().__init__(self.fig)

        self.filename = "scatter_power.csv"
        self.powers = []
        self.powers_pertes = []
        #self.charger_csv()

    def evaluation_puissance(self,p):
        # print(p / 1000, "kW")
        #
        if p < 72:
            return f"Il n'y a pas assez de puissance pour alimenter tous les habitants du village, il manque {abs(p-72): .2f} MW"
        else:
            return f"Il y a {p - 72: .2f} MW en surplus"

    def run_centrale(self,p,perte):
        #rendement = float(input("Quelle est le rendement de la centrale: "))
        #while not (0.6 <= eta <= 0.9):
        #    print("Le rendement de la centrale doit être compris entre 0.6 et 0.9")
        #    eta = float(input("Quelle est le rendement de la centrale: "))
    #
        ##débit = float(input("Quelle est le débit d'eau: "))
        #while not (10 <= Q <= 1000):
        #    print("Le débit de la centrale doit être compris entre 10 et 1000 m³/s")
        #    Q = float(input("Quelle est le débit d'eau: "))

        ##Fichier CSV

        if len(self.powers) >= 10:
            del self.powers[0]  # supprime la plus vieille valeur
            del self.powers_pertes[0]
        self.powers.append(p)  # ajoute toujours le nouveau p
        self.powers_pertes.append(perte)
        self.sauvegarder_csv(p)
        return self.powers


    #def charger_csv(self):
    #    """
    #    charge l'historique des anciens runs depuis scatter_power.csv
    #    appelée automatiquement dans __init__
    #    réinitialise self.power si scatter_power.csv ne fonctionne pas
    #    """
    #    if os.path.exists(self.filename):
    #        try:
    #            with open(self.filename, newline='') as csvfile:
    #                reader = csv.reader(csvfile)
    #                for row in reader:
    #                    if row:
    #                        self.powers.append(float(row[0]))
    #        except (ValueError, IOError) as e:
    #            print(f"Avertissement : erreur de lecture du CSV ({e}). Réinitialisation.")
    #            self.powers = []

    def sauvegarder_csv(self,p):
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([p])

    def afficher_graphique(self, consommation, perte, puissance):
        self.x = list(range(1, len(self.powers) + 1))
        self.ax2.clear()

        #perte puissance
        self.ax2.scatter(self.x, self.powers_pertes, s=10, color='orange', zorder=3, label=f"Pertes ({perte: .2f} MW)")
        self.ax2.set_ylabel("Pertes (MW)", fontsize=8, color='orange')
        self.ax2.yaxis.set_label_position("right")
        self.ax2.yaxis.tick_right()
        #self.ax2.plot(self.x,self.powers_pertes, linestyle="--", marker="*",color="y")

        #puissance
        couleurs = ['green' if p >= consommation else 'red' for p in self.powers]
        self.ax.clear()
        self.ax.scatter(self.x, self.powers, s=10, color=couleurs, zorder=3, label=f"Puissance ({puissance: .2f}MW)")
        self.ax.set_xlabel("Numéro de simulation", fontsize=8)
        self.ax.set_ylabel("Puissance (MW)", fontsize=8)
        self.ax.set_title("Puissance par simulation", fontsize=10)
        self.ax.minorticks_on()
        self.ax.set_xticks(self.x)
        # if max(powers)> 0:
        # print(f"powers max: {max(self.powers)}")
        # print(f"nbr ticks: {len(np.arange(0, max(powself.powersers), 200))}")

        # graduation: 0, max(self.powers, self.powers_pertes, consommation), 200
        #self.y = np.arange(0, max(self.powers), 200)
        self.y = np.arange(0, max(max(self.powers), max(self.powers_pertes), consommation), 200)
        self.ax.set_yticks(self.y)
        # self.xaxis.set_minor_locator(AutoMinorLocator())
        #self.ax.plot(self.x,self.powers, linestyle="-", marker=".",color="c" )

        #consommation
        self.ax.axhline( consommation, color='red', linestyle='--', linewidth=1, label=f"Consommation ({consommation} MW)")

        self.ax.legend(fontsize=7)
        self.ax2.legend(fontsize=7)
        self.ax.grid(color="grey", linestyle="-", linewidth=0.5, alpha=0.8)
        self.ax.grid(which="minor", linestyle="-", linewidth=.5, alpha=0.7)
        self.ax.set_axisbelow(True)
        self.fig.tight_layout()
        self.draw()

    def afficher_tableau(self):
        pass
