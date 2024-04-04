# Java kodunun Python'a dönüştürülmüş hali

# IndexOf(harf/ler) -> verilen harf/lerin indexini verir
# Bugün     IndexOf("B") -> 0 verir

#            012345678
cumle = "Merhaba Dünya"
# h nin oda numarası kaç 3
# a nın oda numarası kaç 4
# Dü nün indexi kaç  8

print("cumle.index('M') = ", cumle.index('M'))  # 0
print("cumle.index('h') = ", cumle.index('h'))  # 3
print("cumle.index('a') = ", cumle.index('a'))  # 4
print("cumle.index('Dü') = ", cumle.index('Dü'))  # 8
print("cumle.index(' ') = ", cumle.index(' '))  # 7
try:
    print("cumle.index('A') = ", cumle.index('A'))  # ValueError: substring not found
except ValueError:
    print("cumle.index('A') = -1")  # -1, bulunamadı
try:
    print("cumle.index('z') = ", cumle.index('z'))  # ValueError: substring not found
except ValueError:
    print("cumle.index('z') = -1")  # -1, bulunamadı

print("cumle.index('a', 5) = ", cumle.index('a', 5))  # 6, 5'ten sonra aramaya başla
print("cumle.index('a', 7) = ", cumle.index('a', 7))  # 12, 7'den sonra aramaya başla


#Java'daki indexOf fonksiyonunun Python'daki karşılığı index fonksiyonudur. İki dil arasındaki temel fark, Python'daki index fonksiyonunun eğer aranan değer bulunamazsa ValueError hatası fırlatmasıdır. Bu durumda, Java'daki -1 dönüş değerine karşılık Python'da -1 değeri dönmez, bunun yerine hata fırlatılır ve gerekirse hata yönetimiyle ele alınır.