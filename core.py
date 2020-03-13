"""
Core classes and functions.
"""
from __future__ import annotations
from typing import Sequence, Tuple, List
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
    _suits = ["s", "h", "d", "c"]

    def __init__(self: Card,
                 suit: str,
                 rank: str
                 ):
        """
        Initialise Card instance with specified rank and suit.

        :param suit: Suit of the card. Allowed suits are "s", "h", "d",
                     "c".
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
        if suit.lower() in self._suits:
            self._suit = suit.lower()
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
        Compare the ranks and suits of two cards.

        :param other: Card to compare to.
        :type other: Card.

        :returns: Whether the two cards are of the same rank.
        :rtype: bool.
        """
        if not isinstance(other, Card):
            return False
        else:
            return self._rank == other.rank and self._suit == other.suit

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

    def __repr__(self: Card) -> str:
        """
        Representation of the card.

        :returns: The rank and suit of the card.
        :rtype: str.
        """
        return self.rank + self.suit

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
    """
    Class to describe the geometry of a table to be displayed in a
    curses display.
    """
    def __init__(self: Table,
                 start_x: int,
                 start_y: int,
                 width: int,
                 height: int
                 ):
        """
        Initialise a Table instance with specified geometry.

        :param start_x: x-coordinate of the Table's top-left corner.
        :type start_x: int.
        :param start_y: y-coordinate of the Table's top-left corner.
        :type start_y: int.
        :param width: Width of the table.
        :type width: int.
        :param height: Height of the table.
        :type height: int.

        :returns: No return; constructor.
        :rtype: N/A.
        """
        self._start_x = start_x
        self._start_y = start_y
        self._width = width
        self._height = height

    @property
    def x(self: Table) -> int:
        """
        Getter for the x-coordinate of the Table's top-left corner.

        :returns: The x-coordinate of the Table's top-left corner.
        :rtype: int.
        """
        return self._start_x

    @property
    def y(self):
        """
        Getter for the y-coordinate of the Table's top-left corner.

        :returns: The y-coordinate of the Table's top-left corner.
        :rtype: int.
        """
        return self._start_y

    @property
    def width(self):
        """
        Getter for the Table's width.

        :returns: The Table's width.
        :rtype: int.
        """
        return self._width

    @property
    def height(self):
        """
        Getter for the Table's height.

        :returns: The Table's height.
        :rtype: int.
        """
        return self._height


class Hand:
    """
    Class to represent a poker hand.
    """
    def __init__(self: Hand,
                 *cards: Sequence[Card]
                 ):
        """
        Initialise a Hand instance with specified cards.

        :param cards: Sequence of card objects.
        :type cards: Sequence[Card].

        :returns: No return; constructor.
        :rype: N/A.
        """
        self._cards = tuple(sorted(cards))

    def __len__(self: Hand) -> int:
        """
        Returns the number of cards in the hand.

        :returns: The number of cards in the hand.
        :rtype: int.
        """
        return len(self.cards)

    def __getitem__(self,
                    index: int
                    ) -> Card:
        """
        [] override to return cards at a specified index.

        :returns: The card at index index.
        :rtype: Card.
        """
        return self._cards[index]

    def __repr__(self: Hand) -> str:
        """
        Return a representation of the hand.

        :returns: The ranks and suits of the cards.
        :rtype: str.
        """
        return "".join([repr(card) for card in self.cards])

    @property
    def cards(self: Hand) -> Tuple[Card]:
        """
        Getter for the cards in the hand.

        :returns: The hand's cards.
        :rtype: Tuple[Card].
        """
        return self._cards

    @property
    def suits(self: Hand) -> Tuple[str]:
        """
        Getter for the suits of the cards in the hand.

        :returns: The hand's cards' suits.
        :rtype: Tuple[str].
        """
        return tuple(card.suit for card in self._cards)


def generate_cards(num: int) -> Tuple[Card]:
    """
    Generates a specified number of randomly selected unique cards.

    :param num: Number of cards to generate (Must be an integer from 0
                to 52.
    :type num: int.

    :returns: A tuple of the specified amount of unique Card objects.
    :rtype: Tuple[Card].
    """
    suits = ["h", "s", "d", "c"]
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

    if num > 52:
        raise ValueError("Cannot generate more than 52 cards.")
    elif num < 0:
        raise ValueError("Cannot generate less than 0 cards.")

    out_list = []
    for _ in range(num):
        card_to_append = None
        while card_to_append not in out_list:
            card_to_append = Card(random.choice(suits),
                                  random.choice(ranks))
            out_list.append(card_to_append)

    return tuple(out_list)


def parse_nl_hand(hand: Hand) -> str:
    """
    Parse a 2-card Hand object into a string description.

    :param hand: Hand to parse.
    :type hand: Hand.

    :returns: String description for a 2-card hand.
    :rtype: str.
    """
    if hand[0].rank == hand[1].rank:
        return hand[0].rank + hand[0].rank
    else:
        token = ["s", "o"][len(set(hand.suits)) - 1]
        if hand[0] > hand[1]:
            return hand[0].rank + hand[1].rank + token
        else:
            return hand[1].rank + hand[0].rank + token


def ranges(position: str,
           range_file: str="default_open_ranges.json"
           ) -> List[str]:
    """
    Read a range for a specified position from a specified file.

    :param position: Position to get the range for.
    :type position: str.

    :returns: A range as a list.
    :rtype: List[str].
    """
    with open(range_file) as infile:
        _ranges = json.load(infile)
    return _ranges[position.lower()]


def correct_move(position: str,
                 hand: Hand
                 ) -> str:
    """
    Returns the correct move for a hand in a position.

    :param position: Position to check the hand.
    :type position: str.
    :param hand: Hand to check.
    :type hand: Hand.

    :returns: "o" for open, "f" for fold.
    :rtype: str.
    """
    if parse_nl_hand(hand) in ranges(position):
        return "o"
    else:
        return "f"
