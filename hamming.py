import numpy as np

class Hamming:
    """Hamming encoding of strings: {1,0}*

    r = number of parity bits per block
    m = number of data bits per block = 2^r - r - 1
    n = number of total bits per block = 2^r - 1

    reference: http://www-math.mit.edu/~djk/18.310/18.310F04/matrix_hamming_codes.html
    """

    def __init__(self, r):
        self.r = r
        self.m = 2**r - r - 1
        self.n = 2**r - 1

        num_digits = len(np.binary_repr(self.n))

        # non systematic h
        h = np.matrix([[int(x) for x in np.binary_repr(i, num_digits)] for i in range(1, self.n+1)])
        h = h.T

        # convert last r cols to identity matrix through swapping columns (systematic)
        for i in range(r):
            x = 2**i - 1
            y = self.n - 1 - i
            h[:,[x,y]] = h[:,[y,x]]


        g = np.concatenate((np.identity(self.m, dtype=int), h[:,:self.m].T), axis=1)

        self.decoding_matrix = h
        self.encoding_matrix = g

    def encode(self, s):
        """Encodes a string of {1,0}* with length a multiple of m"""
        if len(s) % self.m != 0:
            print("Error: encode input string length must be multiple of m")
            return None
        s_array = np.array(list(s), dtype=int)
        s_array_split = np.split(s_array, indices_or_sections=len(s)/self.m)
        s_array_mult = [np.remainder(np.dot(x, self.encoding_matrix), 2) for x in s_array_split]
        out_s = np.concatenate(s_array_mult, axis=1)
        flattened = np.ravel(out_s)
        return "".join([str(x) for x in flattened.tolist()])

    def decode(self, s):
        """Encodes a string of {1,0}* with length a multiple of n"""
        if len(s) % self.n != 0:
            print("Error: decode input string length must be multiple of n")
            return None

        syndrome_mapping = {}
        d = self.decoding_matrix.T
        for i in range(len(d)):
            curr_num_s = "".join([str(x) for x in d[i].tolist()[0]])
            curr_num = int(curr_num_s, 2)
            syndrome_mapping[curr_num] = i

        s_array = np.array(list(s), dtype=int)
        s_array_split = np.split(s_array, indices_or_sections=len(s)/self.n)
        s_array_mult = [np.remainder(np.dot(self.decoding_matrix, x), 2) for x in s_array_split]

        out = ""
        for i in range(len(s_array_mult)):
            curr_num_s = "".join([str(x) for x in s_array_mult[i].tolist()[0]])
            curr_num = int(curr_num_s, 2)
            curr_out = s_array_split[i].tolist()            
            if curr_num != 0:
                incorrect = syndrome_mapping[curr_num]
                curr_out[incorrect] = 1-curr_out[incorrect]
            out += "".join([str(x) for x in curr_out[:self.m]])
        return out

