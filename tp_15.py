def mini(releve, date):
    dico_1 = {}
    for i in range(len(date)):
        dico_1[date[i]] = releve[i]
    min = releve[-1] 
    min_date = 0
    for cle, valeur in dico_1.items():
        if valeur < min:
            min = valeur
            min_date = cle
    return min, min_date

    
    


t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

print(mini(t_moy, annees))


def inverse_chaine(chaine):
    result = ""
    for caractere in chaine:
        result = caractere +result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse == chaine

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)

print(inverse_chaine('bac'))
print(est_palindrome('NSI'))
print(est_palindrome('ISN-NSI'))
print(est_nbre_palindrome(214312))
print(est_nbre_palindrome(213312))