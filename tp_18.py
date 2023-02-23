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
    for i in range(1,len(tab)):
        if 