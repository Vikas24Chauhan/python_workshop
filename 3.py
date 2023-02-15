'''
Create a function named ‘check_string’, the function should accept a string data from the user and the function should check if the user input contains the letter ‘s’ in it.
If it contains the letter ‘s’ then print- ‘The string is containing the letter ‘s’’, if not then print- ‘The string doesn’t contain the letter ‘s’’.
'''
user_string = input("Please enter any string :- ")


def check_string(string):
    if 's' in string:
        print('The string is containing the letter ‘s’')
    else:
        print('The string doesn’t contain the letter ‘s’')


check_string(user_string)
