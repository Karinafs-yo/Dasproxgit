#bernilai true 1
#bakal diprint kalau perintahnya benar. kalau salah ga akan diprint
x = 1
if (x > 0):
    print("Eksekusi perintah ini")

#ada kondisi and coba perhatikan.
x = 3
if (x > 0 and x < 5): #x lebih dari 3 dan x kurang dari 5. Kondisi and itu selalu true jadi kalau bener pasti diprint
    print("Nilai x lebih besar dari 0 dan lebih kecil dari 5")

#KONDISI ELSE
#sesuai dari perintah si if. else itu pilihan lain
x = 3
if (x > 9):
    print("salah")
else:
    print("benar")

#KONDISI TINGKAT, ELIF artinya kondisi bercabang dari benar
umur = 16
if (umur > 18):
    print("Anda boleh membuat SIM")
elif (umur < 17):
    print("Anda belum boleh membuat SIM")

#contoh2
a = 2
b = 5
if (a > b): #tergantung disini, mempengaruhi ngeprint yang mana
    print("nilai a lebih besar dari b")
elif (a < b):
    print("nilai a lebih kecil dari b")
else:
    print("nilai a sama dengan b")

#contoh3 kombinasi
nilai = 80
absen = 70

#nested if


#Kondisi PASS STATEMENT
a = 5