import unittest

from lab1_fun import *

class Lab1Test(unittest.TestCase):

    def test_gcd(self):
		
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(12, 15, 21), 3)
        self.assertEqual(gcd(5, 10), 5)
        self.assertIsNone(gcd(5), None)
        
    def test_count_vowels(self):
            
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("HELLO"), 2)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("12345"), 0)
        
    def test_count_occurrences(self):

        self.assertEqual(count_occurrences("l", "hello"), 2)
        self.assertEqual(count_occurrences("hello", "hellohellohello"), 3)
        self.assertEqual(count_occurrences("he", "hellohehe"), 3)
        self.assertEqual(count_occurrences("a", "aaaa"), 4)
        
    def test_camel_to_lower_with_underscore(self):

        self.assertEqual(camel_to_lower_with_underscore("HelloWorld"), "hello_world")
        self.assertEqual(camel_to_lower_with_underscore("CamelCaseString"), "camel_case_string")
        self.assertEqual(camel_to_lower_with_underscore(""), "")
        self.assertEqual(camel_to_lower_with_underscore("A"), "a")
        
    def test_spiral_order(self):

        matrix1 = [
            ['f', 'i', 'r', 's'],
            ['n', '_', 'l', 't'],
            ['o', 'b', 'a', '_'],
            ['h', 't', 'y', 'p']
        ]
        self.assertEqual(spiral_order(matrix1), "first_python_lab")
        
    def test_is_palindrome_number(self):

        self.assertTrue(is_palindrome_number(121))
        self.assertFalse(is_palindrome_number(123))
        self.assertTrue(is_palindrome_number(1221))
        self.assertFalse(is_palindrome_number(-121))
        
    def test_extract_first_number(self):
        self.assertEqual(extract_first_number("An apple is 123 USD"), 123)
        self.assertEqual(extract_first_number("abc123abc"), 123)
        self.assertIsNone(extract_first_number("No numbers here"))
        
    def test_count_one_bits(self):
        self.assertEqual(count_one_bits(24), 2)
        self.assertEqual(count_one_bits(0), 0)
        self.assertEqual(count_one_bits(1), 1)
        
    def test_most_common_letter(self):
        self.assertEqual(most_common_letter("an apple is not a tomato"), 'a')
        self.assertEqual(most_common_letter("BBBBaaaac"), 'b')
        self.assertIsNone(most_common_letter("12345"))
        
    def test_count_words(self):
        self.assertEqual(count_words("I have Python exam"), 4)
        self.assertEqual(count_words(""), 0)
        self.assertEqual(count_words("One"), 1)
        
    
if __name__ == '__main__':
    unittest.main()