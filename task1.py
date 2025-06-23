   
"""
    Converting a list of digits to the integer that it represents.

    Lets Consider the list [8, 3, 5, 1], the output integer should be 8351.
    We can write the number 8351 as:
    8351: 8000 + 300 + 50 + 1 

    implementation:
        In our code, we can take the output integer to be 0 and explore the list from left to right.
        while exploring for each digit, we can multiply the existing output by 10 (thus shifting one place left) 
        and then add the digit to the output integer.

        so the steps will be:
            output integer = 0
            for digit 8:
                output integer = 0 * 10 + 8 = 8
            
            output integer = 8
            for digit 3:
                output integer = 8 * 10 + 3 = 83

            output integer = 83
            for digit 5:
                output integer = 83 * 10 + 5 = 835

            output integer = 835
            for digit 1:
                output integer = 835 * 10 + 1 = 8351
        
        so final output integer will be 8351
            
"""


def list_to_intger_func(digit_list):
    """
    This function converts a list of digits to the integer that it represents.

    Args:
        digit_list (list): The list of digits that require to be converted

    Returns:
        Integer: integer representation of the list
            
    """
    
    output_integer = 0  # output first initilized to 0

    for digit in digit_list: # for each digit of the list 
        output_integer = output_integer * 10 + digit # Multiply the existing output by 10 to shift it one place left
    
    return output_integer # returning output integer



# Some test cases to demonstrate that it works

print("Test case 1: the list [8,3,5,1] represents the integer :", list_to_intger_func([8,3,5,1]))
print("Test case 2: the list [1,9,0] represents the integer :", list_to_intger_func([1,9,0]))
print("Test case 3: the list [0,9,0] represents the integer :", list_to_intger_func([0,9,0]))
print("Test case 2: the list [9,9,9,9,0] represents the integer :", list_to_intger_func([9,9,9,9,0]))
