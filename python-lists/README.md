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
The slicing can be used to  get of cut some part of a list in multiple different ways using quare bracket and a column `[<startIndex>:<endIndex>]`
* The first part of the column is where you want to the slicing to start `<startIndex>` and the last part is where you want it to end `<endIndex>`
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

## Multidimentional List 

A list can contain another list , Let's se an exmaple of that
* Let's say we have a list that conatains two lists
* First conatains number and the other contains string
* Getting number `2` from the number list will be done like this
```py
listings = [[1,2,3], 'num1', 'num2', 'num3']

listings[0][1] # 2
```

## Changing items of a list

* We can change any item using its index
```py
names = ['Sam', 'Wills', 'Dan']

names[-1] = 'John'

print(names) # ['Sam', 'Wills', 'John']
```

* We can also change couple of items using the slicing trick

```py
    names[:2] = ['Jane', 'Maria']
    print(names) # ['Jane', 'Maria', 'John']
```

* Maybe I just want to remove items from the list
```py 
 names[:2] = []
```

## Adding more to a list

* Let's say I have a list `[1,2,3,4]` and another list `[5,6,7,8]`
```py
num1 = [1,2,3,4]

num2 = [5,6,7,8]

print(num1 + num2) # [1,2,3,4,5,6,7,8]
```
## List Methods 
These are functions you can use on a list. Maybe to modify a list or to manipulate a list. the `len()` is an example of it. 

## Adding to a list with `list.append()`
* This can be use to add item to the end of a list
* Equivalent to `a[len(a):] = [x]`.
```py
names = ['Sam', 'Wills', 'Dan']
names.append('Ali')

print(names) # ['Sam', 'Wills', 'Dan', 'Ali']

```
## Extend a list with `list.extend()`
* You can add more items to a list with `list.extend()`
```py
nums = [1,2,3,4,5]

nums.extend([6,7,8,9,0]) 

print(nums) #  [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
```
## Add item to a specific index with `list.insert()`
* You can insert an item in at given position with `list.insert()`
* The insert method will push the rest of the items to the next indexes
* `insert()` takes the two params, the first is the index and second is what to insert.
```py
    sports = ['Foot Ball', 'Soccer', 'Tennis']
    sports.insert(0, 'Basket Ball')

    print(sports) # ['Basket Ball', 'Foot Ball', 'Soccer', 'Tennis']
```
## Remove item from a list with `list.remove()`
* You can remove an item by passing it to the remove function
* if item doesn't exist it'll return a ValueError.

```py 
 sports = ['Foot Ball', 'Soccer', 'Tennis']
 sports.remove('Soccer')
 print(sports) # ['Foot Ball', 'Tennis']
```

## Removing item using index with `list.pop(i)`
* `pop` method takes an index and remove element at that specific index
* If no index is passed it'll remove the last item in the list
```py 
sports = ['Foot Ball', 'Soccer', 'Tennis']

sports.pop(0) 

print(sports) # ['Soccer', 'Tennis']
```

## Clearing all the elements of a list with `list.clear()`
* This clears all the elements in a list
* Equivalent to `del a[:]`
* Also Equivalent to `a[:] = []`
```py
    numbers = [1,2,3,4,5,6,7]
    print(numbers.clear()) # []
```


## Getting the index of an item with `list.index()`
* the index method takes 3 arguments
* Fist argument is the item to look for 
* Second where to start looking 
* third where to stop looking
* if only one argument is passed then it'll return the first index of the item

```py 
   numbers = [1,'a',3,4,'a',6,7, 'a', 8, 9]
   numbers.index('a') # 1
   numbers.index('a', 2, 6) # 4
   numbers.index('a', 6) # 7
```

## Count the number of times item appear in a list with `list.count()`

```py 
    numbers = [1,'a',3,4,'a',6,7, 'a', 8, 9]
    print(numbers.count('a')) # 3
```

## Reversing elements of a list with `list.reverse()`
* With reverse, elements from the left moves to the right and vice-versa
```py
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums.reverse()

print(nums) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

## Sorting a list alphabetically with `list.sort()`
* This method takes two optional parameters, 
* The `key='...'` and the `reverse='...'`
* The `reverse=` tells the direction of the sort ascending or descending, takes it `True` or `False` value

```py
    #Sorting random numbers 
    nums = [8, 7, 2, 4, 5, 10, 3, 1, 9, 6]
    nums.sort()
    print(nums) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # with reverse=True
    random = [8, 7, 2, 4, 5, 10, 3, 1, 9, 6]
    random.sort(reverse=True)
    print(random) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```
* The `key='...'` option is particularly useful when you're dealing with a list of datatypes like strings or a `dictionary` or a `set` or a `tuple`
* Let's see an example of that.
```py 
    # sorting by length of a string
    nums = ['james', 'jim', 'sam', 'jimmy']
    nums.sort(key=len)
    print(nums) # ['jim', 'sam', 'james', 'jimmy']


    # Sorting tuples list but only the second item in the tuple
    # step i define a func

    coordinates = [(2, 4), (3, 2), (4, 1), (9, 0)]

    def secondItem(val):
        return secondItem[1]
    coordinates.sort(key=secondItem)

    print(coordinates) # [(9, 0), (4, 1), (3, 2), (2, 4)]
```

## The lambda function

