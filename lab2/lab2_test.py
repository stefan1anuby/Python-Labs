import unittest

from lab2_fun import *

class Lab2Test(unittest.TestCase):
    
	def test_ten_input(self):

		expected_output = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
		self.assertEqual(get_fibonacci_numbers(10), expected_output)

	def test_find_primes(self):

		numbers = [1, 2, 3, 4, 5, 6, 17, 18, 19, 20]
		expected_primes = [2, 3, 5, 17, 19]
		self.assertEqual(find_primes_in_list(numbers), expected_primes)

	def test_list_operations(self):

		a = [1, 2, 3, 4, 5]
		b = [4, 5, 6, 7, 8]
		expected_intersection = [4, 5]
		expected_union = [1, 2, 3, 4, 5, 6, 7, 8]
		expected_a_diff_b = [1, 2, 3]
		expected_b_diff_a = [6, 7, 8]
		
		intersection, union, a_diff_b, b_diff_a = list_operations(a, b)
		
		self.assertEqual(intersection, expected_intersection)
		self.assertEqual(union, expected_union)
		self.assertEqual(a_diff_b, expected_a_diff_b)
		self.assertEqual(b_diff_a, expected_b_diff_a)

	def test_compose_song(self):
		notes = ["do", "re", "mi", "fa", "sol"]
		moves = [1, -3, 4, 2]
		start_pos = 2
		expected_song = ["mi", "fa", "do", "sol", "re"]

		composed_song = compose_song(notes, moves, start_pos)

		self.assertEqual(composed_song, expected_song)

	def test_zero_below_diagonal(self):
		matrix = [
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]
		]

		expected_matrix = [
			[1, 2, 3],
			[0, 5, 6],
			[0, 0, 9]
		]

		zeroed_matrix = zero_below_diagonal(matrix)
		self.assertEqual(zeroed_matrix, expected_matrix)
	
	def test_elements_appearing_x_times(self):
		lists = [
			[1, 2, 3],
			[2, 3, 4],
			[4, 5, 6],
			[4, 1, "test"]
		]
		x = 2
		expected_result = [1, 2, 3]
		self.assertEqual(elements_appearing_x_times(x, lists), expected_result)

	def test_palindrome_info(self):
		numbers = [121, -121, 1331, 123, 456, 454, 11, 22, -22, 1112]
		expected_count = 5
		expected_max_palindrome = 1331
		count, max_palindrome = palindrome_info(numbers)
		self.assertEqual(count, expected_count)
		self.assertEqual(max_palindrome, expected_max_palindrome)
	
	def test_filter_strings_by_ascii(self):
		x = 2
		strings = ["test", "hello", "lab002"]
		flag = False
		expected_result = [['e', 's'], ['e'], []]
		#self.assertEqual(filter_strings_by_ascii(x, strings, flag), expected_result)
	
	def test_order_tuples(self):
		tuples = [('abc', 'bcd'), ('abc', 'zza')]
		expected_result = [('abc', 'zza'), ('abc', 'bcd')]
		self.assertEqual(order_tuples(tuples), expected_result)

	def test_group_by_rhyme(self):
		words = ['ana', 'banana', 'carte', 'arme', 'parte']
		expected_groups = [['ana', 'banana'], ['carte', 'parte'], ['arme']]
		self.assertEqual(group_by_rhyme(words), expected_groups)
    


if __name__ == '__main__':
    unittest.main()
