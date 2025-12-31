x = int(input("Enter the value of x: "))
#x is the variable to be matched
match x:
    case 0:
        print("x is 0")
    case 4:
        print("x is 4")
    case __ if x !=90:  #_ is for default case it will only be matched if the above cases hv not been matched   
        print(x,"is not 90") 
    case _ if x!=80:
        print(x,"is not 80")
    case _ if x!=70:
        print(x,"is not 70")
    case _:
        print(x)