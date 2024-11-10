#Pak Dedi merupakan seorang Kepala Laboratorium Komputer di SMAN 2 Harapan. Dia ingin membuat sebuah menu login yang dapat memberikesempatan user untuk memasukkan password kembali ketika dia salah sebanyak3 kali. Ketika user terus memasukkan password yang salah, maka user tersebutakan keluar dari menu login tersebut. Pak budi juga menambahkan bahwapassword ini harus sudah ada dalam sistem yang di buat, sehingga sistem ituhanya mengecek password saja tanpa memperdulikan username.
#Login dengan 3 kesempatan Admin
#username : Daspro2023
#password : Latihan

username = "Daspro2023"
password = "Latihan"

# Fungsi login
def Masuk():
    print("Selamat datang di menu Login")
    attempts = 3 # Maksimal 3 kesempatan untuk password

    while attempts > 0:
        user_pw = input("Masukkan password: ")
        if user_pw == password:
            print("Login berhasil!")
            return True #Login berhasil
        else:
            attempts -= 1
            print(f"Waduh password yang dimasukkan salah! Tenang kamu masih memiliki {attempts} kesempatan lagi.")
    
    #Kalau gagal 3 kali, keluar dari menu login
    print("Anda telah mencoba 3 kali dengan password yang salah. Sistem akan keluar.")
    return False  # Login gagal

# Menjalankan fungsi login
Masuk()
