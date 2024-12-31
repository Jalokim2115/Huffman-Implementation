from Heap import *
from Node import *
from Huffman import *

kodziki = {}
Node1 = Node("a",10)
Node2 = Node("b",7)
Node3 = Node("c",5)
Node4 = Node("d",3)
Node5 = Node("z",1)
heap=[Node1,Node2,Node3,Node4]

Build_Heap(heap,len(heap))
kodziki = Tablica_znakow(Huffman(heap))
print(kodziki)
