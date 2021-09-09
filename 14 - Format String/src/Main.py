# Format String
# Menambahkan f"isi string {}" > Yang berada dalam placeholder (kurung kurawal) adalah variable yang bisa ditambahkan dengan format

# Contoh generic

nama = "Mariana"
format_nama = f"Nama = {nama}"
print(format_nama)

# Boolean
nilai_bool = True
print(f"Boolean = {nilai_bool}")

# angka
angka = 500.5
print(f"Angka = {angka}")

# Bilangan bulat
angka = 50
format_angka = f"Bilangan bulat = {angka:d}" # format harus sesuai dengan tipe data variable, pada kasus ini yaitu integer = d
print(format_angka)

# bilangan orde
angka = 10000
format_ribuan = f"Ribuan = {angka:,}" # Akan memisahkan dengan koma sesuai orde ribuan
print(format_ribuan)

# Bilangan desimal
## Biasa digunakan jika ingin menggunakan beberapa nilai dibelakang koma sesuai keinginan 
angka = 0.65357
format_koma = f"desimal = {angka:.2f}"
print(format_koma)

# Leading Zero
angka = 20000
format_zero = f"Leading zero = {angka:010d}" # Maka jumlah komponen pada angka akan sebanyak 10(termasuk dengan banyaknya komponen angka)
print(format_zero)
# 0 bisa diganti sesuai yang diinginkan(kosongkan jika ingin menggunakan spasi)

# menampilkan tanda mines atau plus
angka_minus = -10.124121
angka_plus = 10
format_minus = f"minus = {angka_minus:-.2f}" # Jika minus bisa ditampilkan tanpa menambahkan minus 
format_plus = f"plus = {angka_plus:+}" # Harus menambahkan + jika ingin menampilakn +
print(format_minus)
print(format_plus)

# Format persen
persen = 0.55
format_persen = f"Persen = {persen:.1%}" # Hanya menampilkan 1 angka di belakang koma
print(format_persen)

# Melakukan operasi aritmatika di dalam placeholder (kurung kurawal)
# Contoh dengan gabungan beberapa metode

harga = 5000
jumlah = 5
discount = 0.44

format_harga = f"|Harga total dengan discount {discount:.0%} = {(harga*jumlah)-(harga*jumlah*discount)}|" # Melakukan operasi aritmatika di dalam place holder

kanan1 = f"Total barang = {jumlah}".rjust(len(format_harga)-1) # Membuat string format dengan menjustify ke kanan sebanyak panjang dari string format_harga
kanan2 = f"Discount {discount:.0%}".rjust(len(format_harga)-1)
kanan = f"Harga per barang Rp.{harga:,}".rjust(len(format_harga)-1)

print(kanan)
print(kanan1)
print(kanan2)
print(format_harga)

# Memformat ke bentuk data lain (binary, octal, hexadecimal)
angka = 100
format_binary = f"Binary = {bin(angka)}"
format_octal = f"Octal = {oct(angka)}"
format_hex = f"Hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)