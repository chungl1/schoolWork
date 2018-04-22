## @file Data.py
# @title Data
# @author Lawrence Chung
# @brief Manipulate data

from Exceptions import *
from CurveADT import CurveT
from SeqServices import interpLin
from SeqServices import index
from SeqServices import isInBounds

MAX_SIZE = 10

class Data:

	## @brief Initializes abstract object
	# @details Initiializes two empty sequences, the independent and dependent sequences
	@staticmethod
	def init():
		Data.S = []
		Data.Z = []

	##@brief adds element to sequenes
	# @details Adds a sequences of CurveT to S and a real value z to Z
	# @param s element to add to sequence S
	# @param z element to add to sequence Z
	@staticmethod
	def add(s, z):

		if(len(Data.S) == MAX_SIZE):
			raise Full("Sequence is full")
		if(len(Data.Z) > 0 and z < Data.Z[len(Data.Z)-1]):
			raise IndepVarNotAscending("Z values not ascending")

		Data.S.append(s)
		Data.Z.append(z)

	## @brief Method to obtain a value in the sequence
	# @param i Indexing value
	# @return Corresponding value in the sequence at the provided index
	@staticmethod
	def getC(i):
 		
 		if(i < 0 or i >= len(Data.S)):
 			raise InvalidIndex("Index out of range")

 		return Data.S[i]

 	## @brief Method to evaluate curve
 	# @details Uses linear interpolation from SeqServices.py to determine the corresponding y value 
 	# @param x independent variable x
 	# @param z x value from Z sequence
	@staticmethod
	def eval(x, z):

		if not (isInBounds(Data.Z, z)):
			raise OutOfDomain("Value is not in domain")

		j = index(Data.Z, z)

		return interpLin(Data.Z[j], Data.S[j][1], Data.Z[j+1], Data.S[j+1][1], z)

	## @brief Slices a curve
	# @param x the value at which the method will slice
	# @param i order of curve
	@staticmethod
	def slice(x, i):

		Y = []
		j = 0
		while(j < len(Data.S)):
			Y.append(int(Data.S[j][1]))
			j += 1

		return CurveT(Data.Z, Y, i)
