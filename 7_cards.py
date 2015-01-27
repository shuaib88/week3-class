# Deck of cards

SUITS = "\u2663 \u2665 \u2666 \u2660".split()
VALUES = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

deck = []
for suit in SUITS:
  for face in VALUES:
    deck.append(face+suit)
    
# How can we shuffle the deck?
##
##import random
##random.shuffle(deck)
##print(deck)
##

# How can we deal the top two cards from the deck?

#Method 1
##
##import random
##random.shuffle(deck)
##print(deck)
##
##print()
##print(deck[0],deck[1])

###Method 2
##import random
##random2 = random.sample(deck, 2)
##print(random2)
