from Heap import *
from Node import *
from Huffman import *
from zakodowywacz import *

heap = []
znaki = {}
kodziki = {}

heap = kodowanie()

kodziki = Tablica_znakow(Huffman(heap))

print(kodziki)