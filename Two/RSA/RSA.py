import random

# coding: utf-8

# In[2]:

#Helper Code

from itertools import izip_longest

def partition(iterable, n, fillvalue=None):
    '''Partition data into blocks of length `n', padding with `fillvalue' if  -
    needed. Return a list of the partitions.
    EXAMPLE:
    >>> partition('ABCDEFG', 3, 'x')
    ['ABC', 'DEF', 'Gxx']
    '''
    args = [iter(iterable)] * n
    pieces = izip_longest(fillvalue=fillvalue, *args)
    return [''.join(block) for block in pieces]

def string_size(n):
    '''Return the maximum number of characters that can be encoded with the  -
    public key (e, n).
    In other words, find the largest integer L, such that if `string' has at most -
    L characters, then a2i(`string') will be less than `n.'
    '''
    L=0
    max_int = 0
    while max_int < n:
        max_int += sum([2**i for i in range(8*L, 8*L+8)])
        L += 1
    return L-1

def string_to_int(msg):
    '''Convert the string `msg' to an integer.
    '''
    # bytearray will give us the ASCII values for each character
    if not isinstance(msg, bytearray):
        msg = bytearray(msg)
    binmsg = []
    # convert each character to binary
    for c in msg:
        binmsg.append(bin(c)[2:].zfill(8))
    return int(''.join(binmsg), 2)

def int_to_string(msg):
    '''Convert the integer `msg' to a string.
    This function is the inverse of string_to_int().
    '''
    # convert to binary first
    binmsg = bin(msg)[2:]
    # we need to pad the message so length is divisible by 8
    binmsg = "0"*(8-(len(binmsg)%8)) + binmsg
    msg = bytearray()
    for block in partition(binmsg, 8):
        # convert block of 8 bits back to ASCII
        msg.append(int(block, 2))
    return str(msg)


# In[3]:

#Extended Euclidean Algorithm
def EucAlg(e,phi_n):
    a = e
    b = phi_n
    x, lastX = 0, 1
    y, lastY = 1, 0
    while b != 0:
        q = a // b
        a, b = b, a % b
        x, lastX = lastX - q * x, x
        y, lastY = lastY - q * y, y
    while lastX < 0:
        lastX += phi_n
        lastY -= 1
    return lastX, lastY


# In[99]:

#Problem 1
def keys(p, q, e):

    '''Create a pair of RSA keys from primes `p' and `q' and encryption
    exponent `e'.
    Return [(e, n), (d, n)] where (e, n) is the public key and (d, n) is
    the private key.
    '''
    
    #first validate the quality of the input
    d = EucAlg(p, q)
    for i in d:
        if i == 0:
            raise Exception("p and q are not relatively prime.")
    
    n = p*q
    phi_n = (p-1)*(q-1)
    d = EucAlg(e, phi_n)
    return [(e,n),(d[0],n)]

def encrypt(message, e, n):
    '''Encrypt the `message' using the public key (e, n).'''
    
    #check to see if the message needs to be split up.  If m > n, then split is necessary
    m = long(string_to_int(message))
    c = pow(m,e,n)
    return c
    
def decrypt(ciphertext, d, n):
    '''Decrypt the `ciphertext' using your private key.'''
    
    m = pow(ciphertext, d, n)
    return int_to_string(m)


# In[102]:

#Problem 2
def encrypt2(message, e, n):
    '''Encrypt `message' using the public key (e, n).
    
    INPUTS:
    message - A string.
    (e, n) - A pair of integers. Should be an RSA public key.
    
    OUTPUTS:
    Partition `message' into pieces of sufficiently small size, padding if
    necessary. Return a list of the encryptions of the pieces.'''

    
    output = []
    
    m = string_to_int(message)
    pieces = partition(message, string_size(n), 'x')
    
    for i in pieces:
        temp_int = string_to_int(i)
        output.append(pow(temp_int, e, n))
        
    return output

def decrypt2(ciphertext, d, n):
    '''Decrypt `ciphertext' using your private key.
    
    INPUTS:
    ciphertext - A list of integers.
    
    OUTPUTS:
    Decrypt each integer in `cipertext' and return a single string.
    '''
    output = ""
    
    for i in xrange(len(ciphertext)):
        m = pow(ciphertext[i], d, n)
        output += int_to_string(m)
    return output


# In[207]:

#Problem 6


def is_prime(n, number_of_tests=5):
    '''Use Fermat's test for primality to see if `n' is probably prime.
    
    INPUTS:
    n - An integer.
    
    Run Fermat's test on at most 5 numbers randomly chosen from [2, n-1].
    If a witness number is found, return the number of tries it took to
    find the witness number. If no witness number is found after 5 tries,
    return 0
    '''
    
    passes = 0
    prime = True #assume prime
    for i in xrange(number_of_tests):
        passes += 1
        random_int = random.randint(2, n-1)
        test = random_int**(n-1) % n
        if test != 1:
            prime = False
            break
    if prime:
        return True
    else:
        return passes

       
    
'''

# In[ ]:

get_ipython().magic(u'timeit 12345671234132**123457123165 % 123231651325')


# In[ ]:

get_ipython().magic(u'timeit pow(12345671234132, 123457123165, 123231651325)')


# In[ ]:

n = 17


passes = 0
random_tests = np.random.choice(range(2, n-1), size = 5)
for i in xrange(len(random_tests)):
    passes += 1
    test = int(random_tests[i])**(n-1) % n
    print "test: " + str(test)
    if test != 1:
        prime = False
        break
if prime:
    return 0
else:
    return passes




# In[136]:

random_tests[0]**16 % 17


# In[145]:

for i in random_tests:
    print i**16 % 17


# In[175]:

random_tests = list(random_tests)


# In[141]:

16 % 17


# In[150]:

(14**16)# % 17


# In[176]:

int(random_tests[0])**16 % 17


# In[154]:

p=random_tests[0]


# In[165]:

14**16


# In[164]:

p**16


# In[156]:

random_tests[0]


# In[157]:

_**16


# In[158]:

14**16


# In[162]:

14**6 == random_tests[0]**6


# In[166]:

random_tests.dtype


# In[167]:

t=14


# In[170]:

type(t**16)


# In[171]:

type(random_tests[0]**16)


# In[ ]:


'''
