def pgcd(x, y):
    while y != 0:
        x, y = y, x % y
    return abs(x)