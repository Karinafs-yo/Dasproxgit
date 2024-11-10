#Karina Fauzia Setiadi2402838
jumlah = 0
for i in range(1, 11):  
    jumlah += i
 
print(jumlah) 


#latihan sebelum uts
cnth = 0
for j in range(1,21):
    cnth += j
print(cnth)

jm = 0
for d in range(2, 17):
    jm +=d
print(jm)

# s: store sum of all numbers
s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
    if n < 0:
        break
print("\n")
print("Sum is: ", s)

print(f"\n")
print("Yang mana lebih besar dan kecil? ")
a = int(input("Masukkan nilai a : "))
b = int(input("Masukkan nilai b : "))
c = int(input("Masukkan nilai c : "))

if a > b and a > c:
    print("Nilai A lebih besar")
elif b > a and b > c:
    print("Nilai B lebih besar")
elif c > a and c > b:
    print("Nilai C lebih besar")
elif a == b and a ==c:
    print("Nilai yang dimasukkan sama")
else:
    print("Masukkan nilai yang benar")




