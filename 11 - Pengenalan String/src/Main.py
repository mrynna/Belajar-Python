# String adalah kumpulan dari karakter
print('')

# Membuat string
data = "Ini adalah data string"
print(data, "|| tipe :", type(data))

"""
    1. Menggunakan single quote '...'
    2. Menggunakan double quote "..."
"""

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

# Contoh menggunakan kutip satu untuk membuat sebuah percakapan
print('"Halo apa kabar"')
print('"Halo baik, namaku makmur"')
print("Hari ini hari jum'at")

# Menggunakan tanda \

print('Hari ini hari jum\'at') # menggunakan tanda \ untuk menampilkan simbol '
print('It looks beutiful isn\'t it')
print("")
# Jika ingin menggunakan simbol backslash \ gunakan dua simbol \
print("Folder nya ada di C:\\User\\Computer")

# tab \t
print("Dia\tmengagumkan")

#backspace
print("dia\b menggunakan backspace")

#newline
print("Baris satu\nbaris dua") # LF -> Line feed (unix, linux, macos)
print("Baris satu\rBaris dua") # CR -> Carriage Return (commodore, acorn, lisp)
print("Baris satu\r\nBaris dua") #CRLF -> Line Feed Carriage Return (Windows)

#String Literal atau raw

print(r'C:User\new folder\file')

# Multiline literal string

print("""
Nama  : Ayon
Kelas : 3B - Listrik
NIM   : 343253124
""")

# Multiline literal string dan raw

print(r"""
Nama   : Ayon
Kela\s : 3B - \Listrik
NIM    : \343253124
""")
