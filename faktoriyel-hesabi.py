sayi=int(input("Faktöriyel hesabı yapmak istediğiniz sayıyı giriniz: "))

faktoriyel = 1
for n in range (1, sayi + 1):
    faktoriyel = faktoriyel * n
    n = n + 1
print( faktoriyel )
