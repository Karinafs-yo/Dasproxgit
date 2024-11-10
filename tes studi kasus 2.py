#Karina Fauzia Setiadi 2402838

#kasus 2 pakai user input nama
print('PROGRAM PREDIKSI COCOK ATAU TIDAK KAMU MENJADI MODEL!')
nama = input('Masukin namamu : ')
umur = int(input('Umur berapa nih? : '))
tinggi_bdn = int(input('Tinggi badanmu berapa? : '))
jenis_kelamin = (input('Apanih jenis kelaminnya? (W/P): '))
iq = int(input('Berapa IQ mu? : '))

lolos = f"selamat, {nama} Kamu lolos dalam kriteria model"
gagal = f"Maaf ya, {nama} Kamu gagal kriteria model"

if (jenis_kelamin == "W" ):
    if (umur >=18 and umur <= 25):
        if(tinggi_bdn >= 170):
            if(iq >= 130):
                print(lolos)
            else:
                print(gagal)
        else:
            print(gagal)
    else:
        print(gagal)
elif (jenis_kelamin == "P"):
    if (umur >=18 and umur <= 25):
        if(tinggi_bdn >= 170):
            if(iq >= 130):
                print(lolos)
            else:
                print(gagal)
        else:
            print(gagal)
    else:
        print(gagal)
else:
    print("Tolong pilih jenis kelamin yang benar")


