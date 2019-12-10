import numpy as np

class Hamming:
    """Hamming encoding of strings: {1,0}*

    r = number of parity bits per block
    m = number of data bits per block = 2^r - r - 1
    n = number of total bits per block = 2^r - 1
    """

    def __init__(self, r):
        self.r = r
        self.m = 2**r - r - 1
        self.n = 2**r - 1

        num_digits = len(np.binary_repr(self.n))
        self.decoding_matrix = np.matrix([[int(x) for x in np.binary_repr(i, num_digits)] for i in range(1, self.n)])
        self.encoding_matrix = []

    def encode(self, s):
        """Encodes a string of {1,0}* with length a multiple of m"""
        if len(s) % self.m != 0:
            print("Error: encode input string length must be multiple of m")
            return None

    def decode(self, s):
        """Encodes a string of {1,0}* with length a multiple of n"""
        if len(s) % self.m != 0:
            print("Error: decode input string length must be multiple of n")
            return None


        


