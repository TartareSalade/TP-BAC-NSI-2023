def multiplication(n1,n2):
    resultat = 0
    if n1 == 0 or n2 == 0:
        return 0
    else:
        if n1 and n2 > 0:
            for i in range(n2):
                resultat += n1
            return resultat
        if (n1 < 0 and n2 > 0) or (n1 > 0 and n2 < 0):
            resultat = -resultat
        if n1 and n2 < 0:
            for i in range(-n2):
                resultat += -(n1)
            return resultat
    

print(multiplication(3, 5))
print(multiplication(-4,-8))
print(multiplication(-2,6))
print(multiplication(-2,0))


def chercher(tab, n, i, j):
    if i < 0 or j > len(tab):
        return None
    elif i > j:
        return None
    m = (i+j) // 2 #On prend le milieu
    if tab[m] < n:
        return chercher(tab, n, m+1,j)
    elif tab[m] > n:
        return chercher(tab, n, i, m-1)
    else:
        return m

print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10))
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 9, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 6, 0, 5))