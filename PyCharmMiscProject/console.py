from generateur import generer_systeme_stellaire

sys = generer_systeme_stellaire()

def imprimer_liste_satellites(planetes):
    for satellite in planetes.satellites:
        print("\nCatégorie:", satellite.formation, "\nDistance:", satellite.distance, "km\nRésonance:", satellite.resonance, "\nMasse:", satellite.masse, "masses terrestres\nGravité:", satellite.gravite, "\nPériode orbitale:", satellite.periode_orbitale, "heures\nTempérature:", satellite.temp-273.15, "C\nComposition atmosphérique:", satellite.atmosphere, "\nHydrographie:", satellite.quantite_eau, satellite.hydrographie)
        if satellite.contient_vie:
            print(satellite.profil_vie)

def determiner_verrouillage(planetes):
    if planetes.verrouillage:
        return str(planetes.periode_rotation) + " jours"
    else:
        return str(planetes.periode_rotation) + " heures"

print("Âge:", sys.age, "milliards d'années.\nMétallicité:", sys.metallicite, "\n----")
for etoile in sys.etoiles:
    print("\nType:", etoile.categorie, "\nClasse spectrale:", etoile.classe_spectrale, "\nMasse:", etoile.masse, "masses solaires\nTempérature:", etoile.temp, "K\nLuminosité:", etoile.luminosite, "luminosités solaires\nRayon:", etoile.rayon, "kilomètres.\nCentre de masse: Étoile numéro", etoile.centre_de_masse+1, "\nDistance du centre de masse:", etoile.distance, "UA")

print("----")

for planete in sys.planetes:
    if planete.categorie == "geante_gazeuse":
        print("\nCentre de masse: Étoile numéro", planete.centre_de_masse+1, "\nCatégorie:", planete.categorie, "\nExcentricité:", planete.excentricite, "\nDistance:", planete.distance, "UA\nRésonance:", planete.resonance, "\nMasse:", planete.masse, "masses terrestres\nAnneaux:", planete.anneau)
        imprimer_liste_satellites(planete)
    elif planete.categorie == "ceinture_asteroide":
        print("\nCentre de masse: Étoile numéro", planete.centre_de_masse+1, "\nCatégorie:", planete.categorie, "\nDistance:", planete.distance, "UA\nRésonance:", planete.resonance)
    else:
        print("\nCentre de masse: Étoile numéro", planete.centre_de_masse + 1, "\nCatégorie:", planete.categorie, "\nExcentricité:", planete.excentricite, "\nDistance:", planete.distance, "UA\nRésonance:", planete.resonance, "\nMasse:", planete.masse, "masses terrestres\nGravité:", planete.gravite, "\nPériode orbitale:", planete.periode_orbitale, "jours\nPériode de rotation:", determiner_verrouillage(planete), "\nInclinaison axiale:", planete.inclinaison_axiale, "degrés.\nTempérature:", planete.temp-273.15, "°C\nComposition atmosphérique:", planete.atmosphere, "\nHydrographie:", planete.quantite_eau, planete.hydrographie*100, "%\nGéologie:", planete.geologie[0], planete.tectonique_mobile, "\nChamp magnétique:", planete.champ_magnetique[0])
        if planete.contient_vie:
            print(planete.profil_vie)
        imprimer_liste_satellites(planete)
    print("---")
print("----")