#!/usr/bin/python

import curses
import threading
import time
from game import Game


def update(game):
	while True:
		if mode == 1:
			game.tick()
			game.paint()
		time.sleep(1)

def init_curses():
	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(1)
	curses.start_color()
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
	curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)
	curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	curses.init_pair(7, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	curses.curs_set(0)
	stdscr.bkgd(curses.color_pair(3))
	stdscr.refresh()
	return stdscr



stdscr = init_curses()
mode = 0
game = Game(stdscr)

game.initialize()

updateThread = threading.Thread(target=update, args=(game,))
updateThread.daemon = True
updateThread.start()





while True:
	c = stdscr.getch()
	if c == ord("q"):
		break
	elif c == ord("s"):
		mode = 1

curses.nocbreak()
stdscr.keypad(0)
curses.curs_set(1)
curses.echo()
curses.endwin()

