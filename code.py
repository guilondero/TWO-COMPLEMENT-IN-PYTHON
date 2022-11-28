# n is your data, need be a binary (0011001...) 

# w is your base (8,16,24,32...)

def twos_complement(n, w):
    if n & (1 << (w - 1)):
         n = n - (1 << w)
    return n
