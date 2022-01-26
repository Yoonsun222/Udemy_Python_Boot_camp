from art import logo
#add
def add(a,b):
    return a+b

#Sub
def subtract(a,b):
    return a-b

#mult
def multiply(a,b):
    return a*b


#divide
def divide(a, b):
    return a/b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number? :"))

    for symbol in operations:
        print(symbol)
    
    state = True

    while state:
        num2 = float(input("What's the second number? :"))
        operation_symbol = input("Pick an operation from the line above:")
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")


        continue_select = input("Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower()
        
        if continue_select == 'n':
            state = False
            calculator()
        else:
            num1 = answer
            


calculator()

