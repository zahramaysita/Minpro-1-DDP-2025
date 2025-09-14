print()
print("Nama : Zahra Maysita")
print("NIM : 2509116015")
print("Kelas : Sistem Informasi A")
print("tema : sistem pencatat biaya skincare")
print()

# list produk skincare
skincare = [
    ("Toner", 40000, "01-09-2025"),
    ("Serum", 140000, "05-09-2025"),
    ("Moisturizer", 60000, "12-09-2025"),
    ("Sunscreen", 50000, "20-09-2025"),
    ("Facial Wash", 80000, "25-09-2025")
]

print("💖 Selamat datang di SISTEM PENCATAT BIAYA SKINCARE 💖")
print("Pilih menu seru berikut ini: ")
print("1. Lihat Produk 👀")
print("2. Tambah Produk 💅")
print("3. Update Produk 📝")
print("4. Hapus Produk ❌")
print("5. Total Pengeluaran 💸")
# input menu
pilihan = int(input("👉 Pilih Menu (1-5): "))

# Read
if pilihan == 1:
    print("=== Daftar Skincare Kamu📝 ===")
    print("1", skincare[0])
    print("2", skincare[1])
    print("3", skincare[2])
    print("4", skincare[3])
    print("5", skincare[4])

# Cerate
elif pilihan == 2:
    print("💅 Tambah produk baru, biar wajahmu makin glowing!")
    nama = input("Masukkan nama produk baru: ")
    harga = int(input("Masukkan harga produk: "))
    tanggal = input("Masukkan tanggal beli (dd-mm-yyyy): ")

# Nomor baru ditentukan manual
    nomor_baru = 6
    skincare.append ((nama, harga, tanggal))

    print(f"🎉 Yeay! Produk '{nama}' berhasil ditambahkan di nomor {nomor_baru}!")
    print("Data terbaru: ")
    print("1.", skincare[0])
    print("2.", skincare[1])
    print("3.", skincare[2])
    print("4.", skincare[3])
    print("5.", skincare[4])
    print("6.", skincare[5])

# Update
elif pilihan == 3:
    print("📝 Update produk favoritmu biar makin cantik!: ")
    print("1.", skincare[0])
    print("2.", skincare[1])
    print("3.", skincare[2])
    print("4.", skincare[3])
    print("5.", skincare[4])

    nomor = int(input("Masukkan nomor produk yang mau di ubah: "))
    index = nomor - 1  # karena list mulai dari 0

    # cek apakah nomor valid (1-5)
    if nomor == 1 or nomor == 2 or nomor == 3 or nomor == 4 or nomor == 5:
        nama = input("Masukkan nama baru: ")
        harga = int(input("Masukkan harga baru: "))
        tanggal = input("Masukkan tanggal beli baru: ")
        skincare[index] = (nama, harga, tanggal)

        print(f"🎉woohoo produk '{nama}' berhasil di update!")
        print("data terbaru skincare kamu: ")
        print("1.", skincare[0][0], "-", skincare[0][1], "-", skincare[0][2])
        print("2.", skincare[1][0], "-", skincare[1][1], "-", skincare[1][2])
        print("3.", skincare[2][0], "-", skincare[2][1], "-", skincare[2][2])
        print("4.", skincare[3][0], "-", skincare[3][1], "-", skincare[3][2])
        print("5.", skincare[4][0], "-", skincare[4][1], "-", skincare[4][2])
    else:
        print("😢aduh produk tidak di temukan!")

# Delete
elif pilihan == 4:
    print("❌ hapus produk yang sudah gak kepake lagi: ")
    print("1.", skincare[0])
    print("2.", skincare [1])
    print("3.", skincare [2])
    print("4", skincare [3])
    print("5", skincare [4])

    nomor = int(input("masukkan nomor produk yang mau di hapus: "))
    produk = None

    # Hapus manual sesuai nomor
    if nomor == 1:
        produk = skincare[0]
        del skincare[0]
    elif nomor == 2:
        produk = skincare[1]
        del skincare[1]
    elif nomor == 3:
        produk = skincare[2]
        del skincare[2]
    elif nomor == 4:
        produk = skincare[3]
        del skincare[3]
    elif nomor == 5:
        produk = skincare[4]
        del skincare[4]
    
    if produk != None:
        print(f"✅ Produk '{produk[0]}' sudah dihapus!")
        print("Data terbaru skincare kamu:")

# nomor 1 dihapus
    if nomor == 1:
        print("1.", skincare[0])
        print("2.", skincare[1])
        print("3.", skincare[2])
        print("4.", skincare[3])
# nomor 2 dihapus
    elif nomor == 2:
        print("1.", skincare[0])
        print("2.", skincare[1])
        print("3.", skincare[2])
        print("4.", skincare[3])
# nomor 3 dihapus
    elif nomor == 3:
        print("1.", skincare[0])
        print("2.", skincare[1])
        print("3.", skincare[2])
        print("4.", skincare[3])
# nomor 4 dihapus
    elif nomor == 4:
        print("1.", skincare[0])
        print("2.", skincare[1])
        print("3.", skincare[2])
        print("4.", skincare[3])
# nomor 5 dihapus
    elif nomor == 5:
        print("1.", skincare[0])
        print("2.", skincare[1])
        print("3.", skincare[2])
        print("4.", skincare[3])
    else:
        print("😢 Aduh, datanya gak ada, coba cek lagi ya!")

# total pengeluaran
elif pilihan == 5:
    print("=== Total Pengeluaran Skincare kamu ===")
    print("Toner:", skincare[0][1])
    print("Serum:", skincare[1][1])
    print("Moisturizer:", skincare[2][1])
    print("Sunscreen:", skincare[3][1])
    print("Facial Wash:", skincare[4][1])
    print("--------------------------")
    total = skincare[0][1] + skincare[1][1] + skincare[2][1] + skincare[3][1] + skincare[4][1]
    print("💅 Karena cantik itu investasi... total skincare kamu: Rp", total )
else:
    print("❌ Whopss Pilihan tidak valid! Pilih 1-5 aja ya 😆")
