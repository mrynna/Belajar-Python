# Operator Bitwise
# Operasi yang dilakukan pada nilai bentuk bit (Binary Operation)
"""
Bitwise dituliskan dengan menggunakan simbol
1. and  ( & )
2. or   ( | )
3. xor  ( ^ )
4. not  ( ~ )

Shifting pada bitwise
digunakan untuk memindahkan nilai bit ke kanan atau ke kiri
"""

a = 15
b = 20
binary_a = format(a,'08b') # Konversi nilai a ke dalam bentuk biner
binary_b = format(b,'08b') # Konversi nilai b ke dalam bentuk biner

print("")
print("============= AND =============")
print("")

# AND (&)
c = a & b 
binary_c = format(c,'08b') # Konversi nilai c ke dalam bentuk biner
print("Nilai", a, "binary :", binary_a)
print("Nilai", b, "binary :", binary_b)
print("--------------------------- (&)")
print("Nilai", c, " binary :", binary_c)

print("")
print("============= OR ==============")
print("")

# OR (|)
c = a | b 
binary_c = format(c,'08b') # Konversi nilai c ke dalam bentuk biner
print("Nilai", a, "binary :", binary_a)
print("Nilai", b, "binary :", binary_b)
print("--------------------------- (|)")
print("Nilai", c, "binary :", binary_c)

print("")
print("============= XOR =============")
print("")
# XOR (^)
c = a ^ b 
binary_c = format(c,'08b') # Konversi nilai c ke dalam bentuk biner
print("Nilai", a, "binary :", binary_a)
print("Nilai", b, "binary :", binary_b)
print("--------------------------- (^)")
print("Nilai", c, "binary :", binary_c)

print("")
print("============= NOT =============")
print("")
# NOT (~)
# Operasi not dibawah hanya akan membalik nilai desimalnya, karena yang di not kan adalah nilai desimalnya
c = ~a
d = ~b 
binary_c = format(c,'08b') # Konversi nilai c ke dalam bentuk biner
binary_d = format(d,'08b') # Konversi nilai c ke dalam bentuk biner
print("Nilai", a, "binary :", binary_a)
print("--------------------------- (~)")
print("Nilai", c, "binary:", binary_c)
print("")
print("Nilai", b, "binary :", binary_b)
print("--------------------------- (~)")
print("Nilai", d, "binary:", binary_d)

print("")
print("=== XOR untuk membalik (NOT pada bit) ===")
print("")
# Jika ingin melakukan operasi pada bit lebih baik melakukan XOR pada nilai bit dengan nilai bit 1023
bit_a = 0b00100010
bit_b = 0b11111111
axorb = bit_a ^ bit_b
print("Nilai", bit_a, "binary :", format(bit_a, '08b'))
print("--------------------------- (^)")
print("Nilai", axorb, "binary:", format(axorb, '08b'))

print("")
print("======== Shifting Right ========")
print("")

# Shifting Right (>>)
b = a >> 2
binary_b = format(b, '08b')
print("Nilai", a, "binary :", binary_a)
print("--------------------------- (>>)")
print("Nilai", b, " binary :", binary_b)

print("")
print("======== Shifting Left ========")
print("")

# Shifting Left (<<)
b = a << 1
binary_b = format(b, '08b')
print("Nilai", a, "binary :", binary_a)
print("--------------------------- (<<)")
print("Nilai", b, " binary :", binary_b)
