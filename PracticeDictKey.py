"""
File: PracticeDictKey.py
Name: Vishal Singh
--------------------------
# This program demonstrates how to use Dictionary to store data.
"""
def main():
    ages = {'Adam': 12, 'Bart': 15, 'Lisa': 13, 'Maggie': 14, 'Anne': 14, 'Chris': 16}

    # Using Function 'get()' to get the value of the key.
    age = ages.get('Adam')
    # Using Function 'get()' to check if the key exists in the dictionary.
    if ages.get('Adam') is not None:
        print(f'Adam is {age} years old.')
    else:
        print('Adam is not in the dictionary.')

    # Using Function: 'pop()' to remove the key-value pair.
    ages.pop('Chris')
    print(ages)

    # Using Function: 'popitem()' to remove the last inserted key-value pair.
    ages.popitem()
    print(ages)

    # Using Function dictionary.keys() to get all the keys in the dictionary.
    ages_keys = ages.keys()
    print(ages_keys)

    # Using Function dictionary.values() to get all the values in the dictionary.
    ages_values = ages.values()
    print(ages_values)

    # Using Function: 'update()' to add more key-value pairs.
    ages.update({'Anne': 15, 'Chris': 16})
    print(ages)

    # Using Function: 'items()' to get all the key-value pairs in the dictionary.
    ages_items = ages.items()
    print(ages_items)

    # Using Function: 'del' to delete the key-value pair.
    del ages['Lisa']
    print(ages)

    # Using Function: 'clear()' to clear all the key-value pairs in the dictionary.

























###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
        main()