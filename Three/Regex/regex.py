'''
impressions
- I think the content near the beginning of the lab can be reduced dramatically
- The stuff we need for sed and awk starts at Literal Characters and Metacharacters
- A good chunk of literals and metacharacters could be trimmed down
- Character class section was good



Template for topics that would need to be covered in the redo:
- metacharacters
- re.match() doesn't match full strings
-   ^ | start of line
-   $ | end of line
-   | | or
-  () | priority
-   * | match any number of times (0+)
-   + | match at least once (1+)
-   ? | match once or not at all (0 or 1)
-  {} | repeat a certain number of times 
      |  {2,4} = match 2-4 times
      |  {2,} = match at least 2 times
      |  {3} = exactly 3 times
      |  {,3} = up to 3 times
- re.search() and re.MULTILINE
- character classes
-   ^ | except
-   - | range
-     | shorthand stuff
-   . | think wildcard-ish  
'''
import re

def problem1():
	pattern_string = r"\^\{\(!%\.\*_\)\}&"
	pattern = re.compile(pattern_string)
	print bool(pattern.match("^{(!%.*_)}&"))
	
def problem2(): # not a massive fan of this problem
	pass
	# any string that has 'one' or 'two' as the first word
	
def problem3():
	pattern_string = r"^(Book|Mattress|Grocery) (store|supplier)$"
	pattern = re.compile(pattern_string)
	strings_to_match = [ "Book store", "Book supplier", "Mattress store", 
						"Mattress supplier", "Grocery store", "Grocery supplier"]
	print all(pattern.match(string) for string in strings_to_match)

def problem4():
	pattern_string = r"^[^d-w]$"
	pattern = re.compile(pattern_string)
	strings_to_match = ["a", "b", "c", "x", "y", "z"]
	uses_line_anchors = (pattern_string.startswith('^') and pattern_string.endswith('$'))
	solution_is_clever = (len(pattern_string) == 8)
	matches_list = all(pattern.match(string) for string in strings_to_match)
	print uses_line_anchors and solution_is_clever and matches_list

def problem5():	
	identifier_pattern_string = r"^[a-zA-Z_]\w\w\w\w$" 
	identifier_pattern = re.compile(identifier_pattern_string)
	valid = ["mouse", "HORSE", "_1234", "__x__", "while"]
	not_valid = ["3rats", "err*r", "sq(x)", "too_long"]
	print all(identifier_pattern.match(string) for string in valid) and not any(identifier_pattern.match(string) for string in not_valid)

def problem6():	
	identifier_pattern_string = r"^[a-zA-Z_]\w*$" 
	identifier_pattern = re.compile(identifier_pattern_string)
	valid = ["mouse", "HORSE", "_1234", "__x__", "while", "longer_string"]
	not_valid = ["3rats", "err*r", "sq(x)"]
	print all(identifier_pattern.match(string) for string in valid) and not any(identifier_pattern.match(string) for string in not_valid)
