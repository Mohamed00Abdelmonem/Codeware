def digitize(n):
    x = list(map(int, str(n)))
    return x[::-1]


print(digitize(34325))
