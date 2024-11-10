class PenyebranganSungai:
    def __init__(self):
        # Keadaan awal
        self.keadaanawal = {'P1', 'I1', 'P2', 'I2', 'P3', 'I3'}
        self.keadaanakhir = set()
        self.perahu = []

    def siapa_dapat_mendayung(self):
        # Menjelaskan bahwa siapapun dapat mendayung perahu
        print("Siapapun dapat mendayung perahu, baik suami maupun istri.")

    def selamat(self):
        # Memeriksa apakah keadaan aman di sisi sungai
        # Cek untuk setiap istri jika mereka bersama pria lain tanpa suami
        if ('I1' in self.keadaanawal and ('P2' in self.keadaanawal or 'P3' in self.keadaanawal) and 'P1' not in self.keadaanawal):
            return False  # I1 tidak boleh bersama P2 atau P3 tanpa P1
        if ('I2' in self.keadaanawal and ('P1' in self.keadaanawal or 'P3' in self.keadaanawal) and 'P2' not in self.keadaanawal):
            return False  # I2 tidak boleh bersama P1 atau P3 tanpa P2
        if ('I3' in self.keadaanawal and ('P1' in self.keadaanawal or 'P2' in self.keadaanawal) and 'P3' not in self.keadaanawal):
            return False  # I3 tidak boleh bersama P1 atau P2 tanpa P3
        
        return True
    
    def pindah(self, orang1, orang2=None):
        # Memindahkan orang ke sisi lain
        if orang2:
            self.perahu = [orang1, orang2]
        else:
            self.perahu = [orang1]
        
        # Memindahkan orang dari sisi yang ada ke sisi seberang
        for orang in self.perahu:
            self.keadaanawal.discard(orang)
            self.keadaanakhir.add(orang)

        # Memeriksa keamanan setelah berpindah
        if not self.selamat():
            # Mengembalikan orang jika tidak aman
            for orang in self.perahu:
                self.keadaanakhir.discard(orang)
                self.keadaanawal.add(orang)
            print(f"Memindahkan {self.perahu} tidak aman, kembali.")
        else:
            print(f"Memindahkan {self.perahu} ke sisi yang lain.")

        self.perahu = []

    def semua_sudah_menyebrang(self):
        # Memeriksa apakah semua pasangan sudah di sisi akhir
        semua_orang = {'P1', 'I1', 'P2', 'I2', 'P3', 'I3'}
        if semua_orang.issubset(self.keadaanakhir):
            print("Semua pasangan sudah menyebrang!")
            return True
        return False

    def menyebrangisungai(self):
        # Panggil fungsi untuk menjelaskan siapa yang dapat mendayung
        self.siapa_dapat_mendayung()
        
        # Algoritma untuk menyeberangkan semua orang
        langkah = [
            ('P1', 'I1'),  # Pindah P1 dan I1
            ('P1',),       # Kembalikan P1
            ('P2', 'I2'),  # Pindah P2 dan I2
            ('P2',),       # Kembalikan P2
            ('P3', 'I3'),  # Pindah P3 dan I3
            ('P1',),       # Kembalikan P1
            ('I1', 'I2'),  # Pindah I1 dan I2
            ('I1',),       # Kembalikan I1
            ('I2', 'I3'),  # Pindah I2 dan I3
            ('I2',)        # Kembalikan I2
        ]
        
        for pindah in langkah:
            if len(pindah) == 2:
                self.pindah(pindah[0], pindah[1])  # Pindah dua orang
            else:
                self.pindah(pindah[0])  # Pindah satu orang

        # Memanggil metode untuk memeriksa apakah semua sudah menyeberang
        self.semua_sudah_menyebrang()

# Menjalankan simulasi
crossing = PenyebranganSungai()
crossing.menyebrangisungai()
