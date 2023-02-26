def max_et_indice(tab):
    assert type(tab) == list, "tab doit être une liste"
    assert len(tab) != 0, "tab doit être non vide"
    max = tab[0]
    indice_max = 0
    for i in range(len(tab)):
        if max < tab[i]:
            max = tab[i]
            indice_max = i
    return max,indice_max

print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(max_et_indice([-2]))
print(max_et_indice([-1, -1, 3, 3, 3]))
print(max_et_indice([1, 1, 1, 1]))


def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon
    '''
    for i in range(1,len(tab)+1):
        if i not in tab:
            return False
    return True



def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui reprÃ©sente un ordre
    de gÃ¨nes de chromosome
    '''
    assert est_un_ordre(ordre) # ordre n'est pas un ordre de gÃƒÂ¨nes
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < len(ordre)-1:
        if (ordre[i+1] - ordre[i]) not in [-1, 1]: # l'ecrat n'est pas 1
            nb = nb + 1
        i = i + 1
    if ordre[-1] != n: # le dernier n'est pas n
        nb = nb + 1
    return nb

print(est_un_ordre([1, 6, 2, 8, 3, 7]))
print(nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]))