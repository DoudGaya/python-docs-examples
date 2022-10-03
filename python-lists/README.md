# Python Lists 

The Python list is the collection of data - in a container called a list, in other languages its called an array. The simplest way to initialize a list is to create a variable name and assigned it to an open and closed square bracket `[]`. Inside of this bracket you can add different datatypes seperated by a ( `,` ). A list in python can contain different datatypes incluidng a function.


- You can store a list of related data in a list
- You can also store mixed data like in example 2
- You can add just about any datatype you want to your list like in example 3


2 - Example of an empty list
```py
# list example 1
list_name = [] #empty list
```
2 - Example of Lists of strings and numbers `str` and `int`
```py
list_of_numbers = [1,2,3,4,5,6,7] # int Lists

list_of_names = ['James', 'jane', 'Wills', 'Dave'] # str lists 
```

3 - Example of list of different types 

```py
# different types 
 def addNums(x,y):
    return x + y

list_of_types = [1, 2,'names', True, False, None, addNums, {'name': 'Doud', 'age': '28'}, (10, 16), [10, 20]]
```


## List manipulations
List are very powerful in python and many other programming languages, because you can add item, remove item, arrange items in specific order and many more. Let's see an exmaples

### List Indexing or accessing elements of a list
- Elements of a list can be accessed using their indexes
- Lists are zero-indexed (Meaning You have to start counting from `0`)

Lets say we have a list of names and numbers
```py

# list_index =   0       1       2        3
    names = ['James', 'Adam', 'Wills', 'Doud']

    print(names[0]) # James
    print(names[1]) # Adam
    print(names[2]) # Wills
```

### Getting the length of a list
You can get the length of a list by using a built-in function `len()` in python. The `len([1,2,3,4])` function takes a list as an argument and return its length. 
