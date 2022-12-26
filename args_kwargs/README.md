# Python Args and Kwargs 

Args or Kwargs are used in python when you want to pass multiple argument to a function. The arguments are recieved in form of a `tuple` (A datatype in python that re), It is especially useful when you don't know the number of arguments upfront. Before we see an example of it let's do a simple demonstration of how a function works and then we'll see the cases where `*args` and `**kwargs` can be very helpful.

## Normal Function
This is how you'd normally define a function in python. This function receives two arguments and return their sum.
```py
def add_nums(number1, number2): 
    sums = number1 + number2
    return sum

print(add_nums(10, 20))
```

But What if we want to add more numbers? Well there are couple of ways to acheive that. Let's see all of them. 

 1 - One way to do it is to pass all the arguments in in the funtion like this

```py

def add_multiple_numbers(a, b, c, d, e, f):
    sum = a + b + c + d + e + f
    return sum

print(add_multiple_numbers(1, 2, 3, 4, 5, 6, 7))

```

2 - Another way is to create a variable of a `list` or a `tuple` and store all the items in it, then pass it as an argument to a function

```py

def add_multiple_numbers(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

print(add_multiple_numbers([1, 2, 3, 4, 5, 6, 7]))
```

3 - The most effective way is to use and `*args` or `**kwargs` the main difference between the two is the keywords and we'll see an example of that later
```py

def add_multiple_numbers(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

print(add_multiple_numbers([1, 2, 3, 4, 5, 6, 7]))
```

