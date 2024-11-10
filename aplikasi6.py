#Karina Fauzia Setiadi_2402838_RPL1A
a = float(input("Masukkan nilai N : "))

def is_prima (x):
    for i in range(2, x):
        if x %  i == 0:
            return False
        return True
