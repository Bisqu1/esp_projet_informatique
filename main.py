##############################################################################################################
# Crée par Mathis Robinet, Rayen Rouz, Alexis Paiement
# Crée le 2026-02-17
#420-ESP-MA INTÉGRATION DES ACQUIS EN SCIENCES DE LA NATURE - PROJET EN INFORMATIQUE: Simulation d'une central hydroélectrique
##############################################################################################################
import numpy
import matplotlib as plt
import loi_physique


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
if p/1000 >

#graphique des valeurs de P



