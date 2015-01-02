
import curses

class Status:
	def __init__(self, xoff, yoff):
		self.lines = 0
		self.blocks = 0
		self.nextBlock = None
		self.win = curses.newwin(15, 20, yoff, xoff)
		self.win.refresh()

	def paint(self):
		self.win.clear()
		if self.nextBlock != None:
			for p in self.nextBlock.pieces:
				self.win.addstr(1 + p.y, p.x - 6, "  ", curses.A_REVERSE)
		self.win.addstr(8, 1, "Lines:  {0:6}".format(self.lines))
		self.win.addstr(9, 1, "Blocks: {0:6}".format(self.blocks))
		self.win.refresh()




