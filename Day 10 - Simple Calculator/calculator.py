def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    if n2 != 0:
        return n1//n2
    else:
        print("Denominator must not be 0")


def calculator(n1,n2,operator):
    """Computes input numbers with chosen operation"""
    operator_selection = operations.get(operator)
    if operator is None:
        print("Invalid operator")
        return
    else:
        result = operator_selection(n1,n2)
        print(f"Result {n1} {operator} {n2}= {result}")
        cont_calculation = input(f"Do you wish to continue with {result}? (Y/N): ")
        if cont_calculation == "Y" or cont_calculation == "y":
            num1 = result
            operator = input("Enter operator (+ - * /): ")
            n2 = float(input("Enter second number: "))
            calculator(result,n2,operator)
        else:
            print(f"Result {n1} {operator} {n2}= {result}")
            return result


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

n1 = float(input("Enter first number: "))
for symbol in operations:
    print(symbol)
operator = input("Enter operator (+ - * /): ")
n2 = float(input("Enter second number: "))

calculator(n1,n2,operator)
