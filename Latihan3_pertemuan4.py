#Karina Fauzia Setiadi 2402838 RPL 1A

student_info = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "physics"},
}
(student_info)
nama = input("Inputkan nama siswa: ")
data_nama =student_info.get(nama)
print(f"Umur {nama} adalah {data_nama["age"]} dan Prodinya adalah {data_nama["major"]}")
