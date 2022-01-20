
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

num1 = float(input("What's the first number? :"))
num2 = float(input("What's the second number? :"))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above:")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")


state = True
while state:
    
    continue_select = input("Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower()
    if continue_select == 'n':
        state = False
        break

    operation_symbol = input("Pck another operation: ")
    num3 = float(input("What's thenext number? : "))
    
    pre_answer = answer

    caclucalculation_function = operations[operation_symbol]
    answer = calculation_function(pre_answer,num3)

    print(f"{pre_answer} {operation_symbol} {num3} = {answer}")