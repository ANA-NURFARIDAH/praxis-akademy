# print("hello world")
x = int(input("Silahkan masukkan sebuah angka: "))
if x < 0:
    x = 0
    print("Replace dengan angka Nol")
elif x == 0:
    print("Nol")
elif x == 1:
    print("Jomblo")
else:
    print("Lainnya")

print(x)