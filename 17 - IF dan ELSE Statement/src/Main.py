# If dan Else statement digunakan untuk mengatur alur dari sebuah program

print("Program sederhana If dan Else statement")
soal = int(input("\nHasil dari 10 x 10 = "))

if soal == 100:
    print("Jawaban yang anda masukkan benar !")
else:
    print("Jawaban yang anda masukkan salah !")

print("\nAkhir dari program")

"""
Jika nilai dari variable soal = 100, maka perintah if yang akan dijalankan yaitu outputny jawaban benar
Jika nilai dari variable soal selain dari 100, maka perintah else yang akan dijalankan yaitu outputnya jawaban salah
Perintah If juga dapat ditulis inline
yaitu if syaratnya nya 1 line dengan statement yang akan dijalankan apabila syaratnya terpenuhi
    if soal == 100 : print("Jawaban yang anda masukkan benar !")
"""