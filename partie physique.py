##############################################################################################################
# Crée par Mathis Robinet, Rayen Rouz, Alexis Paiement
# Crée le 2026-02-17
#420-ESP-MA INTÉGRATION DES ACQUIS EN SCIENCES DE LA NATURE - PROJET EN INFORMATIQUE: Simulation d'une central hydroélectrique
##############################################################################################################
import numpy
import matplotlib.pyplot as plt
import csv
import loi_physique
import os

#exemple utilisation loi physique

print(loi_physique.equation(5,4,3,2,1))

#valeur input
masse_volumique=1000
g=9.81
hauteur=20

rendement=float(input("Quelle est le rendement de la centrale"))

while 0.9 < rendement or 0.6 > rendement:
    print("Le rendement de la centrale doit être compris entre 0.6 et 0.9")
    rendement=float(input("Quelle est le rendement de la centrale"))

débit=float(input("Quelle est le débit d'eau"))

while 10 > débit or 1000 < débit:
    print("Le débit de la centrale doit être compris entre 10 et 1000 m³/s")
    débit = float(input("Quelle est le débit d'eau"))

p = loi_physique.equation(rendement, masse_volumique, g, débit, hauteur)
print(p/1000,"kW")

if p/1000 < 72000:
    print("Il n'y a pas assez d'énergie pour alimenter tous les habitants du village")
else:
    print("Il y a",p/1000-72000,"kW en surplus")

#Graphique des valeurs de p (Chat GPT)

filename = "scatter_power.csv"

# --- Lecture des données existantes ---
powers = []

if os.path.exists(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            powers.append(float(row[0]))  # on stocke juste P
# Sinon, liste vide si premier run
# Ajoute la nouvelle puissance
powers.append(p)

# --- Sauvegarde toutes les données dans le CSV ---
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for p in powers:
        writer.writerow([p])

# --- Préparer les X automatiquement ---
x = list(range(1, len(powers)+1))  # 1,2,3,... numéro du run automatique

# --- Affichage scatter ---
plt.scatter(x, powers)
plt.xlabel("Numéro de run")
plt.ylabel("Puissance (W)")
plt.title("Puissance par run")
plt.grid(True)
plt.show()