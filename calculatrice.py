# TP MODULE 4 - CALCULATRICE

# 1
# Définir 4 fonctions implémentant les 4 opérations mathématiques de base : +, -, *, /
# Chaque fonction prend seulement 2 paramètres, et retourne la valeur de l'opération
# Tester le diviseur(2e param de fonction) car /0 impossible

# Ajouter une 5e : la moyenne, avec nombre variable de valeurs en paramètre
# et calculera la moyenne des valeurs transmises
# /!\ au moins 1 valeur doit être transmise au moment de l'appel
# Appel de la fonction en fin de code

# 2
# Un fichier pour les fonctions de la calculatrice, et un fichier d'appel principal

def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        print('Division par 0 impossible')
    else:
        return a / b


def moyenne(*val):
    if len(val) != 0:
        return sum(val) / len(val)
    else:
        print ('Il faut au moins une valeur pour calculer la moyenne')








