import json
import os

FILENAME = "todo.json"

# Load dari file JSON
def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r') as file:
        return json.load(file)

# Simpan ke file JSON
def save_tasks(tasks):
    with open(FILENAME, 'w') as file:
        json.dump(tasks, file, indent=4)

# Tampilkan daftar tugas
def show_tasks(tasks):
    if not tasks:
        print("📭 Tidak ada tugas.")
    else:
        print("\n📋 Daftar Tugas:")
        for i, task in enumerate(tasks, 1):
            status = "✅ Sudah" if task["done"] else "❌ Belum"
            print(f"{i}. {task['title']} [{status}]")
    print()

# Tambah tugas baru
def add_task(tasks):
    title = input("📝 Masukkan judul tugas: ")
    tasks.append({"title": title, "done": False})
    print("✅ Tugas berhasil ditambahkan.\n")

# Ubah status tugas (Sudah/Belum)
def toggle_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("🔄 Nomor tugas yang ingin diubah statusnya: ")) - 1
        tasks[index]["done"] = not tasks[index]["done"]
        status = "✅ Sudah" if tasks[index]["done"] else "❌ Belum"
        print(f"Status tugas diubah menjadi {status}.\n")
    except (IndexError, ValueError):
        print("⚠️ Nomor tidak valid!\n")

# Edit judul tugas
def edit_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("✏️ Nomor tugas yang ingin diedit: ")) - 1
        new_title = input("🆕 Masukkan judul baru: ")
        old_title = tasks[index]["title"]
        tasks[index]["title"] = new_title
        print(f"✏️ Tugas '{old_title}' diubah menjadi '{new_title}'.\n")
    except (IndexError, ValueError):
        print("⚠️ Nomor tidak valid!\n")

# Hapus tugas
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("🗑️ Nomor tugas yang ingin dihapus: ")) - 1
        removed = tasks.pop(index)
        print(f"Tugas '{removed['title']}' berhasil dihapus.\n")
    except (IndexError, ValueError):
        print("⚠️ Nomor tidak valid!\n")

def menu():
    tasks = load_tasks()
    while True:
        print("=== TO-DO LIST ===")
        print("1. 📂 Tampilkan Tugas")
        print("2. ➕ Tambah Tugas")
        print("3. ✅ Tandai Sudah/Belum")
        print("4. ✏️ Edit Tugas")
        print("5. 🗑️ Hapus Tugas")
        print("6. 💾 Simpan dan Keluar")
        choice = input(">> Pilih opsi (1-6): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            toggle_task(tasks)
        elif choice == '4':
            edit_task(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("📦 Tugas disimpan. Sampai jumpa!\n")
            break
        else:
            print("❌ Pilihan tidak valid!\n")

if __name__ == "__main__":
    menu()
