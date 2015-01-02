
from piece import Piece

class PF:
	# #
	# ###
	def __init__(self, xl, yl):
		self.pieces = [Piece(xl, yl), Piece(xl, yl + 1), Piece(xl + 2, yl + 1), Piece(xl + 4, yl + 1)]
		self.state = 0

	def getTurned(self):
		np = []
		if self.state == 0:
			np.append(self.create(0, 4, 0))
			np.append(self.create(1, 2, -1))
			np.append(self.create(2, 0, 0))
			np.append(self.create(3, -2, 1))
		elif self.state == 1:
			np.append(self.create(0, 0, 2))
			np.append(self.create(1, 2, 1))
			np.append(self.create(2, 0, 0))
			np.append(self.create(3, -2, -1))
		elif self.state == 2:
			np.append(self.create(0, -4, 0))
			np.append(self.create(1, -2, 1))
			np.append(self.create(2, 0, 0))
			np.append(self.create(3, 2, -1))
		else:
			np.append(self.create(0, 0, -2))
			np.append(self.create(1, -2, -1))
			np.append(self.create(2, 0, 0))
			np.append(self.create(3, 2, 1))
		return np

	def create(self, i, x, y):
		p = self.pieces[i]
		return Piece(p.x + x, p.y + y)

	def turn(self):
		self.pieces = self.getTurned()
		self.state = (self.state + 1) % 4


