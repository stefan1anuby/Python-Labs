
class Stack:

	def __init__(self , list_as_parameter = [] ):
		self.list = list(list_as_parameter)

	def push(self , item):
		self.list.append(item)

	def pop(self):
		return self.list.pop() if len(self.list) != 0 else None

	def peek(self):
		return self.list[-1] if len(self.list) != 0 else None
	
	def getSize(self):
		return len(self.list)
		
	def __str__(self):
		return f"Stack : {self.list}"
	
	def __repr__(self):
		return self.__str__()

class Queue:

	def __init__(self , list_as_parameter = [] ):
		self.list = list(list_as_parameter)

	def push(self , item):
		self.list.insert(0,item)

	def pop(self):
		return self.list.pop(0) if len(self.list) != 0 else None

	def peek(self):
		return self.list[0] if len(self.list) != 0 else None
	
	def getSize(self):
		return len(self.list)
		
	def __str__(self):
		return f"Queue : {self.list}"
	
	def __repr__(self):
		return self.__str__()
	
class Matrix:

	def __init__(self , rows , columns):
		self.state = [[0]*columns]*rows
		self.rows =  rows
		self.columns = columns

	def __str__(self):
		return f"Matrix : \n{self.state}"
	
	def __repr__(self):
		return self.__str__()
	
	def get(self , row , col):
		return self.state[row][col] if self.isInBounds(row,col) == True else None
	
	def set(self, row , col , item):
		if self.isInBounds(row,col) == True:
			self.state[row][col] = item

	def apply(self , function):
		for row in self.rows:
			for col in self.columns:
				item = self.state[row][col]
				self.state[row][col] = function(item)

	def isInBounds(self,row,col):
		return True if 0 <= row < self.rows and 0 <= col < self.columns else False
