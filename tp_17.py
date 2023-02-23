def moyenne(liste_notes):
    somme_coeff = 0
    somme_notes = 0
    for element in liste_notes:
        somme_coeff += element[1]
        somme_notes += element[1] * element[0]
    return somme_notes/somme_coeff

print(moyenne([(15, 2), (9, 1), (12, 3)]))



def pascal(n):  
    triangle= [[1]]
    for k in range(1,n+1):
        ligne_k = [1]
        for i in range(1,k):
            ligne_k.append(triangle[k-1][i-1]+triangle[k-1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle

print(pascal(4))
print(pascal(5))