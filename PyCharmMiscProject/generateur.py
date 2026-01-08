from systeme_stellaire import Sys
from jets_de_des import randomd6, random1d100, chercher_tableau

tableau_age = {(1, 43): (0, 2), (43, 77): (2, 3), (77, 96): (5, 3), (96, 100): (8, 1.5), (100, 101): (9.5, 3)}

def generer_systeme_stellaire():
    age = chercher_tableau(random1d100(), tableau_age, True)
    age = age[0] + (age[1]*(random1d100()*0.01))
    metallicite = (randomd6(3)*0.1)*(1.2-(age/13.5))
    if age >= 8:
        metallicite -= 0.2
    if randomd6(1) == 1:
        metallicite += (randomd6(3)*0.1)
    if metallicite < 0:
        metallicite = 0
    if metallicite > 3:
        metallicite = 3
    sys = Sys(age, metallicite)
    sys.etoiles = sys.generer_etoiles()
    sys.planetes = sys.generer_planetes()
    return sys