import random

# (int)(Math.Random()*10) -> 0-9, 0-19, 0-29
# 20-30 arasını istiyorum desen => 10 kadar üret sonra 20 ekle
# aralık nedir?
# 1) aralık kadar üret 0-9
# 2) min umumu çıkan sonuca ekle: 20-29

# Girilen min ve max aralığından rastgele bir sayı üretin
min_deger = int(input("min (alt sınır) = "))
max_deger = int(input("max (üst sınır) = "))

rnd_sayi = random.randint(min_deger, max_deger)
print("rnd_sayi =", rnd_sayi)


#kullanıcının belirttiği min ve max aralıklarında bir rastgele sayı üretir. Python'da, random.randint(a, b) fonksiyonu kullanılarak belirtilen aralıkta (a ve b dahil) bir rastgele tam sayı üretilebilir. Ayrıca, kullanıcıdan giriş almak için input() fonksiyonu kullanılır.