# C = (F - 32) * 5/9


def toC(F):
    C = (F - 32) * 5/9
    return C


F = float(input("Tell me the degrees in Fahrenheit: "))

C = toC(F)

print(C)