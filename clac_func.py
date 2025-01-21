# a basic calculator using python
#operation that can be done i.e add,sub, multiply,div
def add(a, b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        print('invalid operator')
    else:
        return a/b
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

num1=float(input('Enter the first digit:'))
num2=float(input('Enter the second digit:'))
    # Get user input
calculator()
choice = input("Enter choice (1/2/3/4): ")

operations = {
    '1': add,
    '2': sub,
    '3': mul,
    '4': div
}
operation = operations.get(choice)
    # Dictionary to simulate switch-case
if operation:
    result = operation(num1, num2)
    print(f"Result: {result}")
else:
    print("Invalid input")
