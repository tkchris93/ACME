#getting started
from cmath import sqrt

def quotient(a,b):
    integer_quotient = int(a//b)
    regular_quotient = float(a)/b
    return integer_quotient, regular_quotient
    
def quadratic(a,b,c):
    x_plus = (-b + sqrt(b**2 -4*a*c))/(2*a)
    x_minus = (-b - sqrt(b**2 -4*a*c))/(2*a)
    if x_plus.imag == 0:
       return x_plus.real, x_minus.real
    else:
        return x_plus,x_minus
    
def reverse(string):
    return string[::-1]
    
def odds(n):
    return range(1,2*n,2)
    
def pig_latin(string):
    if string[0] in ['a','e','i','o','u']:
        return string + "hay"
    else:
        return string[1:] + string[0] + "ay"
        
def int_to_string(list_of_ints):
    dictionary = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h',
                    9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o',
                    16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v',
                    23:'w', 24:'x', 25:'y', 26:'z'}
    output = []
    for i in list_of_ints:
        output.append(dictionary[i])
    return output

def pi_approx(terms):
    list_of_odds = odds(terms)
    return 4*sum([(-1)**(i)/float(list_of_odds[i]) for i in range(len(list_of_odds))])
