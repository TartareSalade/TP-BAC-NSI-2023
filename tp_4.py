def a_doublon(lst):
    n = len(lst)
    if n < 2:
        return False
    for i in range(n-1):
        if lst[i] == lst[i+1]:
            return True

    return False
print(a_doublon([]))
print(a_doublon([1]))
print(a_doublon([1, 2, 4, 6, 6]))
print(a_doublon([2,5,7,7,7,9]))
print(a_doublon([0,2,3]))


def voisinage(n, ligne, colonne):
    voisins = []
    for l in range(max(0,ligne-1), min(n, ligne+2)):
        for c in range(max(0, colonne-1), min(n, colonne+2)):
            if (l, c) != (ligne, colonne):
                voisins.append((l,c))
    return voisins

def incremente_voisins(grille, ligne, colonne):
    voisins = voisinage(len(grille), ligne, colonne)
    for l, c in voisins:
        if grille[l][c] != -1: #Si ce n'est pas une bombe
            grille[l][c] += 1 #On ajoute un sa valeur           

def genere_grille(bombes):
    n = len(bombes)
    grille = [[0 for colonne in range(n)] for ligne in range(n)]
    for ligne, colonne in bombes:
        grille[ligne][colonne] = -1
        incremente_voisins(grille, ligne, colonne)
    return grille

