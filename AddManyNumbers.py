"""
File: AddManyNumbers.py
Name: Vishal Singh
--------------------------
This file shows how to list to add many numbers and return the sum.
1. User will enter many numbers.
2. The function will add all numbers and return the sum.
"""
def main():
    """
    This program will add many numbers and return the sum.
    """
    print("Let's add many numbers.")
    number = []
    user_input("Enter number separated by spaces (2 33 400): ", number)
    result = add_many_numbers(number)
    print(f"Sum of your given numbers are: {result}.")

def user_input(prompt, lst):
    user_number = input(prompt).strip().split()
    for i in range(len(user_number)):
        num = int(user_number[i])
        lst.append(num)

def add_many_numbers(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total

#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()