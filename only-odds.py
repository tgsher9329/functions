def isEven(num1):
    if (num1 % 2) == 0:
        return "Even"
    else:
        return "Odd"
    
def onlyEvens(list):
    list2 = []
    # counter = 0

    # while counter < len(list):
    #     if isEven(list[counter]) == "Even":
    #         list2.append(list[counter])
    #     counter += 1
    
    # this while loop ^^ and this for loop below does the same thing

    for i in list:
        if isEven(i) != "Even":
            list2.append(i)
    return list2

list = [1,2,3,4,5,6,7, 8, 10]

result = onlyEvens(list)
print(result)