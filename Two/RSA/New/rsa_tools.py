# rsa_tools.py
"""Volume II Lab 3: Public Key Encryption (RSA). Auxiliary file.
Helper code for the 'myRSA' class. Do not modify.
"""

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
