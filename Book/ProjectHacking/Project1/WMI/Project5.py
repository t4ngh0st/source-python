# Membuat Folder Share Di Windows
import wmi

c = wmi.WMI()

result = c.Win32_Share.Create(Path="c:\\temp",Name="temp", Type=0)
if result == 0:
    print("Folder Share Temp Berhasil Dibuat")
else:
    print("Gagal!!!")