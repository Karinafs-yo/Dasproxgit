#Pak Rendi meneliti seberapa lama sebuah mobil balap dapat menyelesaikan 1 putaran.
# Mobil balap itu, ternyata mampu melaju cepat sehingga dapat menyelesaikan 1 putaran
# hanya dalam waktu 13 menit 37 detik. Buatlah sebuah program untuk membantu Pak
# Rendi agar waktu yang didapat tersebut dapat dikonversi satuannya menjadi detik saat
# ditampilkan.#


#Karina Fauzia Setiadi 2402838 RPL1A
#inputkan dulu laju pak radit berlari
menit =float(input('Input berapa menit pak Rendi berlari:'))
detik = float(input('Input berapa detik pak Rendi berlari:'))
#ubah menit jadi detik dan ditambah dengan detik yang tadi diinputkan
konversi = (menit * 60) + 37
#print hasil akhir dari proses hitung konversi
print('laju lari pak radit yang sudah dikonversi dalam bentuk detik adalah =',(konversi),"detik")


