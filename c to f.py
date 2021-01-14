# F = (C * 9/5) + 32



def toF(C):
    F = ((C * 9/5) + 32)
    return F

C = float(input("Give me a degrees in celsius: "))

result = toF(C)


print(result)