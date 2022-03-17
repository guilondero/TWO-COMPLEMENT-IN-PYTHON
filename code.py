def twos_complement(n, w):
    if n & (1 << (w - 1)):
         n = n - (1 << w)
    return n
