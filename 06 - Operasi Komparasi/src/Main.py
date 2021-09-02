"""
Operasi Komparasi pada python
operasi yang menghasilkan boolean (True/False)
Komparator
1. ==       is equal, sama dengan
2. !=       is not equal, tidak sama dengan
3. >        greater than, lebih besar dari
4. <        less than, lebih kecil dari
5. >=       greater than equal, lebih besar sama dengan
6. <=       less than equal, lebih kecil sama dengan
7. is       Komparator yang dilakukan pada objek id (==)
8. is not   Komparator yang dilakukan pada objek id (!=)
"""

# == is Equal
a = 1
b = 1
print("\n=== is Equal (==) ===")
print(a, '==', b, '=', a == b)

# != is Equal
a = 1
b = 2
print(a, '==', b, '=', a == b)

# == is not Equal
a = 1
b = 2
print("\n=== is not Equal (!=) ===")
print(a, '!=', b, '=', a != b)

# == is not Equal
a = 1
b = 1
print(a, '!=', b, '=', a != b)

# > Greater than
a = 1
b = 2
print("\n=== Greater than (>) ===")
hasil = a > b
print(a, '>', b, '=', hasil)

# > Greater than
a = 5
b = 1
hasil = a > b
print(a, '>', b, '=', hasil)

# < Less than
a = 1
b = 5
print("\n=== Less than (<) ===")
hasil = a < b
print(a, '<', b, '=', hasil)

# < Less than
a = 4
b = 1
hasil = a < b
print(a, '<', b, '=', hasil)

# >= Greater than equal
a = 5
b = 1
print("\n=== Greater than equal (>=) ===")
hasil = a >= b
print(a, '>=', b, '=', hasil)


# >= Greater than equal
a = 1
b = 1
hasil = a >= b
print(a, '>=', b, '=', hasil)

# >= Less than equal
a = 2
b = 2
print("\n=== Less than equal (<=) ===")
hasil = a <= b
print(a, '<=', b, '=', hasil)

# <= Less than equal
a = 1
b = 4
hasil = a <= b
print(a, '<=', b, '=', hasil)
print("")

# Komparasi dengan menggunakan is pada objek id
x = 5
y = 5
print("=== is (pada objek id) ===")
print("nilai x = ", x, "id =", hex(id(x)))
print("nilai y = ", y, "id =", hex(id(y)))
hasil = x is y
print('x', "is", 'y', '=', hasil)
print("")

x = 2
y = 5
print("nilai x = ", x, "id =", hex(id(x)))
print("nilai y = ", y, "id =", hex(id(y)))
hasil = x is y
print('x', "is", 'y', '=', hasil)
print("")

# Komparasi dengan menggunakan is not pada objek id
x = 5
y = 5
print("=== is not(pada objek id) ===")
print("nilai x = ", x, "id =", hex(id(x)))
print("nilai y = ", y, "id =", hex(id(y)))
hasil = x is not y
print('x', "is not", 'y', '=', hasil)
print("")

x = 3
y = 5
print("nilai x = ", x, "id =", hex(id(x)))
print("nilai y = ", y, "id =", hex(id(y)))
hasil = x is not y
print('x', "is not", 'y', '=', hasil)

