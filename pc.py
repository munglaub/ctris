
from piece import Piece

class PC:
	# ##
	#  ##
	def __init__(self, xl, yl):
		self.pieces = [Piece(xl, yl), Piece(xl + 2, yl), Piece(xl + 2, yl + 1), Piece(xl + 4, yl + 1)]
		self.up = False

	def getTurned(self):
		np = []
		if self.up:
			np.append(self.create(0, -4, 1))
			np.append(self.create(1, 0, 0))
			np.append(self.create(2, 0, 0))
			np.append(self.create(3, 0, +1))
		else:
			np.append(self.create(0, 4, -1))
			np.append(self.create(1, 0, 0))
			np.append(self.create(2, 0, 0))
			np.append(self.create(3, 0, -1))
		return np

	def create(self, i, x, y):
		p = self.pieces[i]
		return Piece(p.x + x, p.y + y)

	def turn(self):
		self.pieces = self.getTurned()
		self.up = not self.up


