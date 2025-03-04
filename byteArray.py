#creating a byteArray
ba = bytearray([65, 66, 67])  # bytearray(b'ABC')

#Modifying byteArray
ba[0] = 90  # Changes 'A' (65) to 'Z' (90)
print(ba)  # bytearray(b'ZBC')


#Accessing byteArray Elements
ba = bytearray([65, 66, 67, 68])  # bytearray(b'ABCD')

# Access elements by index
print(ba[0])  # Output: 65 (ASCII of 'A')
print(ba[1])  # Output: 66 (ASCII of 'B')

# Convert to character
print(chr(ba[2]))  # Output: 'C'
