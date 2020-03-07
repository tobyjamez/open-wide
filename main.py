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

# TODO introduce other players
# - limpers
#   - iso-raise
#   - overlimp
# - openers
#   - 3!
#   - flat

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

        if k == ord(core.correct_move(position, hand)):
            correct += 1
        else:
            wrong += 1


if __name__ == "__main__":
    curses.wrapper(main)
