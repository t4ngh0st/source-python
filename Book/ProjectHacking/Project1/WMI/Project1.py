# Outputnya Akan MElihat Versi Windows
import wmi

c = wmi.WMI()
for os in c.Win32_OperationgSystem():
    printA(os.Caption)