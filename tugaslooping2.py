#Karina Fauzia Setiadi 2402838
jml = 0
while True:
    try:
        angka = float(input("Masukkan angka : "))
    except ValueError:
        print("Masukan angka yang benar")
        continue
    # Cek untuk angka  negatif
    if angka < 0:
        break
    # Tambahkan angka ke total
    jml += angka

#printjml
print(f"Total jumlah angka yang dimasukkan:", jml)
