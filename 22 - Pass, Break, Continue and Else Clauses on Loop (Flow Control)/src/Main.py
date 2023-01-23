# Pass Berfungsi sebagai perintah untuk tidak menjalankan program sehingga python akan melanjutkan mengeksekusi program di bawahnya
for i in range(50):
    if 10 * 5 == i:
        pass  # tidak menjalankan program ini

# Break menghentikan jalannya program
print("="*50)
print("Contoh Break")
kondisi = True
while kondisi:
    kondisi = input("masukkan n untuk menghentikan perulangan : ")
    if kondisi == 'n':
        break  # Jika kondisi bernilai n, maka akan dijalankan break, yang akan mengehntikan perulangan
print("Perulangan berakhir")

# Continue, melangkahi, untuk melanjutkan jalannya program tanpa menjalankan perintah setelah continue, jadi statement akan dilangkahi namun perulangan akan tetap berlanjut
print("="*50)
print("Contoh Continue")
for i in range(20):
    if i % 2 == 0:  # Jika i modulus 2 = 0 maka continue, yang artinya nilai yang ketika dibagi 2 menghasilkan nilai 0, maka akan dilangkahi
        continue
    print("Nilai i = ", i)

# Else Clauses
print("="*50)
print("Contoh Else Clauses")
for i in range(20):
    for n in range(0, i):
        if i % 2 == 0:
            print(f"{i} adalah bilangan genap")
            break
    else:
        print(f"{i} adalah bilangan ganjil")
