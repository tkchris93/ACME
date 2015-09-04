# name this file 'solutions.py'
"""Volume II Lab 1: The Standard Library
Tanner Christensen
<Class>
Sept 2, 2015
"""

# Add import statements here.
# In future labs, do not modify any PROVIDED import statements.
# You may always add others as needed.
import calculator as calc
import matrix_multiply
import sys
import time

# Problem 1: Implement this function.
def prob1(l):
    """Accept a list 'l' of numbers as input and return a new list with the
    minimum, maximum, and average of the contents of 'l'.
    """
    return min(l), max(l), sum(l)/float(len(l))


# Problem 2: Implement this function.
def prob2():
    """Determine which Python objects are mutable and which are immutable. Test
    numbers, strings, lists, tuples, and dictionaries. Print your results to the
    terminal using the print() function.
    """
    num1 = 6
    num2 = num1
    num1 += 1
    print num1, num2, "Numbers are immutable"
    
    str1 = "Hello"
    str2 = str1
    str1 += "a"
    print str1, str2, "Strings are immutable" 
    
    list1 = [1,2,3]
    list2 = list1
    list1.append(1)
    print list1, list2, "Lists are mutable"
    
    tuple1 = (1,2,3)
    tuple2 = tuple1
    tuple1 = tuple1 + (1,)
    print tuple1, tuple2, "Tuples are immutable"
    
    dict1 = {2:'b', 3:'c'}
    dict2 = dict1
    dict1[1] = 'a'
    print dict1, dict2, "Dictionaries are mutable"

	# numbers, strings, and tuples are immutable.

# Problem 3: Create a 'calculator' module and use it to implement this function.
def prob3(a,b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any methods other than those that are imported from the
    'calculator' module.
    
    Parameters:
        a (float): the length one of the sides of the triangle.
        b (float): the length the other nonhypotenuse side of the triangle.
    
    Returns:
        The length of the triangle's hypotenuse.
    """
    return calc.square_root(calc.add(calc.mult(a,a),calc.mult(b,b)))

# Problem 4: Utilize the 'matrix_multiply' module and 'matrices.npz' file to
#   implement this function.
def prob4():
    """If no command line argument is given, print "No Input."
    If anything other than "matrices.npz is given, print "Incorrect Input."
    If "matrices.npz" is given as a command line argument, use functions
    from the provided 'matrix_multiply' module to load two matrices, then
    time how long each method takes to multiply the two matrices together.
    Print your results to the terminal.
    """
    if len(sys.argv) == 0:
        print "No Input."

    if sys.argv[1] == "matrices.npz":
        A, B = matrix_multiply.load_matrices("matrices.npz")
        
        before = time.time()
        matrix_multiply.method1(A,B)
        after = time.time()
        method1_time = after - before
        
        before = time.time()
        matrix_multiply.method2(A,B)
        after = time.time()
        method2_time = after - before
        
        before = time.time()
        matrix_multiply.method3(A,B)
        after = time.time()
        method3_time = after - before
        
        print "Method 1: " + str(method1_time)
        print "Method 2: " + str(method2_time)
        print "Method 3: " + str(method3_time)
        
    else:
        print "Incorrect Input"


# Everything under this 'if' statement is executed when this file is run from
#   the terminal. In this case, if we enter 'python solutions.py word' into
#   the terminal, then sys.argv is ['solutions.py', 'word'], and prob4() is
#   executed. Note that the arguments are parsed as strings. Do not modify.
if __name__ == "__main__":
    prob4()


# ============================== END OF FILE ================================ #
