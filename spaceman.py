import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    print(secret_word)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
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

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, 
        the string should contain the letter at the correct position.  
        For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters
    #  that have been guessed correctly so far that are saved in letters_guessed 
    # and underscores for the letters that have not been guessed yet

    string_to_return = ''
    for char in secret_word:
        if (char in letters_guessed):
            string_to_return += char
        else:
            string_to_return += '_'
    
    return string_to_return

   


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word

    if guess in secret_word:
        return True
    else:
        return False


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    guessedLetters = []
    numGuessLeft = 7
    gameRunning = True
    
    

    print(f'''
            Welcome to Spaceman!
            The secret word contains: {len(secret_word)} letters.
            You have 7 incorrect guesses, please enter one letter per round.
            --------------------------------------------------------------
          ''')
    
    
    
    while (gameRunning):

        is_single_letter = False
        while (is_single_letter == False):
            letterGuessed = input("Enter a letter: ")
            if (len(letterGuessed) == 1):
                is_single_letter = True
                if (letterGuessed not in guessedLetters):
                    guessedLetters.append(letterGuessed)
        
        #TODO: show the player information about the game according to the project spec <<<---CHECK
        #TODO: Ask the player to guess one letter per round and check that it is only one letter <<<---CHECK 
        #TODO: Check if the guessed letter is in the secret or not and give the player feedback

        if (is_guess_in_word(guessedLetters[-1], secret_word)):
            print("Your guess appears in the word!\n")
        else:
            print("Sorry your guess was not in the word, try again.")
            numGuessLeft -= 1
            print(f"Number of guesses left: {numGuessLeft}\n")

        #TODO: show the guessed word so far
        guesed_so_far = get_guessed_word(secret_word, "".join(guessedLetters))

        print(f"Guessed word so far: {guesed_so_far}")

        #TODO: check if the game has been won or lost
        if numGuessLeft <= 0 and not is_word_guessed(secret_word, "".join(guessedLetters)):
            print("Sorry, you are out of guesses. You lose!")
            gameRunning = False
        
        elif numGuessLeft > 0 and is_word_guessed(secret_word, "".join(guessedLetters)):
              print("You won!!")
              gameRunning = False
            
        
#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)