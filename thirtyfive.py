from collections import deque
import random
# initialize deck of cards
deck = deque((f"{value} of {suit}" for value in
             ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
             for suit in ["Hearts", "Diamond", "Clubs", "Spades"]))
#Shuffle the desk
random. shuffle(deck)
#players and their hands
player1 = []
player2 = []
# Draw 5 cards for eah player
for _ in range(3):
    player1.append(deck.popleft())
    player2.append(deck.popleft())
# display players hands 
print("Player 1's Hand:")
print(player1)
print("\nPlayer 2's Hand:")
print(player2)
