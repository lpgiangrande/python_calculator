from calculatrice import addition, soustraction, multiplication, division, moyenne

if __name__ == "__main__":

    test_division = division(6, 10)
    print('Le résultat de la division est : {}'.format(test_division))

    test_addition = addition(6, 3)
    print("Le résultat de l'addition est : {}".format(test_addition))

    test_soustraction = soustraction(6, 3)
    print('Le résultat de la soustraction est : {}'.format(test_soustraction))

    test_multiplication = multiplication(6, 3)
    print('Le résultat de la multiplication est : {}'.format(test_multiplication))

    test_moyenne = moyenne(2, 4, 3, 10)
    print('Le résultat de la moyenne est : {}'.format(test_moyenne))