import random

class Card:
    # Define the valid ranks and suits for standard playing cards
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, suit, rank):
        """
        Initialize a Card object with a suit and rank.
        Raises a ValueError if either attribute is invalid.
        """
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        self._suit = suit
        self._rank = rank

    def __eq__(self, other):
        """
        Compares two cards for equality based on their rank.
        """
        return self.rank == other.rank

    def __gt__(self, other):
        """
        Compares the relative order of two cards based on their rank.
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __str__(self):
        """
        Returns the string representation of a card, combining rank and suit.
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        Provides a representation suitable for containers like lists.
        """
        return self.__str__()

    @property
    def suit(self):
        """
        Accessor for the suit attribute.
        """
        return self._suit

    @property
    def rank(self):
        """
        Accessor for the rank attribute.
        """
        return self._rank

class Deck:
    def __init__(self):
        """
        Constructs a full deck of 52 unique cards using all combinations
        of valid suits and ranks.
        """
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        """
        Returns a string representation of the deck.
        """
        return str(self._deck)

    def shuffle(self):
        """
        Randomly shuffles the order of cards in the deck.
        """
        random.shuffle(self._deck)

    def deal(self):
        """
        Removes and returns the top card from the deck.
        """
        return self._deck.pop(0)

# Example usage
deck = Deck()
print(deck)
deck.shuffle()
print(deck)
print(deck.deal())
