print("1. Indexing list\n")
angka = [10, 20, 30, 40, 50]
print(angka[0])
print(angka[2])
print("\n")

print("2. Mengakses isi list\n")
data = [1, 2, 3, 4]
for i in data:
    print(i)
print("\n")

print("3. Fungsi len()\n")
data = [1, 2, 3, 4, 5]
panjang = len(data)
print(panjang)
print("\n")

print("4. Menghapus elemen dari list\n")
data = [10, 20, 30, 40]
del data[1]
print(data)
print("\n")

print("5. Negative index\n")
data = [10, 20, 30, 40]
print(data[-1])
print(data[-2])
print("\n")

print("6. Kuis 19 (method)\n")
topi_list = [1, 2, 3,4,5]
print(topi_list)
print("\n")

print("7. Contoh 1 append() dan insert()\n")
data = [1, 2, 3]
data.append(4)
data.insert(1, 10)
print(data)
print("\n")

print("8. Contoh 2 (list kosong + append)\n")
data = []
data.append(1)
data.append(2)
print(data)
print("\n")

print("9. Contoh 2 (perulangan)\n")
data = []
for i in range(5):
    data.append(i)
print(data)
print("\n")

print("10. Menggunakan list (penjumlahan)\n")
data = [1, 2, 3]
total = 0
for i in data:
    total += i
print(total)
print("\n")

print("11. Menggunakan list (tukar nilai)\n")
a = 1
b = 2
a, b = b, a
print(a, b)
print("\n")

print("12. List in action 2\n")
my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
    print(my_list[i])
print("\n")

print ("13 kuis 20\n")
exo = ["Suho", "Xiumin", "Lay", "Baekhyun", "Chen", "Chanyeol", "D.O", "Kai", "Sehun"]
print("langkah 1:",exo)
print("langkah 2:",exo)
print("langkah 3:",exo)
print("langkah 4:",exo)
print("langkah 5:",exo)
print("Jumlah anggota exo", len(exo))