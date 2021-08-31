"""
Operasi Aritmatika pada Python
1. Penjumlahan > +
2. Pengurangan > -
3. Perkalian   > *
4. Pembagian   > /
5. Modulus     > %
6. Eksponen/pangkat > **
7. Floor Division/Pembagian yang dibulatkan ke bawah > // 
"""

print("\n=== Program Operasi Aritmatika sederhana ===")
a = int(input("Masukkan nilai a : "))
b = int(input("Masukkan nilai b : "))

# Penjumlahan
hasil = a + b
print(a, '+', b, '=', hasil)

# Pengurangan
hasil = a - b
print(a, '-', b, '=', hasil)

# Perkalian
hasil = a * b
print(a, '*', b, '=', hasil)

# Pembagian
hasil = a / b
print(a, '/', b, '=', hasil)

# Modulus
hasil = a % b
print(a, '%', b, '=', hasil)

# Eksponen
hasil = a ** b
print(a, '^', b, '=', hasil)

# Floor division
hasil = a // b
print(a, '//', b, '=', hasil)

"""
Pada operasi aritmatika terdapat prioritas untuk operasi yang dilakukan terlebih dulu
urutannya adalah

1. ()
2. Eksponen **
3. Perkalan/pembagian/modulus/floor division *, /, %, //
4. Penjumlahan/Pengurangan

"""

# contoh

hasil = a + b / b * a ** b - b % (b // a + (b - a))
print(a, '+', b, '/', b, '*', a, '**', b, '-', b, '%', '(',b, '//', a, '+', '(',a, '-', b,')',')', '=', hasil)

"""
di atas Yang pertama kali dioperasikan adalah yang berada dalam kurung, yaitu a-b, kemudian yang selanjutnya sesuai dengan urutan prioritas operasi 
"""