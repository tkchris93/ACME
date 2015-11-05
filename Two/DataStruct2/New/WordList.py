# WordList.py
"""Volume II Lab 5: Data Structures II (Trees). Auxiliary file
Use this function to complete problem 4. Do not modify.
"""

import numpy as np

# Use this function in problem 4.
def create_word_list(filename='English.txt'):
    """Read in a list of words from the specified file.
    Randomize the ordering and return the list.
    """
    file = open(filename, 'r')      # Open the file with read-only access
    file = file.read()              # Read in the text from the file
    file = file.split('\n')         # Get each word, separated by '\n'
    file = file[:-1]                # Remove the last endline
                                    # Randomize, convert to a list, and return.
    return list(np.random.permutation(file))

# You do not need this function, but read it anyway.
def export_word_list(words, outfile='Test.txt'):
    """Write a list of words to the specified file. You are not required
    to use this function, but it may be useful in testing sort_words().
    Note that 'words' must be a Python list.
    
    These two functions are examples of how file input / output works in
    Python. This concept will resurface many times in later labs.
    """
    file = open(outfile, 'w')       # Open the file with write-only access
    for w in words:                 # Write each word to the file, appending
        file.write(w + '\n')        #   an endline character after each word
    f.close()                       # Close the file.