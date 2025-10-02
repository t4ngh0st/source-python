try:
    hasil = 10 / 0
except ZeroDivisionError:
    print("Tidak Dapat Dibagi Nol")
except Except as e:
    print(f"Error: {e}")
finally:
    print("Selesai")