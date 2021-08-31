# Mengambil user input pada python dan menyimpannya ke dalam sebuah variable
# Data yang tersimpan dalam sebuah variable ini nantinya dapat digunakan untuk jalannya pemrosesan pada program

"""
Pada python cara untuk mengambil input dari user adalah
        variable = input("Teks")

        variable : tempat untuk menyimpan inputan kita
        teks     : sebuah teks yang nantinya akan muncul pada saat kita ingin menginput
"""

print("\n=== Program sederhana mengambil user input ===")
nama = input("Masukkan nama : ")
print("Nama :", nama, ", Tipe data : ", type(nama))

"""
Output dari perintah diatas adalah untuk mengambil input dari user yang nantinya akan di simpan kedalam variable nama
kemudian variable nama ini di print/tampilkan ke layar beserta dengan tipe datanya
"""

# Pada python setiap input yang kita masukkan mau itu sebuah teks ataupun sebuah angka, tipe datanya akan selalu menjadi String
# Maka dari itu jika kita ingin mengambil input user dalam bentuk int ataupun tipe data lain maka diperlukan casting

angka = int(input("Masukkan angka : "))
print("Angka :", angka, ", Tipe data :", type(angka))

"""
Jika kita menggunakan casting maka inputan yang dalam bentuk string tadi akan menjadi integer
"""

# Berbeda jika kita ingin mengambil input user dalam bentuk boolean maka kita perlu melakukan casting sebanyak 2 kali
# Hal ini dikarenakan jika kita hanya mengcasting string ke boolean, maka apapun nilai/teks yang kita masukkan maka nilainya akan menjadi true

data_bool = bool(int(input("Masukkan 0/1 : ")))
print("Boolean :", data_bool, ", Tipe data :", type(data_bool))