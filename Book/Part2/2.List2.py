# Menghapus Item Di List
print("List Yang Sempurna")
todo_list = [
    "Belajar Python",
    "Belajar Pentest",
    "Belajar Bug Hunting",
    "Belajar Turu",
    "Belajar Taekwondo",
    "Belajar English Speaking",
    "Belajar Nahwu",
    "belajar Sharaf"
]

todo_list1 = todo_list.copy()
print(todo_list)
print(" ")

# Menghapus Index-3 Dengan 'del'
print("Menghapus Index-3(Turu) Dengan 'del'")
del todo_list[3]
print(todo_list)
print(" ")

# Menghapus Index-5 Dengan 'remove(item)'
print("Menghapus Index-5(English Speaking) Dengan 'remove(item)'")
todo_list1.remove("Belajar English Speaking")
print(todo_list1)
print(" ")

# Menghapus Dengan 'pop' Hanya Dapat Menghapus Index terakhir
print("Menghapus Dengan 'pop' Hanya Dapat Menghapus Index terakhir")
todo_list1.pop()
print(todo_list1)
print(" ")

# Membalikan List
x = [1, 2, 3, 4, 5]
print(x)
x.reverse()
print(x)
print(" ")

# Mengurutkan List
a = [3,2,5,7,9,1,4,6,8]
print(a)
a.sort()
print(a)
print(" ")

# Mengurutkan List(Custom)
Yu = [
    'Pentest',
    'Bug',
    'Hacking',
    'Coder'
]
print(Yu)
Yu.sort()
print(Yu)
print(" ")

# Memotong List
b = [1,2,3,4,5,6,7,8,9,10]
print(b [3: 6])
print(b [4: 9])
print(b [6: 11])