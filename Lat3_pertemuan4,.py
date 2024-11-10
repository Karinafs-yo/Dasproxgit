#Karina Fauzia Setiadi 2402838 RPL 1A

#Dictionary yang berisi student_info
student_info = {
    "Karina": {"age": 20, "major": "Computer Science"},
    "una": {"age": 21, "major": "Mathematics"},
    "dwi": {"age": 19, "major": "physics"},
}
(student_info)
#variabel yang menampung user dan perintah menginputkan nama siswa
nama = input("Inputkan nama siswa: ")
#Sinkronkan antara variable nama ke variable data_nama  yang memuat dictionary dengan fungsi get()
data_nama =student_info.get(nama)
#perintah print untuk menghasilkan output
print(f"Umur {nama} adalah {data_nama["age"]} dan Prodinya adalah {data_nama["major"]}")

info_Siswa = {
    1: {"nama": "Karina", "ipk": 36.0},
    2: {"nama": "Rifdah", "ipk": 36},
    3: {"nama": "gugun", "ipk": 34.0},
}
(info_Siswa)

absen = (float(input("Masukan nomor absen : ")))
data_absen = info_Siswa.get(absen)

print(f"No absen {absen} adalah {data_absen["nama"]} dengan ipk {data_absen["ipk"]}")