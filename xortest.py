import binascii
m = input('what do you want to say?\n> ').encode()

print("m is", m)

hexstr = binascii.hexlify(m)

print("hex string is", hexstr)

integer_m = int(hexstr, 16)

print("integer m is", integer_m)

testxor = bin(320945240 ^ integer_m)

print("xor'd is ", testxor)

# backtoint = (bin(320945240) ^ testxor)
backtoint = (int(bin(320945240), 2) ^ int(testxor, 2))

print("back to integer is", backtoint)

backtohex = hex(backtoint)

print("back to hex is", backtohex)

shaveprefix = backtohex[2:]

backtostring = binascii.unhexlify(shaveprefix)

print("back to string is", backtostring)