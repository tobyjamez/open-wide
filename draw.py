import curses
import random
import core

def draw_table(stdscr, hand, position):

    stdscr.clear()
    stdscr.refresh()

    height, width = stdscr.getmaxyx()

    curses.start_color()

    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_WHITE)

    table = core.Table(int(width / 3),
                       int(height / 3),
                       int(width / 3),
                       int(height / 3))

    start_x_position = int(width / 2 ) - len(position)
    stdscr.addstr(int(height / 2), start_x_position, position)

    top = "/" + "".join(["-"] * (table.width - 2)) + "\\"
    bottom = "\\" + "".join(["-"] * (table.width - 2)) + "/"

    stdscr.attron(curses.color_pair(2))
    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(table.y, table.x, top)
    stdscr.addstr(2 * table.y, table.x, bottom)
    for y in range(table.height + 1, table.height * 2):
        stdscr.addstr(y, table.x - 1, "|")
        stdscr.addstr(y, table.x + table.width, "|")

    draw_hand(stdscr, hand, table)
    


def draw_hand(stdscr, hand, table):
    color_dict = dict(H = curses.color_pair(4),
                      D = curses.color_pair(4),
                      S = curses.color_pair(3),
                      C = curses.color_pair(3))
    stdscr.attroff(curses.A_BOLD)
    stdscr.attron(curses.color_pair(3))
    n_cards = len(hand.cards)
    for index, card in enumerate(hand.cards):
        for y in range(int((table.y + table.height / 1.4)),
                       int(table.y + table.height)):

            stdscr.addstr(y,
                          int(table.x + (table.width / (n_cards + 2)) * (index + 1)),
                          "|" + "".join(["-"] * int((table.width / (n_cards + 2)) - 1)) + "|")

        if card is not None:
            stdscr.addstr(int((table.y + table.height / 1.4)), 
                          int(table.x + (table.width / (n_cards + 2)) * (index + 1)),
                          "/" + "".join(["-"] * int((table.width / (n_cards + 2)) - 1)) + "\\")

            stdscr.attron(color_dict[card.suit])
            stdscr.addstr(int((table.y + table.height / 1.4)) + 1, 
                          int(table.x + (table.width / (n_cards + 2)) * (index + 1)) + 2,
                          card.rank)

            stdscr.addstr(int((table.y + table.height / 1.4)) + 2, 
                          int(table.x + (table.width / (n_cards + 2)) * (index + 1)) + 2,
                          card.suit)
            stdscr.attron(curses.color_pair(3))
        else:
            stdscr.addstr(int((table.y + table.height / 1.4)), 
                          int(table.x + (table.width / (n_cards + 2)) * (index + 1)),
                          "\\")
    stdscr.attroff(curses.color_pair(3))
