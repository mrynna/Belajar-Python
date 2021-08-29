# Casting pada Python
# Digunakan untuk mengkonversi tipe data satu ke tipe data lain
"""
Cara :
        variable_after = tipe_data(variable_before) 

        variable_after  : variable baru yang digunakan untuk menyimpan data hasil konversi
        tipe_data       : Jenis Tipe data yang diinginkan (int, float, str, bool)
        variable_before : Variable yang ingin dikonversi

contoh :
        data_integer = 10
        data_float = float(data_integer)
"""

# Integer ke tipe data lain
print("\nINTEGER >> TIPE DATA LAIN")
data_int = 5
print("Data : ", data_int, " Bertipe : ", type(data_int))

data_float = float(data_int) # Datanya akan dikonversi dalam bentuk koma
data_str   = str(data_int) # Datanya akan dikonversi dalam bentuk string
data_bool  = bool(data_int) # Akan bernilai false apabila nilainya = 0
print("Hasil konversi : ")
print("Data : ", data_float, " Bertipe : ", type(data_float))
print("Data : ", data_str, " Bertipe : ", type(data_str))
print("Data : ", data_bool, " Bertipe : ", type(data_bool))

# Float ke tipe data lain
print("\nFLOAT >> TIPE DATA LAIN")

data_float = 5.8
print("Data : ", data_float, " Bertipe : ", type(data_float))

data_int   = int(data_float) # Datanya akan menjadi bilangan bulat, dan dibulatkan ke bawah
data_str   = str(data_float) # Datanya akan dikonversi dalam bentuk string
data_bool  = bool(data_float) # Akan bernilai false apabila nilainya = 0
print("Hasil konversi : ")
print("Data : ", data_int, " Bertipe : ", type(data_int))
print("Data : ", data_str, " Bertipe : ", type(data_str))
print("Data : ", data_bool, " Bertipe : ", type(data_bool))

# String ke tipe data lain
print("\nSTRING >> TIPE DATA LAIN")

data_str = "12"
print("Data : ", data_str, " Bertipe : ", type(data_str))

data_int   = int(data_str) # Data yang dikonversi harus berupa angka dan dalam bentuk bilangan bulat
data_float = float(data_str) # Data yang dikonversi harus berupa angka
data_bool  = bool(data_str) # Akan bernilai false apabila data string kosong
print("Hasil konversi : ")
print("Data : ", data_int, " Bertipe : ", type(data_int))
print("Data : ", data_float, " Bertipe : ", type(data_float))
print("Data : ", data_bool, " Bertipe : ", type(data_bool))

# Boolean ke tipe data lain
print("\nBOOLEAN >> TIPE DATA LAIN")

data_bool = True
print("Data : ", data_bool, " Bertipe : ", type(data_bool))

data_int   = int(data_bool) # Akan diubah kedalam bentuk angka
data_float = float(data_bool) # Akan diubah kedalam bentuk angka
data_str  = str(data_bool) 
print("Hasil konversi : ")
print("Data : ", data_int, " Bertipe : ", type(data_int))
print("Data : ", data_float, " Bertipe : ", type(data_float))
print("Data : ", data_str, " Bertipe : ", type(data_str))

