num = int(input("Enter your number"))
#Nested if statmens are that we can use if,if-else,elif statements inside other statements as well

if (num < 0):
    print("The number is negative")
elif (num > 0):
    if (num <= 10):
        print("The number is between 1 and 10")
    elif (num > 10 and num <= 20 ):
        print("the number is between 11 and 20")
    else:
        print("The number is greater than 20")
else:
    print("The number is zero")
