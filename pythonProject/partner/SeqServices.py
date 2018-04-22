## @file SeqServices.py
# @title SeqServices
# @author Sophia Tao
# @brief Methods for sequence operations.
# @date Feb 20, 2018


## @brief tells whether a sequence is ascending.
# @param X a list.
# @return boolean of whether X is ascending

def isAscending(X):
    return all(X[j] <= X[j+1] for j in range(len(X)-1))

## @brief tells whether an item is within range of sequence.
# @details whether the item is greater than the minimum and less than the maximum.
# @param X the index.
# @param x the value.
# @return boolean of whether x is within bounds of the list X.
def isInBounds(X, x):
    return x <= X[len(X)-1] and x >= X[0]

## @brief Finds linear interpolation at a point.
# @details Uses formula (y2-y1)/(x2-x1)*(x-x1)+y1.
# @param x1 the first known x value.
# @param x2 the second known x value.
# @param y1 the first known y value.
# @param y2 the second known y value.
# @param x the x-point at which to extrapolate from.
# @return the linear interpolation evaluated at x.
def interpLin(x1,y1,x2,y2,x):
    return (y2-y1)/(x2-x1)*(x-x1)+y1

## @brief Finds quadratic interpolation at a point.
# @details Uses formula y1+(y2-y0)/(x2-x0)*(x-x1) + (y2-2*y1+y0)/(2*(x2-x1)**2)*(x-x1)**2
# @param x0 the first known x value.
# @param x1 the second known x value.
# @param x3 the third known x value.
# @param y0 the first known y value.
# @param y1 the second known y value.
# @param y2 the third known y value.
# @param x the x-point at which to extrapolate from.
# @return the linear interpolation evaluated at x.
def interpQuad(x0,y0,x1,y1,x2,y2,x):
    return y1+(y2-y0)/(x2-x0)*(x-x1) + (y2-2*y1+y0)/(2*((x2-x1)**2))*((x-x1)**2)

## @brief Finds index of the term immediately less than given value.
# @param X The sequence.
# @param x The value to find the index of.
# @return The index of the term immediately less than given value. None if there is an error.
def index(X, x):
    for index, item in enumerate(X):
        if(item <= x):
            if X[index+1] >= x:
                return index