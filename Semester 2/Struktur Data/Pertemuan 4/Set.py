# MATERI: STRUKTUR DATA SET PADA PYTHON

# 1. dengan menggunakan kurung kurawal {}
import sys

kata_set = {"saya", "makan", "nasi"}
print(kata_set)  
print(type(kata_set))
print("ukuran memori:", sys.getsizeof(kata_set))

# 2. dengan menggunakan fungsi set()
kata_lain: set[str] = set(["saya", "makan", "nasi"])
print(kata_lain)
print(type(kata_lain))
print("ukuran memori:", sys.getsizeof(kata_lain))

# membuktikan tidak menganut konsep indeks
# print(kata_lain[0])  # ERROR

# menambahkan anggota set
# 1. add()
kata_set.add("minum")
print(kata_set)

# 2. update()
kata_lain.update(["minum", "teh"])

# menghapus anggota set
# kata_set.remove("makan")
# kata_set.discard("nasi")
# kata_set.pop()

print(kata_set)
print(kata_lain)

# implementasi operasi pada set

# 1. union
angkaA: set[int] = {1, 2, 3}
angkaB: set[int] = {3, 4, 5}

print(angkaA | angkaB)
print(angkaA.union(angkaB))

# 2. intersection
print(angkaA & angkaB)
print(angkaA.intersection(angkaB))

# 3. difference
print(angkaA - angkaB)
print(angkaB.difference(angkaA))

# 4. symmetric difference
print(angkaA ^ angkaB)
print(angkaA.symmetric_difference(angkaB))