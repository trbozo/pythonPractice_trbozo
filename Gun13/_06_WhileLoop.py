# Girilen 5 tam sayının toplamını yazdır

sayac = 0
toplam = 0

while sayac < 5:
    sayi = int(input("Sayı giriniz="))
    toplam += sayi
    sayac += 1

print("toplam =", toplam)


#kullanıcıdan 5 tam sayı alarak toplamını hesaplar ve yazdırır. sayac değişkeni başlangıçta 0 olarak atanır ve her döngüde bir artırılır. toplam değişkeni ise her döngüde kullanıcının girdiği sayıyı eklenerek güncellenir. Döngü 5 kez çalıştıktan sonra toplam değeri ekrana yazdırılır. Ayrıca, kullanıcıdan giriş almak için input() fonksiyonu kullanılır.