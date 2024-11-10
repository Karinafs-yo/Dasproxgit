#Karina Fauzia Setiadi 2402838
for i in range(1, 51):
    #buat nentuin dikelipatan lima harus munculin "pass"
    if i % 6 == 0:
        print("pass")
    else:
        print(i)


for s in range(1, 68):
    if s % 2 == 0:
        print("pass")
    else:
        print(s)


for jm in range(1, 11):
    print(jm)

jm = 0
while jm <= 10:
    jm += 1
    print(jm)

print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")

