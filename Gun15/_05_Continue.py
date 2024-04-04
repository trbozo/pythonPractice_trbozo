# Kullanıcıdan 5 tane sayı isteyiniz.
# Bu sayılardan 6 ile 10 arasındakiler hariç, diğerlerini toplasın.

toplam = 0

for i in range(1, 6):  # bu döngü kaç döner
    # sayı oku
    # ve kriter geçerli ise topla
    sayi = int(input(f"{i}. Sayı giriniz="))

    if 6 < sayi < 10:
        continue  # döngünün bundan sonrasını pass geç
        # bir sonraki adıma devam et

    toplam = toplam + sayi

print("toplam =", toplam)


# #Dil Sözdizimi: Java ve Python farklı sözdizimine sahiptir. Java'da kod blokları {} ile belirtilirken, Python'da girinti kullanılır.
# Döngü İfadesi: Java'da döngü ifadesi for(int i=1; i <= 5; i++) şeklinde tanımlanırken, Python'da for i in range(1, 6): şeklinde tanımlanır.
# Kullanıcı Girişi Alma: Java'da kullanıcı girişi alma işlemi Scanner sınıfıyla yapılırken, Python'da input() fonksiyonu kullanılır.
# Değişken Tanımlama: Java'da değişken tanımlamak için veri tipi belirtilirken, Python'da veri tipi belirtilmeden doğrudan değişken tanımlanabilir.
# String Formatlama: Java'da string formatlama işlemi System.out.print(i+".Sayı giriniz=") şeklinde yapılırken, Python'da farklı bir string formatlama yöntemi kullanılır.
# Kod Açıklamaları: Python'da kod açıklamaları # işareti ile belirtilirken, Java'da // veya /* ... */ kullanılır.