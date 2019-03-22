import binascii
import sys
from string import ascii_letters
import codecs

def xor_strings(xs, ys,i=0):
    result = "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs[i:], ys))
    print("XOR of {} and {} gives {}".format(xs,ys,result))
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs[i:], ys))

def byte_xor(xs,ys,i=0):
    tmp_xs = xs[i:]
    int_var = int.from_bytes(tmp_xs, sys.byteorder)
    int_key = int.from_bytes(ys, sys.byteorder)
    int_enc = int_var ^ int_key
    print(int_var, int_key,  int_enc)
    byte_form = int_enc.to_bytes(len(ys), sys.byteorder)
    return hex_to_string(line_to_hex(byte_form))

def xor_str_to_arr(xs,ys):
    [ord(x) ^ ord(y) for x,y in zip(xs,ys)]

def line_to_hex(line):
    result = binascii.hexlify(line)
    print(result)
    return result

def hex_to_line(line):
    result = binascii.unhexlify(line)
    print(result)
    return result

# encode(hex)
def string_to_hex(line):
    result = codecs.encode( bytes(line, 'utf-8'), "hex" )
    print(result)
    return result

# decode(hex)
def hex_to_string(line):
    return hex_to_line(line).decode('utf-8', 'backslashreplace')
    # result = codecs.decode( line,"hex")
    # print(result)
    # return result

def is_ascii(word):
    for letter in word:
        if letter not in ascii_letters:
            return False
    return True

# word = "jakaś tam linijka"
# string_to_hex(word)
# hex_to_string(string_to_hex(word))
# line = "Jakaś tam linijka"
#1 print(line)
#2 print(line.encode())
#3 print(line_to_hex(line.encode()))
#4 print(hex_to_line(line_to_hex(line.encode())))
#5 print(hex_to_line(line_to_hex(line.encode())).decode())

#1 Jakaś tam linijka
#2 b'Jaka\xc5\x9b tam linijka'
#3 b'4a616b61c59b2074616d206c696e696a6b61'
#4 b'Jaka\xc5\x9b tam linijka'
#5 Jakaś tam linijka

# for l in b'48656c6c6f20576f726c64':
#     print(l)
#
# print(byte_xor(b'48656c6c6f20576f726c64',b"7375706572736563726574"))
#
# print(xor_strings("Hello World", "the program", 0))

g =  "Some gibber"
m1 = "Hello World"
m2 = "the prógram"
sec= "12345678912"
c1 = xor_strings(m1, sec)
c2 = xor_strings(m2, sec)
m1_m2 = xor_strings(c1,c2)
key_ = xor_strings(g,c1)
h_m1 = xor_strings(key_,c1)