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
