from hamming import Hamming

def test_hamming():
    print("Testing Hamming")
    h = Hamming(3)
    my_str = "111100001010"
    e = h.encode(my_str)
    print("original string: ", my_str)
    print("original encoded: ", e)
    e = e[:-1] + "1"
    e = "0" + e[1:]
    print("errored encoded:  ", e)
    d = h.decode(e)
    print("decoded string:  ", d)

test_hamming()
