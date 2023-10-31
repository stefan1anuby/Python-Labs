import unittest
from lab4_fun import *

class TestStackOperations(unittest.TestCase):

	def test_init(self):
		empty_stack = Stack()
		str_repr_expected = "Stack : []"
		self.assertEqual(str(empty_stack),str_repr_expected)

		some_list = [1,2,3,"ceva"]
		stack = Stack(some_list)
		str_repr_expected = "Stack : [1, 2, 3, 'ceva']"
		self.assertEqual(str(stack),str_repr_expected)
	
	def test_push(self):
		stack = Stack()

		item_list = [4,5,6]
		for item in item_list:
			stack.push(item)
		
		self.assertEqual(stack.list , item_list)

	def test_pop(self):
		item_list = [1,2,3]
		stack = Stack(item_list)

		for item in item_list[::-1]:
			self.assertEqual(stack.pop(),item)

		self.assertIsNone(stack.pop())

	def test_peek(self):
		item_list = [0,1,5]
		stack = Stack(item_list)

		for item in item_list[::-1]:
			self.assertEqual(stack.peek(),item)
			stack.pop()

		self.assertIsNone(stack.peek())		

class TestMatrixOperations(unittest.TestCase):
	
	def test_init(self):
		matrix = Matrix(2,3)
		#print(matrix)

	def test_get(self):
		matrix = Matrix(2,3)
		self.assertEqual(matrix.get(1,2) , 0)
		self.assertNone(matrix.get(4,4))

	def test_set(self):
		matrix = Matrix(2,2)
		print(matrix)
		matrix.set(0,0 ,"ceva")
		print(matrix)

		expected_matrix = [["ceva",0],[0,0]]
		self.assertEqual(matrix.state,expected_matrix)

	def test_apply(self):
		matrix = Matrix(2,2)
		matrix.apply(lambda x : x+1)
		#print(matrix)

if __name__ == '__main__':
    unittest.main()