def get_fibonacci_numbers(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_number)
        return fib_sequence
    
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_list(numbers):
    primes = [num for num in numbers if is_prime(num)]
    return primes

def list_operations(a, b):
    a_set = set(a)
    b_set = set(b)

    intersection = list(a_set & b_set)
    union = list(a_set | b_set)
    a_difference_b = list(a_set - b_set)
    b_difference_a = list(b_set - a_set)

    return sorted(intersection), sorted(union), sorted(a_difference_b), sorted(b_difference_a)

def compose_song(notes, moves, start_pos):
    song = []
    current_pos = start_pos % len(notes) 
    
    for move in moves:
        song.append(notes[current_pos])
        current_pos = (current_pos + move) % len(notes) 
    song.append(notes[current_pos])
    
    return song

def zero_below_diagonal(matrix):
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("The input matrix must be square")

    new_matrix = [row[:] for row in matrix]
    row_count = len(matrix)
    
    for i in range(1, row_count):
        for j in range(0, i):
            new_matrix[i][j] = 0
            
    return new_matrix

def elements_appearing_x_times(x, lists):
    item_counter_dict = {}
    
    for list in lists:
        for item in list:
            item_counter_dict[item] = item_counter_dict.get(item, 0) + 1
    result = []
    for k,v in item_counter_dict.items():
        if v == x :
            result.append(k)
            
    return result

def palindrome_info(numbers):
    palindromes = [num for num in numbers if str(num) == str(num)[::-1] and num >= 0]
    if palindromes:
        return len(palindromes), max(palindromes)
    else:
        return 0, None

def filter_strings_by_ascii(x=1, strings=[], flag=True):
	def is_divisible(c):
		return ord(c) % x == 0
	
	filtered_strings = [
		[chr for chr in string if is_divisible(chr) == flag] for string in strings
	]
	return filtered_strings

from itertools import zip_longest

def combine_elements(*lists):
    return list(zip_longest(*lists, fillvalue=None))

def order_tuples(tuples):
    return sorted(tuples, key=lambda x: x[1][2])

def group_by_rhyme(words):
    rhymes = {}
    
    for word in words:
        if len(word) < 2:
            continue
        rhyme = word[-2:]  # get the last two characters of the word
        
        if rhyme not in rhymes:
            rhymes[rhyme] = []
        rhymes[rhyme].append(word)

    # Convert dictionary to list of lists
    return list(rhymes.values())
