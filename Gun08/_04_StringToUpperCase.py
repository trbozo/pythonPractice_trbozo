# Java kodunun Python'a dönüştürülmüş hali

# ToUpperCase : stringin büyük harf halini verir

text = "merhaba dünya"

print("text =", text)  # merhaba dünya
print("text.upper() =", text.upper())  # MERHABA DÜNYA

print("text.startswith('M') =", text.startswith("M"))  # False
print("text.upper().startswith('M') =", text.upper().startswith("M"))  # True


#Java'daki toUpperCase() metodu Python'daki upper() metodu ile aynı işlevi yerine getirir. Bu metodun kullanımı ve sonuçları Java ile aynıdır. Ancak, Python'da stringler değiştirilemez (immutable) olduğu için, bir dizenin upper() metodu çağrıldığında, orijinal dizeyi değiştirmez ve dönüştürülmüş bir kopyasını döndürür. Bu nedenle, dönüştürülmüş dizeyi kullanmak istiyorsanız, upper() metodunu çağırarak yeni dizeyi bir değişkene atamalısınız.