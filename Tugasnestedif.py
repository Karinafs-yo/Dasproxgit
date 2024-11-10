#Karina Fauzia Setiadi 2402838

#buat ngitung kalau nilai inputnya positif
x = int(input("Masukin nilai : "))
if (x > 0 ):
    print("Angka adalah bilangan positif")
    if (x % 2 == 0):
        print("dan termasuk bilangan genap")
    else:
        print("x bilangan ganjil")
#buat ngitung kalau nilai inputnya negatif
elif (x < 0):
    print("Angka adalah bilangan negatif")
    if (x % 2 == 0):
        print("dan termasuk bilangan genap")
    else:
        print("dan termasuk ganjil")
