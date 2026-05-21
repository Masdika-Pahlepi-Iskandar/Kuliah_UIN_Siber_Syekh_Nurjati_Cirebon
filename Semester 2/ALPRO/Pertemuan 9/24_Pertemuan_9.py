# 1. Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


data = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(data)
print(data)


# 2. Interactive Bubble Sort
data = []

n = int(input("Jumlah data: "))

for i in range(n):
    angka = int(input("Masukkan angka: "))
    data.append(angka)

for i in range(len(data)):
    swapped = False

    for j in range(len(data) - i - 1):

        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            swapped = True

    if not swapped:
        break

print(data)


# 3. Method Sort
data = [5, 6, 7, 8, 9]

data.sort()

print(data)


# 4. Method Reverse
data = [5, 6, 7, 8, 9]

data.reverse()

print(data)


# 5. The Inner Life of List - 1
list_1 = [1]

list_2 = list_1

list_1[0] = 2

print(list_2)


# 6. Slice – 1 [awal:akhir]
data = [5, 6, 7, 8, 9]

print(data[1:3])


# 7. Slice – 2 [positif:negative]
data = [5, 6, 7, 8, 9]

print(data[1:-1])


# 8. Slice – 3 [negative:positif]
data = [5, 6, 7, 8, 9]

print(data[-1:1])


# 9. Slice – 4 [:akhir]
data = [5, 6, 7, 8, 9]

print(data[:2])


# 10. Slice – 5 [awal:]
data = [5, 6, 7, 8, 9]

print(data[2:])


# 11. Slice – 6 [:]
my_list = [5, 6, 7, 8, 9]

new_list = my_list[:]

print(new_list)


# 12. Menghapus Slice
my_list = [5, 6, 7, 8, 9]

del my_list[1:3]

print(my_list)


# 13. Menghapus Semua Elemen List
my_list = [5, 6, 7]

del my_list[:]

print(my_list)


# 14. Menghapus List
my_list = [1, 2, 3]

del my_list

print(my_list)


# 15. Penggunaan Operator in
data = [11, 12, 13, 14, 15]

print(5 in data)


# 16. Penggunaan Operator not in
data = [11, 12, 13, 14, 15]

print(5 not in data)


# 17. Simple Program dari List – 1
data = [11, 15, 21, 3, 7]

largest = data[0]

for i in range(1, len(data)):

    if data[i] > largest:
        largest = data[i]

print(largest)


# 18. Simple Program dari List – 2
data = [11, 15, 21, 3, 7, 22, 17]

largest = data[0]

for i in data:

    if i > largest:
        largest = i

print(largest)


# 19. Simple Program dari List – 3
data = list(range(11, 21))

to_find = 15

found = False

for i in range(len(data)):

    if data[i] == to_find:
        found = True
        break

if found:
    print("Ditemukan di index", i)

else:
    print("Tidak ditemukan")


# 20. Simple Program dari List – 4
tebakan = [3, 7, 11, 42, 34, 49]
hasil = [5, 9, 11, 42, 3, 49]

benar = 0
angka_benar = []

for angka in tebakan:

    if angka in hasil:
        benar += 1
        angka_benar.append(angka)

print(f"Angka yang benar: {angka_benar}")
print(f"Jumlah tebakan benar: {benar}")


# 21. Simple Program dari List – 5
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

temp = []

for angka in my_list:

    if angka not in temp:
        temp.append(angka)

print(f"List awal : {my_list}")
print(f"List unik : {temp}")