# Operasi dan Manipulasi String

#1. Menyambung Stirng (Contatenate)
first_name = "Aldo"
last_name = "Firmansyah"

full_name = first_name + " " +last_name
print("Nama lengkap :", full_name)

#2. Menghitung panjang string
panjang = len(full_name)
print("Panjang dari nama lengkap" , panjang)

#3. Operator untuk string

#Mengecek apakah ada komponen char atau string pada string

cek = "Aldo"
cek2 = "Bayu"
status1 = cek in full_name
status2 = cek2 in full_name

print(cek, "ada di di string", full_name, ":", status1)
print(cek2, "ada di di string", full_name, ":", status2)

#Menhecek apakah tidak ada komponen char atau string pada string

cek = "Bayu"
status1 = cek not in full_name
print(cek, "tidak ada di di string", full_name, ":", status1)

#Multiply string
print("wk" * 10)
print(20 * "wk")

#Indexing
index_0 = full_name[0]
print("Indeks-0 Nama lengkap :", index_0)
print("Indeks-2 Nama lengkap :", full_name[2])
print("Indeks-(-3) Nama lengkap :", full_name[-3]) # Akan mengambil dari belakang
print("Indeks-(0:3) :", full_name[0:3]) # Mengambil indeks dari 0 sampai sebelum 3 ( 0 - 2 )
print("Indeks-(0, 2, 4, 6, 8, 10, 12, 14) :", full_name[0:15:2]) # Mengambil indeks dengan increment (dimana pada contoh disamping 2 adalah incrementnya)

# Item yang terkecil
print("Paling kecil :", min(full_name))
# Item yang terbesar
print("Paling besar :", max(full_name))

#Item yang terkecil dan terbesar dihitung berdasarkan ASCII code
ascii_code = ord(" ") # Mengambil nilai dari space
print("ASCII code untuk spasi =", ascii_code)
data  = 121
ascii_code = chr(data) # Mengubah nilai 121 menjadi character berdasarkan ASCII code
print("ASCII code untuk 121 =", ascii_code)

# Operator menggunakan method
full_name = "Naruto uzumaki"
jumlah_u = full_name.count("u") # Menghitung jumlah u pada string full_name
print("Jumlah huruf u pada " + full_name + " = " + str(jumlah_u))