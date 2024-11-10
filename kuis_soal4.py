#Nabila merupakan seorang pemilik online shop. Ia membutuhkan program yang dapat
# menyimpan seluruh barang jualan di online shop-nya. Pada bulan Juli lalu,
# barang-barang yang dijual oleh online shop Nabila antara lain:
# Kerudung, Kemeja, Rok, Celana Panjang, Baju Renang, Topi, Tas, Sepatu, dan Kacamata
# Mulai bulan ini, online shop tersebut berhenti berjualan Baju Renang dan diganti
# menjadi Piyama. Selain itu, karena banyaknya permintaan pelanggan, kini online
# shop-nya pun memproduksi Ikat Rambut dan Sendal. Program yang Nabila butuhka
# harus dapat menampilkan daftar barang jualan pada bulan Juli berserta jumlah jenis
# barangnya dan daftar barang jualan bulan ini berserta jumlah jenis barangnya. Buatlah
# program yang dapat memenuhi kebutuhan Nabila. (bobot: 15 point)


#Karina fauzia setiadi 2402838 RPL 1A
print ("selamat datang di Toko Online shop Nabila")
print ("Daftar barang dibulan Juli:")
#buat list barang dibulan juli
Juli = ["Kerudung, kemeja, rok, celana panjang, baju renang, topi, tas, sepatu, dan kacamata"]
print(Juli)
#buat daftar barang dibulan agustus dan gunakan code untuk mengganti nama barang dan menambah barang
print ("Daftar barang dibulan Agustus:")
a = ["Kerudung", "kemeja", "rok", "celana panjang", "baju renang", "topi", "tas", "sepatu","kacamata"]
a[4] = "piyama"
a.insert(2,"ikat rambut")
a.insert(3,"sendal")
print(a)



