# Écrire une fonction en Python qui, étant donnée une chaîne de caractères, retourne le premier caractère non répétitif. Si tous les caractères sont répétitifs, la fonction doit retourner None


def first_non_repeating_letter(s):
    s_as_list = list(s)
    dico = {}

    for cc in s_as_list:
        k = list(dico.keys())

        if cc in k:
            dico[cc] += 1
        else:
            dico[cc] = 1

    for k, v in dico.items():
        if v == 1:
            return k
    return None
