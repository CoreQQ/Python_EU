#Choise operator, return result
def oper(num1, num2):
    oper = input("""
    * Множення
    / Ділення
    + Додавання
    - Віднімання
    ^ Степінь
    v Кврадратний Корінь

    Enter operator""")

    if oper == "+":
        return num1 + num2
    elif oper == "-":
        return num1 - num2
    elif oper == "*":
        return num1 * num2
    elif oper == "/":
        return num1 / num2
    elif oper == "^":
        return num1 ** num2
    elif oper == "v":
        return num1 ** 0.5
    else:
        print("You make error")
        return oper(num1, num2)


#Get num1, num2. Print result
def main():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    print(f"Result: {oper(num1, num2)}")


if __name__ == "__main__":
    main()