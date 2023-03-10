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



def getFrequencyDict(word):
    hand = {}
    for letter in word:
        hand[letter] = hand.get(letter,0) + 1
   
    #key 순으로 정렬을 한번 더 해준다
    #hand의 key만 list로 추출해서 sort
    hand_keys = list(hand.keys())
    hand_keys.sort()

    #새로운 dictionary sorted_hand에 i:hand[i]로 dictionary를 만드는데, 이때 for 순서는 정렬된 hand_keys 순서
    #sorted_hand = {i:hand[i] for i in hand_keys}

    #위의 내용을 쉬운 코드로 하면
    sorted_hand = {}
    for i in hand_keys:
        sorted_hand[i] = hand[i]
    

    return sorted_hand



def displayHand(hand):
    words = ""
    handcopy = hand.copy()

    hand_keys = list(hand.keys())
    hand_keys.sort()    
    sorted_hand = {i:handcopy[i] for i in hand_keys}

    for letter in sorted_hand.keys():
        for i in range(sorted_hand[letter]):
            print(letter, end=" ")


    print("")

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}    
#print(hand['e'])
#print(hand.get('q',0))

# print(getFrequencyDict("hlelo"))

displayHand(hand)
# hand = updateHand(hand, 'quail')

# print(hand)


# displayHand(hand)

print(updateHand({'x': 1, 'a': 1, 'd': 2, 'w': 1, 'p': 1, 't': 1, 'n': 1, 'k': 1, 'i': 1, 'o': 1}, 'daikon'))