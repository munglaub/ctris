
import curses
from piece import Piece

class Game:
	def __init__(self, screen):
		self.screen = screen
		self.height = 40
		self.width = 40
		self.field = curses.newwin(self.height, self.width, 0, 0)
		self.field.box()
		self.c = 0
		self.piece = Piece()

	def initialize(self):
		self.field.clear()
		self.field.box()
		self.field.refresh()

	def tick(self):
		self.c += 1
		if self.piece.pos < self.height-2:
			self.piece.pos += 1

	def paint(self):
		self.field.clear()
		self.field.box()
		self.field.addstr(1, 1, str(self.c))
		self.field.addstr(self.piece.pos, 5, "x")
		self.field.refresh()



