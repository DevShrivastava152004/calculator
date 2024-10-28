import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
}

def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        print("available operations:")
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        if operation_symbol not in operations:
            print("Invalid operation.Please try again")
            continue
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"type 'y' to continue calculating with {answer}, or  type 'n' to stop calculating")

        if choice == "y":
                num1= answer
        else:
                should_accumulate = False
                print("\n"*20)
                calculator()
calculator()