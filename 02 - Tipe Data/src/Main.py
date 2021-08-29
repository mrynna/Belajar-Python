# Tipe data pada Python
# Tipe data adalah jenis data yang digunakan data. Misalnya bilangan bulat menggunakan tipe data integer
# Pada python tipe data langsung ditentukan berdasarkan datanya, berbeda pada bahasa pemrograman sejenis c, c++, 
# ataupun java yang menggunakan deklarasi.
# Misalnya jika kita membuat variabel "var = 2" , maka secara otomatis tipe datanya ditentukan berdasarkan datanya 
# dimana datanya yaitu berupa bilangan bulat sehingga tipe datanya adalah integer

# Data Integer (bilangan bulat)
data_integer = 10 
print("data : ", data_integer, " tipe datanya adalah ", type(data_integer))

# Data Float (bilangan pecahan/koma)
data_float = 2.5
print("data : ", data_float, " tipe datanya adalah ", type(data_float))

# Data String (Kumpulan karakter)
data_string = "tutorial"
print("data : ", data_string, " tipe datanya adalah ", type(data_string))

# Data Boolean (True/False)
data_bool = True
print("data : ", data_bool, " tipe datanya adalah ", type(data_bool))

# Data bilangan kompleks
data_kompleks = complex(4, 5)
print("data : ", data_kompleks, " tipe datanya adalah ", type(data_kompleks))

# Pada bahasa Python kita juga bisa mengambil tipe data dari bahasa C
# Caranya adalah dengan mengimport packagenya dengan cara : from ctypes import c_double >> c_double dapat diganti sesuai dengan tipe data yang ingin di import

# Tipe data dari bahasa C

from ctypes import c_long, c_double

data_double = c_double(20.5)
print("data : ", data_double, " tipe datanya adalah ", type(data_double))

data_long = c_long(2000)
print("data : ", data_long, " tipe datanya adalah ", type(data_long))