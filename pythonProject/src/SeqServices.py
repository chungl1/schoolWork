## @file SeqServices.py
# @title SeqServices
# @author Lawrence Chung
# @brief Sequence operations


## @brief determines whether sequence is ascending
# @param X a sequence in the form of a list
# @return boolean, true if ascending, false if not
def isAscending(X):
	j = 0
	i = 0
	while(j < len(X)-1):
		if(X[j+1] >= X[j]):
			i += 1
		j += 1
	if(i == len(X)-1):
		return True
	else:
		return False

## @brief determines if input value is in sequence
# @param X a Sequence of values 
# @param x value to be checked
# return boolean, True if in bounds, False if not
def isInBounds(X, x):
	if(x < X[0] or x > X[len(X)-1]):
		return False
	else:
		return True

## @brief linear interpolation
# @details Determines the corresponding y using formula
# @param x1 independent variable of first set of poitns
# @param y1 dependent variable of first set of points
# @param x2 independent variable of second set of points
# @param y2 dependent variable of second set of points
# @param x the x value that will be interpolated
# @return the y value determined through interpolation
def interpLin(x1, y1, x2, y2, x):
	tempVal = (y2 - y1)/(x2 - x1)
	val = tempVal*(x - x1) + y1
	return val

## @brief Quadratic interpolation
# @details Determines the corresponding y using formula
# @param x0 independent variable of first set of poitns
# @param y0 dependent variable of first set of points
# @param x1 independent variable of second set of points
# @param y1 dependent variable of second set of points
# @param x2 independent variable of third set of points
# @param y2 dependent variable of third set of points
# @param x the x value that will be interpolated
# @return the y value determined through interpolation
def interpQuad(x0, y0, x1, y1, x2, y2, x):
	tempVal = ((y2 - y0)/(x2- x0))*(x - x1)
	tempVal2 = ((y2 - 2*y1 + y0)/(2*(x2-x1)**2))*(x-x1)**2
	val = y1 + tempVal + tempVal2
	return val

## @brief Determines index of value in sequence
# @param X A sequence of x values
# @param x a value in Sequence X
# @return the index of the x value
def index(X, x):
	if(isInBounds(X,x) and isAscending(X)):
		i = 0
		while(i < len(X)):
			if(X[i] == x):
				return i
			i += 1
