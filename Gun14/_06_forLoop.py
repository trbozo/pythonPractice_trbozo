# Girilen 5 tam sayının toplamının sonucunu yazdırınız

# Döngünün içinde neler var?
# Sayıyı oku, toplam = toplam + sayı
# Döngü şartı sayac < 5
toplam = 0

for sayac in range(1, 6):
    sayi = int(input(str(sayac) + ". sayı giriniz="))
    toplam += sayi

print("toplam =", toplam)


#for döngüsü kullanılarak 5 tam sayı girilmesi istenir ve bu sayıların toplamı hesaplanır. Döngü her çalıştığında, kullanıcıdan bir sayı alınır ve toplam değişkenine eklenir. Sonunda, toplam değeri yazdırılır.