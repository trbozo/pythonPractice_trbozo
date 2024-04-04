# Java kodunun Python'a dönüştürülmüş hali

# ReplaceAll: replace gibi çalışır. Farkı, kriter (regex) verilebiliyor.
# Regex: regular expression / düzenli ifadeler
# TODO (yapılacak): regex olarak neler yazılabiliyor, Google'dan araştırılacak

text = "Merhaba12 Dünya23"

print("text = " + text)
print("abn -> _ = " + text.replace("[abn]", "_"))  # abn'yi _ ile değiştir
print("123 ->   = " + text.replace("[123]", ""))  # 123'ü sil
print("0-9 ->   = " + text.replace("[0-9]", ""))  # 0-9 arasındakileri sil
print("a-z ->   = " + text.replace("[a-z]", ""))  # a-z arasındakileri sil
print("0-9 ->   = " + text.replace("[^0-9]", ""))  # 0-9 DIŞINDAKİLERİ sil
print("A-Z ->   = " + text.replace("[A-Z]", ""))  # A-Z arasındakileri sil

print(text.replace("[A-Z]", "").replace("[a-z]", ""))  # tüm harfleri siler


##Java'da replaceAll() metodu Python'daki replace() metodu ile benzer şekilde kullanılabilir. Python'da düzenli ifadeler (regular expressions) doğrudan replace() fonksiyonu içinde kullanılmaz; bunun yerine re modülü kullanılarak düzenli ifadelerle ilgili işlemler yapılır.