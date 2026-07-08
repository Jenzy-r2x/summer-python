number1 = int(input("please insert a number: "))
number2 = int(input("please insert another number: "))
signs = input("Please select a opperation: ")

if signs == "+":
    total = number1 + number2
    print(total)
elif signs == "-":
    total= number1 - number2
    print(total)
elif signs == "*":
    total=number1 * number2
    print(total)
elif signs == "/":
    total=number1/number2
    print(total)
    #Number,Signs,Total, Arithmetics