import random
from ExEucAlg import EucAlg
from rsa_tools import *
from Crypto.PublicKey import RSA

class myRSA(object):
    def __init__(self):
        self.public_key = None
        self._private_key = None
        self.generate_keys(1000003,608609,1234567891)
        
    def generate_keys(self, p, q, e):
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
        
        self._private_key = (d[0],n)
        self.public_key = (e,n)			
        
    def encrypt(self, message, pub_key=None):
        '''Encrypt `message' using the public key (e, n).
        
        INPUTS:
        message - A string.
        (e, n) - A pair of integers. Should be an RSA public key.
        
        OUTPUTS:
        Partition `message' into pieces of sufficiently small size, padding if
        necessary. Return a list of the encryptions of the pieces.'''
        
        #Check validity of public key
        if self.public_key is None:
            raise Exception("invalid public key!")
        elif pub_key is None:		
            e = self.public_key[0]
            n = self.public_key[1]
        else:
            e = pub_key[0]
            n = pub_key[1]
        
        output = []
        m = string_to_int(message)
        pieces = partition(message, string_size(n), '~')
        
        for i in pieces:
            temp_int = string_to_int(i)
            output.append(pow(temp_int, e, n))
            
        return output
            
    def decrypt(self, ciphertext):
        '''Decrypt `ciphertext' using your private key.

        INPUTS:
        ciphertext - A list of integers.

        OUTPUTS:
        Decrypt each integer in `cipertext' and return a single string.
        '''

        #check validity of _private_key
        if self._private_key is None:
            raise Exception("invalid private key")

        output = ""

        d = self._private_key[0]
        n = self._private_key[1]

        for i in xrange(len(ciphertext)):
            m = pow(ciphertext[i], d, n)
            output += int_to_string(m)
            
        #strip '~' characters
        output = output[:output.find('~')]
        
        return output

    def is_prime(self, n, number_of_tests=5):
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
            test = pow(random_int, n-1, n)
            if test != 1:
                prime = False
                break
        if prime:
            return 0
        else:
            return passes

class PyCrypto(object):
    def __init__(self):
        self._keypair = RSA.generate(2048)
        self.public_key = self._keypair.publickey().exportKey()
        
    def encrypt(self, message, key=None):
        if key is None:
            key = self.public_key
        encrypter = RSA.importKey(key)
        return encrypter.encrypt(message, 2048)
        
    def decrypt(self, encoded_message):
        return self._keypair.decrypt(encoded_message)
