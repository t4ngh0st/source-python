def time(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Waktu Eksekusi: {end - start} detik")
        return result
    return wrapper

@time
def prosesData():
    # Simulasi Proses Berat
    import time
    time.sleep(2)
    
prosesData()