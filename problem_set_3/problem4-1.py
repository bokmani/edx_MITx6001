import string

def isWordGuessed(secretWord, lettersGuessed):
    result = True
    for letter in secretWord:
        if lettersGuessed.count(letter) == 0:
            result = False
            break

    return result

def getGuessedWord(secretWord, lettersGuessed):
    result = secretWord

    for letter in secretWord:
        if lettersGuessed.count(letter) == 0:
            result = result.replace(letter, '_')

    return result

def getAvailableLetters(lettersGuessed):
    secretWord = string.ascii_lowercase
    #print(secretWord)
    result = secretWord

    for letter in secretWord:
        if lettersGuessed.count(letter) > 0:
            result = result.replace(letter, '')

    return result   


def hangman(secretWord):
    #시도횟수
    mistakesMade = 0
    #가능한 단어
    availableLetters = string.ascii_lowercase
    #추측한 글자 list
    lettersGuessed = []
    #print 결과
    result = ""

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))

    # 8번 반복
    while 8 - mistakesMade > 0:
        # 단어가 맞으면 congrat print하고 break
        if isWordGuessed(secretWord,lettersGuessed) == True:
            print("-----------")
            print("Congratulations, you won!")
            break
        else:   
            #횟수 / 입력가능한 문자 표시하고 입력 받음
            print("-----------")
            print("You have {} guesses left.".format(8 - mistakesMade))
            print("Available Letters: ", getAvailableLetters(lettersGuessed))
        
            guess = str(input('Please guess a letter:')).lower()

            # 입력받은 글자가 정답에 있고, 이전에 추측한 문자에 없다면, 
            # letterGuessed에 글자 추가하고, Good guess 출력
            if guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            # 이미 추측한 문자에 있다면 aleady guess 출력
            elif guess in lettersGuessed:
                print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))   
            # 정답에 없다면, oops 출력하고, 추측한 문자 list에 추가 / 횟수 1 추가
            elif guess not in secretWord:
                print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))    
                lettersGuessed.append(guess)
                mistakesMade +=1
            
        

        # 횟수가 8이 되면 Sorry 출력, break
        if mistakesMade == 8:
            print('------------')
            print('Sorry, you ran out of guesses. The word was', secretWord)
            break       
                              
               



hangman("c")
