"""
FIle: MemoryGame.py
Name: Vishal Singh
----------------------
This program lets the user play a memory game using lists.
1. Create the truth list.
2. Shuffle the list by using function random.shuffle(list).
3. Create a displayed list.
    a) Use the '*' symbol to denote that a value is hidden to the user.
    b) if user given index matches the truth value then display the value for those index only, rest will be hidden as * .
    c) Length of the list is equal to truth list.
4. Get two valid indices from the user.
    a) A valid number, greater than or equal to 0 and less than or equal to the index of the last element in the list.
    b) The second index the user supplies in the pair must not be equal to the first (i.e. the two indices supplied must be distinct)
    c) Both User Index should be a number as explained in point a).
5. Check correct.
    a) Get two valid inputs from the user and check if there is a match (the values of the indices in the truth lists are equal).
    b) If the values don't match:
        i) Do not update the displayed list.
        ii) Print out the values at the two guessed indices.
        iii) Print "No match. Try again."
        iv) Use input() to wait for the user to press the "Enter" key before continuing.
        v) Clears the terminal screen by printing multiple newlines.
    c) If the values do match:
        i) Update the displayed list
        ii) Print "Match!"
        iii) Do not print the values at each guessed index. wait for the user to press "Enter" to continue.
        iv) Clears the terminal screen by printing multiple newlines.
        v) Print the display list with as many pairs has been matched.
6. Play multiple turns until all the pairs have been correctly located.
    a) Between turns make sure to clear terminal by printing multiple newlines.
    b) Print out the display array
    c) Get two valid indices from the user
    d) Determine if they indices have matching values in truth_list.
    e) If it is a match, print "Match!" and call clear_terminal(). (No waiting for the Enter key).
7. When the game is won:
    a) Print out the display array (which will now be fully uncovered)
    b) Print 'Congratulations! You won!'
"""
import random

# Game configuration - number of pairs to match
NUM_PAIRS = 3


def main():
    """
    Main game function that manages the memory matching game flow.
    Initializes the game board, handles player turns, and checks for matches.
    """
    # Generate the solution list with random pairs and shuffle them
    truth_list = random_pairs_truth_list(NUM_PAIRS)
    # Create display list that players see (all hidden initially)
    display_list = ['*'] * len(truth_list)

    # Continue game until all pairs are found (no more '*' in display)
    while '*' in display_list:
        # Show current game board
        print(display_list)

        # --- FIRST INDEX SELECTION ---
        # Get valid first index from player
        index1 = get_valid_input("Enter an index: ", len(truth_list))
        # Ensure selected position hasn't been matched yet
        while display_list[index1] != '*':
            print("This number has already been matched. Try again.")
            index1 = get_valid_input("Enter an index: ", len(truth_list))

        # --- SECOND INDEX SELECTION ---
        # Get valid second index from player
        index2 = get_valid_input("Enter an index: ", len(truth_list))
        while True:
            # Validate second index:
            # - Not same as first index
            # - Not already matched
            if index2 == index1:
                print("You entered the same index twice. Try again.")
            elif display_list[index2] != '*':
                print("This number has already been matched. Try again.")
            else:
                break  # Valid selection
            index2 = get_valid_input("Enter an index: ", len(truth_list))

        # --- CHECK FOR MATCH ---
        if truth_list[index1] == truth_list[index2]:
            # Match found - reveal the numbers permanently
            display_list[index1] = truth_list[index1]
            display_list[index2] = truth_list[index2]
            print("Match!")
            clear_terminal()  # Clear screen to hide previous selections
        else:
            # No match - show values temporarily
            print(f"Value at index {index1} is {truth_list[index1]}")
            print(f"Value at index {index2} is {truth_list[index2]}")
            print("No match. Try again.")
            input("Press Enter to continue...")
            clear_terminal()  # Clear screen to hide values

    # Game completed - show final board and victory message
    print(display_list)
    print("Congratulations! You won!")


def get_valid_input(prompt, max_val):
    """
    Validates and returns a number input from the player.
    Ensures input is a number within valid range.

    Args:
        prompt: Message to display when asking for input
        max_val: Maximum allowed value (exclusive)

    Returns:
        Valid integer between 0 and max_val-1
    """
    while True:
        user_input = input(prompt)

        # Check if input is numeric
        if not user_input.isdigit():
            print("Not a number. Try again.")
            continue

        val = int(user_input)

        # Check if input is within valid range
        if val < 0 or val >= max_val:
            print("Invalid index. Try again.")
            continue

        return val


def random_pairs_truth_list(num_pairs):
    """
    Generates and shuffles the solution list containing number pairs.

    Args:
        num_pairs: Number of unique number pairs to generate

    Returns:
        Shuffled list containing each number twice in random order
    """
    truth_list = []
    # Create pairs of numbers (0,0, 1,1, etc.)
    for i in range(num_pairs):
        truth_list.append(i)
        truth_list.append(i)
    # Randomize the order of numbers
    random.shuffle(truth_list)
    return truth_list


def clear_terminal():
    """
    Clears the terminal screen by printing multiple newlines.
    Note: This is a simple solution; platform-specific methods may be better.
    """
    for i in range(20):
        print('\n')


# Standard Python idiom to execute main() when script is run directly
if __name__ == '__main__':
    main()