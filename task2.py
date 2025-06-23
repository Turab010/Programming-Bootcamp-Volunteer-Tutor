  
"""
    *******       Number guessing game       ***********

    This game randomly generates a number between 1 to 100 using python's random library.
    It then prompts the user to guess the randomly generated number.

        -> If the user guess is not a digit or a number between 1 to 100, It notifies the user and re-prompt for valid input
    
    When user enters a valid number

        -> If the guess is lower, notifies the user that the guess is lower.
        -> If the guess is higher, notifies the user that the guess is higher.
        -> If the guess matched, notifies the user that the guess is successful.
            
"""

import random

def display_welcome_message():

    """
    This function displays a welcome message to play the game.

    Args:
        None

    Returns:
        None     
    """

    print("Greetings! Welcome to the Game") 


def generate_random_number():
     
    """
    This function generates a random number.

    Args:
        None

    Returns:
        Integer: returns the randomly generated number     
    """
     
    random_number = random.randint(1, 100) # Using python's random library to generate a random number
    return random_number


def take_user_input(): 

    """
    This function takes input from user.

    Args:
        None

    Returns:
        String: returns the user input as string format, will cast into integer later   
    """
    user_number = input(" Please Enter your Guess: ") # taking input from the user
    return user_number


def isValid_user_input(user_number):

    """
    This function checks whether user input is valid or not.

    Args:
        user_number (String): User input number in string format

    Returns:
        Boolean:
            False: Returns False if the user input is not valid
            True: Returns True if the user input is valid
    """
    try:
        user_input = int(user_number) # Casting the user input to integer

    except ValueError: # If can't Cast successfully then the input is not a digit
        print("Your input is not a digit, Please enter a valid digit")
        return False
     
    if not (user_input <= 100 and user_input >= 1): # Checking whether the user input is in the valid range (between 1 to 100)
        print("Please enter a digit between 1 and 100")
        return False
    
    return True # if the user input is a valid digit between 1 to 100, return True

    
def is_guess_matched(target_number, guess_number):

    """
    This function checks whether user guess is successful or not.

    Args:
        target_number (Integer): Randomly generated number
        guess_number (String): User guessed number

    Returns:
        Boolean:
            False: If the user guess is not successful
            True: If the user guess is successful
    """
       
    if guess_number < target_number: # Guess number is less than the random number
        print("Guess is lower, guess again")
        return False
    
    elif guess_number > target_number: # Guess number is higher than the random number
        print("Guess is higher, guess again")
        return False
    
    else: # Guess number and the random targer number are the same
        print("Guess is Successful") 
        return True



def play_game():

    """
    This function is the main function to play the game

    Args:
        None

    Returns:
        None
    """
   
    display_welcome_message()
    is_guess_successful = False # intiliazing the boolean value to False
    attempt = 0 # Counting the number of attempts, for points and other purpose
    random_number = generate_random_number() # Generates a random number
    
    while not is_guess_successful:
        user_number = take_user_input() # Take input from user
        attempt = attempt + 1 # incrementing the attempt count
        isValid_input = isValid_user_input(user_number) # Checking whether user input is valid or not

        if isValid_input:
            is_guess_successful = is_guess_matched(random_number, int(user_number)) #Checking whether the guess is successful
            if is_guess_successful:
                print(f"Guess is Successful after {attempt} attempts") # Print the final Successful message if the game is successful
        

# Test cases to demonstrate that it works

play_game() # Start the game