
from piece import Piece

class PD:
	#  ##
	# ##
	def __init__(self, xl, yl):
		self.pieces = [Piece(xl + 2, yl), Piece(xl + 4, yl), Piece(xl, yl + 1), Piece(xl + 2, yl + 1)]
		self.up = False

	def getTurned(self):
		np = []
		if self.up:
			p = self.pieces[0]
			np.append(Piece(p.x, p.y))
			p = self.pieces[1]
			np.append(Piece(p.x + 4, p.y + 1))
			p = self.pieces[2]
			np.append(Piece(p.x, p.y + 1))
			p = self.pieces[3]
			np.append(Piece(p.x, p.y))
		else:
			p = self.pieces[0]
			np.append(Piece(p.x, p.y))
			p = self.pieces[1]
			np.append(Piece(p.x - 4, p.y - 1))
			p = self.pieces[2]
			np.append(Piece(p.x, p.y - 1))
			p = self.pieces[3]
			np.append(Piece(p.x, p.y))
		return np

	def turn(self):
		self.pieces = self.getTurned()
		self.up = not self.up

