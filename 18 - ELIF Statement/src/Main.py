# Elif statement digunakan untuk membuat cabang yang banyak dari sebuah if statement

print("Program sederhana menggunakan elif statement")
print("Masukkan salah satu nama di bawah ini")
print("""1. Agus
2. Antoni
3. Bagas""")
nama = str(input("Nama = "))

if nama == 'Agus' or nama == 'agus':
    print("\nNama : Agus\nNIM  : 32118021\nTTL  : Malang, 15 Agustus 2000")
elif nama == 'Antoni' or nama == 'antoni' :
    print("\nNama : Antoni\nNIM  : 32118024\nTTL  : Bojonegoro, 20 Maret 1998")
elif nama == 'Bagas' or nama == 'bagas':
    print("\nNama : Bagas\nNIM  : 32118010\nTTL  : Lampung, 12 Maret 1999")
else:
    print("\nNama yang dimasukkan tidak terdaftar")

print("\nAkhir dari program")