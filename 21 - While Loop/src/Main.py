# While Loop pada Python

print("Program sederhana While Loop")

i = 0
akhir = 10

while i < akhir:
    print("Nilai i = ", i)
    i+=1

print("Akhir perulangan 1")

# Pada python tidak terdapat do while loop maka kita bisa mengakalinya dengan menggunakan if pada while loop jika ingin membuat seperti do while
# Dengan do while maka statement akan dijalankan terlebih dahulu kemudian melihat kondisi untuk perulangan berikutnya
print("")
print("="*80)
print("\nProgram While Loop, mengimplementasikan do while loop ke python")
kondisi = True
i = 1


while kondisi:
    print(f"Program dijalankan yang ke-{i}")
    i+=1
    kondisi = int(input("Apakah ingin melanjutkan, masukkan 1 untuk lanjut, 0 untuk berhenti : "))
    #Menambahkan kondisi pemicu
    if not kondisi:
        break # Break berfungsi untuk mengehntikan perulangan, yang dimana perulangan akan berhenti jika kondisi bernilai false

print("Akhir perulangan 2")

