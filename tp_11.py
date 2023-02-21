def convertir(tab):
    resulat = 0
    n = len(tab)
    for i in range(n):
        resulat += tab[i] * 2**(n-i-1)
    return resulat

print(convertir([1, 0, 1, 0, 0, 1, 1]))
print(convertir([1, 0, 0, 0, 0, 0, 1, 0]))


liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        #La variable j est utilisée pour déterminer ou placer la valeur à insérer 
        j = i 
        # tant qu'on a pas trouvé la place de l'élément à insérer
        # on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j = j-1
        tab[j] = valeur_insertion 

tri_insertion(liste)
print(liste)
