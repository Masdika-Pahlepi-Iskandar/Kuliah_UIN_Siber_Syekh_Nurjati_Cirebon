# 1. List Comprehensions
nilai = [75, 85, 60, 95, 70]

lulus = [n for n in nilai if n >= 80]

print(lulus)


# 2. Array 2 Dimensi
data = [
    [10, 20],
    [45, 50]
]

print(data[1][0])


# 3. List Multidimensi
data = [
    [
        ["Buku", "Pensil"],
        ["Penghapus", "Pensil Warna"]
    ]
]

print(data[0][1][1])


# 4. Fungsi Berparameter
def hitung_total(harga, jumlah):
    return harga * jumlah

print(hitung_total(7000, 2))

# 5. Kuis 1
hasil = [x * 3 for x in range(1, 11) if x % 2 == 0]
print(hasil)

# 6. Kuis 2
array = [[j + i*3 for j in range(1, 4)] for i in range(3)]
for baris in array:
    print(baris)

# 7. Kuis 3
data =[[2,4], [6,8], [10,12]]
hasil = [angka for baris in data for angka in baris]
print(hasil)

# 8. Slice 4
def hitung_luas(panjang, lebar):
    return panjang * lebar

print(hitung_luas(10, 6))