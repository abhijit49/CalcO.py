def main():
    print("CALCULATOR PROGRAM::")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")

    choice = input("Enter your Choice: ")
    match choice:
        case "1":
            num1 = int(input("Enter 1st number: "))
            num2 = int(input("Enter 2nd number: "))
            result = add(num1, num2)
            print(result)
        case "2":
            num1 = int(input("Enter 1st number: "))
            num2 = int(input("Enter 2nd number: "))
            result = sub(num1, num2)
            print(result)
        case "3":
            num1 = int(input("Enter 1st number: "))
            num2 = int(input("Enter 2nd number: "))
            result = mul(num1, num2)
            print(result)
        case "4":
            num1 = int(input("Enter 1st number: "))
            num2 = int(input("Enter 2nd number: "))
            result = divide(num1, num2)
            print(result)
        case "5":
            num1 = int(input("Enter 1st number: "))
            power = int(input("num1" + "raised to power of: "))
            result = square(num1, power)
            print(result)


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def square(n, p):
    return pow(n, p)


main()
