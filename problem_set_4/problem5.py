
SCRABBLE_LETTER_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

def displayHand(hand):
    words = ""
    
    hand_keys = list(hand.keys())
    hand_keys.sort()    
    sorted_hand = {i:hand[i] for i in hand_keys}

    for letter in sorted_hand.keys():
        for i in range(sorted_hand[letter]):
            print(letter, end=" ")


    print("")

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    
    score = score * len(word)

    if len(word) == n:
        score = score + 50

    return score

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    len = 0
    for letter in hand.keys():
        len += hand[letter]

    return len   
     
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    handcopy = hand.copy()

    for letter in word:
        if handcopy.get(letter,0) > 0:
            handcopy[letter] -= 1

    hand_keys = list(hand.keys())
    hand_keys.sort()
    sorted_hand = {i:handcopy[i] for i in hand_keys}
    return sorted_hand

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function

    result = True
    if word not in wordList:
        result = False

    
    if result == True:
        hand_copy = hand.copy()
        for letter in word:
            if hand_copy.get(letter,0) > 0:
                hand_copy[letter] -= 1
            else:
                result = False
                break


    return result

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE (download ps4a.py to see)

    total_point = 0

    while calculateHandlen(hand) > 0:

        print("Current Hand: ", end= " ") 
        displayHand(hand)
        word = str(input('Enter word, or a "." to indicate thant you are finishend: ')).lower()
        if word == ".":
            print("Goodbye! Total score: {0} points.".format(total_point))
            return

        if isValidWord(word, hand, wordList):
            hand = updateHand(hand, word)
            point = getWordScore(word, n)
            total_point += point
            print('"{0}" earned {1} points. Total : {2} points'.format(word, point, total_point))
        else:
            print("Invalid word, please try again.")


    print("Run out of letters. Total score: {0} point".format(total_point))


wordList = ["test","test2"]
playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)