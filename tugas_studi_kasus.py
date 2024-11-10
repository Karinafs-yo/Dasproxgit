#Karina Fauzia Setiadi 2402838


#SOAL NOMOR 1
#program untuk mengambil list ke 2-5
a = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
print(a[1:5])

#prograam hapus item "apel" yang kedua
a = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
a.pop(4)
print(a)

#Ganti item dengan nama “ceri” menjadi “cherry”
a = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
a[2] = "cherry"

print(a)

#Tambahkan item dengan nama “strawberry” ke dalam index ke-3
a = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
a.insert(2, "strawberry")
print(a)

#Urutkan item pada list sesuai dengan abjadnya
a = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
a.sort()
print(a)



#SOAL NOMOR 2
#Buatlah program untuk mengambil tuple ke 2-5
a = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
print(a[2:5])

#Manipulasi tuple buah agar item “durian” dapat dihapus
a = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
x = list (a) #mengubah tuple a menjadi list  x
x.pop(3) #menghapus item dilist index[3]
a = tuple(x) #mengubah list x menjadi tuple a

print(a)

#Manipulasi tuple buah agar ada tambahan item “manggis” diantara item “jeruk” dan “ceri”
a = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
x = list (a) #mengubah tuple a menjadi list  x
x.insert(2, "manggis") #menambah manggis diantara item "jeruk" dan "ceri"
a = tuple(x) #mengubah list x menjadi tuple a

print(a)


x = [1, 2, 3, 4] 
x[2] = 10 
print(x)

a = {"Rokok", "Korek", "Asbak"}
print("Rokok" in a)

a = {"Rokok", "Korek", "Asbak"}
print(a)
