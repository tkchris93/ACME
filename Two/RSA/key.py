# solutions.py
"""Volume II Lab 3: Public Key Encryption (RSA)
Solutions file. Written by Shane A. McQuarrie.
"""

# Students will implement the Extended Euclidean Algorithm as part of a
# homework exercise, and they should use it to complete problem 1.
# This is one possible implementation.
def eea(a, b):
    """The Extended Euclidean Algorithm.
    
    Inputs:
        a (int)
        b (int)
    
    Returns:
        gcd (int), c (int), d (int) such that gcd = ac + bd.
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = eea(b % a, a)
        return (g, x - (b // a) * y, y)


# ============================== rsa_tools.py =============================== #
# Helper code for the myRSA class. Provide to the students.

from itertools import izip_longest

def partition(iterable, n, fillvalue=None):
    """Partition data into blocks of length 'n', padding with 'fillvalue'
    if needed. Return a list of the partitions.
    """
    args = [iter(iterable)] * n
    pieces = izip_longest(fillvalue=fillvalue, *args)
    return [''.join(block) for block in pieces]

def string_size(n):
    """Return the maximum number of characters that can be encoded with the
    public key (e, n). In other words, find the largest integer L such that
    if 'string' has at most L characters, then string_to_int('string') will
    be less than 'n'.
    """
    L=0
    max_int = 0
    while max_int < n:
        max_int += sum([2**i for i in range(8*L, 8*L+8)])
        L += 1
    return L-1

def string_to_int(msg):
    """Convert the string 'msg' to an integer.
    This function is the inverse of int_to_string().
    """
    # bytearray will give us the ASCII values for each character 
    if not isinstance(msg, bytearray):
        msg = bytearray(msg)
    binmsg = []
    # convert each character to binary
    for c in msg:
        binmsg.append(bin(c)[2:].zfill(8))
    return int(''.join(binmsg), 2) 

def int_to_string(msg):
    """Convert the integer 'msg' to a string.
    This function is the inverse of string_to_int().
    """
    # convert to binary first
    binmsg = bin(msg)[2:]
    # pad the message so length is divisible by 8
    binmsg = "0"*(8-(len(binmsg)%8)) + binmsg
    msg = bytearray()
    # convert block of 8 bits back to ASCII
    for block in partition(binmsg, 8):
        msg.append(int(block, 2))
    return str(msg)


# ============================== solutions.py =============================== #

# import rsa_tools as rtl
from numpy.random import randint
from Crypto.PublicKey import RSA


# Problem 1: Implement the following RSA system.
class myRSA(object):
    """RSA String Encryption System. Do not use any external modules except for
    'rsa_tools' and your implementation of the Extended Euclidean Algorithm.
    
    Attributes:
        public_key (tup): the RSA key that is available to everyonem, of the
            form (e, n). Used only in encryption.
        _private_key (tup, hidden): the secret RSA key, of the form (d, n).
            Used only in decryption.
    
    Examples:
        >>> r = myRSA()
        >>> r.generate_keys(1000003,608609,1234567891)
        >>> print(r.public_key)
        (1234567891, 608610825827)
        
        >>> r.decrypt(r.encrypt("SECRET MESSAGE"))
        'SECRET MESSAGE'
        
        >>> s = myRSA()
        >>> s.generate_keys(287117,104729,610639)
        >>> s.decrypt(r.encrypt("SECRET MESSAGE",s.public_key))
        'SECRET MESSAGE'
    """
    def __init__(self):
        """Initialize public and private key variables."""
        self.public_key = None
        self._private_key = None
        # Or self.generate_keys() here, if you provide default values.
    
    def generate_keys(self, p, q, e):
        """Create a pair of RSA keys.
        
        Inputs:
            p (int): A large prime.
            q (int): A second large prime .
            e (int): The encryption exponent. 
        
        Returns:
            Set the public_key and _private_key attributes.
        """
        n = p*q
        phi_n = (p-1)*(q-1)
        d = eea(e,phi_n)                        # Use the Extended Euc. Alg.
        if d[0] != 1:                           # Check relative primality
            raise ValueError("e and phi(n) not relatively prime")
        d = d[1]
        d %= phi_n
        
        self.public_key = (e,n)                 # Set key attributes
        self._private_key = (d,n)
    
    def encrypt(self, message, key=None):
        """Encrypt 'message' with a public key and return its encryption as a
        list of integers. If no key is provided, use the 'public_key' attribute
        to encrypt the message.
        
        Inputs:
            message (str): the message to be encrypted.
            key (int tup, opt): the public key to be used in the encryption.
                 Defaults to 'None', in which case 'public_key' is used.
        """
        if key is None:
            key = self.public_key
        part = partition(message, string_size(key[1]), '~')
        numbers = []                            # Partition the message
        for i in part:                          # Convert each piece to numbers
            numbers.append(string_to_int(i))
        ciphertext = []
        for i in numbers:                       # Encrypt the numbers
            ciphertext.append(pow(i,key[0],key[1]))
        return ciphertext
    
    def decrypt(self, ciphertext):
        """Decrypt 'ciphertext' with the private key and return its decryption
        as a single string. You may assume that the format of 'ciphertext' is
        the same as the output of the encrypt() function. Remember to strip off
        the fill value used in rsa_tools.partition().
        """
        key = self._private_key
        decryptions = []
        for i in ciphertext:                    # Decrypt each number
            decryptions.append(pow(i,key[0],key[1]))
        text = []
        for i in decryptions:                   # Convert back to string
            text.append(int_to_string(i))
        text = "".join(text)                    # Splice the strings together
        # Common mistake: stip off the fill value incorrectly
        while text.endswith('~'):               # Strip off the fill value.
            text = text[:-1]
        return text


# Problem 2: Partially test the myRSA class with this function.
#   Use Exceptions to indicate inappropriate arguments or test failure.
def test_myRSA(message, p, q, e):
    """Create a 'myRSA' object. Generate a pair of keys using 'p', 'q', and
    'e'. Encrypt the message, then decrypt the encryption. If the decryption
    is not exactly the same as the original message, raise a ValueError with
    error message "decrypt(encrypt(message)) failed."
    
    If 'message' is not a string, raise a TypeError with error message
    "message must be a string."
    
    If any of p, q, or e are not integers, raise a TypeError with error
    message "p, q, and e must be integers."
    
    Inputs:
        message (str): a message to be encrypted and decrypted.
        p (int): A large prime for key generation.
        q (int): A second large prime for key generation.
        e (int): The encryption exponent.
        
    Returns:
        True if no exception is raised.
    """
    # Input validation 1
    if type(message) != str:
        raise TypeError("message must be a string.")
    
    # Input validation 2
    if type(p) != int or type(q) != int or type(e) != int:
        raise TypeError("p, q, and e must be integers.")
    
    # Test myRSA
    r = myRSA()
    r.generate_keys(p,q,e)
    if message != r.decrypt(r.encrypt(message)):
        raise ValueError("decrypt(encrypt(message)) failed.")
    
    # return True if no exception has been raised.
    return True
    
    # Or, a slightly longer way,
    ciphertext = r.encrypt(message)
    new_message = r.decrypt(ciphertext)
    if message != new_message:
        raise ValueError("decrypt(encrypt(message)) failed.")


# Problem 3: Fermat's test for primality.
def is_prime(n):
    """Use Fermat's test for primality to see if 'n' is probably prime.
    Run the test at most five times, using integers randomly chosen from
    [2, n-1] as possible witnesses. If a witness number is found, return the
    number of tries it took to find the witness. If no witness number is found
    after five tries, return 0.
    
    Inputs:
        n (int): the candidate for primality.
    
    Returns:
        The number of tries it took to find a witness number, up to 5
        (or 0 if no witnesses were found).
    
    """
    for i in range(5):          # Try at most 5 times
        a = randint(2,n)            # pick a random witness
        if 1 != pow(a,n-1,n):       # If a witness is found,
            return i+1                  # return the number of tries
    return 0                    # return 0 if no witness is found.


# Problem 4: Implement the following RSA system using PyCrypto.
class PyCrypto(object):
    """RSA String Encryption System. Do not use any external modules except for
    those found in the 'Crypto' package.
    
    Attributes:
        _keypair (RSA obj, hidden): the RSA key (both public and private).
            Facilitates encrypt() and decrypt().
        public_key (str): A sharable string representation of the public key.
    
    Examples:
        
        >>> p = PyCrypto()
        >>> p.decrypt(p.encrypt("SECRET MESSAGE"))
        'SECRET MESSAGE'
        
        >>> print(p.public_key)
        -----BEGIN PUBLIC KEY-----
        MIIBIjANBgkqhkiG9w0BAQ...
        ...
        ...HwIDAQAB
        -----END PUBLIC KEY-----
        
        >>> q = PyCrypto()
        >>> q.decrypt(p.encrypt("SECRET MESSAGE",q.public_key))
        'SECRET MESSAGE'
    
    """
    def __init__(self):
        """Initialize the _keypair and public_key attributes."""
        self._keypair = RSA.generate(2048)
        self.public_key = self._keypair.publickey().exportKey()
    
    def encrypt(self, message, key=None):
        """Encrypt 'message' with a public key and return its encryption. If
        no key is provided, use the '_keypair' attribute to encrypt 'message'.
        
        Inputs:
            message (str): the message to be encrypted.
            key (str, opt): the string representation of the public key to be
                used in the encryption. Defaults to 'None', in which case
                '_keypair' is used to encrypt the message.
        """
        if not key:
            return self._keypair.encrypt(message, 2048)
        else:
            return RSA.importKey(key).encrypt(message, 2048)
    
    def decrypt(self, ciphertext):
        """Decrypt 'ciphertext' with '_keypair' and return the decryption."""
        return self._keypair.decrypt(ciphertext)


# =========================== END OF SOLUTIONS ========================== #


# prime number generator for sample key generation. Not part of the lab.
def prime(n):
    """Calculates the nth prime number."""
    primes = [2,3,5,7]  # start with some primes
    if n < len(primes): print primes[n-1]; return
    i = 11              # initialize the prime candidate
    while len(primes) < n:
        unique = True
        j = 1           # check divisibility by prior primes
        while unique and j < len(primes):
            if i % primes[j] == 0: unique = False
            j += 1
        if unique: primes.append(i)
        i += 2          # increment the candidate by 2 (avoid evens)
    print primes[len(primes) - 1]
    return primes


# Test script
def test(student_module, late=False):
    """Test script. You must import the student's solutions file as a module.
    
    20 points for problem 1
    10 points for problem 2
    10 points for problem 3
    10 points for problem 4
    
    Inputs:
        student_module: the imported module for the student's solutions file.
        late (bool): if True, half credit is awarded.
    
    Returns:
        score (int): the student's score, out of 50.
        feedback (str): a printout of test results for the student.
    """
    
    def crypt(o,p,message):
        """Test encrypt() and decrypt(). Return 1 on success, 0 else."""
        new_message = o.decrypt(p.encrypt(message,o.public_key))
        if message == new_message: return 1, ""
        else:
            error = "\n\tmessage:\n\t\t" + message
            if o == p: error += "\n\tdecrypt(encrypt(message)):\n\t\t"
            else:
                error += "\n\tq.decrypt(p.encrypt(message,q.public_key)):\n\t\t"
            error += new_message
            return 0, error
    
    def primality(n):
        """Call the student's is_prime() function 10 times on 'n'."""
        total = 0
        for i in xrange(10):
            total += s.is_prime(n)
            if total > 0: break
        return total
    
    def strTest(p, m):
        """Manually grade a problem worth 'p' points and failure message 'm'."""
        part = -1
        while part > p or part < 0:
            part = int(input("\nScore out of " + str(p) + ": "))
        if part == p: return p, ""
        else: return part, m
        
    s = student_module
    score = 0
    total = 50
    feedback = ""
    
    try:    # Problem 1: 20 points
        feedback += "\n\nProblem 1 (20 points):"
        points = 0
        r1 =   myRSA()
        r2 = s.myRSA()
        # Test public key (2 pts)
        r1.generate_keys(287117,104729,610639)
        r2.generate_keys(287117,104729,610639)
        if r1.public_key == r2.public_key: points += 1
        else: feedback += "\n\tmyRSA.public_key failed"
        r1.generate_keys(562739,7927,588949)
        r2.generate_keys(562739,7927,588949)
        if r1.public_key == r2.public_key: points += 1
        else: feedback += "\n\tmyRSA.public_key failed"
        # Test encrypt() and decrypt() together, default key (8 pts)
        r2.generate_keys(610639,287117,104729)
        p,f = crypt(r2,r2,"small test")
        points += p; feedback += f
        p,f = crypt(r2,r2,"really very extremely interesing long test!!")
        points += p; feedback += f
        r2.generate_keys(287117,104729,610639)
        p,f = crypt(r2,r2,"_xx_Message_xx_")
        points += (p * 2); feedback += f
        p,f = crypt(r2,r2,"!@#$%^&*^$%##%^%&*&^&$%^#%#$@#%$&")
        points += (p * 2); feedback += f
        r2.generate_keys(562739,7927,588949)
        p,f = crypt(r2,r2,"F!I*N@A(L)_ ### _&T+E=S^T")
        points += (p * 2); feedback += f
        # Test encrypt() and decrypt() together, non-default public key (10 pts)
        r1.generate_keys(12899,3853,17393)
        p,f = crypt(r1,r2,"small test")
        points += p; feedback += f
        p,f = crypt(r1,r2,"really very extremely interestingly long-ish test")
        points += (p * 2); feedback += f
        r1.generate_keys(610639,287117,104729)
        p,f = crypt(r1,r2,"_xx_Message_xx_")
        points += (p * 2); feedback += f
        p,f = crypt(r1,r2,"!@#$%^&*^$%##%^%&*&^&$%^#%#$@#%$&")
        points += (p * 2); feedback += f
        r1.generate_keys(287117,104729,610639)
        p,f = crypt(r1,r2,"F!I*N@A(L)_ ### _&T+E=S^T")
        points += (p * 3); feedback += f
        # Manually check that encrypt() actually returns an encryption
        print("Student Encryption:")
        print(r2.encrypt("test message"))
        p,f = strTest(1,"\n\tmyRSA.encrypt() must encrypt the message!")
        points *= p; feedback += f
        
        score += points; feedback += "\n  Score += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    try:    # Problem 2: 10 points
        feedback += "\n\nProblem 2 (10 points):"
        points = 0
        print("\nCorrect response:\tmessage must be a string.")
        print("Student response:\t"),
        try: s.test_myRSA(1,2,3,4)
        except TypeError as e:
            points += 1; print(e.message)
            p,f = strTest(1,"\n\tTypeError did not report for 'message'.")
            points += p; feedback += f
        print("Correct response:\tp, q, and e must be integers.")
        print("Student response:\t"),
        try: s.test_myRSA("secret",p="tunnels",q=1,e=2)
        except TypeError as e:
            points += 1; print(e.message)
            p,f = strTest(1,"\n\tTypeError did not report for 'p'.")
            points += p; feedback += f
        print("Correct response:\tp, q, and e must be integers.")
        print("Student response:\t"),
        try: s.test_myRSA("secret",p=1,q="tunnels",e=2)
        except TypeError as e:
            points += 1; print(e.message)
            p,f = strTest(1,"\n\tTypeError did not report for 'q'.")
            points += p; feedback += f
        print("Correct response:\tp, q, and e must be integers.")
        print("Student response:\t"),
        try: s.test_myRSA("secret",p=1,q=2,e="tunnels")
        except TypeError as e:
            points += 1; print(e.message)
            p,f = strTest(1,"\n\tTypeError did not report for 'e'.")
            points += p; feedback += f
        try:
            s.test_myRSA(message="secret",p=287117,q=104729,e=610639)
            points += 2
        except ValueError as e:
            feedback += "\n\t" + e.message + "(message = 'secret')"
        
        score += points; feedback += "\n  Score += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    try:    # Problem 3: 10 points
        feedback += "\n\nProblem 3 (10 points):"
        points = 0
        # Feedback messages
        prime = "\n\tis_prime() failed (prime marked as nonprime: "
        nonprime = "\n\tis_prime() failed (nonprime marked as prime: "
        # Correct response with primes
        if primality(547) == 0: points += 1
        else: feedback += prime + "547)"
        if primality(4421) == 0: points += 1
        else: feedback += prime + "4421)"
        if primality(9739) == 0: points += 1
        else: feedback += prime + "9739)"
        if primality(16411) == 0: points += 1
        else: feedback += prime + "16411)"
        if primality(43063) == 0: points += 1
        else: feedback += prime + "43063)"
        # Correct response with composites
        if primality(10) > 0: points += 1
        else: feedback += nonprime + "10)"
        if primality(1000) > 0: points += 1
        else: feedback += nonprime + "1000)"
        if primality(542) > 0: points += 1
        else: feedback += nonprime + "542)"
        if primality(1643) > 0: points += 1
        else: feedback += nonprime + "1643)"
        if primality(340561) > 0: points += 1
        else: feedback += nonprime + "340561)"
        
        score += points; feedback += "\n  Score += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    try:    # Problem 4: 10 points
        feedback += "\n\nProblem 4 (10 points):"
        points = 0
        # Test encrypt() and decrypt together(), default key
        r2 = s.PyCrypto()
        p,f = crypt(r2,r2,"small test")
        points += p; feedback += f
        p,f = crypt(r2,r2,"really very extremely interestingly long-ish test")
        points += p; feedback += f
        r2 = s.PyCrypto()
        p,f = crypt(r2,r2,"!@#$%^&*^$%##%^%&*&^&$%^#%#$@#%$&")
        points += p; feedback += f
        p,f = crypt(r2,r2,"_xx_Message_xx_")
        points += p; feedback += f
        p,f = crypt(r2,r2,"F!I*N@A(L)_ ### _&T+E=S^T")
        points += p; feedback += f
        # Test encrypt() and decrypt() together, nondefault public key
        r1 =   PyCrypto()
        r2 = s.PyCrypto()
        p,f = crypt(r2,r1,"small test")
        points += p; feedback += f
        p,f = crypt(r2,r1,"really very extremely interestingly long-ish test")
        points += p; feedback += f
        p,f = crypt(r2,r1,"!@#$%^&*^$%##%^%&*&^&$%^#%#$@#%$&")
        points += p; feedback += f
        p,f = crypt(r1,r2,"_xx_Message_xx_")
        points += p; feedback += f
        p,f = crypt(r1,r2,"F!I*N@A(L)_ ### _&T+E=S^T")
        points += p; feedback += f
        # Manually check that encrypt() actually returns an encryption
        print("\nStudent Encryption:")
        print(r2.encrypt("test message"))
        p,f = strTest(1,"\n\tPyCrypto.encrypt() must encrypt the message!")
        points *= p; feedback += f
        
        score += points; feedback += "\n  Score += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    # Late submission penalty
    if late:
        feedback += "\n\nHalf credit for late submission."
        feedback += "\nRaw score: " + str(score) + "/" + str(total)
        score *= .5
    
    # Report final score.
    feedback += "\n\nTotal score: " + str(score) + "/" + str(total)
    percentage = (100.0 * score) / total
    feedback += " = " + str(percentage) + "%"
    if   percentage >=  98.0: feedback += "\n\nExcellent!"
    elif percentage >=  90.0: feedback += "\n\nGreat job!"
    feedback += "\n\n-------------------------------------------------------\n"
    return score,feedback

# =============================== END OF FILE =============================== #