"""
This work is licensed under the Creative Commons Attribution 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/

Date: August 3, 2025
Author: Michael C. Hernandez
email: michaelhern@hotmail.com

This program generates a randomized password.  By default it is 12 characters, but it can be
made longer or shorter (4 chars is minimum).  User can adjust probibilities of generating a 
letter, number, or special character using input arguements, but the default is a 45% chance 
of a letter of some sort, a 21% chance of a number, and a 34% chance of generating a special
character.
"""
import argparse
import secrets
import sys

# Word List
f = open('words.txt', 'r')
raw_list = f.read()
WORD_LIST = raw_list.split("\n") # contains 2001 words

def generate_password(
    num_of_words = 5,
    number = False
    ):
    """ 
    Generates a secrets password with the given parameters
    """
    password_word_list = []

    # Randomly select words from the list of possible words
    for i in range(0, num_of_words):
        word_index = secrets.randbelow(len(WORD_LIST) + 1) # Generate a random index for the word list
        selected_word = WORD_LIST[word_index]
        selected_word = selected_word[0].upper() + selected_word[1:].lower() # Make the first letter upper case
        password_word_list.append(selected_word)

    if number == True:
        password_word_list.append(secrets.randbelow(10))

    # Shuffle the list of words
    secrets.SystemRandom().shuffle(password_word_list)

    # Put the list of words together into a usable password
    output_password = ''
    for word in password_word_list:
        output_password = output_password + str(word) + '-' # Include a hyphen between words

    # Remove the final hyphen
    output_password = output_password[:-1]
    return output_password


def main():
    """
    The main function used to assign input arguements and call the generate_password() function.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--num_of_words', type=int, default=5, help="Number of words to have in your password")
    parser.add_argument('-n', '--number', action='store_true', default=False, help="Include an int in the password")
    # Run the parser and places the extracted data in a argparse.Namespace object
    args = parser.parse_args()

    if args.num_of_words < 1:
        print("The minimum required number of words is 1")
        return -1

    return generate_password(
        num_of_words = args.num_of_words,
        number = args.number
    )

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit