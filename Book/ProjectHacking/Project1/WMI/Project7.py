# Mengetahui Group & User Dalam Sistem Windows
import wmi

c = wmi.WMI()
for group in c.Win32_Group():
    print(group.Caption+":")
    for user in group.associators(wmi_result_class = "Win32_UserAccount"):
        print("- " + user.Caption)