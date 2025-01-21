a = int(input('Enter the first number:'))
b = int( input('Enter the second number:'))
op = input('Select the operator:')
if op == "+":
    print('The sum is {}'.format(a+b))
elif op =="-":
    print('The difference is{}'.format(a-b))
elif op =="*":
    print(f'The product is {(a*b)}')
elif op =="/":
    print('The divison is {}'.format(a/b))
else:
    print('Invalid operator:')