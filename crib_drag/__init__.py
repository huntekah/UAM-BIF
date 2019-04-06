# plan for the program:
# load encripted file into x bytes chunks
# Try to solve the key for the XOR of chunk_1 & chunk_2
#     take most frequent word in lang, XOR it with the chunk_1 XOR chunk_2
#     for each pseudo_word that comes out of XOR:
#         1) find all full words that'd fit to the dictionary. If any of those words wont find us next word in the XOR chunk, we try 2)
#         2) make list of possible extensions:
#             ie. for example "em du" could extend to ["jestem duzy", "bylem durny", "dzem duch" ... ]
#             for each extension, again try to find new words in XOR chunk.
#             strings may also by space surrounded, or dot ended.
#
#
#
# TEST IT ON MY OWN ENCRYPTED PHRASE! (dry run)
import binascii

myHEX = """"""

def  line_to_hex(line):
    return binascii.hexlify(line)

def hex_to_line(line):
    return binascii.unhexlify(line)

def string_to_hex(s1):
    output = ""
    for letter in s1:
        print()

def show_hex_ciphers():
    line = "Jakaś tam linijka"
    line = u"""os papierów z obliczeniami urósł. W pierwszej chwili Pirx myślał, że Langner mówi o kolacji, ale chodziło o rakietę. Pirx władował na siebie wypchany plecak. Langner miał jeszcze większy, wyładowany jakby kamieniami, potem się okazało, że oprócz koszul, my"""
    print(line)
    print(line.encode())
    print(line_to_hex( line.encode()))
    print(hex_to_line(line_to_hex( line.encode())))
    print(hex_to_line(line_to_hex( line.encode())).decode())

    with open("XOR-ciphertext/088.xor","rb") as ciphertext:
        i = 2
        line = ciphertext.read(256)
        print("start")
        for letter in line:
            print(type(letter))
        print("end")
        # print(line.decode("UTF-8"))
        # line = binascii.a2b_uu("jakas laka")
        lineXOR = line_to_hex(line)


        print("(BIN).", line)
        print("(HEX1).", (lineXOR).decode("utf-8"))

        line = ciphertext.read(256)
        # print(line.decode("UTF-8"))
        # line = binascii.a2b_uu("jakas laka")
        lineXOR = line_to_hex(line)
        print("(HEX2).", lineXOR.decode("utf-8"))
        # while True:
        #     i += 1
        #     line = line_to_hex(ciphertext.read(256)).decode("utf-8")
        #     if not line:
        #         break
        #     print("({}).".format(i), line)
        #     print()


PASSPHRASE = """ie. Zdaje się, że Langner coś do niego mówił, ale Pirx zasnął. W ubraniu. Zbudził się nagle : Langner, pochylony nad łóżkiem, dotknął jego ramienia.

— Już czas — powiedział tylko.

Pirx usiadł. Wyglądało na to, że tamten przez cały czas czytał i pisał; st"""

if __name__ == "__main__":
    show_hex_ciphers()