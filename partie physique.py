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

# Graphique des valeurs de puissance par run
import os
import csv
import matplotlib.pyplot as plt

filename = "scatter_power.csv"

# --- Lecture des données existantes ---
powers = []

if os.path.exists(filename):
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:  # ignore les lignes vides
                    powers.append(float(row[0]))
    except (ValueError, IOError) as e:
        print(f"Avertissement : erreur de lecture du CSV ({e}). Réinitialisation.")
        powers = []

# --- Ajout de la nouvelle puissance (variable non écrasée) ---
powers.append(p)  # 'p' reste intact, pas de boucle qui l'écrase

# --- Sauvegarde dans le CSV ---
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for power_val in powers:          # ✅ variable renommée pour ne pas écraser p
        writer.writerow([power_val])

# --- Axes automatiques ---
x = list(range(1, len(powers) + 1))  # 1, 2, 3, ... numéro de run

# --- Affichage scatter ---
plt.figure(figsize=(8, 5))
plt.scatter(x, [p / 1000 for p in powers], color='steelblue', zorder=3)  # ✅ W → kW
plt.xlabel("Numéro de run")
plt.ylabel("Puissance (kW)")                                               # ✅ label mis à jour
plt.title("Puissance par run")
plt.xticks(x)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()