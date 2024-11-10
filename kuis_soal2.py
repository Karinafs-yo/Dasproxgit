#Bu Rinda merasa badannya kurang fit dan berencana untuk berenang sore ini. Beliau
# memiliki kolam renang yang akan digunakannya nanti dengan dengan ukuran panjang
# 10 meter, lebar 15 meter, dan memiliki kedalaman 200 centimeter. Buatlah sebuah
# program untuk menghitung volume maksimal air yang bisa diisi pada kolam renang
# milik Bu Rinda dalam satuan meter kubik. Gunakan rumus menghitung volume balok.


#Karina Fauzia Setiadi 2402838 RPL 1A
print(f"Yuk kita hitung berapa volume maksimal air yang bisa diisi pada kolam renang milik Bu Rinda \n")
#masukan ukuran kolam renang
panjang = float(input("Input panjang berapa meter: "))
lebar = float(input('Input lebar berapa meter: '))
kedalaman = float(input('Input kedalaman berapa centimeter: '))
kedalamanubah = (kedalaman/100)
#hitung rumus volume balok kemudian ubah jadi satuan meterkubik
luas = (panjang * lebar * kedalamanubah * 1000)
#print hasil akhir
print('Volume maksimal air yang bia diisi pada kolam =',(luas), "meter kubik")