import re

# PROBLEM 1
def problem1():
    pattern_string = r""  # Edit this line
    pattern = re.compile(pattern_string)
    print bool(pattern.match("^{(!%.*_)}&"))

# PROBLEM 2
def problem2():
    pattern_string = r""  # Edit this line
    pattern = re.compile(pattern_string)
    strings_to_match = [ "Book store", "Book supplier", "Mattress store", 
                        "Mattress supplier", "Grocery store", "Grocery supplier"]
    print all(pattern.match(string) for string in strings_to_match)

# PROBLEM 3
def problem3():
    pattern_string = r""  # Edit this line
    pattern = re.compile(pattern_string)
    strings_to_match = ["a", "b", "c", "x", "y", "z"]
    uses_line_anchors = (pattern_string.startswith('^') and pattern_string.endswith('$'))
    solution_is_clever = (len(pattern_string) == 8)
    matches_list = all(pattern.match(string) for string in strings_to_match)
    print uses_line_anchors and solution_is_clever and matches_list

# PROBLEM 4
def problem4():	
    identifier_pattern_string = r""  # Edit this line 
    identifier_pattern = re.compile(identifier_pattern_string)
    valid = ["mouse", "HORSE", "_1234", "__x__", "while"]
    not_valid = ["3rats", "err*r", "sq(x)", "too_long"]
    print all(identifier_pattern.match(string) for string in valid) and not any(identifier_pattern.match(string) for string in not_valid)

# PROBLEM 5
def problem5():	
    identifier_pattern_string = r""  # Edit this line 
    identifier_pattern = re.compile(identifier_pattern_string)
    valid = ["mouse", "HORSE", "_1234", "__x__", "while", "longer_string"]
    not_valid = ["3rats", "err*r", "sq(x)"]
    print all(identifier_pattern.match(string) for string in valid) and not any(identifier_pattern.match(string) for string in not_valid)

# PROBLEM 6
def problem6():
    parameter_pattern_string = r""  # Edit this line
    parameter_pattern = re.compile(parameter_pattern_string)
    valid = ["max=4.2", "string= ''", "num_guesses", "msg ='\\'", "volume_fn=_CALC_VOLUME"] 
    not_valid = ["300", "no spaces", "is_4=(value==4)", "pattern = r'^one|two fish$'", 'string="these last two are actually valid in python, but they should not be matched by your pattern"'] 
    print all(parameter_pattern.match(string) for string in valid) and not any(parameter_pattern.match(string) for string in not_valid)

# PROBLEM 7
"""
1.
2.
3.
"""
