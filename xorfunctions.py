import binascii

# m being the string we want to encrypt, I guess m is for 'message'? (pulled from CPEG472 (Applied Cryptography Class 3)
m = input('What do you want to XOR?\n> ').encode()

key = int(input('What do you want the key to be? (Integer)\n> '))

print("m is", m)

hexstr = binascii.hexlify(m)

print("hex string is", hexstr)

integer_m = int(hexstr, 16)

print("integer m is", integer_m)

testxor = bin(key ^ integer_m)

print("xor'd is ", testxor)

backtoint = (int(bin(key), 2) ^ int(testxor, 2))

print("back to integer is", backtoint)

backtohex = hex(backtoint)

print("back to hex is", backtohex)

shaveprefix = backtohex[2:]

backtostring = binascii.unhexlify(shaveprefix)

print("back to string is", backtostring)