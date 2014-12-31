
from piece import Piece

class PA:
	# ##
	# ##
	def __init__(self, xl, yl):
		self.pieces = [Piece(xl, yl), Piece(xl+2, yl), Piece(xl, yl+1), Piece(xl+2, yl+1)]

	def getTurned(self):
		return self.pieces

	def turn(self):
		pass

