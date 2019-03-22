# Tajnƈ kod zacania: d3968Ɨd943eaǞ69ǅf2ddc87acǵ7715e6
from dictionary_pl import PolishDict
import os
from text_helpers import *

message1 = u"""ie. Zdaje się, że Langner coś do niego mówił, ale Pirx zasnął. W ubraniu. Zbudził się nagle : Langner, pochylony nad łóżkiem, dotknął jego ramienia.

— Już czas — powiedział tylko.

Pirx usiadł. Wyglądało na to, że tamten przez cały czas czytał i pisał; st"""

message = u"""os papierów z obliczeniami urósł. W pierwszej chwili Pirx myślał, że Langner mówi o kolacji, ale chodziło o rakietę. Pirx władował na siebie wypchany plecak. Langner miał jeszcze większy, wyładowany jakby kamieniami, potem się okazało, że oprócz koszul, my"""

m4 = """"""

class Solver():
    def __init__(self, indeks="088"):
        self.dictionary = PolishDict()
        self.load_ciphers(indeks)
        # self.compute_cipher_XOR()

    def load_ciphers(self, indeks):
        self.cipher = []
        path = os.path.join("XOR-ciphertext", indeks +".xor")
        with open(path, "rb") as ciphertext:
            while True:
                line = ciphertext.read(256)
                line = line_to_hex(line) # "hex"
                # print(line)
                line = hex_to_string(line)
                # print(line)

                if not line:
                    break
                self.cipher.append(line)
        print("Loaded {} cipher chunks".format(len(self.cipher)))

    def initial_drag(self):
        words_count = 50
        found_words = 0
        while found_words < words_count:
            word = self.dictionary.random_word()
            print("Próboję: ", word)
            crib = string_to_hex(word)
            for cipher in self.cipher:
                for position in range(len(cipher) - len(crib)):
                    # key = xor_strings(cipher, crib.decode("hex"), position).encode("hex")
                    # print(cipher)
                    key = xor_strings(cipher, word ,position)
                    # key = cipher ^ crib
                    # key = byte_xor(cipher,crib, position) # INTOM TOO BIG TO CONVERT -.-
                    print(key)
                    for cipher2 in self.cipher:
                        possible_message = xor_strings(cipher2, string_to_hex(key), position)
                        if is_ascii(possible_message):
                            print("ZNALEZIONO:", possible_message)
                            words_count +=1

    def multi_xor_all(self):
        with open("output_log.txt","w") as log:
            for c1 in self.cipher:
                for c2 in self.cipher:
                    m1_m2 = xor_strings(c1, c2)
                    solution = xor_strings(m1_m2, message)
                    print(solution,end = "")
                    try:
                        log.write(solution)
                    except:
                        pass
                print("\n\n\nNEW BLOCK\n\n\n")
                log.write("\n\n\n\n\n\n\n\n\n\n")

    def xor_second_with_all_with_solution(self):
        special_cipher = self.cipher[0]
        for cipher in self.cipher:
            key = xor_strings(cipher, special_cipher)
            # key = cipher ^ crib
            # key = byte_xor(cipher,crib, position) # INTOM TOO BIG TO CONVERT -.-
            print()
            print("key: \n",repr(key))
            solution = xor_strings(key, message)
            print()
            print("solution: \n",solution)


    def c2_xor_m2(self):
        key = xor_strings(self.cipher[0], message)
        print("key(repr): \n", repr(key))
        print("key: \n", key)
        self.holy_key = key

    def decrypt_all(self):
        self.c2_xor_m2()
        for cipher in self.cipher:
            msg = xor_strings(cipher, self.holy_key)
            # key = cipher ^ crib
            # key = byte_xor(cipher,crib, position) # INTOM TOO BIG TO CONVERT -.-
            print(msg)

    def compute_cipher_XOR(self):
        pass
        # for cipher1 in self.cipher:


solver = Solver()
# solver.initial_drag()
# solver.xor_second_with_all_with_solution()
# solver.c2_xor_m2()
# solver.decrypt_all()
print(len(message))
# print(len(message2))
solver.multi_xor_all()
