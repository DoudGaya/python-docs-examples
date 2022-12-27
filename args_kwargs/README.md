# Python Args and Kwargs 

Args or Kwargs are used in python when you want to pass multiple argument to a function. The arguments are recieved in form of a `tuple` (Main difference between tuple and a list is that tuples are immutable) , It is especially useful when you don't know the number of arguments upfront. Before we see an example of it let's do a simple demonstration of how a function works and then we'll see the cases where `*args` and `**kwargs` can be very helpful.

## Normal Function
This is how you'd normally define a function in python. This function receives two arguments and return their sum.
```py
# Example 1 - Normal Function Definition
def add_nums(number1, number2): 
    sums = number1 + number2
    return sum

print(add_nums(10, 20)) # 30
```

But What if we want to add more numbers? Well there are couple of ways to acheive that. Let's see all of them. 

 1 - One way to do it is to pass all the arguments in in the funtion like this

```py
# Example 2 - Passing Multiple arguments the naive way
def add_multiple_numbers(a, b, c, d, e, f):
    sum = a + b + c + d + e + f
    return sum

print(add_multiple_numbers(1, 2, 3, 4, 5, 6, 7)) # 21

```

2 - Another way is to create a variable of a `list` or a `tuple` and store all the items in it, then pass it as an argument to a function

```py
# Example 3 - Passing an Array of arguments 
def add_multiple_numbers(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

print(add_multiple_numbers([1, 2, 3, 4, 5, 6, 7])) # 21
```

## Using the *Args Variable 

3 - The most effective way is to use and `*args` or `**kwargs` the main difference between the two is the keywords and we'll see an example of that later. With `*args` you can directly pass different number of arguments without requiring a list or anything.
```py
# Example 4 - Passing Multiple arguments using the *args
def add_multiple_numbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add_multiple_numbers(1, 2, 3, 4, 5, 6, 8)) # 29
```
Note: While using the `*args` parameter, you don't have to explicitly use the `args` keyword, it is not required. You can use name it however you want just like a normal argument. What's important is that you use the unpacking operator `*` before the argument to let the function know that this is suppose to receive multiple parameters. 

```py

# Example 5 - Passing Multiple arguments using the *args
def add_multiple_numbers(*whatever_i_want):
    sum = 0
    for i in whatever_i_want:
        sum += i
    return sum
print(add_multiple_numbers(1, 2, 3, 4, 5, 6, 8)) # 29

# This will still work fine 
```


## **Kwargs Variable

