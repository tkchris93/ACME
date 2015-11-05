import re

def problem1():
    pattern_string = r"\^\{\(!%\.\*_\)\}&"
    pattern = re.compile(pattern_string)
    print bool(pattern.match("^{(!%.*_)}&"))

def problem2():
    pattern_string = r"^(Book|Mattress|Grocery) (store|supplier)$"
    pattern = re.compile(pattern_string)
    strings_to_match = [ "Book store", "Book supplier", "Mattress store", 
                        "Mattress supplier", "Grocery store", "Grocery supplier"]
    print all(pattern.match(string) for string in strings_to_match)

def problem3():
    pattern_string = r"^[^d-w]$"
    pattern = re.compile(pattern_string)
    strings_to_match = ["a", "b", "c", "x", "y", "z"]
    uses_line_anchors = (pattern_string.startswith('^') and pattern_string.endswith('$'))
    solution_is_clever = (len(pattern_string) == 8)
    matches_list = all(pattern.match(string) for string in strings_to_match)
    print uses_line_anchors and solution_is_clever and matches_list

def problem4():	
    identifier_pattern_string = r"^[a-zA-Z_]\w\w\w\w$" 
    identifier_pattern = re.compile(identifier_pattern_string)
    valid = ["mouse", "HORSE", "_1234", "__x__", "while"]
    not_valid = ["3rats", "err*r", "sq(x)", "too_long"]
    print all(identifier_pattern.match(string) for string in valid) and not any(identifier_pattern.match(string) for string in not_valid)

def problem5():	
    identifier_pattern_string = r"^[a-zA-Z_]\w*$" 
    identifier_pattern = re.compile(identifier_pattern_string)
    valid = ["mouse", "HORSE", "_1234", "__x__", "while", "longer_string"]
    not_valid = ["3rats", "err*r", "sq(x)"]
    print all(identifier_pattern.match(string) for string in valid) and not any(identifier_pattern.match(string) for string in not_valid)

def problem6():
    pass

def problem7():
    '''
    grep 'Ross,\(Nicholas\|Zoey\)' transactions.txt
    awk ' BEGIN{FS=";"} {if ($4 ~ /3298/) print $3} ' < transactions.txt | sort
    awk ' BEGIN{FS=";"} {if ($2 ~ /2014061[3-5]/) print $4} ' < transactions.txt | sort
    '''
