import binascii

m = b"Hi there"

print("m is", m)

hexstr = binascii.hexlify(m)

print("hex string is", hexstr)

integer_m = int(hexstr, 16)

print("integer m is", integer_m)

back2hex = hex(integer_m)

print("back to hex is", back2hex)

withoutPrefix = back2hex[2:]

print("without prefix is", withoutPrefix)

plaintext = binascii.unhexlify(withoutPrefix)

print("plaintext is", plaintext)