#  Lists Examples 

# List of names 
list_of_names = ['John', 'Jane', 'Will']

# list of numbers 
list_of_numbers = [1, 2, 3, 4, 5]

def addNums():
    return 2 + 2

# list of types
list_of_types = [1, 2,'names', True, False, None, addNums, {'name': 'Doud', 'age': '28'}, (10, 16), [10, 20]]

print(type(list_of_types[len(list_of_types) - 1]))