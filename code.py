# Code for a Calculator:
def add(a,b):
    addition = (a+b)
    return addition
def sub(a,b):
    subtraction =  (a-b)
    return subtraction
def multi(a,b):
    multiplication = (a*b)
    return multiplication
def div(a,b):
    division = (a/b)
    return division

def main(a,b):
    op = ["A","S","M","D"]
    n = input("Choose the Operation A/S/M/D: ")
    if n in op :
        
        if n == "A":
            addition = add(a,b)
            print(addition)
        elif n == "B":
            subtraction = sub(a,b)
            print(subtraction) 
        elif n == "M":
            multiplication = multi(a,b)
            print(multiplication)
        else:
            division = div(a,b)
            print(division)
    else:
        print("Enter Valid Operation!")

main(a = int(input("Input Value of A: ")), b = int(input("Input Value of B: ")))
