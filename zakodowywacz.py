from Heap import *
from Node import *
from Huffman import *
from bitarray import bitarray

def kodowanie(file):
    znaki = {}

    with open(file) as f:
        for line in f:
            for c in line:
                if c not in znaki:
                    znaki[c] = 1
                else:
                    znaki[c] += 1

    return znaki

def zapis(kodziki,file1,file2):
    with open(file2, "w") as f:
        f.write(str(kodziki))
        f.write("\n")
    
    with open(file1, "r") as f:
        bit_string = str(''.join(kodziki[c] for line in f for c in line))

    
    bits = bitarray(bit_string)
    with open(file2, "ab") as f:
        bits.tofile(f)