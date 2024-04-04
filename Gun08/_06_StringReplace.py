# Java kodunun Python'a dönüştürülmüş hali

# replace: bir stringin içindeki karakter/leri verilenle değiştirir
# hepsini dönüştürür

text = "Merhaba Dünya"
print("text = " + text)

print("text.replace(a, e) = " + text.replace("a", "e"))  # Merhebe Dünye
print("text.replace(ba, de) = " + text.replace("ba", "de"))  # Merhade Dünya
print("text.replace(a, aaa) = " + text.replace("a", "aaa"))  # Merhaaabaaa Dünyaaa
print("text.replace(a,  ) = " + text.replace("a", ""))  # Merhb Düny
print("text.replace(a, ***) = " + text.replace("a", "***"))  # Merh***b*** Düny***


#Java'daki replace() metodu Python'daki replace() metodu ile aynı işlevi yerine getirir. Ancak, Python'da metot çağrısı biraz farklı yazılır, yani nokta (.) işareti yerine, değişkenin adı ve ardından fonksiyon adı parantezlerle kullanılır. Ayrıca, Python'da tek tırnak yerine çift tırnak veya ters eğik tırnak da kullanılabilir.