import random

def randomd6(nombre):
    total = 0
    for i in range(nombre):
        total += random.randint(1,6)
    return total

def random1d100():
    return random.randint(1,100)

def chercher_tableau(nombre, tableau, est_aleatoire):
    if est_aleatoire:
        for cle, valeur in tableau.items():
            if cle[0] <= nombre < cle[1]:
                return valeur
    else:
        for cle, valeur in tableau.items():
            if nombre == cle:
                return valeur
