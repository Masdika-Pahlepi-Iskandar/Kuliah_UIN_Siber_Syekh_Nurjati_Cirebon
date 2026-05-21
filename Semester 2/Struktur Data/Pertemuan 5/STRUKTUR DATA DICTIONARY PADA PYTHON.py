# MATERI: STRUKTUR DATA DICTIONARY PADA PYTHON

# membuat struktur data dictionary
user_login: dict[str, int | str] = {
    "name": "alfa", 
    "age": 21, 
    "role": "admin"
}
print(type(user_login))

# mengakses data dalam dictionary
print(f"Nama Akun : {user_login['name']}")
print(f"Usia Akun : {user_login['age']}")
print("Peran Akun : %s" % user_login['role'])

print(user_login)

# menambahkan data baru ke dalam dictionary
user_login["email"] = "contoh@email.com"
print(user_login)

# update data dalam dictionary
user_login["role"] = "sales"
print(user_login)

# hapus data dalam dictionary
del user_login["role"]
print(user_login)

# menghapus seluruh data dalam dictionary
# user_login.clear()
# print(user_login)

# dictionary bersarang
tabel_login: dict[str, dict[str, int | str]] = {
    "user1": {
        "name": "alfa",
        "age": 21,
        "role": "admin"
    },
    "user2": {
        "name": "beta",
        "age": 22,
        "role": "sales"
    },
    "user3": {
        "name": "gamma",
        "age": 23,
        "role": "marketing"
    }
}
print(tabel_login)