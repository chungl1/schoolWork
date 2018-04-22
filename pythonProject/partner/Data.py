## @file Data.py
# @title Data
# @author Sophia Tao
# @brief Methods for manipulating data.
# @date Feb 20, 2018

from CurveADT import CurveT
from SeqServices import interpLin, index, isInBounds
from Exceptions import Full, IndepVarNotAscending, InvalidIndex

class Data:
    # state variables
    MAX_SIZE = 10 #maximum size of a curve
    S = [] #list of CurveT objects
    Z = [] #list of curve values

    ## @brief Initializer
    # @details Initializes two sequences for the independent and dependent variables.
    @staticmethod
    def init():
        Data.S = []
        Data.Z = []

    ## @brief Method for adding data values.
    # @details Adds a CurveT to list S and curve value z to list Z.
    # @param s the element to add to S.
    # @param z The element to add to Z.
    @staticmethod
    def add(s,z):
        if (len(Data.S) == Data.MAX_SIZE): raise Full('The list is full')
        if (len(Data.Z) > 0 and z <= Data.Z[len(Data.Z)-1]):
            print(z)
            print(Data.Z[len(Data.Z)-1])
            raise IndepVarNotAscending('Independent variables added must be greater than previous')
        Data.S.append(s)
        Data.Z.append(z)

    ## @brief Method for retrieving a member of the sequence.
    # @param i the index to add.
    # @return the value of the sequence at given index.
    @staticmethod
    def getC(i):
        if i < 0 or i >= len(Data.S): raise InvalidIndex("Index not valid")
        return Data.S[i]

    ## @brief Method for evaluating a curve at a particular x-value.
    # @details Uses linear interpolation to find the value of the curve.
    # @param x the value to evaluate the curve at.
    # @param z An adjacent x value.
    @staticmethod
    def eval(x,z):
        if not isInBounds(Data.Z,z): raise InvalidIndex("The independent variable is not in bounds")
        j = index(Data.Z,z)
        return interpLin(Data.Z[j],Data.S[j].eval(x),Data.Z[j+1],Data.S[j+1].eval(x),z)

    ## @brief Method for slicing a curve.
    # @param x the x to slice at
    # @param i the order of the curve
    @staticmethod
    def slice(x,i):
        Y = [Data.S[j].eval(x) for j in range(len(Data.Z))]
        return CurveT(Data.Z, Y, i)