
from piece import Piece

class PB:
	# ####
	def __init__(self, xl, yl):
		self.pieces = [Piece(xl, yl), Piece(xl+2, yl), Piece(xl+4, yl), Piece(xl+6, yl)]
		self.up = False

	def getTurned(self):
		np = []
		if self.up:
			np.append(self.create(0, -4, 2))
			np.append(self.create(1, -2, 1))
			np.append(self.create(2, 0, 0))
			np.append(self.create(3, 2, -1))
		else:
			np.append(self.create(0, 4, -2))
			np.append(self.create(1, 2, -1))
			np.append(self.create(2, 0, 0))
			np.append(self.create(3, -2, 1))
		return np

	def create(self, i, x, y):
		p = self.pieces[i]
		return Piece(p.x + x, p.y + y)

	def turn(self):
		self.pieces = self.getTurned()
		self.up = not self.up

