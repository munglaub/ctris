#!/usr/bin/python3

import curses
import threading
import time
from game import Game
from highscore import Highscore


def update(game):
	global mode
	global highscore
	while True:
		try:
			if mode == 1:
				mode = game.tick()
				game.paint()
				if mode == 2:
					highscore.addScore(game.getLines(), game.getBlocks())
			time.sleep(1)
		except:
			pass

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
# 0 - initial mode - game not started
# 1 - game running
# 2 - game over
# 3 - pause/show highscore
mode = 0

highscore = Highscore()

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
		game.initialize()
		mode = 1
	elif mode == 1 and (c == curses.KEY_LEFT or c == ord("j")):
		game.tryMoveLeft()
		game.paint()
	elif mode == 1 and (c == curses.KEY_RIGHT or c == ord("l")):
		game.tryMoveRight()
		game.paint()
	elif mode == 1 and (c == curses.KEY_DOWN or c == ord("k")):
		game.tryMoveDown()
		game.paint()
	elif mode == 1 and (c == curses.KEY_UP or c == ord("i")):
		game.tryTurn()
		game.paint()
	elif mode == 1 and c == ord(" "):
		game.fall()
		mode = game.tick()
		game.paint()
		if mode == 2:
			highscore.addScore(game.getLines(), game.getBlocks())
	elif c == ord("h"):
		if mode == 3:
			mode = 1
		else:
			mode = 3
			highscore.showHighscore()

curses.nocbreak()
stdscr.keypad(0)
curses.curs_set(1)
curses.echo()
curses.endwin()


