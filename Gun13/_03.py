# Girilen bir sayının birler basamağının değerini yazı ile yazdırın
# Örneğin:
# 234 -> birler basamağı -> 4 -> dört
# 45 -> beş
# 6 -> altı

sayi = int(input("Sayı giriniz="))

birler_basamagi = sayi % 10

# Birler basamağına göre switch-case yapısı oluşturarak yazı ile yazdırma
if birler_basamagi == 0:
    print("Sıfır")
elif birler_basamagi == 1:
    print("Bir")
elif birler_basamagi == 2:
    print("İki")
elif birler_basamagi == 3:
    print("Üç")
elif birler_basamagi == 4:
    print("Dört")
elif birler_basamagi == 5:
    print("Beş")
elif birler_basamagi == 6:
    print("Altı")
elif birler_basamagi == 7:
    print("Yedi")
elif birler_basamagi == 8:
    print("Sekiz")
elif birler_basamagi == 9:
    print("Dokuz")


#kullanıcının girdiği sayının birler basamağının değerini yazı ile yazdırır. Birler basamağına göre switch-case yapısı oluşturarak, birler basamağının değerini belirli sayılarla eşleştirir ve sonucu yazdırır. Ayrıca, kullanıcıdan giriş almak için input() fonksiyonu kullanılır.