"""
Core classes and functions.
"""
from __future__ import annotations
import random
import json


class Card:
    """
    Class to represent a card.
    Has a rank and a suit.
    """
    # Dict to allow comparison of cards
    _rank_values = {"2": 2,
                    "3": 3,
                    "4": 4,
                    "5": 5,
                    "6": 6,
                    "7": 7,
                    "8": 8,
                    "9": 9,
                    "T": 10,
                    "J": 11,
                    "Q": 12,
                    "K": 13,
                    "A": 14}
    # Allowed suits
    _suits = ["S", "H", "D", "C"]

    def __init__(self: Card,
                 suit: str,
                 rank: str
                 ):
        """
        Initialise Card instance with specified rank and suit.

        :param suit: Suit of the card. Allowed suits are "S", "H", "D",
                     "H".
        :type suit: str.
        :param rank: Rank of the card. Allowed ranks are "A", the digits
                     "2" through "9", "T", "J", "Q", "K".
        :type rank: str.

        :returns: No return; constructor.
        :rtype: N/A.
        """

        # Just to check...
        rank, suit = str(rank), str(suit)

        # Check suit
        if suit.upper() in self._suits:
            self._suit = suit.upper()
        else:
            raise ValueError(f"Suit {suit} is not a valid suit")

        # Check rank
        if rank == "10":
            rank = "T"
        if rank.upper() in self._rank_values.keys():
            self._rank = rank.upper()
        else:
            raise ValueError(f"Rank {rank} is not a valid rank")

    def __eq__(self: Card,
               other: Card
               ) -> bool:
        """
        Compare the ranks of two cards.
        Does not compare suit.

        :param other: Card to compare to.
        :type other: Card.

        :returns: Whether the two cards are of the same rank.
        :rtype: bool.
        """
        return self._rank == other.rank

    def __gt__(self: Card,
               other: Card
               ) -> bool:
        """
        Compare the ranks of two cards.
        Does not compare suit.

        :param other: Card to compare to.
        :type other: Card.

        :returns: Whether the first card is of greater rank than the
                  second.
        :rtype: bool.
        """
        return self._rank_values[self._rank] > self._rank_values[other.rank]

    def __lt__(self, other):
        """
        Compare the ranks of two cards.
        Does not compare suit.

        :param other: Card to compare to.
        :type other: Card.

        :returns: Whether the first card is of lesser rank than the
                  second.
        :rtype: bool.
        """
        return self._rank_values[self._rank] < self._rank_values[other.rank]

    @property
    def suit(self: Card) -> str:
        """
        Getter for the card's suit.

        :returns: The suit of the card.
        :rtype: str.
        """
        return self._suit

    @property
    def rank(self: Card) -> str:
        """
        Getter for the card's rank.

        :returns: The rank of the card.
        :rtype: str.
        """
        return self._rank


class Table:
    def __init__(self, start_x, start_y, width, height):
        self._start_x = start_x
        self._start_y = start_y
        self._width = width
        self._height = height

    @property
    def x(self):
        return self._start_x

    @property
    def y(self):
        return self._start_y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height


class Hand:
    def __init__(self, *cards):
        self._cards = cards

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self._cards[key]

    @property
    def cards(self):
        return self._cards

    @property
    def suits(self):
        return [card.suit for card in self._cards]


def generate_cards(num):
    suits = ["H", "S", "D", "C"]
    ranks = ["A",
             "2",
             "3",
             "4",
             "5",
             "6",
             "7",
             "8",
             "9",
             "T",
             "J",
             "Q",
             "K"]

    # Toby you know there's a more elegant way to do this
    # Yes Toby I know but it's midnight
    out_list = []
    for _ in range(num):
        out_list.append(Card(random.choice(suits),
                             random.choice(ranks)))

    return tuple(out_list)


def parse_nl_hand(hand):
    """
    """
    if hand[0] == hand[1]:
        return hand[0].rank + hand[0].rank
    else:
        token = ["s", "o"][len(set(hand.suits)) - 1]
        if hand[0] > hand[1]:
            return hand[0].rank + hand[1].rank + token
        else:
            return hand[1].rank + hand[0].rank + token


def ranges(position, range_file="default_open_ranges.json"):
    with open(range_file) as infile:
        _ranges = json.load(infile)
    return _ranges[position.lower()]


def correct_move(position, hand):
    if parse_nl_hand(hand) in ranges(position):
        return "o"
    else:
        return "f"
