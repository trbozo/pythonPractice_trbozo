# // String s1="meRhaba";
# // String s2="MERhABa";
s1 = "meRhaba"
s2 = "MERhABa"

# // System.out.println("s1.equalsIgnoreCase(s2) = " + s1.equalsIgnoreCase(s2));
print(f"s1.equalsIgnoreCase(s2) = {s1.lower() == s2.lower()}")


# Java kodunun Python'a dönüştürülmüş hali

# EqualsIgnoreCase
# equals aynı çalışır sadece büyük küçük harf ayrımı yapmaz

s1 = "meRhaba"
s2 = "MERhABa"

print("s1.equals(s2) =", s1 == s2)  # false
print("s1.equalsIgnoreCase(s2) =", s1.lower() == s2.lower())  # true


#Bu Python kodu, lower() metodu kullanılarak her iki stringin de küçük harfe dönüştürülmesini sağlar. Daha sonra == operatörü ile karşılaştırma yapılır. Bu şekilde büyük-küçük harf ayrımı yapılmadan eşitlik kontrolü gerçekleştirilir.






