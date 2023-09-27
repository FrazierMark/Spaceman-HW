"""Module providing a function for random integers"""
import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    '''

    with open('words.txt', 'r', encoding='utf-8') as file:
        words_list = file.readlines()

    # comment this line out if you use a words.txt file with each word on a new line
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    print(secret_word)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    '''

 # Loop through the letters in the secret_word and check if a letter is not in letters_guessed
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word
     and underscores for letters that have not been guessed yet.
    '''

    string_to_return = ''
    for char in secret_word:
        if char in letters_guessed:
            string_to_return += char
        else:
            string_to_return += '_'

    return string_to_return


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    '''

    return guess in secret_word


def available_letters(guessed_letters, all_letters):
    '''
    Function to return letter that have yet to be guessed
    '''
    remaining_letters = []
    for letter in all_letters:
        if letter not in guessed_letters:
            remaining_letters.append(letter)
    return remaining_letters


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    '''

    guessed_letters = []
    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                   'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num_guess_left = 7
    game_running = True

    print(f'''
            Welcome to Spaceman!
            The secret word contains: {len(secret_word)} letters.
            You have 7 incorrect guesses, please enter one letter per round.
            --------------------------------------------------------------
          ''')

    while game_running:

        # Prompt user for single letter input
        # Reprompt if more than 1 letter
        is_single_letter = False
        while is_single_letter is False:
            letter_guessed = input("Enter a letter: ")
            if len(letter_guessed) == 1:
                is_single_letter = True
                if letter_guessed not in guessed_letters:
                    guessed_letters.append(letter_guessed)

        if is_guess_in_word(guessed_letters[-1], secret_word):
            print("Your guess appears in the word!")
            print("".join(available_letters(guessed_letters, all_letters)))
        else:
            print("Sorry your guess was not in the word, try again.")
            num_guess_left -= 1
            print(f"Number of guesses left: {num_guess_left}")
            print("".join(available_letters(guessed_letters, all_letters)))

        guesed_so_far = get_guessed_word(secret_word, "".join(guessed_letters))

        print(f"Guessed word so far: {guesed_so_far}\n")

        if num_guess_left <= 0 and not is_word_guessed(secret_word, "".join(guessed_letters)):
            print("Sorry, you are out of guesses. You lose!")
            print(f"The secret word was {secret_word}")
            game_running = False

        elif num_guess_left > 0 and is_word_guessed(secret_word, "".join(guessed_letters)):
            print("You won!!")
            game_running = False


# Function calls that will start the game
word = load_word()
spaceman(word)
