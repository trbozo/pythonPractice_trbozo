# // String s1="merhaba";
# // String s2="MERHABA";
s1 = "merhaba"
s2 = "MERHABA"

# // System.out.println("esitMi = " + s1.equals(s2));
# // System.out.println("esitMi = " + s1.equals("merhaba"));
print(f"esitMi = {s1 == s2}")
print(f"esitMi = {s1 == 'merhaba'}")


# Java kodunun Python'a dönüştürülmüş hali

# Equals: 1 stringi diğeriyle eşit mi sorar
# sonuç boolean

s1 = "merhaba"
s2 = "MERHABA"

sonuc = s1 == s2  # s1 s2 ye eşit mi
print("esitMi =", sonuc)  # false

print("esitMi =", s1 == s2)  # 2.yöntem     false
print("esitMi =", s1 == "merhaba")  # true


# == operatörünü kullanarak iki stringin eşit olup olmadığını kontrol eder. Sonuç, True veya False olarak verilir.






