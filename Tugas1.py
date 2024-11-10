#Buat Deret Fibonacci dengan menggunakan fungsi sebanyak N dari user input
#Karina Fauzia Setiadi 2402838

def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for i in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
n = int(input("Masukkan jumlah angka Fibonacci yang kamu mau: "))
fib_result = fibonacci(n)
print("Deret Fibonacci:", fib_result)
