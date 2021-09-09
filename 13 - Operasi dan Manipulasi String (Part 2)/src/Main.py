# Operasi dan Manipulasi String (Part 2)
# Dengan menggunakan method > module builtin python

## Merubah case dari string

# Merubah String ke UpperCase
Nama = "Agus sudarsono"
print(Nama)
Nama = Nama.upper()
print(Nama)

# Merubah ke lowerCase
Nama = Nama.lower()
print(Nama)

# Merubah ke huruf besar setiap awal huruf kata
Nama = Nama.title()
print(Nama)

## Pengecekan pada string menggunakan isX method

"""
    islower > Pengecekan apakah komponen string dalam bentuk lowercase semua
    isupper > Pengecekan apakah komponen string dalam bentuk uppercase semua
    istitle > Pengecekan apakah komponen string setiap kata diawali huruf besar semua
    isalpha > huruf saja
    isdecimal > angka saja
    isalnum > Huruf dan angka
    isspace > spasi, tab, new line

    Hasil dari pengecekan bernilai boolean

"""

# istitle
cek = Nama.istitle()
print("String " + Nama + " Dalam bentuk title : " + str(cek))

## Mengecek kompnen startswith() endswith() > Untuk mengecek apakah string dimlai atau diakhiri dengan kata yang dimasukkan
# Menghasilkan nilai boolean

cek_start = Nama.startswith('Agus')
print("Apakah " + Nama + " Di awali dengan Agus : " + str(cek_start))

cek_end = "Agus Sudarsono".endswith('Sudarsono')
print("Apakah Agus Sudarsono Di akhiri dengan Sudarsono : " + str(cek_end))

## Penggabungan komponen dengan join() dan split()
# Digunakan di list (kumpulan data string)
# join akan membuat list menjadi sebuah string tunggal dan split akan membuat string tunggal menjadi list

# Join
list1 = ['Agus', 'Sudarsono', 'Anak', 'Keren']
gabunglist = ' '.join(list1)
print(list1)
print(gabunglist)

# Split
contoh = "Agus sudarsono nak keren"
pisah = contoh.split(' ') # Yang berada dalam tanda kutip method adalah sebagai pemisah, jadi setiap karakter spasi yang ada pada string akan menjadi pemisah
print("Sebelum di pisah ", contoh)
print("Setelah dipisah ", pisah) # Pisah di sini adalah sebuah list

# Alokasi karakter dengan rjust(), ljust(), center()

kanan = "kanan".rjust(15) # Apabila tidak memasukkan argumen kedua maka otomatis yang dipilih adalah spasi
print('|' + kanan + '|')

kiri = "kiri".ljust(15, "-")
print('|' + kiri + '|')

tengah = "tengah".center(15, '=') # Menggunakan tanda =
print('|'+ tengah + '|')

# Kebalikan dari atas adalah > strip()
# Maka akan menghapus karakter yang dimasukkan

kanan = kanan.strip() # Apabila tidak memasukkan argumen kedua maka otomatis yang dipilih adalah spasi
print(kanan)

kiri = kiri.strip('-') #Menghilangkan tanda -
print(kiri)

tengah = tengah.strip('=')
print(tengah)