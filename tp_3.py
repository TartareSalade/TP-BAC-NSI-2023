def moyenne(tab:list):
    moyenne = 0
    somme_coeff = 0
    total_moynne = 0
    for element, coeff in tab:
        somme_coeff += coeff
        moyenne += element * coeff
    total_moynne = moyenne / somme_coeff
    return total_moynne
        


coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
 [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
 [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
    """
    Affichag d'une grille : les 1 sont représentés par des
    des "*", les 0 par deux espaces " ".
    La valeur "" donnée au paramètre end permet de ne pas avoir
    de saut de ligne 
    """
    for ligne in dessin:
        for col in ligne:
            if col == 1 :
                print("*", end="")
            else:
                print("  ", end= "")
        print()

def zoomListe(liste_depart, k):
    """
    Renvoie une liste contenant k fois chaque
    élement de liste_depart
    """
    liste_zoom = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom


def zoomDessin(grille,k):
    """
    Renvoie une grille ou les lignes sont zoomés k fois ET répétes k fois
    """
    grille_zoom = []
    for elt in grille:
        liste_zoom = zoomListe(elt, k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom

affiche(coeur)
affiche(zoomDessin(coeur, 3))