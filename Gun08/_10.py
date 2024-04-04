# Java kodunun Python'a dönüştürülmüş hali

# Java'da aritmetik işlemler
a = 9
b = 5

print("Toplama İşlemi = ", a + b)  # 14
print("Çıkartma İşlemi = ", a - b)  # 4
print("Çarpma İşlemi = ", a * b)  # 45

print("Bölme işlemi = ", a // b)  # 1
print("Bölme işlemi = ", a / b)  # 1.8
# Normal sonuç 1.8, fakat bilgisayar her iki sayıyı da tam sayı tipinde alırsa, küsüratı atar.
# Bu sebeple sonuç 1 olur, yuvarlama yapmaz. int/int bölüm sonucu int olur.
# Küsüratlı sonuç istiyorsan, işleme girenlerden en az birisi float (ondalıklı sayı) olmalı.

kalan = 9 % 5  # Modül (%) bu işlemi böler ve sadece kalanı verir
print("kalan =", kalan)


#Java'da int türünde bir bölme işlemi sonucunda ondalıklı bir değer elde edilirse, sonuç tam sayı olarak yuvarlanır ve kesir kısmı atılır. Python'da ise / operatörü her zaman ondalıklı bir sonuç verir. Tam sayı bölme işlemi yapmak için // operatörü kullanılır.