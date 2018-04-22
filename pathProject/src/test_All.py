from SeqServices import *
from CurveADT import CurveT
from Data import *

def test_CurveMin(): #Start tests for CurveADT normal cases

	testX = [1,2,3,4,5,6,7]
	testY = [1,4,9,16,25,36,49]
	
	a = CurveT(testX, testY, 2)

	assert(a.minD() == 1) #Normal cases

def test_CurveMax():

	testX = [1,2,3,4,5,6,7]
	testY = [1,4,9,16,25,36,49]
	
	a = CurveT(testX, testY, 2)

	assert(a.maxD() == 7)

def test_CurveOrder():

	testX = [1,2,3,4,5,6,7]
	testY = [1,4,9,16,25,36,49]
	
	a = CurveT(testX, testY, 2)

	assert(a.order() == 2)

def test_CurveEval(): 

	testX = [1,2,3,4,5,6,7]
	testY = [1,4,9,16,25,36,49]
	
	a = CurveT(testX, testY, 2)

	assert(a.eval(2) == 4) #Fail due to floating point approximation

def test_dfdx(): 

	testX = [1,2,3,4,5,6,7]
	testY = [1,4,9,16,25,36,49]
	
	a = CurveT(testX, testY, 2)

	assert(a.dfdx(2) == 4) #Fail due to floating point approximation

def test_df2dx2(): #End tests for CurveADT normal cases

	testX = [1,2,3,4,5,6,7]
	testY = [1,4,9,16,25,36,49]
	
	a = CurveT(testX, testY, 2)

	assert(a.d2fdx2(2) == 2) #Fail due to floating point approximation

def test_CurveMinExc(): #Start tests for CurveADT Exception cases

	testX = [1,2,1,4,5,6,7]
	testY = [1,4,9,16,25,36,49]
	
	a = CurveT(testX, testY, 2)

	assert(a.minD() == None) #Fail due to exception thrown at init

def test_CurveMaxExc():

	testX = [1,2,3,4,5,6,7,8]
	testY = [1,4,9,16,25,36,49]
	
	a = CurveT(testX, testY, 2)

	assert(a.maxD() == None) #Fail due to exception thrown at init

def test_CurveOrderHigh(): #End tests for CurveADT Exception cases

	testX = [1,2,3,4,5,6,7]
	testY = [1,4,9,16,25,36,49]
	
	a = CurveT(testX, testY, 3)

	assert(a.order() == None) #Fail due to exception thrown at init

def test_DataAddGet(): #Start tests for Data normal cases

	Data.init()
	Data.add([1,1],1) 
	Data.add([2,4],4)
	Data.add([3,5],9) 
	Data.add([4,16],16)
	Data.add([5,25],25) 
	Data.add([6,36],36)

	assert(Data.getC(0) == [1,1]) #Success implies Data.add successful

def test_Eval(): #End tests for Data normal cases

	Data.init()
	Data.add([1,1],1) 
	Data.add([2,4],4)
	Data.add([3,5],9) 
	Data.add([4,16],16)
	Data.add([5,25],25) 
	Data.add([6,36],36)

	assert(Data.eval(0,1) == 1)

def test_DataAdd(): #Start tests for Data exception cases

	Data.init()
	Data.add([1,1],1) 
	Data.add([2,4],4)
	Data.add([3,5],9) 
	Data.add([4,16],16)
	Data.add([5,25],25) 
	Data.add([6,36],36)
	Data.add([7,49],49)
	Data.add([8.64],64)
	Data.add([9,81],81)
	Data.add([10,100],100)
	Data.add([11,121],121) #Fail because array length > MAX_SIZE

def test_DataGet():

	Data.init()
	Data.add([1,1],1) 
	Data.add([2,4],4)
	Data.add([3,5],9) 
	Data.add([4,16],16)
	Data.add([5,25],25) 
	Data.add([6,36],36)
	Data.add([7,49],49)
	Data.add([8.64],64)
	Data.add([9,81],81)

	assert(Data.getC(11) == None) #Fail because index out of range

def test_DataEval():

	Data.init()
	Data.add([1,1],1) 
	Data.add([2,4],4)
	Data.add([3,5],9) 
	Data.add([4,16],16)
	Data.add([5,25],25) 
	Data.add([6,36],36)
	Data.add([7,49],49)
	Data.add([8.64],64)
	Data.add([9,81],81)

	assert(Data.eval(10,10) == None) #Fail because index out of range

def test_Slice(): #End tests for data exception cases

	Data.init()
	Data.add([1,1],1) 
	Data.add([2,4],4)
	Data.add([3,5],9) 
	Data.add([4,16],16)
	Data.add([5,25],25) 
	Data.add([6,36],36)
	Data.add([7,49],49)
	Data.add([8.64],64)
	Data.add([9,81],81)

	assert(Data.slice(2,3) == None) #Fail because index out of range

def test_SequencesAscend(): #Start tests for SeqServices normal cases

	testX = [1,2,3,4,5,6,7]
	testY = [1,4,9,16,25,36,49]

	assert(isAscending(testX) == True)

def test_Bounds():

	testX = [1,2,3,4,5,6,7]
	testY = [1,4,9,16,25,36,49]
	assert(isInBounds(testX, 2) == True)

def test_interpL():

	assert(interpLin(1,1,2,4,2) == 4)

def test_interpQ():
	assert(interpQuad(1,1,2,4,3,9,2) == 4)

def test_index(): #End tests for SeqServices True cases

	testX = [1,2,3,4,5,6,7]
	testY = [1,4,9,16,25,36,49]

	assert(index(testX, 2) == 1)

def test_SequencesNotAscend(): #Start tests for SeqServices False/Exception cases

	testX = [1,2,3,2,5,6,7]
	testY = [1,4,9,16,25,36,49]

	assert(isAscending(testX) == False)

def test_OutBounds():
	testX = [1,2,3,4,5,6,7]
	testY = [1,4,9,16,25,36,49]
	assert(isInBounds(testX, 9) == False)

def test_indexOutBounds():

	testX = [1,2,3,4,5,6,7]
	testY = [1,4,9,16,25,36,49]

	assert(index(testX, 9) == None) 

def test_indexNotAscend(): #End tests for SeqServices False/Exception Cases

	testX = [1,2,3,2,5,6,7]
	testY = [1,4,9,16,25,36,49]

	assert(index(testX, 2) == None) 