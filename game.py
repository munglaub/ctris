
import curses
from piece import Piece
from pa import PA

class Game:
	def __init__(self, screen):
		self.screen = screen
		self.height = 40
		self.width = 40
		self.field = curses.newwin(self.height, self.width, 0, 0)
		self.field.box()
		self.c = 0
		self.current = PA(10, 0)

	def initialize(self):
		self.field.clear()
		self.field.box()
		self.field.refresh()

	def tick(self):
		self.c += 1
		if self.canMoveDown():
			self.moveDown()
		else:
			#TODO: matrix..
			self.current = PA(10, 0)

	def paint(self):
		self.field.clear()
		self.field.box()
		self.field.addstr(1, 1, str(self.c))
		for p in self.current.pieces:
			self.field.addstr(p.y, p.x, "XX")
		self.field.refresh()

	def tryMoveDown(self):
		if self.canMoveDown():
			self.moveDown()

	def canMoveDown(self):
		for p in self.current.pieces:
			if p.y + 1 < 0 or p.y + 1 > self.height - 2:
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
			if p.x - 2 <= 0:
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
			if p.x + 2 >= self.width:
				return False
		return True

	def moveRight(self):
		for p in self.current.pieces:
			p.x += 2
