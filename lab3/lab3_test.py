import unittest
from lab3_fun import *

class TestSetOperations(unittest.TestCase):

    def test_set_operations(self):
        
        list_a = [1, 2, 3, 4]
        list_b = [3, 4, 5, 6]
        expected_result = [{3, 4}, {1, 2, 3, 4, 5, 6}, {1, 2}, {5, 6}]
        self.assertEqual(set_operations(list_a, list_b), expected_result)
        
    def test_character_count(self):
        
        string = "Ana has apples."
        expected_result = {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}
        self.assertEqual(character_count(string), expected_result)
        
    def test_dict_equal(self):
        
        #self.assertTrue(dict_equal({'a': 1, 'b': [2,{"c" : 2}]}, {'a': 1, 'b': [2,{"c" : 3}]}))
        self.assertFalse(dict_equal({'a': 1, 'b': 2}, {'a': 1, 'b': 3}))
        
        dict1 = {'a': {'b': {'c': 1}}, 'd': 2}
        dict2 = {'a': {'b': {'c': 1}}, 'd': 2}
        self.assertTrue(dict_equal(dict1, dict2))
        
        dict2['a']['b']['c'] = 3
        self.assertFalse(dict_equal(dict1, dict2))
        
        dict3 = {'a': [1, 2, 3], 'b': 2}
        dict4 = {'a': [1, 2, 3], 'b': 2}
        self.assertTrue(dict_equal(dict3, dict4))
        
        dict4['a'] = [1, 2, 4]
        self.assertFalse(dict_equal(dict3, dict4))
        
		
        
    def test_xml_element_building(self):
        
        expected = '<a href="http://python.org" _class="my-link" id="someid"> Hello there </a>'
        result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
        self.assertEqual(result, expected)
        
    def test_count_elements(self):
        lst = [1, 2, 3, 2, 3, 4, 5, 5]
        self.assertEqual(count_elements(lst), (5, 3))
        
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(count_elements(lst), (5, 0))
        
        lst = [1, 1, 1, 1, 1]
        self.assertEqual(count_elements(lst), (1, 1))
        
    def test_set_operations(self):
        s1 = {1, 2}
        s2 = {2, 3}
        expected = {
            "{1, 2} | {2, 3}": {1, 2, 3},
            "{1, 2} & {2, 3}": {2},
            "{1, 2} - {2, 3}": {1},
            "{2, 3} - {1, 2}": {3}
        }
        self.assertEqual(set_operations(s1, s2), expected)
        
    def test_sample(self):
        mapping = {
            'start': 'a',
            'b': 'a',
            'a': '6',
            '6': 'z',
            'x': '2',
            'z': '2',
            '2': '2',
            'y': 'start'
        }
        self.assertEqual(loop(mapping), ['a', '6', 'z', '2' ,'2'])
        
    def test_my_function(self):
        result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
        self.assertEqual(result, 3)
    
if __name__ == '__main__':
    unittest.main()