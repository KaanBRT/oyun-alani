import random
gizli_sayi = random.randint(1,100)
hak = 0
tahmin = int(input("Tahmini gir: "))

while gizli_sayi != tahmin:
    if gizli_sayi < tahmin:
         if gizli_sayi * 110/100 < tahmin:
                print("çok büyük")
         else:
                print("yakın ama hala büyük")
    else:
         if gizli_sayi > tahmin * 110/100:
                print("çok küçük")
         else:
                print("yakın ama küçük")
    hak += 1
    if hak == 5:
        print(f"Hakkın bitti ;( Gizli sayı {gizli_sayi} idi")
        break
    tahmin = int(input("Tahmini gir: "))
if gizli_sayi == tahmin:
    print("Tebrikler")