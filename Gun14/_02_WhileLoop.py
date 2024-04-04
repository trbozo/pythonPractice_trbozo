# Kullanıcının gireceği 6 sayıdan tek olanlarının toplamını bul

sayac = 0
toplam = 0

while sayac < 6:
    sayi = int(input("Sayı giriniz="))

    if sayi % 2 == 1:  # Tek sayı kontrolü
        toplam += sayi

    sayac += 1

print("toplam =", toplam)
