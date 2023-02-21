def max_dico(dico):
    """
    Renvoie le maximum d'un dictionnaire, sous forme d'une tuple
    """
    max_val = 0
    max_nom = ""
    for cle, valeurs in dico.items():
        if valeurs > max_val:
            max_val = valeurs
            max_nom = cle
    return max_nom, max_val

print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))


class Pile:
    """
    Classe définissant une structure de pile.
    """
    def __init__(self):
        self.contenu = []
    
    def est_vide(self):
        return self.contenu == []

    def empiler(self,v):
        self.contenu.append(v)

    def depiler(self):
        if not self.est_vide():
            return self.contenu.pop()

def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != "+" and element != "*":
            p.empiler(element)
        else:
            if element == "+":
                resultat = p.depiler() + p.depiler()
                """
                 si l’élément parcouru est un opérateur, on récupère les deux éléments situés au
                sommet de la pile et on leur applique l’opérateur. On place alors le résultat au sommet
                de la pile ; idem pour le else
                """
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat) #Empile le résultat
    return p.depiler() #Renvoie le résultat dernière ligne consigne


print(eval_expression([2, 3, '+', 5, '*']))


