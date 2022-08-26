# print(f.read())

# print(f.read())

# print(f.readline())

# print(f.readline())

# print(f.readline())

# for line in f:
#     print((line, end=''))

# print(f.write('This is a test\n'))

# value = ('the answer', 42)
# s = str(value)  # convert the tuple to string
# print(f.write(s))

# f = open('workfile', 'rb+')
# print(f.write(b'0123456789abcdef'))

print(f.seek(5))     # Go to the 6th byte in the file

print(f.read(1))

print(f.seek(-3, 2)  # Go to the 3rd byte before the end)

# f.read(1)