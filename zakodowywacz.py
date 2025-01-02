from Heap import *
from Node import *
from Huffman import *

def kodowanie():
    znaki = {}
    heap = []

    with open("test.txt") as f:
        for line in f:
            for c in line:
                if c not in znaki:
                    znaki[c] = 1
                else:
                    znaki[c] += 1
    for key, value in znaki.items():
        heap.append(Node(f"{key}",value))   
        
    return  heap
    