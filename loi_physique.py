##############################################################################################################
# Crée par Mathis Robinet, Rayen Rouz, Alexis Paiement
# Crée le 2026-02-17
# 420-ESP-MA INTÉGRATION DES ACQUIS EN SCIENCES DE LA NATURE - PROJET EN INFORMATIQUE: Simulation d'une central hydroélectrique
# Loi physique
##############################################################################################################


#rendement=0.9
#densite=1000
#gravite=9.81
#debit= 100
#hauteur=50

    #fonction equation central
def calculer_puissance(Q ,h ,eta ,rho=1000,g=9.81):
    """
    Calcule la puissance d'une centrale hydroélectrique.
    P = eta * rho * g * h * Q

    Q: débit (m³/s)
    h: hauteur de chute (m)
    eta: rendement de la turbine [0,1]
    g: gravité (m/s²)
    rho: densité du fluide (kg/m³)
    """
    puissance_W= Q * h * eta * rho * g
    return puissance_W




    #appel fonction
#print(calculer_puissance(rendement,densite,gravite,debit,hauteur,), "MW")
