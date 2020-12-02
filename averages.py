#Reese Allen rga2uz CS1110-004  Apostolellis


def mean(a, b, c):
    return (a + b + c)/3


def median(a, b, c,):
    if a < b < c or c < b < a:
        return b
    elif a < c < b or b < c < a:
        return c
    elif b < a < c or c < a < b:
        return a
    elif a == b == c:
        return a
    elif a == b < c or a == c < b or a == b > c or a == c > b:
        return a
    elif b == c < a or b == c > a:
        return b


def rms(a, b, c,):
    a = a ** 2
    b = b ** 2
    c = c ** 2
    return (mean(a, b, c))**(1/2)


def middle_average(a, b, c):
    x = mean(a, b, c)
    y = median(a, b, c)
    z = rms(a, b, c)
    return median(x, y, z)





