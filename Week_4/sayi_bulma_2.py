import random
tahmin2 = random.randint(1,100)
secret_sayi = int(input("Gizli sayiyi belirle: "))
hak = 0
alt_sinir = 0.0
üst_sinir = 100.0
while True:
    hak += 1
    if hak == 8:
        print("Başarısız oldun tüm tahmin hakların bitti")
        break
    elif secret_sayi < tahmin2:
        print(f"{tahmin2} Sayı büyük")
        üst_sinir = tahmin2
    elif secret_sayi > tahmin2:
        print(f"{tahmin2} Sayı küçük")
        alt_sinir = tahmin2
    else:
        print("Bilgisayar bildi")
        break
    tahmin2 = int((alt_sinir + üst_sinir) / 2)
