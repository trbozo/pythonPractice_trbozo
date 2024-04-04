# // Scanner oku=new Scanner(System.in);
# // System.out.print("Adınız=");
# // String ad=oku.nextLine();
# // System.out.print("Soyadınız=");
# // String soyad=oku.nextLine();
# // System.out.println("Adınız ve Soyadınız= " + ad+" "+soyad);
ad = input("Adınız=")
soyad = input("Soyadınız=")
print("Adınız ve Soyadınız=", ad, soyad)


# Bu Java kodunun Python'a çevrilmiş hali:

import sys

# Kullanıcıdan adı ve soyadı ayrı ayrı isteyelim
print("Adınız=")
ad = input()  # Kullanıcıdan adı alalım

print("Soyadınız=")
soyad = input()  # Kullanıcıdan soyadı alalım

# Adı ve soyadını birlikte ekrana yazdıralım
print("Adınız ve Soyadınız= " + ad + " " + soyad)
