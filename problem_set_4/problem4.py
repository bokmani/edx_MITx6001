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



print(calculateHandlen({'b': 1, 'a': 1}))