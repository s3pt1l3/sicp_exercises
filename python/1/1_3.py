def square(x):
    return x * x

def sum_squares(x, y):
    return square(x) + square(y)

def x(a, b, c):
    if (a + b >= b + c) and (a + b >= a + c):
        return sum_squares(a, b)
    elif (a + c >= b + c) and (a + c >= a + b):
        return sum_squares(a, c)
    else:
        return sum_squares(b, c)
