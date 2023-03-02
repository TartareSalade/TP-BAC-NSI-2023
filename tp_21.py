def codage_delta(liste):
    tab_final = []
    premier_element = liste[0]
    for i in range(len(liste)):
        tab_final.append(liste[i]-liste[i-1])
    tab_final[0] = premier_element
    return tab_final


print(codage_delta([1000,800,802,1000,1003]))
print(codage_delta([42]))


class Noeud:
    '''
    classe implÃ©mentant un noeud d'arbre binaire
    '''

    def __init__(self, g, v, d):
        '''
        un objet Noeud posséde 3 attributs :
        - gauche : le sous-arbre gauche,
        - valeur : la valeur de l'étiquette,
        - droit : le sous-arbre droit.
        '''
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __str__(self):
        '''
        renvoie la représentation du noeud en chaine de caractères
        '''
        return str(self.valeur)

    def est_une_feuille(self):
        '''
        renvoie True si et seulement si le noeud est une feuille
        '''
        return self.gauche is None and self.droit is None


def expression_infixe(e):
    """
    En réalité le problème s'effectue en deux étapes 
    On s'occupe de l'arbre de gauche donc on aura l'expression de la première partie
    donc parenthèse + l'expression + l'appel recursif de la partie gauche
    on converti sa en string
    et ensuite partie droite 
    """
    s = ""
    if e.gauche is not None:
        s = '(' + s + expression_infixe(e.gauche)
    s = s + str(e.valeur) #On s'occupe du noeud valeur
    if e.gauche is not None:
        s = s + expression_infixe(e.droit) + ')' #On s'occupe de noued droit (de la partie droite dans l'expression) 
        #En parant de e.gauche car recursif donc on ajoute l'expression de ce qu'on a fait avant
        # s + = s + expression infixe de la partie droite + la paranthese fermante
    return s

e = Noeud(Noeud(Noeud(None, 3, None),
    '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))),
    '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))

print(expression_infixe(e))