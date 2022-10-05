def calculator ():
    num1, operator, num2 = input('Calculate: ').split()
    num1 = input('Num1: ')
    num2 = input('num2: ')
    operator = input('Operator: ')
    try:
        add = int(num1) + int(num2)
        sub = int(num1) - int(num2)
        div = int(num1) / int(num2)
        mul = int(num1) * int(num2)
        mod = int(num1) % int(num2)
    except:
        print('Use a valid Number: ')
        calculator()

    if operator == '+':
        print('{} plus {} = {} '.format(num1, num2, add))
    elif operator == '-':
        print('{} minus {} = {} '.format(num1, num2, sub))
    elif operator == '*':
        print('{} times {} = {} '.format(num1, num2, mul))
    elif operator == '/':
        print('{} divide by {} = {} '.format(num1, num2, div))
    elif operator == '%':
        print('{} reminder {} = {} '.format(num1, num2, mod))
    else:
        print('Please use the right operator')
        calculator()
        return 'Finished'
calculator()