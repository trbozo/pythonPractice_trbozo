# Girilen 6 sayıdan sadece pozitif olanlarının toplamını bul

sayac = 0
toplam = 0

while sayac < 6:
    sayi = int(input("Sayı giriniz="))

    if sayi > 0:
        toplam += sayi

    sayac += 1

print("toplam =", toplam)
