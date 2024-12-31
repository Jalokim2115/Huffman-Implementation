from Heap import *
from Node import *


def Huffman(Lista):
    while len(Lista) > 1:
        z = Node()
        z.left = x = Heap_Extract(Lista) 
        z.right = y = Heap_Extract(Lista)
        z.label = x.label + y.label
        z.freq = x.freq + y.freq
        Heap_Insert(Lista,z)
    return Heap_Extract(Lista)

def Tablica_znakow(root):
    def DFS(root, kod):
        if root.left is not None:
            DFS(root.left, kod + [0])
            
        if root.right is not None:
            DFS(root.right, kod + [1])
            
        if root.left is None and root.right is None:
            slownik[root.label] = ''.join(map(str, kod))
            
    slownik = {}
    kod = []
    DFS(root,kod)
    return slownik