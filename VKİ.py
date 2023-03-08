Boy = float(input("Boyunuzu giriniz(m): "))
Kilo = float(input("Kilonuzu giriniz(kg): "))


Vücut_Kitle_Endeksi=(Kilo/Boy**2)
Yeni_Vücut_Kitle_Endeksi=int(Vücut_Kitle_Endeksi)

if (Vücut_Kitle_Endeksi<18.5):
    print(f"Vücut kitle endeksiniz {Yeni_Vücut_Kitle_Endeksi}, zayıfsınız.")
elif(Vücut_Kitle_Endeksi>18.5 and Vücut_Kitle_Endeksi<25):
    print(f"Vücut kitle endeksiniz {Yeni_Vücut_Kitle_Endeksi}, normal kilodasınız.")
elif(Vücut_Kitle_Endeksi>25 and Vücut_Kitle_Endeksi<30):
    print(f"Vücut kitle endeksiniz {Yeni_Vücut_Kitle_Endeksi}, fazla kilolusunuz.")
elif(Vücut_Kitle_Endeksi>30 and Vücut_Kitle_Endeksi<35):
    print(f"Vücut kitle endeksiniz {Yeni_Vücut_Kitle_Endeksi}, obezsiniz.")
elif(Vücut_Kitle_Endeksi>35):
    print(f"Vücut kitle endeksiniz {Yeni_Vücut_Kitle_Endeksi}, morbid obezsiniz.")