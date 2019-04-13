
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
from status import Status
from target import Target

class Game:
	def __init__(self, screen):
		self.screen = screen
		self.height = 40
		self.width = 38
		self.maxPiecesPerLine = int((self.width - 4)/2)
		self.field = curses.newwin(self.height, self.width, 0, 0)
		self.field.box()

	def initialize(self):
		self.next = self.createNext()
		self.current = self.createNext()
		self.pieces = []
		self.status = Status(self.width + 2, 0)
		self.target = Target(self.width - 2, 0, self.height)
		self.target.current = self.current
		self.status.nextBlock = self.next
		self.field.clear()
		self.field.box()
		self.field.refresh()

	def tick(self):
		self.status.lines += self.checkLines()
		if self.canMoveDown():
			self.moveDown()
			return 1
		else:
			self.pieces += self.current.pieces
			self.current = self.next
			self.target.current = self.current
			self.next = self.createNext()
			self.status.nextBlock = self.next
			self.status.blocks += 1
			for p in self.current.pieces:
				if not self.check(p.x, p.y):
					return 2
			return 1

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
		for p in self.current.pieces:
			self.field.addstr(p.y, p.x, "  ", curses.A_REVERSE)
		for p in self.pieces:
			if p != None:
				self.field.addstr(p.y, p.x, "  ", curses.A_REVERSE)
		self.field.refresh()
		self.status.paint()
		self.target.paint()

	def getLines(self):
		return self.status.lines

	def getBlocks(self):
		return self.status.blocks

	def check(self, x, y):
		if x <= 0 or x >= self.width - 2:
			return False
		if y <= 0 or y > self.height - 2:
			return False
		for p in self.pieces:
			if p.x == x and p.y == y:
				return False
		return True

	def checkLines(self):
		count = 0
		for row in range(0, self.height):
			rowPieces = []
			for p in self.pieces:
				if p.y == row:
					rowPieces.append(p)
			if len(rowPieces) >= self.maxPiecesPerLine:
				count += 1
				for p in rowPieces:
					self.pieces.remove(p)
				for p in self.pieces:
					if p.y < row:
						p.y += 1
		return count

	def fall(self):
		while self.canMoveDown():
			self.moveDown()

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

