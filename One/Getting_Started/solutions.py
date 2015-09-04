# GettingStarted_solutions.py
"""Volume I Lab 1: Getting Started
Written Summer 2015 (Tanner Christensen)
"""

# The student's file should be called solutions.py

# Problem 1: Write and run a "Hello World" script.
# There is nothing to grade for this problem.


# Problem 2: Implement this function.
def sphere_volume(r):
    """Return the volume of the sphere of radius 'r'."""
    return (4 * 3.14159 / 3)*r**3


# Problem 3: Implement the first_half() and reverse() functions.
def first_half(my_string):
    """Return the first half of the string 'my_string'.

    Example:
        >>> first_half("python")
        'pyt'
    """
    return my_string[:len(my_string)/2]
    
def reverse(my_string):
    """Return the reverse of the string 'my_string'.
    
    Example:
        >>> reverse("python")
        'nohtyp'
    """
    return my_string[::-1]
    
# Problem 4: Perform list operations
my_list =  ["ant","baboon","cat","dog"] 
my_list.append("elephant")
my_list.remove("ant")
my_list.remove(my_list[1])
my_list[2] = "donkey"
my_list.append("fox")
# Resulting list should be ['baboon', 'donkey', 'elephant', 'fox']
    

# Problem 5: Implement this function.
def pig_latin(word):
    """Translate the string 'word' into Pig Latin
    
    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
    if word[0] in "aeiou":
        return word + "hay"
    else:
        return word[1:] + word[0] + "ay"
        

# Problem 6: Implement this function.
def int_to_string(my_list):
    """Use a dictionary to translate a list of numbers 1-26 to corresponding
    lowercase letters of the alphabet. 1 -> a, 2 -> b, 3 -> c, and so on.
    
    Example:
        >>> int_to_string([13, 1, 20, 8])
        ['m', 'a', 't', 'h'] 
    """
    my_dictionary = {1:'a',  2:'b',  3:'c',  4:'d',  5:'e',  6:'f',  7:'g',
                     8:'h',  9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n',
                    15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u',
                    22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
    output = []
    for number in my_list:
        output.append(my_dictionary[number])
    return output


# Problem 7: Implement this generator.
def squares(n):
    """Yield all squares less than 'n'.

    Example:
        >>> for i in squares(10):
        ...     print(i)
        ... 
        0
        1
        4
        9
    """
    i = 0
    while i*i < n:
        yield i*i
        i += 1


# Problem 8: Implement this function.
def stringify(my_list):
    """Using a list comprehension, convert the list of integers 'my_list'
    to a list of strings. Return the new list.

    Example:
        >>> stringify([1, 2, 3])
        ['1', '2', '3']
    """
    return [str(n) for n in my_list]


# Problem 9: Implement this function and use it to approximate ln(2).
def alt_harmonic(n):
    """Return the partial sum of the first n terms of the alternating
    harmonic series. Use this function to approximae ln(2).
    """
    return sum([(-1)**(i+1)/float(i) for i in xrange(1,n)])

ln2 = alt_harmonic(500000) # put your approximation for ln(2) here


