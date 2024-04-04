# Java kodunun Python'a dönüştürülmüş hali

# replaceFirst: bir stringin içindeki karakter/lerin sadece ilkini
# verilenle değiştirir

text = "Merhaba Dünya"
print("text = " + text)

print("text.replaceFirst(a, e) = " + text.replace("a", "e", 1))  # Merheba Dünya
print("text.replaceFirst(ba, de) = " + text.replace("ba", "de", 1))  # Merhade Dünya
print("text.replaceFirst(a, aaa) = " + text.replace("a", "aaa", 1))  # Merhaaaba Dünya
print("text.replaceFirst(a,  ) = " + text.replace("a", "", 1))  # Merhba Dünya
print("text.replaceFirst(a, ***) = " + text.replace("a", "***", 1))  # Merh***ba Dünya


#Java'daki replaceFirst() metodu Python'daki replace() metodu ile benzerdir, ancak son parametre olan limit parametresi ile farklılık gösterir. Bu parametre, kaç adet değiştirme işleminin yapılacağını belirler. Python'da ise replace() fonksiyonu kullanılırken bu parametreye gerek yoktur; bunun yerine replace() fonksiyonu sadece belirtilen karakterlerin hepsini değiştirir.






