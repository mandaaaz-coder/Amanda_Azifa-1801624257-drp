from datetime import datetime

print("=========================================")
print("     APLIKASI MANAJEMEN AKTIVITAS        ")
print("=========================================")

# 1. Meminta user memasukkan kegiatan
# .strip().lower() digunakan agar input tidak sensitif huruf besar/kecil & spasi tak sengaja
kegiatan = input("Masukkan kegiatan yang akan dilakukan (sarapan/berangkat kerja): ").strip().lower()

print("-----------------------------------------")

# PERCABANGAN UTAMA
if kegiatan == "sarapan":
    # 1a. Logika jika memilih Sarapan
    menu = input("Menu sarapan apa yang kamu inginkan? ").strip().lower()
    
    # Cek ketersediaan bahan di lokasi
    if menu in ["telur", "ikan", "nugget"]:
        print(f"Log: Bahan untuk membuat [{menu.capitalize()}] tersedia di lokasi.")
        print("Hasil: Kamu perlu memasaknya terlebih dahulu ya!")
    else:
        print(f"Log: Bahan untuk [{menu.capitalize()}] tidak tersedia di rumah.")
        print("Hasil: Kamu harus pergi membeli bahannya terlebih dahulu.")

elif kegiatan == "berangkat kerja":
    # 1b. Logika jika memilih Berangkat Kerja
    waktu_sekarang = datetime.now()
    
    # Mengambil jam dan menit dari komputer saat ini
    jam = waktu_sekarang.hour
    menit = waktu_sekarang.minute
    
    print(f"Waktu komputer saat ini: {jam:02d}:{menit:02d}")
    
    # Batas masuk kerja jam 08:00. 
    # Jika jam lebih dari 8, ATAU tepat jam 8 tapi menitnya sudah lewat dari 0, berarti telat.
    if jam > 8 or (jam == 8 and menit > 0):
        print("⚠️ NOTIFIKASI: Kamu SUDAH TERLAMBAT masuk kerja! Buruan berangkat!")
    else:
        print("✅ NOTIFIKASI: Kamu BELUM TERLAMBAT. Masih aman, hati-hati di jalan!")

else:
    # Improvisasi: Menangani jika user memasukkan kegiatan di luar pilihan
    print("Hasil: Kegiatan tidak dikenali. Silakan pilih 'sarapan' atau 'berangkat kerja'.")

print("=========================================")