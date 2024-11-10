#MATERI SET

#nambah item di set dari sebuah list
a = {"apel", "jeruk", "ceri", "durian"}
b= { "strawberry", "blueberry"}
a.update(b)
print(a)

#Hapus item paling terakhir di set dengan pop()
a = {"Rokok", "Korek", "Asbak"}
print("Udang" in a)

#Ga ada indeks jadi kalau diprint itu set bakal ngacak
a = {"Rokok", "Korek", "Asbak"}
print(a)


a = {"Rokok", "Korek", "Asbak"}
b= { "motor"}
a.update(b)
print(a)

#Menambahkan 2 buah set dengan union()method
a = {"apel", "jeruk", "ceri", "durian"}
b= { "strawberry", "blueberry", "apel"}
c = a.union(b)
print(c)

#Hanya menampilkan item yang sama aja, dari dua buah set menggunakan metode intersection()
# (harus disimpan dalam set yang baru)
a = {"apel", "jeruk", "ceri", "durian"}
b= { "strawberry", "blueberry", "apel", "jeruk"}
c = a.intersection(b)
print(c)

#Hanya menampilkan item berbeda dari dua buah set menggunakan metode symmetric_difference_update()
a = {"apel", "jeruk", "ceri", "durian"}
b= { "strawberry", "blueberry", "apel", "jeruk"}
a.symmetric_difference_update(b)
print(a)


#Tipe data Dictionary
#Mengecek berapa jumlah item
kucing = {
    "Nama": "Kuro", 
    "Umur": "3 Tahun",
    "Ras": "persia"}
print(len(kucing))

#Membuat dictionary baru dengan method dict()
buah = dict(nama = "apel", warna = "merah", manis = True)
print(buah)

#akses item di dictionary dengan nama key
kucing = {
    "Nama": "Kuro", 
    "Umur": 3,
    "Ras": "persia"}
print(kucing["Ras"])

#mengambil seluruh values
kucing = {
    "Nama": "Kuro", 
    "Umur": 2,
    "Ras": "persia",
    "jantan": True,
    "hobi": ["makan", "tidur"]}
print(kucing.values())

#update values dari sebuah keys dengan menambahkan key di dictionary
kucing = {
    "Nama": "Kuro", 
    "umur": 2,
    "ras": "persia",
    "jantan": True,
    "hobi": ["makan", "tidur"]}

print(kucing) #print dict sebelum update
kucing["umur"] = 1.5 #update value dari key"umur"
print(kucing) #print dict setelah update
kucing["lucu"] = True #tambah key "lucu" dan value-nya true




#update values dari sebuah keys dan menambahkan item dengan menggunakan method update()
kucing = {
    "nama": "Kuro", 
    "umur": 2,
    "ras": "persia",
    "jantan": True,
    "hobi": ["makan", "tidur"]}
kucing.update({"umur": 1.5})
print(kucing)
kucing.update({"warna": ["putih", "hitam", ], "nama": "miko"})
print(kucing)

#mengubah item pada dictionary menjadi sebuah tuple dalam list menggunakan method items()dan mengecek apakah terdapat suatu key dalam dictionary
kucing = {
    "nama": "Kuro", 
    "umur": 2,
    "ras": "persia",
    "jantan": True,
    "hobi": ["makan", "tidur"]}
x = kucing.items()
print(x)

