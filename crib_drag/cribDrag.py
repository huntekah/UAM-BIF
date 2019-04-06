# Tajnƈ kod zacania: d3968Ɨd943eaǞ69ǅf2ddc87acǵ7715e6
# TƐjny kod zadƒnia: d39Ǉ8fd943eab694f2ddc87ac67715e6
# Tajny kod zadania: d3968fd943eab694f2ddc87ac67715e6
from dictionary_pl import PolishDict
import os
from text_helpers import *

message1 = u"""ie. Zdaje się, że Langner coś do niego mówił, ale Pirx zasnął. W ubraniu. Zbudził się nagle : Langner, pochylony nad łóżkiem, dotknął jego ramienia.

— Już czas — powiedział tylko.

Pirx usiadł. Wyglądało na to, że tamten przez cały czas czytał i pisał; st"""

message = u"""os papierów z obliczeniami urósł. W pierwszej chwili Pirx myślał, że Langner mówi o kolacji, ale chodziło o rakietę. Pirx władował na siebie wypchany plecak. Langner miał jeszcze większy, wyładowany jakby kamieniami, potem się okazało, że oprócz koszul, my"""

m4 =  """os papierów z obliczeniami urósł. W pierwszej chwili Pirx myślał, że Langner mówi o kolacji, ale chodziło o rakietę. Pirx władował na siebie wypchany plecak. Langner miał jeszcze większy, wyładowany jakby kamieniami, potem się okazało, że oprócz koszul, my"""

class Solver():
    def __init__(self, indeks="088"):
        self.dictionary = PolishDict()
        # self.load_ciphers(indeks)
        # self.compute_cipher_XOR()

    def load_ciphers(self, indeks):
        self.cipher = []
        path = os.path.join("XOR-ciphertext", indeks + ".xor")
        with open(path, "rb") as ciphertext:
            while True:
                line = ciphertext.read(256)
                line = line_to_hex(line)  # "hex"
                # print(line)
                line = hex_to_string(line)
                # print(line)
                print(len(line))
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
        message1 = hex_to_string(string_to_hex( m4 ))
        message = message1
        with open("output_log.txt","w") as log:
            for i1, c1 in enumerate(self.cipher):
                print("cipher_method {} :\n\n".format(i1))
                for i2, c2 in enumerate(self.cipher):
                    m1_m2 = xor_strings(c1, c2)
                    solution = xor_strings(m1_m2, message)

                    print(i2,": ", solution, "\n")
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

    def load_raw_ciphers(self, indeks):
        self.raw_cipher = []
        path = os.path.join("XOR-ciphertext", indeks + ".xor")
        with open(path, "rb") as ciphertext:
            while True:
                line = ciphertext.read(256)
                print(len(line))
                if not line:
                    break
                self.raw_cipher.append(line)
        print("Loaded {} raw_cipher chunks".format(len(self.raw_cipher)))

    def get_msg_raw(self):
        self.msg_raw = [ord(x) for x in message]
        print(self.msg_raw)
        print(list_quality(self.msg_raw))

        return self.msg_raw


    def multi_xor_all_raw(self):
        self.get_msg_raw()
        with open("output_log.txt", "w", encoding="utf-8") as my_log:
            for i1, c1 in enumerate(self.raw_cipher):
                print("cipher_method {} :\n\n".format(i1))
                whole_message = []
                my_log.write("\n\ncipher_method {} :\n".format(i1))
                quality_whole = 0
                for i2, c2 in enumerate(self.raw_cipher):
                    xor_lists = lambda l1,l2 : [x ^ y for x, y in zip(l1,l2)]
                    m1_m2 = xor_lists(c1,c2)
                    solution = xor_lists(m1_m2, self.msg_raw)
                    whole_message = whole_message + solution


                    quality_solution = list_quality(solution)
                    quality_whole = list_quality(whole_message)
                    if quality_whole > 0.75:
                        print(quality_whole)
                        line = "".join( [chr(x % 256) for x in solution] )
                        my_log.write("\n\n")
                        writable_solution = "".join( [ "< {} : {} >\n".format(x,chr(x)) for x in solution ]  )
                        my_log.write(writable_solution+"\n")
                        my_log.write(line+"\n")
                    # print(solution)
                    # print(i2,": ", line, "\n")

                print("\n\n\nNEW BLOCK\n\n\n")


solver = Solver()
# solver.initial_drag()
# solver.xor_second_with_all_with_solution()
# solver.c2_xor_m2()
# solver.decrypt_all()
print(len(message))
# print(len(message2))
# solver.multi_xor_all()
solver.load_raw_ciphers("088")
solver.multi_xor_all_raw()
