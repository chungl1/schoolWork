## @file Plot.py
# @title Plot
# @author Lawrence Chung
# @brief Module to plot graph

from CurveADT import CurveT
from Exceptions import *
import matplotlib.pyplot as plt

## @brief Plots Sequences of curve
# @details uses maplotlib to plot graph 
# @param X Sequence of x values
# @param Y Sequence of y values
def PlotSeq(X, Y):

	if(len(X) != len(Y)):
		raise SeqSizeMismatch("X and Y are different lengths")

	plt.plot(X, Y, 'b')
	plt.show()

## @brief Plot Sequences of curve based on size of n
# @details uses matplotlib to plot graph
# @param c A curve object
# @param n Value determining amount of spaced points
def PlotCurve(c, n):

	X = []
	Y = []
	interval = (c.maxD() - c.minD())/n

	if(c.order() == 1):
		j = 0
		i = c.minD()
		while(i <= n-2):
			X.append(i)
			i += interval
		for j in X:
			Y.append(c.eval(j))

	elif(c.order() == 2):
		i = c.minD() + interval
		j = 0
		while(i <= n-2):
			X.append(i)
			i += interval
		for j in X:
			Y.append(c.eval(j))

	plt.plot(X, Y, 'b')
	plt.show()
