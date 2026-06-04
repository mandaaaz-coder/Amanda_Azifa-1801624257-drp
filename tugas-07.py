# Layout papan catur 8x8

for baris in range(8):
    for kolom in range(8):
        if (baris + kolom) % 2 == 0:
            print("⬜", end=" ")
        else:
            print("⬛", end=" ")
    print()

    # List kosong untuk menyimpan data aktivitas
daftar_aktivitas = []

print("=== PROGRAM PENDATAAN AKTIVITAS ===")

jumlah = int(input("Berapa aktivitas yang ingin diinput? "))

for i in range(jumlah):
    print(f"\nAktivitas ke-{i+1}")

    aktivitas = input("Masukkan nama aktivitas : ")
    kategori = input("Masukkan kategori aktivitas : ")
    waktu = input("Masukkan waktu aktivitas : ")
    status = input("Masukkan status aktivitas (Selesai/Belum) : ")

    # Simpan ke dalam dictionary
    data = {
        "aktivitas": aktivitas,
        "kategori": kategori,
        "waktu": waktu,
        "status": status
    }

    # Masukkan ke list
    daftar_aktivitas.append(data)

# Menampilkan hasil
print("\n=== DATA AKTIVITAS ===")

for index, item in enumerate(daftar_aktivitas, start=1):
    print(f"""
Aktivitas #{index}
-------------------------
Nama Aktivitas : {item['aktivitas']}
Kategori       : {item['kategori']}
Waktu          : {item['waktu']}
Status         : {item['status']}
""")
    