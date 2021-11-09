def calculator(a, b, c):
    # a = int(input("enter first value: "))
    # b = int(input("enter second value: "))
    # c = input('enter + - * /: ')
    if c == '*':
        result = a * b
    elif c == '+':
        result = a + b
    elif c == '-':
        result = a - b
    elif c == '/':
        result = a / b
    else: print('!Wrong values!')
    print(result)

calculator(12, 43, '+')





