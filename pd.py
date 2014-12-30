
from piece import Piece

class PD:
	#  ##
	# ##
	def __init__(self, xl, yl):
		self.pieces = [Piece(xl + 2, yl), Piece(xl + 4, yl), Piece(xl, yl + 1), Piece(xl + 2, yl + 1)]


