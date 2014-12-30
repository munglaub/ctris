
from piece import Piece

class PB:
	# ####
	def __init__(self, xl, yl):
		self.pieces = [Piece(xl, yl), Piece(xl+2, yl), Piece(xl+4, yl), Piece(xl+6, yl)]

