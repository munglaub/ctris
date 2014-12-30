
from piece import Piece

class PC:
	# ##
	#  ##
	def __init__(self, xl, yl):
		self.pieces = [Piece(xl, yl), Piece(xl + 2, yl), Piece(xl + 2, yl + 1), Piece(xl + 4, yl + 1)]


