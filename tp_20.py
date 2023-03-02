def ajoute_dictionnaire(d1,d2):
    d = {}
    for k in d1:
        if k in d2:
            d[k] = d1[k] + d2[k] #Premier cas
        else:
            d[k] = d1[k]
    for k in d2:
        if k not in d:
            d[k] = d2[k]
    return d

print(ajoute_dictionnaire({1: 5, 2: 7}, {2: 9, 3: 11}))
print(ajoute_dictionnaire({}, {2: 9, 3: 11}))
print(ajoute_dictionnaire({1: 5, 2: 7}, {}))

from random import randint

def nbre_coups():
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < nbre_cases:
        x = randint(1,6)
        case_en_cours = (case_en_cours + x) % nbre_cases
        """
        Dans le code ci-dessus, le modulo est utilisé pour s'assurer que la case en cours est bien dans la plage de cases de 0 à 11 inclus. 
        En effet, si la somme du nombre obtenu sur le dé et de la case en cours dépasse 11, le joueur doit revenir au début de la piste. 
        C'est pourquoi on utilise le modulo pour obtenir le reste de la division de la somme par le nombre total de cases (12).
        """
        if case_en_cours not in cases_vues :
            cases_vues.append(case_en_cours)
        n+=1
    return n 

print(nbre_coups())
print(nbre_coups())