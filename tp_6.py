from math import sqrt
def recherche(tab,n):
    if n not in tab:
        return len(tab)
    liste_inter = []
    for i in range(len(tab)):
        if tab[i] == n:
            liste_inter.append(i)
    return liste_inter[-1]
            

print(recherche([5, 3], 1))
print(recherche([2, 4], 2))
print(recherche([2, 3, 5, 2, 4], 2))

def distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)


def plus_courte_distance(tab, depart):
    """
    Renvoie le point du tableau se trouvant à la plus courte distance du point de depart.
    """
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range(1,len(tab)):
        if distance(tab[i], depart)<point:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point