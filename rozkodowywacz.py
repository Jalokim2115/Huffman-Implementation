from Heap import *
from Node import *
from Huffman import *
from bitarray import bitarray
import ast

def odczyt(file1,file2):
    with open(file1, "rb") as f:

        kodziki_text = f.readline().decode('latin-1').strip()
        kodziki = ast.literal_eval(kodziki_text)


        bits = bitarray()
        bits.fromfile(f)  


    bit_string = bits.to01()


    decoded_text = []
    temp_bits = ""

    for bit in bit_string:
        temp_bits += bit  
        if temp_bits in kodziki.values(): 
            decoded_text.append([k for k, v in kodziki.items() if v == temp_bits][0])  
            temp_bits = "" 
            
    decoded_text_str = ''.join(decoded_text)


    with open(file2, "w", encoding="utf-8") as f:
        f.write(decoded_text_str)