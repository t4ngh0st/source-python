# Mematikan Service Tertentu
import wmi

c = wmi.WMI()
for service in c.Win32_Service(State="Running"):
    print(service.Name)
NamaService = input("Nama Service Yang Akan Dimatikan : ")

try:
    service in c.Win32_Service(State="Running"):
        if str(service.Name)==str(NamaService)
            result = service.StopService()
            if result == 0:
                print("Service", service.Name, "Berhenti")
            else:
                print("Ada Masalah")
                break
except:
    print("Error")