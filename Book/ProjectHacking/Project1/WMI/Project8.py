# Mengetahui Daftar Aplikasi & PID Yang Sedang Berjalan Dalam Sistem Dan Mematikannya
import wmi
c = wmi.WMI(find_classes = False)
for i in c.Win32_Process(["Caption","ProcessID"]):
    print(i.Caption, i, ProcessID)
noid = input("ID Program Yang Akan Dimatikan : ")
c.Win32_Process(ProcessId=noid) [0].Terminate()