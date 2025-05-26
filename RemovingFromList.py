"""
File: RemovingFromList.py
Name: Vishal Singh
--------------------------
# This program removes the items from a list.
# Function: remove_from_list(lst, num)
# Input: lst: a list of integers, num: an integer
# Output: lst: a list of integers
"""
def main():
    numbers = [1, 2, 3, 4, 5]
    # Calling the function to remove the first item from the list.
    remove_from_list(numbers, 0)
    print(numbers)

# function: remove_from_list(lst, num) using pop()
def remove_from_list(lst, num):
    # Checking the length of the list to see if it is empty. If it is not empty, proceed.
    # Checking the index of the item to be removed to see if it is out of range.
    if len(lst) > 0 and num < len(lst):
        # Removing the item from the list. num is the index of the item to be removed.
        lst.pop(num)
        # Returning the list.
        return lst
    # If the list is empty, return the message.
    return print("Removed noting from the List because the list is empty. or the index is out of range.")

#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()