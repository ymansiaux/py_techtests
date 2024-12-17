# Écrivez une fonction en Python qui détermine si une chaîne de caractères est un palindrome. Un palindrome est une chaîne qui se lit de la même manière de gauche à droite et de droite à gauche.


def is_palindrome(pa):
    list_not_rev = list(pa)
    list_rev = list_not_rev[::-1]

    for i in range(len(list_not_rev)):
        if list_not_rev[i] != list_rev[i]:
            return False
    return True
