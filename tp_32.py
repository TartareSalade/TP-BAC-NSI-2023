def min_max(tab):
    dict_final = {}
    max = tab[0]
    min = tab[0]
    for element in tab:
        if max < element:
            max = element
        else:
            min = element
    for element in tab:
        if min > element:
            min = element
    dict_final["min"] = min
    dict_final["max"] = max
    return dict_final

print(min_max([0,1,4,2,-2,9,3,1,7,1]))
print(min_max([0,1,2,3]))

class Carte:
    def __init__(self, c, v):
        """ Initialise les attributs couleur (entre 1 et 4), et valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v

    def get_valeur(self):
        """ Renvoie la valeur de la carte : As, 2, ..., 10, Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def get_couleur(self):
        """ Renvoie la couleur de la carte (parmi pique, coeur, carreau, trÃ¨fle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trÃ¨fle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52 objets Carte possibles
            rangÃ©s par valeurs croissantes en commenÃ§ant par pique, puis coeur,
            carreau et trÃ¨fle. """
        # A complÃƒÂ©ter
        self.paquet = []
        for couleur in range(1,5):
            for valeur in range(1,14):
                self.paquet.append(couleur, valeur)

    def get_carte(self, pos):
        """ Renvoie la carte qui se trouve Ãƒ  la position pos (entier compris entre 0 et 51). """
        # A complÃƒÂ©ter
        return self.paquet[pos]
