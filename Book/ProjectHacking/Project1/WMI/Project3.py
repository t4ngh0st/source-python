# Mengetahui Informasi Drive
import wmi

c = wmi.WMI()
for disk in c.Win32_LogicalDisk(DriveType=3):
    print(disk)
# Berlaku 1 Fixed Drive,Jika Drivernya 3 Maka Info Menanmpilkan Semua

Untuk Mengetahui Drive Non Fixed 

import wmi
c = wmi.WMI()
wql = "SELECT Caption, Description FROM Win32_LogicalDisk WHERE DriveType <> 3"
for disk in c.query(wql):
    print(disk)