def fusion(l1, l2):
    """Fusion entre deux listes (algo tri fusion) de manière récursive

    Args:
        l1 (list): une liste triée d'entiers
        l2 (list): une liste triée d'entiers

    Returns:
        list: La fusion entre les 2 listes dans l'orde croissant
    """
    if not l1:
        return l2
    elif not l2:
        return l1
    if l1[0] < l2[0]:
        return [l1[0]] + fusion(l1[1:], l2)
    elif l1[0] >= l2[0]:
        return [l2[0]] + fusion(l1, l2[1:])

print(fusion([3,5], [2,5]))
print(fusion([-2, 4], [-3,5,10]))
print(fusion([4], [2,6]))

romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre):
    """
    Renvoie l'écriture décimal du nombre donnée en chiffres 
    romains
    """
    if len(nombre) == 1:
        return romains[nombre[0]]
    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]

print(traduire_romain("XIV"))
print(traduire_romain("CXLII"))
print(traduire_romain("CXLII"))
print(traduire_romain("MMXXIII"))
