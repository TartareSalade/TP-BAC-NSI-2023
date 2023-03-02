def multiplication(n1,n2):
    resultat = 0
    if n1 > 0 and n2 >0:
        for i in range(n1):
            resultat += n2
        return resultat
    if n1 < 0 and n2 <0:
        for i in range(abs(n1)):
            resultat += n2
        resultat = resultat * -1
        return resultat
    if n1 < 0 and n2 > 0:
        for i in range(abs(n1)):
            resultat += n2
        resultat *= -1
        return resultat     
    if n2 < 0:
        for i in range(n1):
            resultat += abs(n2)
        resultat *= -1
        return resultat
    if n1 == 0 or n2 == 0:
        return 0



def dichotomie(tab, x):
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x   : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut+fin) // 2
        if x == tab[m]:
            return True #Comparé a algo dicho classique on retourne True ou false ici au lieu de la valeur
        if x > tab[m]:
            debut = m + 1
        else:
             fin = m-1
    return False
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))