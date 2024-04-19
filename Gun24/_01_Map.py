# def main():
#     # Anahtar-değer çiftleri ile bir sözlük (dictionary) oluşturuluyor
#     hm = {}
#     hm[1001] = "İsmet Temur"
#     hm[2001] = "Esma"
#     hm[2] = "Oğuzhan"
#     hm[1003] = "Kaan"
#     hm[1001] = "Ahmet Kaya"  # Aynı anahtar kullanıldığı için değer güncellenir
#
#     print("hm =", hm)
#
#     # Belirli bir anahtara ait değeri alma
#     print("hm.get(2001) =", hm.get(2001))
#     print("hm.get(1003) =", hm.get(1003))
#
#     # Anahtar veya değerin sözlükte olup olmadığını kontrol etme
#     print("1003 in hm =", 1003 in hm)
#     print("'Kaan' in hm.values() =", "Kaan" in hm.values())
#
#     # Tüm anahtarlar ve değerlerin listesini alma
#     print("hm.keys() =", list(hm.keys()))
#     print("hm.values() =", list(hm.values()))
#
#     # Bir anahtar-değer çiftini kaldırma
#     del hm[1001]
#     print("hm =", hm)
#     print("hm.size() =", len(hm))
#
#     # Sözlüğü temizleme
#     hm.clear()
#     print("hm =", hm)
#
# if __name__ == "__main__":
#     main()


def main():
    # Anahtar-değer çiftleri ile bir sözlük (dictionary) oluşturuluyor
    hm = {}
    hm[1001] = "İsmet Temur"
    hm[2001] = "Esma"
    hm[2] = "Oğuzhan"
    hm[1003] = "Kaan"
    hm[1001] = "Ahmet Kaya"  # Aynı anahtar kullanıldığı için değer güncellenir

    print("hm =", hm)

    # Belirli bir anahtara ait değeri alma
    print("hm.get(2001) =", hm.get(2001))
    print("hm.get(1003) =", hm.get(1003))

    # Anahtar veya değerin sözlükte olup olmadığını kontrol etme
    print("1003 in hm =", 1003 in hm)
    print("'Kaan' in hm.values() =", "Kaan" in hm.values())

    # Tüm anahtarlar ve değerlerin listesini alma
    print("hm.keys() =", list(hm.keys()))
    print("hm.values() =", list(hm.values()))

    # Bir anahtar-değer çiftini kaldırma
    del hm[1001]
    print("hm =", hm)
    print("hm.size() =", len(hm))

    # Sözlüğü temizleme
    hm.clear()
    print("hm =", hm)

if __name__ == "__main__":
    main()


# Bu Python kodu, Java'daki HashMap kullanımına eşdeğer işlevler gerçekleştirir:
#
# Sözlük oluşturma ve değer eklemek.
# .get() kullanarak değerlere erişmek.
# Anahtar ve değer varlığını kontrol etmek (in operatörü ile).
# .keys() ve .values() ile anahtar ve değer listelerini almak.
# del kullanarak bir anahtar-değer çiftini kaldırmak.
# .clear() ile tüm sözlüğü temizlemek.
# Her iki dilde de anahtar-değer çiftlerini saklamak ve yönetmek için kullanışlı yapılar mevcut.






