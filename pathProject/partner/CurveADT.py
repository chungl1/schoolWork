## @file CurveADT.py
# @title CurveT
# @author Sophia Tao
# @brief Abstract data type representing a curve.
# @date Feb 20, 2018

import SeqServices
from Exceptions import OutOfDomain, SeqSizeMismatch, IndepVarNotAscending, InvalidInterpOrder

MAX_ORDER = 2 # state constant for maximum order of curve
DX = 0.001 # state constant for DX

## @brief finds the interpolation of the function.
# @param X list of X values.
# @param Y list of Y values.
# @param o the order of interpolation.
# @param v the value to interpolate at.
# @return the value of the interpolation.
def interp(X,Y,o,v):
    i = SeqServices.index(X,v)
    if (o == 1):
        return SeqServices.interpLin(X[i], Y[i], X[i+1], Y[i+1], v)
    else:
        return SeqServices.interpQuad(X[i], Y[i], X[i+1], Y[i+1], X[i+2], Y[i+2], v)

class CurveT:

    ## @brief Constructor for CurveT class.
    # @param self The CurveT object pointer.
    # @param X the list of x values.
    # @param Y the list of y values.
    def __init__(self, X, Y, i):
        print(X)
        if (len(X) != len(Y)):
            raise SeqSizeMismatch("length of X and Y not equal")
        if not SeqServices.isAscending(X):
            raise IndepVarNotAscending("X values not ascending")
        if i < 1 or i > MAX_ORDER:
            raise InvalidInterpOrder("Order not 1 or 2")
        self.__o = i
        self.__minx = X[0]
        self.__maxx = X[len(X)-1]
        self.__f = lambda v : interp(X, Y, i, v)

    ## @brief getter for minimum X value.
    # @return the curve's minimum X value.
    def minD(self):
        return self.__minx

    ## @brief getter for maximum X value.
    # @return the curve's maximum X value.
    def maxD(self):
        return self.__maxx

    ## @brief getter for the curve's order.
    # @return the curve's order.
    def order(self):
        return self.__o

    ## @brief retrieves function for interpolating the curve at a value..
    # @param x x-value to be used in interpolation.
    # @return a function for interpolating the curve at x.
    def eval(self, x):
        if not (self.__minx <= x) or not (x <= self.__maxx):
            raise OutOfDomain("x out of domain")
        return self.__f(x)

    ## @brief finds first derivative at x.
    # @param x x-value to be used.
    # @return the first derivative at x.
    def dfdx(self,x):
        if not (self.__minx <= x) and (x <= self.__maxx):
            raise OutOfDomain("x out of domain")
        return (self.__f(x+DX)-self.__f(x))/DX

    ## @brief finds second derivative at x.
    # @param x x-value to be used.
    # @return the second derivative at x.
    def d2fdx2(self,x):
        if not (self.__minx <= x) and (x <= self.__maxx):
            raise OutOfDomain("x out of domain")
        return (self.__f(x+2*DX)-2*self.__f(x+DX)+self.__f(x))/(DX**2)

