pa = "Kayak"
nopa = "Kakyyy"


def is_palindrome(pa):
    list_not_rev = list(pa)
    list_rev = list_not_rev[::-1]

    for i in range(len(list_not_rev)):
        if list_not_rev[i] != list_rev[i]:
            return False
    return True


a = 123
l = list(str(a))
