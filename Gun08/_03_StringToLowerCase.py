# Java kodunun Python'a dönüştürülmüş hali

# toLowerCase : stringi küçük harfe çevirir

text = "Merhaba Dünya"

print("text =", text)  # Merhaba Dünya
print("text.lower() =", text.lower())  # merhaba dünya

print("text.startswith('m') =", text.startswith("m"))  # False
print(text.lower().startswith('m'))  # True


#Java'daki toLowerCase() metodu Python'daki lower() metodu ile aynı işlevi yerine getirir. Bu metodun kullanımı ve sonuçları Java ile aynıdır. Ancak, Python'da stringler değiştirilemez (immutable) olduğu için, bir dizenin lower() metodu çağrıldığında, orijinal dizeyi değiştirmez ve dönüştürülmüş bir kopyasını döndürür. Bu nedenle, dönüştürülmüş dizeyi kullanmak istiyorsanız, lower() metodunu çağırarak yeni dizeyi bir değişkene atamalısınız.