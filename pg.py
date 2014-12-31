
from piece import Piece

class PG:
	#   #
	# ###
	def __init__(self, xl, yl):
		self.pieces = [Piece(xl + 4, yl), Piece(xl, yl + 1), Piece(xl + 2, yl + 1), Piece(xl + 4, yl + 1)]
		self.state = 0

	def getTurned(self):
		np = []
		if self.state == 0:
			p = self.pieces[0]
			np.append(Piece(p.x, p.y + 2))
			p = self.pieces[1]
			np.append(Piece(p.x + 2, p.y - 1))
			p = self.pieces[2]
			np.append(Piece(p.x, p.y))
			p = self.pieces[3]
			np.append(Piece(p.x - 2, p.y + 1))
		elif self.state == 1:
			p = self.pieces[0]
			np.append(Piece(p.x - 4, p.y))
			p = self.pieces[1]
			np.append(Piece(p.x + 2, p.y + 1))
			p = self.pieces[2]
			np.append(Piece(p.x, p.y))
			p = self.pieces[3]
			np.append(Piece(p.x - 2, p.y - 1))
		elif self.state == 2:
			p = self.pieces[0]
			np.append(Piece(p.x, p.y - 2))
			p = self.pieces[1]
			np.append(Piece(p.x - 2, p.y + 1))
			p = self.pieces[2]
			np.append(Piece(p.x, p.y))
			p = self.pieces[3]
			np.append(Piece(p.x + 2, p.y - 1))
		else:
			p = self.pieces[0]
			np.append(Piece(p.x + 4, p.y))
			p = self.pieces[1]
			np.append(Piece(p.x - 2, p.y - 1))
			p = self.pieces[2]
			np.append(Piece(p.x, p.y))
			p = self.pieces[3]
			np.append(Piece(p.x + 2, p.y + 1))
		return np

	def turn(self):
		self.pieces = self.getTurned()
		self.state = (self.state + 1) % 4





