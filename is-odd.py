def isOdd(num1):
    if (num1 % 2) == 0:
        return False
    else:
        return True

num1 = int(input("Please enter a whole number. Odd numbers will return true: "))
result = isOdd(num1)

print(result)