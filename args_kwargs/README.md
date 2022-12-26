# Python Args and Kwargs 

Args is used in python when you want to recieve multiple argument to a function. It is especially useful when you don't know the number of arguments upfront. Now let's see an example of. but before we do I want to make some few demonstarations on how you can pass an argument to a function the normal way and how its different from using the `*args` and `**kwargs`


```py
def add_nums(number1, number2): 
    sums = number1 + number2
    return sum

print(add_nums(10, 20))
```