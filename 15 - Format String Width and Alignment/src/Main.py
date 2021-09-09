print("")

# Data
nama = "Agus Arianto"
kelas = "2B"
nim = 423212342
ttl = "20 Oktober 2000"

# String
data_mahasiswa = f"Nama : {nama}, kelas : {kelas}, NIM : {nim}, tempat/tgl lahir : {ttl}"
print(data_mahasiswa)

# Memberi baris baru dengan new line \n
data_mahasiswa = f"\nNama : {nama}\nkelas : {kelas}\nNIM : {nim}\ntempat/tgl lahir : {ttl}"
print(data_mahasiswa)

# Multiline string dengan kutip triplet
data_mahasiswa = f"""
Nama : {nama}
kelas : {kelas}
NIM : {nim}
tempat/tgl lahir : {ttl}
"""
print(data_mahasiswa)

# Mengatur lebar (width)
# Memberi width jarak sejauh yang diinginkan, jumlah termasuk dengan jumlah komponen pada string
# Misal memberi jarak 20, maka 20 dikurang dengan jumlah komponen pada string , hasilnya itulah yang akan menjadi lebar width
data_mahasiswa = f"""
Nama             : {nama:>20}
kelas            : {kelas:>10}
NIM              : {nim:>10}
tempat/tgl lahir : {ttl:>10}
"""
print(data_mahasiswa)