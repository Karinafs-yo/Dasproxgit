#Karina fauzia setiadi 2402838

students = {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Mathematics"
}

students.update({"Alice": "Prodi Computer Science", "Bob": "Prodi Mathematics", "Charlie": "Prodi Physics", "David": "Prodi Computer Science", "Eva": "Prodi Mathematics"})
print(students)
value_counts = {value: list(students.values()).count(value)for value in students.values()}
print(value_counts)




print(students.keys())
student_name = input("masukkan nama: ")
if student_name in student_info:
    age = student_info[student_name]["age"]
    major = student_info[student_name]["major"]
    print(f"Umur {student_name} adalah {age} dan prodinya adalah {major}")

student_info["age"]
["major"]

x = student_info.items()
print(x)

if "Alice" in student_info:
    print("Ada key 'age' pada dictionary")
