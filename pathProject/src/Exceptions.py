## @file Exceptions.py
# @title Exceptions
# @author Lawrence Chung
# @brief Exception handling

## @brief Exception for non-Ascending list
# @param Exception Exception to be displayed
# @return message for exception
class IndepVarNotAscending(Exception):

	def __init__(self, message):
		self.message = message

	def __str__(self):
		return str(self.message)

## @brief Exception for order too great
# @param Exception Exception to be displayed
# @return message for exception
class InvalidInterpOrder(Exception):

	def __init__(self, message):
		self.message = message

	def __str__(self):
		return str(self.message)

## @brief Exception for two Sequences of different lengths
# @param Exception Exception to be displayed
# @return message for exception
class SeqSizeMismatch(Exception):

	def __init__(self, message):
		self.message = message

	def __str__(self):
		return str(self.message)

## @brief Exception for sequence length too great
# @param Exception Exception to be displayed
# @return message for exception
class Full(Exception):

	def __init__(self, message):
		self.message = message

	def __str__(self):
		return str(message)

## @brief Exception for index non-existent
# @param Exception Exception to be displayed
# @return message for exception
class InvalidIndex(Exception):

	def __init__(self, message):
		self.message = message

	def __str__(self):
		return str(message)

## @brief Exception for x value not in sequence
# @details Exception if desired x value is not in list
# @param Exception Exception to be displayed
# @return message for exception
class OutOfDomain(Exception):

	def __init__(self, message):
		self.message = message

	def __str__(self):
		return str(message)