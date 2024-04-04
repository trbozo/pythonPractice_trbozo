# Soru: Girilen bir sayının sıfır mı, negatif mi, pozitif mi olduğunu
# Ternary operatör ile yazdırınız.

sayi = int(input("Sayı: "))

sonuc = "Sıfır" if sayi == 0 else ("pozitif" if sayi > 0 else "negatif")

print("sonuc =", sonuc)
