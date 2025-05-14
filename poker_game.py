from deck import Deck, Card

"""
Defines a PokerHand class for evaluating basic poker hand types such as flush, pair,
full house, etc., using a hand of 5 cards dealt from a deck.
"""

class PokerHand:
    def __init__(self, deck):
        """
        Initializes a PokerHand by dealing 5 cards from a given deck.

        Args:
            deck (Deck): An instance of the Deck class.
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        Accessor for the hand's cards.
        """
        return self._cards

    def __str__(self):
        """
        Returns a string representation of the hand.
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Checks if all cards share the same suit.

        Returns:
            bool: True if all cards are of the same suit.
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
            return True

    @property
    def is_full_house(self):
        """
        Checks if the hand forms a full house (three of a kind and a pair).

        Returns:
            bool: True if full house conditions are met.
        """
        return self.number_matches == 8

    @property
    def number_matches(self):
        """
        Calculates the total number of rank matches between cards.

        Returns:
            int: The number of matches, used to infer hand categories.
        """
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Checks for exactly one pair.

        Returns:
            bool: True if a pair is present.
        """
        return self.number_matches == 2

    @property
    def is_two_pair(self):
        """
        Checks for exactly two pairs.

        Returns:
            bool: True if two pairs are present.
        """
        return self.number_matches == 4

    @property
    def is_trips(self):
        """
        Checks for three of a kind.

        Returns:
            bool: True if three cards share the same rank.
        """
        return self.number_matches == 6

    @property
    def is_quads(self):
        """
        Checks for four of a kind.

        Returns:
            bool: True if four cards share the same rank.
        """
        return self.number_matches == 12

    @property
    def is_straight(self):
        """
        Checks for a straight (five cards in sequence).

        Returns:
            bool: True if cards form a sequence with no repeated ranks.
        """
        self.cards.sort()
        distance = Card.RANKS.index(self.cards[4].rank) - \
                   Card.RANKS.index(self.cards[0].rank)
        return self.number_matches == 0 and distance == 4

# Simulate the probability of being dealt a full house
count = 0
matches = 0
while matches < 10:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_full_house:
        matches += 1
        print(hand)
    count += 1

print(f"probability of a full house is {100*matches/count}%")