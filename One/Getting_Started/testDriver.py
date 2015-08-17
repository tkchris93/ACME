# testDriver.py
"""Test Driver for Getting Started Lab"""

# Test script
def test(student_module, late=False):
    """Test script. You must import the students file as a module.
    
    X points for problem 1
    X points for problem 2
    X points for problem 3
    X points for problem 4
    ...
    
    Parameters:
        student_module: the imported module for the student's file.
        late (bool, opt): if True, half credit is awarded.
    
    Returns:
        score (int): the student's score, out of 'total'.
        feedback (str): a printout of results for the student.
    """
    
    # possible helper functions
    def strTest(x,y,m):
        """Test to see if x and y have the same string representation. If
        correct, award a points and return no message. If incorrect, return
        0 and return 'm' as feedback.
        """
        if str(x) == str(y): return 1, ""
        else:
            m += "\n\t\tCorrect response: " + str(x)
            m += "\n\t\tStudent response: " + str(y)
            return 0, m
    
    def grade(p,m):
        """Manually grade a problem worth 'p' points with error message 'm'."""
        part = -1
        while part > p or part < 0:
            part = int(input("\nScore out of " + str(p) + ": "))
        if part == p: return p,""
        else: return part,m

    s = student_module
    score = 0
    total = 100
    feedback = s.__doc__
    
    try:    # Problem 1: 5 points
        feedback += "\n\nTesting problem 1 (5 points):"
        points = 5
        # Test problem 1 here
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    try:    # Problem 2: 10 points
        feedback += "\n\nTesting problem 2 (10 points):"
        points = 10
        # Test problem 2 here
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 3: 10 points
        feedback += "\n\nTesting problem 3 (10 points):"
        points = 10
        # Test problem 3 here
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 4: 10 points
        feedback += "\n\nTesting problem 4 (X points):"
        points = 10
        # Test problem 4 here
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message

    try:    # Problem 5: 10 points
        feedback += "\n\nTesting problem 5 (10 points):"
        points = 10
        # Test problem 5 here
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 6: 15 points
        feedback += "\n\nTesting problem 6 (15 points):"
        points = 15
        # Test problem 6 here
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    try:    # Problem 7: 10 points
        feedback += "\n\nTesting problem 7 (10 points):"
        points = 10
        # Test problem 7 here
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 8: 10 points
        feedback += "\n\nTesting problem 8 (10 points):"
        points = 10
        # Test problem 8 here
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    try:    # Problem 9: 20 points
        feedback += "\n\nTesting problem 9 (20 points):"
        points = 20
        # Test problem 9 here
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    
    
    if late:    # Late submission penalty
        feedback += "\n\nHalf credit for late submission."
        feedback += "\nRaw score: " + str(score) + "/" + str(total)
        score *= .5
    
    # Report final score.
    feedback += "\n\nTotal score: " + str(score) + "/" + str(total)
    percentage = (100.0 * score) / total
    feedback += " = " + str(percentage) + "%"
    if   percentage >=  98.0: feedback += "\n\nExcellent!"
    elif percentage >=  90.0: feedback += "\n\nGreat job!"
    return score, feedback
