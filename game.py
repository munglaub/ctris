
import curses
import random
from piece import Piece
from pa import PA
from pb import PB
from pc import PC
from pd import PD
from pe import PE
from pf import PF
from pg import PG

class Game:
	def __init__(self, screen):
		self.screen = screen
		self.height = 40
		self.width = 38
		self.field = curses.newwin(self.height, self.width, 0, 0)
		self.field.box()
		self.c = 0
		self.current = self.createNext()
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
			self.current = self.createNext()

	def createNext(self):
		i = random.randint(0, 6)
		if i == 0:
			return PA(10, 1)
		elif i == 1:
			return PB(10, 1)
		elif i == 2:
			return PC(10, 1)
		elif i == 3:
			return PD(10, 1)
		elif i == 4:
			return PE(10, 1)
		elif i == 5:
			return PF(10, 1)
		else:
			return PG(10, 1)

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


	def tryTurn(self):
		if self.canTurn():
			self.turn()

	def canTurn(self):
		for p in self.current.getTurned():
			if not self.check(p.x, p.y):
				return False
		return True

	def turn(self):
		self.current.turn()

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

