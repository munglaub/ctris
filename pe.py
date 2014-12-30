
from piece import Piece

class PE:
	#  #
	# ###
	def __init__(self, xl, yl):
		self.pieces = [Piece(xl + 2, yl), Piece(xl, yl + 1), Piece(xl + 2, yl + 1), Piece(xl + 4, yl + 1)]



