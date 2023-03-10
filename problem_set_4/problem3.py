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

ret = isValidWord('kwijibo', {'w': 1, 'i': 2, 'k': 1, 'b': 1, 'o': 1, 'j': 1},['test','abcd','kwijibo'])
print(ret)