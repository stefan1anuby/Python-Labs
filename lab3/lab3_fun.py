

def set_operations(a, b):
    set_a = set(a)
    set_b = set(b)
    
    intersection = set_a & set_b
    union = set_a | set_b
    difference_a_b = set_a - set_b
    difference_b_a = set_b - set_a
    
    return [intersection, union, difference_a_b, difference_b_a]

def character_count(s):
    char_dict = {}
    for char in s:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def dict_equal(dict1, dict2):
    
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    for key in dict1:
        val1 = dict1[key]
        val2 = dict2[key]

        if type(val1) != type(val2):
            return False

        if isinstance(val1, dict):
            if not dict_equal(val1, val2):
                return False

        elif isinstance(val1, (list, tuple, set)):
            if len(val1) != len(val2) or not all(dict_equal(v1, v2) if isinstance(v1, dict) else v1 == v2 for v1, v2 in zip(val1, val2)):
                return False

        else:
            if val1 != val2:
                return False

	#DE ARATAT SI PARTEA ASTA :
	for key in dict2:
        val1 = dict1[key]
        val2 = dict2[key]

        if type(val1) != type(val2):
            return False

        if isinstance(val1, dict):
            if not dict_equal(val1, val2):
                return False

        elif isinstance(val1, (list, tuple, set)):
            if len(val1) != len(val2) or not all(dict_equal(v1, v2) if isinstance(v1, dict) else v1 == v2 for v1, v2 in zip(val1, val2)):
                return False

        else:
            if val1 != val2:
                return False
    return True

def build_xml_element(tag, content, **attributes):
    
    attrs = ''.join(f' {key}="{value}"' for key, value in attributes.items())
    return f'<{tag}{attrs}> {content} </{tag}>'

def count_elements(lst):
    unique_elements = set()
    duplicates = set()

    for item in lst:
        if item in unique_elements:
            duplicates.add(item)
        else:
            unique_elements.add(item)

    return (len(unique_elements), len(duplicates))

# AM SARIT EX 5 !!

def set_operations(*sets):
        result = {}
        for i in range(len(sets)):
            for j in range(i+1, len(sets)):
                a = sets[i]
                b = sets[j]
                result[f"{a} | {b}"] = a | b
                result[f"{a} & {b}"] = a & b
                result[f"{a} - {b}"] = a - b
                result[f"{b} - {a}"] = b - a
                
        return result

def loop(mapping):
    key = 'start'
    visited = set()
    result = []

    while mapping[key] not in visited and key in mapping:
        visited.add(mapping[key])
        result.append(mapping[key])
        key = mapping[key]

    return result

def my_function(*args, **kwargs):
    return sum(1 for arg in args if arg in kwargs.values())

