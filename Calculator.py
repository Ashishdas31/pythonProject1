def add(a,b):
    answer=(a+b)
    print(answer)

def sub(a,b):
    answer=a-b
    print(answer)

def mul(a,b):
    answer=a*b
    print(answer)

def div(a,b):
    answer=a/b
    print(answer)

while True:
    print("A=addition")
    print("S= Substraction")
    print("M= Multiplication")
    print("D= Division")
    print("E = Exit")

    Choice = input("input your choice:- ")

    if Choice == "A" or Choice == "a":
        print("Addition")
        a = int(input("input first number"))
        b = int(input("input second number"))
        add(a, b)
    elif Choice == "S" or Choice == "s":
        print("Substraction")
        a = int(input("input first number"))
        b = int(input("input second number"))
        sub(a, b)
    elif Choice == "M" or Choice == "m":
        print("Multiplication")
        a = int(input("input first number"))
        b = int(input("input second number"))
        mul(a, b)
    elif Choice == "D" or Choice == "d":
        print("Division")
        a = int(input("input first number"))
        b = int(input("input second number"))
        div(a, b)
    elif Choice == "E" or Choice == "e":
        print("Program ended")
        quit()




