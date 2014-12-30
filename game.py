
import curses
from piece import Piece
from pa import PA
from pb import PB

class Game:
	def __init__(self, screen):
		self.screen = screen
		self.height = 40
		self.width = 40
		self.field = curses.newwin(self.height, self.width, 0, 0)
		self.field.box()
		self.c = 0
		self.current = PA(10, 0)
		self.mat = []
		for i in range(0, self.width):
			row = []
			for j in range(0, self.height):
				row.append(None)
			self.mat.append(row)

	def initialize(self):
		self.field.clear()
		self.field.box()
		self.field.refresh()

	def tick(self):
		self.c += 1
		if self.canMoveDown():
			self.moveDown()
		else:
			for p in self.current.pieces:
				self.mat[p.x][p.y] = p
			self.current = PA(10, 1)
			#self.current = PB(10, 1)

	def paint(self):
		self.field.clear()
		self.field.box()
		self.field.addstr(1, 1, str(self.c))
		for p in self.current.pieces:
			self.field.addstr(p.y, p.x, "  ", curses.A_REVERSE)
		for row in self.mat:
			for p in row:
				if p != None:
					self.field.addstr(p.y, p.x, "  ", curses.A_REVERSE)
		self.field.refresh()

	def check(self, x, y):
		if x <= 0 or x >= self.width - 2:
			return False
		if y <= 0 or y > self.height - 2:
			return False
		if self.mat[x][y] != None:
			return False
		return True


	def tryMoveDown(self):
		if self.canMoveDown():
			self.moveDown()

	def canMoveDown(self):
		for p in self.current.pieces:
			if not self.check(p.x, p.y + 1):
				return False
		return True

	def moveDown(self):
		for p in self.current.pieces:
			p.y += 1

	def tryMoveLeft(self):
		if self.canMoveLeft():
			self.moveLeft()

	def canMoveLeft(self):
		for p in self.current.pieces:
			if not self.check(p.x - 2, p.y):
				return False
		return True

	def moveLeft(self):
		for p in self.current.pieces:
			p.x -= 2

	def tryMoveRight(self):
		if self.canMoveRight():
			self.moveRight()

	def canMoveRight(self):
		for p in self.current.pieces:
			if not self.check(p.x + 2, p.y):
				return False
		return True

	def moveRight(self):
		for p in self.current.pieces:
			p.x += 2

