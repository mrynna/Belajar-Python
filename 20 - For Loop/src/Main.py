# For Loop pada Python

"""
for kondisi:
    statement/aksi
"""

print("Program for loop sederhana")


print("\n==== Dengan List ====")
# For loop dengan list

ini_list = [0,2,4,6,8,10]
print(f"Dengan List {ini_list}")
for i in ini_list:
    print("Nilai i = ", i)


print("\n==== Dengan String ====")
#For loop dengan String
data_str = "Agung Setiawan"
print(data_str)
for i in data_str:
    print(i)


print("\n==== Dengan Range ====")
# For loop dengan Range
# Pada range nilai akhir adalah nilai sebelum nilai range, misal range(10), maka akan mulai dengan 0, dan diakhiri dengan 9
print("Dengan Range range(10)")
for i in range(10):
    print("Nilai i = ", i)

## Mengganti nilai awal range
# Secara default nilai start index adalah 0, jadi jika tidak memasukkan start index, maka nilainya = 0
print(f"\nDengan range {range(2,10)}")
for i in range(2,10): # 2 adalah start index, dan 10 adalah stop index, yang artinya akan dimulai dari 2 dan diakhiri dengan nilai sebelum 10 yaitu 9
    print("Nilai i = ", i)

## Mengganti step nilai(increment)
print(f"\nDengan range {range(1,10,2)}")
for i in range(1,10,2): # 2 adalah increment, jadi akan dimulai dengan 1, dan diakhiri di angka 9, dengan penambahannya/step nilai adalah 2
    print("Nilai i = ", i)

## range dengan menggunakan decrement
print(f"\nDecrement dengan range {range(10, 0, -2)}")
for i in range(10, 0, -2):
    print("Nilai i = ", i)

print("\n=============")

# Mengimplementasikan for loop dari style bahasa lain
"""
int nilai_awal = 0;
int nilai_akhir = 20;
for(nilai_awal, nilai_awal < nilai_akhir, nilai_awal+=2){
    print(nilai_awal);
}
"""

nilai_awal = 0
nilai_akhir = 20

for i in range(nilai_awal, nilai_akhir, 2): # nilai_awal dan nilai_akhir disini hanya berperan sebagai parameter dari range
    print(i)