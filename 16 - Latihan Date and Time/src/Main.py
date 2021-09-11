# Date and Time
# Date time adalah package builtin python
import datetime as dt
from os import system

system('cls')
print("Program sederhana pendeteksi hari lahir")
print("Masukkan tanggal, bulan dan tahun lahir")

tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan : "))
tahun = int(input("Tahun : "))

tgl = dt.date(tahun, bulan, tanggal)

if dt.date.weekday(tgl) == 0:
    hari = 'Senin'
elif dt.date.weekday(tgl) == 1:
    hari = 'Selasa'
elif dt.date.weekday(tgl) == 2:
    hari = 'Rabu'
elif dt.date.weekday(tgl) == 3:
    hari = 'Kamis'
elif dt.date.weekday(tgl) == 4:
    hari = "Jum'at"
elif dt.date.weekday(tgl) == 5:
    hari = 'Sabtu'
else:
    hari = 'Minggu'

system('cls')

print("Tanggal lahir anda :", tgl)
print(f"Anda lahir pada hari {hari}")

hari_ini = dt.date.today()
umur = (hari_ini - tgl) // 365
bulan_sisa = (((hari_ini-tgl).days)%365) // 30

print(f"Hari ini anda berumur {umur.days} tahun {bulan_sisa} bulan")
print('')
