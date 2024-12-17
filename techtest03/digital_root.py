# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.


def digital_root(number):
    if number < 10:
        return number
    else:
        l = list(str(number))
        return digital_root(sum([int(x) for x in l]))
