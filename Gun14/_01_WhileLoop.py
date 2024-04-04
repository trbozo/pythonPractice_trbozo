# 1'den 100'e kadar olan sayıların toplamını bul

sayac = 1
toplam = 0

while sayac < 100:
    toplam += sayac
    sayac += 1

print("toplam =", toplam)


# 1'den 100'e kadar olan sayıların toplamını hesaplar ve ekrana yazdırır. sayac değişkeni başlangıçta 1 olarak atanır ve her döngüde bir artırılır. toplam değişkeni ise her döngüde sayac değeri toplamına eklenerek güncellenir. Döngü 100'e kadar olduğu sürece devam eder ve sonunda toplam değeri ekrana yazdırılır.