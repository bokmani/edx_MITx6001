import string

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    #시도횟수
    mistakesMade = 8
    #가능한 단어
    availableLetters = string.ascii_lowercase
    lettersGuessed = False
    result = ""

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))

    for letter in secretWord:
      result += "_"

    while result != secretWord and mistakesMade > 0:
        print("-----------")
        print("You have {} guesses left.".format(mistakesMade))
        print("Available Letters: ", availableLetters)
        
        guess = str(input('Please guess a letter:')).lower()

        lettersGuessed = False
        if guess in availableLetters:
          availableLetters = availableLetters.replace(guess,"")
          i=0

          if guess in secretWord:
            for letter in secretWord:
              if guess == letter:
                result = result[:i] + letter + result[i+1:]
                lettersGuessed = True
              i+=1                   

          if lettersGuessed:
            print("Good guess: ",result)
          else:
            mistakesMade -=1
            print("Oops! That letter is not in my word: ",result)    
        else:
            print("Oops! You've already guessed that letter: ",result)                  


    print("-----------")

    if mistakesMade > 0:
      print("Congratulations, you won!")
    else:
      print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))




hangman("c")
