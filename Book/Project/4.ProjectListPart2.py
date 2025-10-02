# Membuat List Kosong Untuk Menampung Variable(Hobi)
hobi = []
i = 0
while True:
    hobi_baru = input(f"[?] Masukkan Hobimu Yang Ke-{i+1} : ")
    hobi.append(hobi_baru)
    # Increment i
    i += 1
    
    # Variable Question
    # Beri Nilai Default 'y' Jika Pengguna Hanya Menekan Enter
    que = input("[?] Mau Ngulang Lagi ?(Y/n) :")
    # Periksa apakah input adalah salah satu dari kondisi berhenti (case-insensitive)
    if que.lower() in ['', 'y', 'ya', 'yes','Y', 'Ya', 'Yes']:
        continue # Melanjutkan Loop
    elif que.lower() in ['n', 'no','N','No']:
        break # Hentikan loop jika input adalah 'n' atau 'no'
    # Jika input kosong (Enter) atau 'y' (atau lainnya), loop akan lanjut
    else:
        print("System Error ...")
        exit()
        
# Cetak Semua Hobi
print('-' * 20)
print(f"Kamu Memiliki {len(hobi)} hobi : ") # Menggunakan f-string untuk format yang lebih modern
for idx, hb in enumerate(hobi):# Menggunakan enumerate untuk mendapatkan nomor urut
    print(f"{idx + 1}. {hb}")