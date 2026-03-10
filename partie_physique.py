##############################################################################################################
# Crée par Mathis Robinet, Rayen Rouz, Alexis Paiement
# Crée le 2026-02-17
#420-ESP-MA INTÉGRATION DES ACQUIS EN SCIENCES DE LA NATURE - PROJET EN INFORMATIQUE: Simulation d'une central hydroélectrique
##############################################################################################################
import numpy
import matplotlib.pyplot as plt
import csv

from matplotlib.backends.backend_template import FigureCanvas

import loi_physique
import os



def run_centrale(debit, hauteur, rendement, masse_volumique=1000, g=9.81):
    #rendement = float(input("Quelle est le rendement de la centrale: "))
    #while not (0.6 <= rendement <= 0.9):
    #    print("Le rendement de la centrale doit être compris entre 0.6 et 0.9")
    #    rendement = float(input("Quelle est le rendement de la centrale: "))
#
    ##debit = float(input("Quelle est le débit d'eau: "))
    #while not (10 <= debit <= 1000):
    #    print("Le débit de la centrale doit être compris entre 10 et 1000 m³/s")
    #    debit = float(input("Quelle est le débit d'eau: "))
#
    ##Calcul
    p = loi_physique.calculer_puissance(rendement, masse_volumique, g, debit, hauteur)/1_000_000
    #print(p / 1000, "kW")

    #if p / 1000 < 72000:
    #    print("Il n'y a pas assez d'énergie pour alimenter tous les habitants du village")
    #else:
    #    print(f"Il y a {p / 1000 - 72000} kW en surplus")
#
    #Fichier CSV
    filename = "scatter_power.csv"
    powers = []

    if os.path.exists(filename):
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row:
                        powers.append(float(row[0]))
        except (ValueError, IOError) as e:
            print(f"Avertissement : erreur de lecture du CSV ({e}). Réinitialisation.")
            powers = []

    if len(powers) >= 10:
        del powers[0]  # supprime la plus vieille valeur
    powers.append(p)  # ajoute toujours le nouveau p

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for power_val in powers:
            writer.writerow([power_val])

    #Graphique Scatter par run

    return powers


#Appel test du def
#run_centrale(rendement=0.8,debit=700)