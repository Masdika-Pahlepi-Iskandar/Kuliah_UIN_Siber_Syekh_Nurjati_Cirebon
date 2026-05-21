                                                            # Membuat tuple

import sys
import streamlit as st
logApps = ("User1 login", "User2 login", "User3 logout")
print(logApps)
print (sys.getsizeof(logApps)) 
#sys gunanya untuk mendapatkan informasi tentang ukuran objek dalam byte, 
#sehingga kita dapat melihat berapa banyak memori yang digunakan oleh tuple logApps.

#getsizeof() adalah fungsi yang digunakan untuk mendapatkan ukuran objek dalam byte,
#dalam hal ini, kita ingin mengetahui berapa banyak memori yang digunakan oleh tuple logApps.

#membuktikan memory tuple lebih kecil daripada list
logappslist = ["User1 login"]
print (logappslist)
print ("Memiliki ukuran list",sys.getsizeof(logappslist))  

# pembuktian bahwa tuple itu imutabel

#1 tambah
#logApps.append("User4 login")  
#2 ubah
#logApps[0] = "User1 logout"  
#3 hapus
#del logApps[1] 

# Pembuktian tuple bisa diakses dengan indeks
print (logapps[0])
print (logapps[1])
print (logapps[-2])

#menduplikat tuple
logappsbackpup = logApps
print ("ini isi backup",logappsbackup)   
print ("ini isi logApps",logApps)
