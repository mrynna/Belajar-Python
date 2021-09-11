from tkinter import *

import counter

root = Tk()

def konfirmasi1():
    tanggal = int(entry1.get())
    bulan = int(entry2.get())
    tahun = int(entry3.get())
    hari = Label(root, text=f"Anda lahir dihari {counter.hari(tahun, bulan, tanggal)}").grid(row=5, columnspan=2, padx=10)
    tgl = Label(root, text=f"Umur anda sekarang {counter.tgl(tahun, bulan, tanggal)}").grid(row=6, columnspan=2, ipadx=10)

menu_label = Label(root, text="Masukkan Data")
menu_label.grid(row=0, column=0, columnspan=2, padx=5, pady=15)

label1 = Label(root, text="Tanggal").grid(row=1, column=0, sticky='e', padx = 10)
entry1 = Entry(root, width=10)
entry1.grid(row=1, column=1, padx = 10, sticky='w')
label2 = Label(root, text="Bulan").grid(row=2, column=0, sticky='e', padx = 10)
entry2 = Entry(root, width=10)
entry2.grid(row=2, column=1, padx = 10, sticky='w')
label3 = Label(root, text="Tahun").grid(row=3, column=0, sticky='e', padx = 10)
entry3 = Entry(root, width=10)
entry3.grid(row=3, column=1, padx = 10, sticky='w')
getButton = Button(root, text="Konfirmasi", command=konfirmasi1).grid(column = 0, row=4, padx=15, pady=15, columnspan=2)

root.title("Penghitung Usia")
root.mainloop()
