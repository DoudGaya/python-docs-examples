# Python Args and Kwargs 

Args or Kwargs are used in python when you want to pass multiple arguments to a function. The arguments are received in form of a `tuple` (The main difference between a tuple and a list is that tuples are immutable), It is especially useful when you don't know the number of arguments upfront. Before we see an example of it let's do a simple demonstration of how a function works and then we'll see the cases where `*args` and `**kwargs` can be very helpful. 

## Normal Function
This is how you'd normally define a function in python. This function receives two arguments and returns their sum.
```py
# Example 1 - Normal Function Definition
def add_nums(number1, number2): 
    sums = number1 + number2
    return sum

print(add_nums(10, 20)) # 30
```

But What if we want to add more numbers? Well, there are a couple of ways to achieve that. Let's see all of them. 

1 - One way to do it is to pass all the arguments in the function like this


```py
# Example 2 - Passing Multiple arguments the naive way
def add_multiple_numbers(a, b, c, d, e, f):
    sum = a + b + c + d + e + f
    return sum

print(add_multiple_numbers(1, 2, 3, 4, 5, 6, 7)) # 21

```

2 - Another way is to create a `list` or a `tuple` and store all the items in it, then pass it as an argument to a function

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

3 - The most effective way is to use `*args` or `**kwargs` the main difference between the two is the keywords and we'll see an example of that later. With `*args` you can directly pass a different number of arguments without requiring a list or anything.

```py
# Example 4 - Passing Multiple arguments using the *args
def add_multiple_numbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add_multiple_numbers(1, 2, 3, 4, 5, 6, 8)) # 29
```
Note: While using the `*args` and `**kwargs` parameters, you don't have to explicitly use the `args` or `kwargs` keywords, it is not required. You can use name it, however, you want just like a normal argument. What's important is that you use the unpacking operators `*` `**` before the arguments name to let the function know that it is supposed to receive multiple parameters. 

```py

# Example 5 - Passing Multiple arguments using the *args
def add_multiple_numbers(*whatever_i_want):
    sum = 0
    for i in whatever_i_want:
        sum += i
    return sum
print(add_multiple_numbers(1, 2, 3, 4, 5, 6, 8)) # 29

# This will still work fine as expected
```
## Using **Kwargs Variable

The Kwargs accepts keyword Variables in their parameters and returns a key-value pair or a python dictionary `dict`.

```py
# Example 5 - Passing Multiple arguments using the *args
def add_multiple_numbers(**kwargs):
    sum = 0
    for i in whatever_i_want:
        sum += kwargs[i]
    return sum
print(add_multiple_numbers(num1=10, num2=20, num3=30)) # 60
```

Now that we've learned how the `**kwargs` and `args` works, Let's exlore a bit further to full understand how to use them all in a single funtion. 

In some cases you may need to use the `*args` and `**kwargs` in a single function, maybe you might want to even include an named argument arguments. 

## Using both `*args` and `**kwargs` in the same function

When the need is required. `*args` will come first before `kwargs` and if you have normal named argument it will come even before the `*args`. Trying to pass `*args` before normal named parameters like `name and surname` or `**kwagrs` before `*args` like  `def func(*args, name):` or `def func(**kwargs, *args ):` will result in an error.



```py
# Now lets create a function that receives first and lastname of a user, then recieve all the the money notes he have, and lasttly the items in his bap pack.
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
    total: {1}
    items: {2} 
    '''.format(full_name, sum, all_items)
print(multiple_args('Doud', 'Gaya', 10,20,30, item1="Pen, ", item2="Paper,", item3=" and Laptop!"))

# Name:  Doud Gaya
# total: 60
# items: Pen, Paper, and Laptop!

```

Note: the `''' string '''` is a template literals use to print special types of string and the ` format() ` is a [string](../python_string/string.py) method to print a formatted string. To learn more about [string manipulation](../python_string/string.py) check out this [link here](../python_string/string.py)



## THe Unpacking Operators `*` and `**`

The two eperators can be used to do alot of cool stuffs beyond just parsing arguments to a function.

