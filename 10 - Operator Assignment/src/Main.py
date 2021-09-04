# Operator Assignment
# Digunakan untuk menyederhanakan bentuk operasi

# Operasi pada aritmatika
print("")
a = 5
print("Nilai a =", a)

a += 2 # a = a + 2
print("Nilai a += 5 bernilai :", a)

a -= 1 # a = a - 1
print("Nilai a -= 1 bernilai :", a)

a *= 8 # a = a * 8
print("Nilai a *= 8 bernilai :", a)

a /= 2 # a = a / 2
print("Nilai a /= 5 bernilai :", a)

a %= 9 # a = a % 9
print("Nilai a %= 9 bernilai :", a)

a //= 2 # a = a // 2
print("Nilai a //= 2 bernilai :", a)

a **= 3 # a = a ** 3 
print("Nilai a **= 3 bernilai :", a)

print("")

# Operasi pada Logika
b = True
print("Nilai b =", b)

b |= False # b = b | false
print("Nilai b |= False menjadi :", b)

c = False
print("Nilai c =", c)

c |= False # c = c | false
print("Nilai c |= False menjadi :", c)

print('')

b = True
print("Nilai b =", b)

b &= False # b = b & False
print("Nilai b &= False, menjadi :", b)

c = True
print("Nilai c =", c)

c &= True # c = c & True
print("Nilai c &= True menjadi :", c)

print('')

b = True
print("Nilai b =", b)

b ^= False # b = b ^ False
print("Nilai b ^= False, menjadi :", b)

c = True
print("Nilai c =", c)

c ^= True # c = c ^ True
print("Nilai c ^= True menjadi :", c)

print("")

# Shifting

a = 0b0110
print("Nilai a =", format(a, '04b'))
a >>= 1 # a = a >> 1
print("Nilai a >>= 1, menjadi :", format(a, '04b'))
a <<= 2 # a = a << 2
print("Nilai a <<= 2, menjadi :", format(a, '04b'))

