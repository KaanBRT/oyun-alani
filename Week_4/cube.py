sayi = float(input("Küp kökünü bulmak istediğiniz pozitif sayıyı girin: "))
epsilon = 0.01
low = 0.0
high = max(1.0, sayi)
guess = (low + high) / 2

while abs(guess ** 3 - sayi) > epsilon:
    if guess ** 3 < sayi:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2

print(f"Küp kökü: {guess}")