# // String cumle="Merhaba Dünya";
cumle = "Merhaba Dünya"

# // System.out.println("varMi a="+ cumle.contains("a"));
# // System.out.println("varMi ya="+ cumle.contains("ya"));
# // System.out.println("varMi z="+ cumle.contains("z"));
# // System.out.println("varMi aü="+ cumle.contains("aü"));
print(f"varMi a= {'a' in cumle}")
print(f"varMi ya= {'ya' in cumle}")
print(f"varMi z= {'z' in cumle}")
print(f"varMi aü= {'aü' in cumle}")


# Java kodunun Python'a dönüştürülmüş hali

# contains: aranan harf/ler stringin içinde var mı yok mu onu verir
# boolean cinsinden sonucu verir

cumle = "Merhaba Dünya"

varMi = "a" in cumle  # true
print("varMi =", varMi)

print("varMi a=", "a" in cumle)  # 2. yöntem
print("varMi ya=", "ya" in cumle)  # true
print("varMi z=", "z" in cumle)  # false
print("varMi aü=", "aü" in cumle)  # false


#Bu Python kodu, in operatörünü kullanarak bir stringin içinde belirli bir karakterin veya karakter dizisinin bulunup bulunmadığını kontrol eder. Sonuç, True veya False olarak verilir.






