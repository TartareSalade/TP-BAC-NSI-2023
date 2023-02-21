import random
def lancer(n):
    liste = []
    for i in range(n):
        liste.append(random.randint(1,6))
    return liste


def paire_6(tab):
    occurences_6 = 0
    for element in tab:
        if element == 6:
            occurences_6 += 1
    if occurences_6 >= 2:
        return True
    else:
        return False

lancer1 = lancer(5)
print(lancer1)
print(paire_6(lancer1))
lancer2 = lancer(5)
print(lancer2)
print(paire_6(lancer2))


def nbLig(image):
    """
    Renvoie le nbre de ligne de l'image
    """
    return len(image)

def nbCol(image):
    """
    Renvoie la largeur de l'image
    """
    return len(image[0])

def negatif(image):
    """
    Renvoie le négatif de l'image sous la forme 
    d'une liste de liste
    """
    #On créer une image de 0 aux même dimensions que le paramètre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            L[i][j] = 255 - image[i][j]
    return L


def binaire(image, seuil):
    """
    Renvoie une image binarisée de l'image sous la forme 
    d'une liste de listes contenant des 0 si la valeur du pixel
    est strcitement inférieur au seuil et 1 sinon
    """
    #On créer une image de 0 aux même dimensions que le paramètre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            if image[i][j] < seuil:
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L



