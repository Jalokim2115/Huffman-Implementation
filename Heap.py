from Node import *

def MIN_Heapify(lista, i, Heap_size):
    left = (2 * i) + 1
    right = (2 * i) + 2
    smaller = i

    if left < Heap_size:
        if lista[smaller].freq > lista[left].freq:
            smaller = left
            
    if right < Heap_size:
        if lista[smaller].freq > lista[right].freq:
            smaller = right
            
    if smaller != i:
        lista[i], lista[smaller] = lista[smaller], lista[i]
        MIN_Heapify(lista, smaller, Heap_size)

def Build_Heap(lista, Heap_size):
    for i in range((Heap_size - 2) // 2, -1, -1):
        MIN_Heapify(lista, i, Heap_size)

def Heap_Sort(lista):
    Heap_size = len(lista)
    Build_Heap(lista, Heap_size)
    sorted_list = []
    for i in range(len(lista)):
        sorted_list.append(lista[0])
        lista[0], lista[Heap_size - 1] = lista[Heap_size - 1], lista[0]
        Heap_size -= 1
        MIN_Heapify(lista, 0, Heap_size)
    return sorted_list

def Heap_Extract(lista):
    result = lista[0]
    lista[0], lista[len(lista)-1] = lista[len(lista)-1], lista[0]
    del lista[len(lista) - 1]
    MIN_Heapify(lista,0,len(lista))
    return result
    
def Heap_Insert(lista,Node):
    lista.append(Node)
    Build_Heap(lista,len(lista))