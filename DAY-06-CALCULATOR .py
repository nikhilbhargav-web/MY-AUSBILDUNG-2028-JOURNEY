print("----- MY CALCULATOR -----")


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


pehla = int(input("pehla number daalaa: "))
doosra = int(input("Doosra number daal: "))
operation = input("Operation daal + - * / : ")


if operation == "+":
    result = add(pehla, doosra)
    print(f"answer: {result}")
elif operation == "-":
    result = subtract(pehla, doosra)
    print(f"answer: {result}")
elif operation == "*":
    result = multiply(pehla, doosra)
    print(f"answer: {result}")
elif operation == "/":
    result = divide(pehla, doosra)
    print(f"answer: {result}")
else:
    print("GALAT OPERATION BHAI")

    print("---------- DONE ----------")
