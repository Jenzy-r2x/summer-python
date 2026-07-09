
def addition(x,y):
    total=0
    total= x + y
    return total

def multiplication(x,y):
    total=0
    total= x * y 
    return total

def subtraction(x,y):
    total=0
    total= x-y
    return total
    
def divison(x,y):
    total=0
    total= x/y
    return total 

def main():
    x = int(input("please insert a number: "))
    y = int(input("please insert another number: "))
    signs = input("Please select a opperation: ")
    if signs == "+":
       print(addition(x,y)) 
    elif signs == "-":
        print(subtraction(x,y))   
    elif signs == "/":
        print(divison(x,y))
    elif signs == "*":
        print(multiplication(x,y))
main()