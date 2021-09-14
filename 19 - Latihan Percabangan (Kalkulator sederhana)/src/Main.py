print("Program kalkulator sederhana")
angka1 = float(input("Masukkan angka pertama : "))
operasi = str(input("Masukkan operasi ( + , - , x , : , % ): "))
angka2 = float(input("Masukkan angka kedua : "))

if operasi == '+': print(f"{angka1} {operasi} {angka2} = {angka1 + angka2}")
elif operasi == '-': print(f"{angka1} {operasi} {angka2} = {angka1 - angka2}")
elif operasi == 'x': print(f"{angka1} {operasi} {angka2} = {angka1 * angka2}")
elif operasi == ':': print(f"{angka1} {operasi} {angka2} = {angka1 / angka2}")
elif operasi == '%': print(f"{angka1} {operasi} {angka2} = {angka1 % angka2}")
else: print("Anda salah memasukkan operasi")

print("\nAkhir dari program")