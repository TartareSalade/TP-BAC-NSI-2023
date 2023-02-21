def recherche(a, tab):
    nb_occurrences = 0
    for element in tab:
        if element == a:
            nb_occurrences += 1
    return nb_occurrences

print(recherche(5, []))
print(recherche(5, [-2, 3, 4, 8]))
print(recherche(5, [-2, 3, 1, 5, 3, 7, 4]))
print(recherche(5, [-2, 5, 3, 5, 4, 5]))


pieces = [1, 2, 5, 10, 20, 50, 100, 200]
def rendu_monnaie(somme_due, somme_verse):
    rendu = []
    a_rendre = somme_verse - somme_due
    i = len(pieces) - 1
    while a_rendre > 0:
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else:
            i = i-1
    return rendu


print(rendu_monnaie(700, 700))
print(rendu_monnaie(102, 500))