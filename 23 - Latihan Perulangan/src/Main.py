# Latihan perulangan
# Membuat segitiga siku-siku

sisi = 5

# Menggunakan for loop
print("for loop")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1
print("")

# menggunakan while
print("while loop")
count = 1
while True:
    print("*"*count) # memprint * pada console yang setiap perulangan dikalikan dengan nilai count
    count += 1 # nilai count ditambahkan setiap perulangan
    if count > sisi:
        break # break ketika nilai count lebih dari nilai sisi
print("")

# membuat segitiga mirror
print("mirror")
count = 1
spasi = 4
while True:
    print(" "*spasi, "*"*count)
    spasi -= 1
    count += 1
    if count > sisi:
        break 

print("")

# membuat segitiga terbalik
print("Segitiga terbalik")
count = 5
spasi = 1
while True:
    print("*"*count, " "*spasi)
    spasi += 1
    count -= 1
    if spasi > sisi:
        break

print(" ")

# terbalik mirror
print("terbalik mirror")
count = 5
spasi = 0
while True:
    print(" "*spasi, "*"*count)
    count -= 1
    spasi += 1
    if spasi > sisi:
        break
print(" ")

# segitiga sama sisi
print("segitiga sama sisi")
sisi = 9
count = 1
spasi = int(sisi/2)
while True:
    if (count % 2):
        print(" "*spasi, "*"*count)
        count += 1
        spasi -= 1
    else:
        count += 1
        continue

    if count > sisi:
        break
print(" ")
