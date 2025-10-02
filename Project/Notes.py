import os
import json
from datetime import datetime

# File untuk menyimpan data
DATA_FILE = "notes_data.json"

def load_data():
    """Memuat Data Dari File JSON"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,'r') as file:
            return json.load(file)
        return {"notes": [], "categories":["Personal", "Work", "Ideas", "Shopping"]}

def save_data():
    """Menyimpan Data Ke File JSON"""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def main_menu():
    """Menampilkan Menu Utama"""
    print("\n=== List-To-List (Notes) ===")
    print("1. Lihat Semua Catatan")
    print("2. Tambah Catatan Baru")
    print("3. Edit Catatan")
    print("4. Hapus Catatan")
    print("5. Kelola Kategori")
    print("6. Cari Catatan")
    print("7. Keluar")
    return input("Pilih Menu(1-7): ")

def display_notes():
    """Menampilkan Daftar Catatan"""
    if not notes:
        print("\nTidak Ada Catatan")
        return
    
    print("\nDaftar Catatan :")
    print("ID   | Judul                     | Kategori      | Dibuat Pada")
    print("-----|---------------------------|---------------|------------------------")
    for note in notes:
        print(f"{note['id']:3} | {note['title'[:20]:20]} | {note['category'][:10]:10} | {note['create_at']}")

def add_note(data):
    """Menambahh Catatan Baru"""
    print("\n=== Menambah Catatan Baru ====")
    title = input("Judul Catatan : ")
    
    print("\nKategori Yang Tersedia: ")
    fo i, category in enumerate(data['category'], start=1)
    print("{i}. {category}")
    
    while True:
        try:
            cat_choise 

# if __name__ == "__main__":
