def recherche(elt, tab):
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    return -1


print(recherche(1, [2, 3, 4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(50, [1, 50, 1]))
print(recherche(15, [8, 9, 10, 15]))
print(recherche(50, []))
print(recherche(4, [2, 4, 4, 3, 4]))

def insere(a, tab):
    """ InsÃ¨re l'Ã©lÃ©ment a (int) dans le tableau tab (list)
    triÃ© par ordre croissant Ã  sa place et renvoie le
    nouveau tableau. """
    l = list(tab) #l contient les memes elements que tab
    l.append(a)
    i = len(l)-1
    while a < tab[i] and i >= 0:
        l[i+1] = l[i]
        l[i] = a
        i = i-1
    return l