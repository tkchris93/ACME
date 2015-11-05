# name this file 'solutions.py'
"""Volume II Lab 3: Public Key Encryption (RSA)
Tanner Chritsensen
Sept 11, 2015
"""
from rsa_tools import *
from Crypto.PublicKey import RSA
import random

def myEEA(a,b):
    """Solves gcd(a,b) = ax+by using the 
    Extended Euclidean Algorithm
    
    Input:
        a (int) : first number
        b (int) : second number
        
    Returns:
        gcd (int) : gcd(a,b)
        x (int): x such that gcd(a,b) = ax+by
        y (int): y such that gcd(a,b) = ax+by
    """
    r,last_r = b,a
    x,last_x = 0,1
    y,last_y = 1,0
    while r != 0:
        q = last_r // r
        last_r, r = r, last_r%r
        last_x, x = x, (last_x - q*x)
        last_y, y = y, (last_y - q*y)
    gcd = last_r
    x = last_x
    y = last_y
    return gcd, x, y

# Problem 1: Implement the following RSA system.
class myRSA(object):
    """RSA String Encryption System. Do not use any external modules except for
    'rsa_tools' and your implementation of the Extended Euclidean Algorithm.
    
    Attributes:
        public_key (tup): the RSA key that is available to everyone, of the
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
    
    def generate_keys(self, p, q, e):
        """Create a pair of RSA keys.
        
        Inputs:
            p (int): A large prime.
            q (int): A second large prime .
            e (int): The encryption exponent. 
        
        Returns:
            Set the public_key and _private_key attributes.
        """
        d = myEEA(p, q)
        for i in d:
            if i == 0:
                raise Exception("p and q are not relatively prime.")
        
        n = p*q
        phi_n = (p-1)*(q-1)
        d = myEEA(e, phi_n)
        
        d_prime = d[1]
        while d_prime < 0:
            d_prime += phi_n
        
        d = d_prime
        self._private_key = (d_prime,n)
        self.public_key = (e,n)
    
    def encrypt(self, message, key=None):
        """Encrypt 'message' with a public key and return its encryption as a
        list of integers. If no key is provided, use the 'public_key' attribute
        to encrypt the message.
        
        Inputs:
            message (str): the message to be encrypted.
            key (int tup, opt): the public key to be used in the encryption.
                 Defaults to 'None', in which case 'public_key' is used.
        """
        if self.public_key is None:
            raise Exception("invalid public key!")
        elif key is None:
            e = self.public_key[0]
            n = self.public_key[1]
        else:
            e = key[0]
            n = key[1]
        
        output = []
        m = string_to_int(message)
        pieces = partition(message, string_size(n), '~')
        
        for i in pieces:
            temp_int = string_to_int(i)
            output.append(pow(temp_int, e, n))
            
        return output
    
    def decrypt(self, ciphertext):
        """Decrypt 'ciphertext' with the private key and return its decryption
        as a single string. You may assume that the format of 'ciphertext' is
        the same as the output of the encrypt() function. Remember to strip off
        the fill value used in rsa_tools.partition().
        """
        if self._private_key is None:
            raise Exception("invalid private key")

        output = ""

        d = self._private_key[0]
        n = self._private_key[1]

        for i in xrange(len(ciphertext)):
            m = pow(ciphertext[i], d, n)
            output += int_to_string(m)
            
        #strip '~' characters
        if output[-1] == '~':
            output = output[:output.find('~')]
        
        return output


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
    if type(message) != str:
        raise TypeError("message must be a string.")
    elif (type(p) != int) or (type(q) != int) or (type(e) != int):
        raise TypeError("p, q, and e must be integers.")
    
    r = myRSA()
    r.generate_keys(p,q,e)
    if message != r.decrypt(r.encrypt(message)):
        raise ValueError("decrypt(encrypt(message)) failed")
    else:
        return True

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
    number_of_tests = 5
    passes = 0
    prime = True #assume prime
    for i in xrange(number_of_tests):
        passes += 1
        random_int = random.randint(2, n-1)
        test = pow(random_int, n-1, n)
        if test != 1:
            prime = False
            break
    if prime:
        return 0
    else:
        return passes

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
        if key is None:
            key = self.public_key
        encrypter = RSA.importKey(key)
        return encrypter.encrypt(message, 2048)      
    
    def decrypt(self, ciphertext):
        """Decrypt 'ciphertext' with '_keypair' and return the decryption."""
        return self._keypair.decrypt(ciphertext)

# ============================== END OF FILE ============================== #
