"""
File: DoublingList.py
Name: Vishal Singh
--------------------------
This file shows how to use take a list and make doubling the value of the elements.
"""
def main():
    """
    This program will double the value of the elements in a list.
    """
    numbers = [1, 2, 3, 4, 5]
    for i in range(len(numbers)):
        numbers[i] = numbers[i]*2
    print(numbers)

#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()