# List pada Python

# List pada python biasa disebut array pada bahasa pemrograman lain
# Pada python jika ingin menggunakan array maka digunakan library seperti numpy
# Pada Python, list digunakan untuk menampung beberapa data dengan tipe yang berbeda, sedangkan array menampung beberapa data dengan tipe yang sama
# Array pada python dapat melakukan operasi aritmatika lebih efisien dibandingkan dengan list

# Membuat List

# list numbers
data_angka = [1, 5, 3, 1, 6]
print(data_angka)

# list string
data_string = ["rahmat", "Bagus", "Anya"]
print(data_string)

# List boolean
data_bool = [True, False, True, True]
print(data_bool)

# List campuran
data_campuran = [2, "rahmat", True, "Agus", 3, 5, False]
print(data_campuran)

## Cara alternatif membuat list
data_range = range(0,10,2) # range(start, stop, stepper)
print(data_range)
data_range_list = list(data_range) # Membuat list dari variable data_range
print(data_range_list)

# Membuat list dengan for loop, list comprehension
list_for = [i for i in range(1, 10)] # Start nya 1 dan stop pada 10 (artinya 10 tidak termasuk/diproses)
print(list_for)

list_for = [i**2 for i in range(10)] # Kuadratkan i nya. Nilai default dari start pada range yaitu 0
print(list_for)

# List dengan for dan if (kondisi)
list_for = [i for i in range(10) if i%2 == 0] # Membuat list dengan kondisi angka genap saja dari range 0-10
print(list_for)

list_for = [i for i in range(10) if i%2 > 0] # Membuat list dengan kondisi angka ganjil saja dari range 0-10
print(list_for)

list_for = [i for i in range(10) if i != 0 and i != 5 and i != 3] # Menghilangkan bebarapa angka dalam list dari range 0-10
print(list_for)