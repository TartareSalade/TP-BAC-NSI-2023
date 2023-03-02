def recherche(tab,n):
    indice_debut = 0
    indice_fin = len(tab)-1
    while indice_debut <= indice_fin:
        milieu = (indice_debut + indice_fin) // 2
        if n == tab[milieu]:
            return milieu
        elif n < tab[milieu]:
            indice_fin = milieu - 1
        else:
            indice_debut = milieu + 1
    return -1

print(recherche([2, 3, 4, 5, 6], 5))
print(recherche([2, 3, 4, 6, 7], 5))


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def position_alphabet(lettre):
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c)+decalage) % 26 #On prend la position de l'alphabet + le décalage qu'on veut
            resultat = resultat + ALPHABET[indice]
        else:
            resultat += c #Sinon, si il n'est pas compris entre A et Z, on rajoute directement le caractère
    return resultat

print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4))
print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5))