#creating function to return true if the inputed int is even false if it is odd


def isEven(num1):
    if (num1 % 2) == 0:
        return "Even"
    else:
        return "Odd"

num1 = int(input("Please enter a whole number. Even numbers will return true: "))

result = isEven(num1)
print(result)