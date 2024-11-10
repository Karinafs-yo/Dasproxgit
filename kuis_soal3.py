#Pak Abi berencana untuk membangun rumah sederhana untuk keluarganya. Beliau
# sudah membuat desain rumah yang berbentuk sebagai berikut:
# Buatlah sebuah program untuk dapat menghitung total biaya yang Pak Abi harus
# keluarkan untuk membuat bangunan tersebut dimana biaya untuk pembuatan
# dindingnya yaitu Rp. 580.000/m2
# Tinggi 350cm, lebar 8m, panjang 1000cm
# Untuk menghitung luas permukaan dinding gunakan
# rumus 2 × (Panjang × Tinggi) + 2 × (Lebar × Tinggi) (bobot: 15 point)

#Karina Fauzia Setiadi 2402838 RPL 1A
print('Menghitung total biaya dinding pak Abi')
#ubah cm ke m2
tinggi = 350 * 100
lebar = 8 
#ubah cm ke m2
panjang = 1000 * 100
biaya_perdinding = 580000
#Hitung luas rumah pak Abi
luas = (2 * panjang * tinggi) + (2 * lebar * tinggi) 
print('luas permukaan dinding = ',round(luas))
#hitung total luas rumah dikali dengan biaya perdinding
dana = (biaya_perdinding * luas)
print('Total biaya yang pak abi harus keluarkan adalah =',round(dana),"rupiah")