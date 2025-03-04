#Creating bytes
b1 = b"Hello"  
b2 = bytes([65, 66, 67])  # b'ABC'

#Accessing bytes
b = b"Sami"
print(b[0])  # 83 (ASCII of 'S')
print(chr(b[1]))  # 'a'

#Immutable(cant modify)
b[0] = 90  # ❌ TypeError

#coverting string to bytes and vice-versa
text = "hello".encode()  # b'hello'
print(text.decode())  # "hello"


