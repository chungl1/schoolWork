## @file CurveADT.py
# @title CurveADT
# @author Lawrence Chung
# @brief ADT for a Curve

from scipy.interpolate import interp1d
from Exceptions import *
from SeqServices import *

MAX_ORDER = 2
DX = 1*(10**(-3))

class CurveT:

	## @brief Constructor for CurveT
	# @param X Sequence of x values
	# @param Y Sequence of Y values
	# @param i the order of the curve
	def __init__(self, X, Y, i):
		
		if not isAscending(X):
				raise IndepVarNotAscending("X values not Ascending")
		if(len(X) != len(Y)):
			raise SeqSizeMismatch("Sizes of arrays do not match")	
		if(i > MAX_ORDER):
			raise InvalidInterpOrder("Order of function too great")

		self.x = X
		self.y = Y
		self.i = i
		self.f = interp1d(X, Y, i)

		self.minx = self.x[0]
		self.maxx = self.x[len(self.x)-1]

	## @brief determines minimum value in sequence
	# @return the first element in the Sequence
	def minD(self):
		return self.minx

	## @brief determines maximum value in sequence
	# @return the last element in the Sequence
	def maxD(self):
		return self.maxx

	## @brief determines the order of the Curve
	# @return the third argument of the Constructor
	def order(self):
		return self.i

	def interp(self, X, Y, i, v):
		index = index(X, v)
		if(i == 1):
			return interpLin(X[index], Y[index], X[index+1], Y[index+1], v)
		if(i == 2):
			return interpQuad(X[index-1], Y[index-1], X[index], Y[index], X[index+1], Y[index+1], v)

	## @brief Evaluates curve at an x value
	# @details Uses interp1d from scipy module to evaluate
	# @param x the x value at which the Curve will be evaluated
	def eval(self, x):
		if(x < self.minD() or x > self.maxD()):
			raise OutOfDomain("The x value is out of domain")

		return self.f(x)

	## @brief Approximates first derivative 
	# @details Uses formula of Forwarded Divided Difference to approximate
	# @param x The x value at which the curve will be evaluated
	def dfdx(self, x):
		if(x < self.minD() or x > self.maxD()):
			raise OutOfDomain("The x value is out of domain")

		return ((self.f(x + DX) - self.f(x))/DX)

	## @brief Approximates second derivative
	# @details Uses formula of Forwarded Divided Difference to apprximate
	# @param x The x value at which the curve will be evaluated
	def d2fdx2(self, x):
		if(x < self.minD() or x > self.maxD()):
			raise OutOfDomain("The x value is out of domain")

		return ((self.f(x + 2*DX) - 2*self.f(x + DX) + self.f(x))/DX**2)
