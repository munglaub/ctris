
import curses

class Target:
	def __init__(self, width, xoff, yoff):
		self.width = width
		self.win = curses.newwin(10, self.width, yoff, xoff)
		self.win.refresh()
		self.current = None

	def paint(self):
		self.win.clear()
		if self.current != None:
			for p in self.current.pieces:
				self.win.addstr(0, p.x, "  ", curses.A_REVERSE)
		self.win.refresh()


