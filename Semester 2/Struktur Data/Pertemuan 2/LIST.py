                            #LIST PERTEMUAN 2 (2/16/2024)

print ("1 List adalah struktur data untuk menyimpan banyak nilai dalam satu variabel")
#buah = ["apel", "jeruk", "mangga", 1,2,3]
print("apel", "jeruk", "mangga", 1,2,3)
print ("\n")


print ("2 MUTABLE (bisa diubah)")
#Penghitungan list dimulai dari 0
angka = [1, 2, 3]
angka[0] = 10
print(angka)
print ("\n")


buah = ["apel", "jeruk", "mangga"]
print ("3 Slicing (mengambil indeks tertentu dalam list)")
print(buah[:1] )  
print(buah[1:3])  
print ("\n")


print ("4 Menambahkan Data ke List di posisi tertentu")
buah.insert(1, "punya Ahmad")
print(buah)
print ("\n")


print ("5 Menambahkan Data ke list di posisi belakang")
buah.append("semangka")
print(buah)
print ("\n")


print ("6 Menghapus Data dari List")
buah.remove("jeruk")    #bisa juga pop
print(buah)
print ("\n")


print ("7 Menghapus Data dari List dengan indeks tertentu")
del buah[0]
print(buah)
print ("\n")


print ("8 Menghapus Data dari List dengan pop")
buah.pop(2)  
print(buah)
print ("\n")


print ("9 Menghitung jumlah data dalam List")
jumlah_buah = len(buah)
print("Jumlah buah:", jumlah_buah)
print ("\n")


print ("10 Mengurutkan List")
buah.sort()
print(buah)
print ("\n")


print ("11 Membalik urutan List")
buah.reverse()
print(buah)
print ("\n")


print ("12 Menggabungkan dua List")
buah_lain = ["pisang", "nanas"]
semua_buah = buah + buah_lain
print(semua_buah)
print ("\n")


print ("13 Menghitung jumlah kemunculan suatu nilai dalam List")
jumlah_apel = semua_buah.count("apel")
print("Jumlah apel:", jumlah_apel)
print ("\n")


print ("14 Mencari indeks suatu nilai dalam List")
indeks_mangga = semua_buah.index("mangga")
print("Indeks mangga:", indeks_mangga)
print ("\n")


print ("15 Mengosongkan List")
semua_buah.clear()
print(semua_buah)
print ("\n")


print ("16 Membuat List dengan tipe data campuran")
campuran = [1, "dua", 3.0, True]
print(campuran)
print ("\n")
