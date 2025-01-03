from Heap import *
from Node import *
from Huffman import *
from zakodowywacz import *
from rozkodowywacz import *
heap = []
znaki = {}
kodziki = {}
file1 ="test.txt"
file2 = "output.txt"
file3 = "result.txt"
znaki = kodowanie(file1)

for key, value in znaki.items():
        heap.append(Node(f"{key}",value))       
Build_Heap(heap, len(heap))
       
kodziki = Tablica_znakow(Huffman(heap))

zapis(kodziki,file1,file2)

odczyt(file2,file3)