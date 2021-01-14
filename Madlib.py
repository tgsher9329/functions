def madlib(name, subject):
    output = f"{name}'s favorite subject is {subject}"
    return output

# items = input("Enter your name and your favorite subject seperated by a space.")
#items = ("Tucker", "Army")
#final = madlib(items)
# ^^^^^^ this was the first try


name, subject = input("Enter youre name and your favorite subject: ").split()

result = madlib(name, subject)

#below this worked, but will have to use print(result) commenting it out to try to get input from user
# result = madlib('Tucker', 'math')
print(result)