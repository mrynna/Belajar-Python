# Latihan Komparasi dan Logika

print("")
nilai = int(input("Masukkan nilai lebih kecil dari 5 : "))
nilai2 = int(input("Masukkan nilai lebih besar dari 6 : "))

# Akan bernilai true apabila salah satu nilai yang dimasukkan sesuai 
hasil = (nilai < 5) or (nilai2 > 6)
print("Anda memasukkan salah satu nilai sesuai :", hasil)

# Akan bernilai true apabila kedua nilai yang dimasukkan sesuai
hasil2 = (nilai < 5) and (nilai2 > 6)
print("Anda memasukkan kedua nilai sesuai :", hasil2)

# Akan bernilai true apabila kedua nilai yang dimasukkan tidak sesuai
hasil3 = not ((nilai < 5) or (nilai2 > 6))
print("Anda tidak memasukkan kedua nilai dengan sesuai :", hasil3) 

# 
print("")
nilai = int(input("Masukkan nilai antara rasio 5 dan 12 (Tidak termasuk 5 dan 12) : "))

# Bernilai true apabila nilai yang dimasukkan berada di antara 5 - 12
hasil = nilai > 5 & nilai < 12
print("Anda memasukkan angka yang sesuai :", hasil)

# Quiz sederhana
print("")
print("Jawab nilai yang sesuai")
nomor1 = int(input("2 + 2 = "))
hasil1 = nomor1 == 4
print("Nilai yang anda masukkan :", hasil1)
nomor2 = int(input("5 - 2 = "))
hasil2 = nomor2 == 3
print("Nilai yang anda masukkan :", hasil2)
nomor3 = int(input("5 x 5 = "))
hasil3 = nomor3 == 25
print("Nilai yang anda masukkan :", hasil3)

hasils = hasil1 & hasil2 & hasil3
print("Apakah anda menjawab semua soal dengan benar :", hasils)
