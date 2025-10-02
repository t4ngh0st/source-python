# Menjalankan Aplikasi Tertentu Pada LocalHost
import wmi

SW_SHOW_NORMAL = 1
try:
    c = wmi.WMI("127.0.0.1")
    ProcessStartup = c.Win32_ProcessStartuo.new()
    ProcessStartup.ShowWindow = SW_SHOW_NORMAL
    process_id, result = c.Win32_Process.Create(CommandLine="notepad.exe",ProcessStartupInformation=ProcessStartup)
    if result == 0:
        print("Process Started Successfully : %d" process_id)
    else:
        print("Gagal")
        
except:
    print("Error")