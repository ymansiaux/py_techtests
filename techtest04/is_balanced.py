# Écrire une fonction qui vérifie si une chaîne de caractères contenant uniquement les caractères (, ), {, }, [ et ] est bien équilibrée. Une chaîne est considérée comme équilibrée si chaque parenthèse ouvrante possède une parenthèse fermante correspondante dans le bon ordre.

from collections import Counter


def is_balanced(s):
    c = Counter(s)
    if c["{"] == c["}"] and c["["] == c["]"] and c["("] == c[")"]:
        return True
    return False
