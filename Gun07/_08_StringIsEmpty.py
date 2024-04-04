# // String s1="Merhaba";
# // String s2="";
s1 = "Merhaba"
s2 = ""

# // System.out.println("s1.isEmpty() = " + s1.isEmpty());
# // System.out.println("s2.isEmpty() = " + s2.isEmpty());
print(f"s1.isEmpty() = {s1 == ''}")
print(f"s2.isEmpty() = {s2 == ''}")


# IsEmpty  :  bir string içinde bir veya daha fazla karakter var mı yok mu ?
# boolean

s1 = "Merhaba"
s2 = ""

print("s1.isEmpty() =", len(s1) == 0)  # s1 boşMu  false
print("s2.isEmpty() =", len(s2) == 0)  # true


#Bu Python kodunda, len() fonksiyonu kullanılarak stringin uzunluğu kontrol edilir. Eğer uzunluk 0 ise, yani string boşsa, isEmpty() metodu True döndürür, aksi halde False döndürür.






