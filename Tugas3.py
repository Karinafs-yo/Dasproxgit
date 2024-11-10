#Aira diminta guru Olahraganya untuk menghitung waktu teman-temannya mulai berlari 
# dan selesai berlari. Ia juga diminta untuk menghitung selisih waktu yangdia buat 
# dan menuliskan hasilnya ke dalam format Jam - Menit - Detik. 
# Bantulah Aira untuk menyelesaikan masalah tersebut agar dapat dilakukan dengan cepat.
#Karina Fauzia Setiadi 2402838 RPL 1A

#Fungsi hitung selisih waktu
def hitung_selisih(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai):
    # Menghitung total detik dari waktu mulai dan selesai
    total_detik_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
    total_detik_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai

    #Hitung selisih waktu dalam detik
    selisih_detik = total_detik_selesai - total_detik_mulai

    #Hitung jam, menit, dan detik dari selisih waktu
    jam = selisih_detik // 3600
    mnt = (selisih_detik % 3600) // 60
    dtk = selisih_detik % 60

    return jam, mnt, dtk

#Aira input waktu mulai
jam_mulai = int(input("Input mulai:\nJam: "))
menit_mulai = int(input("Menit: "))
detik_mulai = int(input("Detik: "))

#Aira input waktu selesai
jam_selesai = int(input("Input selesai:\nJam: "))
menit_selesai = int(input("Menit: "))
detik_selesai = int(input("Detik: "))

#Hitung selisih waktu
jam, mnt, dtk = hitung_selisih(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai)

#Tampilkan hasil selisih waktu
print(f"Hitung selisih:\n{jam} jam - {mnt} menit - {dtk} detik")
