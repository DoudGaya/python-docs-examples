# Example 1

def add_nums(number1, number2): 
    sums = number1 + number2
    return sums

print(add_nums(10, 20))



# Example 2

def add_multiple_numbers(a, b, c, d, e, f):
    sum = a + b + c + d + e + f
    return sum

print(add_multiple_numbers(1, 2, 3, 4, 5, 6))



# Example 3
def add_multiple_numbers(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

print(add_multiple_numbers([1, 2, 3, 4, 5, 6]))


# Example 2 - Passing Multiple arguments using the *args
def add_multiple_numbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add_multiple_numbers(1, 2, 3, 4, 5, 6, 8))


# Example 5 - Passing Multiple arguments using the *args
def add_multiple_numbers(**kwargs):
    sum = 0
    for i in kwargs:
        sum += kwargs[i]
    return sum
print(add_multiple_numbers(num1=10, num2=20, num3=30)) # 60



def multiple_args(name, surname, *cash, **items):
    full_name = name + ' ' + surname
    sum = 0
    all_items = ''
    for num in cash:
        sum += num
    
    for item in items:
        all_items += items[item]
    return '''
    Name:  {0} 
    total: {1}, 
    items: {2} 
    '''.format(full_name, sum, all_items)
print(multiple_args('Doud', 'Gaya', 10,20,30, item1="Pen, ", item2="Paper,", item3=" and Laptop!"))