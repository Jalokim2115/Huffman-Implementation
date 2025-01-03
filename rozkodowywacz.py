from Heap import *
from Node import *
from Huffman import *
from bitarray import bitarray
import ast

def odczyt(file1,file2):
    with open(file1, "rb") as f:
        # Odczytanie słownika (z pliku tekstowego)
        kodziki_text = f.readline().decode('latin-1').strip()  # Odczytaj linię jako tekst
        kodziki = ast.literal_eval(kodziki_text)  # Zamień tekst na słownik

        # Odczytanie bitów
        bits = bitarray()
        bits.fromfile(f)  # Odczytujemy bity z pliku binarnego

    # Konwertowanie bitów do ciągu znaków ('0' i '1')
    bit_string = bits.to01()

    # Dekodowanie bitów do tekstu
    decoded_text = []
    temp_bits = ""

    for bit in bit_string:
        temp_bits += bit  # Dodajemy bit do obecnego fragmentu
        if temp_bits in kodziki.values():  # Jeśli fragment bitów pasuje do jakiegoś kodu
            decoded_text.append([k for k, v in kodziki.items() if v == temp_bits][0])  # Dodaj znak
            temp_bits = ""  # Zresetuj fragment bitów

    decoded_text_str = ''.join(decoded_text)  # Połącz listę znaków w jeden ciąg

    # Zapisz rozkodowany tekst do pliku
    with open(file2, "w", encoding="utf-8") as f:
        f.write(decoded_text_str)