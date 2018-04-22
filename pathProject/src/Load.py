## @file Load.py
# @title Load
# @author Lawrence Chung

from CurveADT import *
from Data import *

## @brief Method to write data from file
# @details Uses loops to write data into Sequence, filling empty slots with commas
# @param s file name of type string
def Load(s):

	Data.init()
	f = open(s, 'r')
	S = []
	X = []
	Y = []
	Z = []
	k = 0
	stringVal = ""
	for i in f:
		l = 0
		m = 0
		j = 0
		if(k == 0):
			while(l < len(i)):		
				if(i[l] == "," or i[l] == "\n"): 
					Z.append(float(stringVal))
					stringVal = ""
					l += 1
				elif(i[l] != ","):
					stringVal += i[l]
					l += 1

		if(k >= 2):
			while(l < len(i)):		
				if(i[l] == "," or i[l] == "\n"): 
					if(j % 2 == 0):
						if(k == 2):
							X.append([float(stringVal)])
						else:
							if(stringVal == " "):
								X[m].append(",")
							else:
								X[m].append(float(stringVal))
					else:
						if(k == 2):
							Y.append([float(stringVal)])
						else:
							if(stringVal == " "):
								Y[m].append(",")
							else:
								Y[m].append(float(stringVal))
						m += 1
					j += 1
					stringVal = ""
					l += 1
				elif(i[l] != ","):
					stringVal += i[l]
					l += 1


		k += 1

	S.append(X)
	S.append(Y)
	Data.add(S, Z)
	
	

