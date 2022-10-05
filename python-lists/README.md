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

## Accessing elements of a list ( List Indexing )
- Elements of a list can be accessed using their indexes
- Lists are zero-indexed (Meaning You have to start counting from `0`)
- The first element of a list is at the index `0`
- The last element of a list is at the index the index `( length of that list - 1 )`

Lets say we have a list of names
```py

# list_index =   0       1       2        3
    names = ['James', 'Adam', 'Wills', 'Doud']

    print(names[0]) # James
    print(names[1]) # Adam
    print(names[2]) # Wills
```

## Getting the length of a list
You can get the length of a list by using a built-in function `len()` in python. The `len([1,2,3,4])` function takes a list as an argument and return its length. 

```python
# Getting the length of a List
nums = [1, 2, 3, 4, 5, 6, 'end']

print(len(numbers)) # 7

# getting the last index by subtracting the 1 from the length
print(nums[len(numbers) - 1]) # end
```
## Negative Indexing 

You can add a negative value to the square brackets when getting or indexing elements of a list to start from the last. 
* The last item in the list will have the index of `-1`
* Second to the last will have the index of `-2` and
* And the list goes on. 

```py
#Let's say we want to get the last item of the nums list
print(nums[-1]) # end
print(nums[-2]) # 6
print(nums[-3]) # 5
```
## List Slicing 
The slicing can be used to  get of cut some part of a list in multiple different ways using quare bracket and a column `[<start index>:<end index>]`
* The first part of the column is where you want to the slicing to start `<start index>` and the last part is where you want it to end `<end index>`
* If you leave the first part empty and and specify the second part like this `[:3]` it'll start from the index `0` to the  index `3`
* If you leave the last part empty it'll like this `[2:]` start from `2` to the end of the list. 
* Not specifying anything will give you a copy of the array from 1st to last 

```py
# Let's say we have a list of numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers[3:7]) # [4, 5, 6, 7]
print(numbers[:3]) # [1, 2, 3]
print(numbers[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```


* Let's say we want to get the last `3` item of the numbers list

```py
print(numbers[-3:]) # [8, 9, 10]
```

