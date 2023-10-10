from collections import Counter
from typing import List, Optional
import re

"""
FUNCTIILE SUNT AICI , TESTELE PENTRU ELE SUNT IN `lab1_test.py`
"""

#exercise 1
def gcd(*numbers) -> Optional[int]:
    
    def gcd_two_numbers(a, b):
        while b:
            a, b = b, a % b
        return a

    if len(numbers) == 2:
        return gcd_two_numbers(numbers[0], numbers[1])
    elif len(numbers) > 2:
        temp_gcd = gcd_two_numbers(numbers[0], numbers[1])
        for i in range(2, len(numbers)):
            temp_gcd = gcd_two_numbers(temp_gcd, numbers[i])
        return temp_gcd
    else:
        return None
    
#exercise 2
def count_vowels(input_string: str) -> int:
    
    vowels = set("aeiouAEIOU")
    return sum(1 for char in input_string if char in vowels)

#exercise 3
def count_occurrences(substring: str, main_string: str) -> int:
    return main_string.count(substring)

#exercise 4
def camel_to_lower_with_underscore(camel_case_str: str) -> str:
    if not camel_case_str:
        return ""
    
    snake_case_str = [camel_case_str[0].lower()]

    for char in camel_case_str[1:]:
        if char.isupper():
            snake_case_str.append('_')
            snake_case_str.append(char.lower())
        else:
            snake_case_str.append(char)

    return ''.join(snake_case_str)

#exercise 5
def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return ''.join(result)

#exercise 6
def is_palindrome_number(n: int) -> bool:
    return str(n) == str(n)[::-1]

#exercise 7
def extract_first_number(text: str) -> int:
    numbers = re.findall(r'\d+', text)
    return int(numbers[0]) if numbers else None

#exercise 8
def count_one_bits(n: int) -> int:
    return bin(n).count('1')

#exercise 9
def most_common_letter(text: str) -> str:
   
    letters = re.findall(r'[a-zA-Z]', text.lower())
    return Counter(letters).most_common(1)[0][0] if letters else None

#exercise 10
def count_words(text: str) -> int:
    return len(text.split()) if text else 0