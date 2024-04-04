# Kullanıcının gireceği sayının tek mi çift mi olduğunu yazdırınız.

sayi = int(input("Sayı: "))

# Normal yöntem
if sayi % 2 == 0:
    print("çift")
else:
    print("tek")

# if-else için kısa yöntem (Ternary operator)
sonuc = "Evet" if sayi % 2 == 0 else "Hayır"
print("sonuc =", sonuc)
