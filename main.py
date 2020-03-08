#!/usr/bin/python3.8

import random
import draw
import core
import curses

# TODO introduce menu to allow:
# - specifying ranges
# - saving stats
# - viewing more stats
#   - % accuracy
#   - best/worst positions
# - viewing history

# TODO introduce other players
# - limpers
#   - iso-raise
#   - overlimp
# - openers
#   - 3!
#   - flat

HAND_HISTORY_FILE = ".hand_history.csv"

def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    cursor_x = 0
    cursor_y = 0
    curses.curs_set(0)

    k = 0

    correct = 0
    wrong = 0

    while k != ord('q'):
        k = 0
        
        card1, card2 = core.generate_cards(2)
        while card1.suit == card2.suit and card1.rank == card2.rank:
            card1, card2 = core.generate_cards(2)
        hand = core.Hand(card1, card2)
        positions = ["SB",
                     "UTG",
                     "UTG+1",
                     "MP1",
                     "LJ",
                     "HJ",
                     "CO",
                     "BU"]

        position = random.choice(positions)

        draw.draw_table(stdscr, hand, position)
        stdscr.addstr(0, 0, "Correct: {}, Wrong: {}".format(correct, wrong),
                      curses.color_pair(1))
        
        while k not in (ord("o"), ord("f"), ord('q')):
            k = stdscr.getch()

        if k == ord(correct_move := core.correct_move(position, hand)):
            correct += 1
            correct_choice = 1
        else:
            wrong += 1
            correct_choice = 0

        with open(HAND_HISTORY_FILE, 'a') as hand_history_file:
            hand_history_file.write(position + " " +
                                    repr(hand) + " " +
                                    correct_move + " " +
                                    str(correct_choice) + "\n")

if __name__ == "__main__":
    curses.wrapper(main)
