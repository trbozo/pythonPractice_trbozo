# // Scanner oku=new Scanner(System.in);
# // System.out.print("Tarlanın 1 kenar uzunluğu=");
# // int kenar=oku.nextInt();
# // System.out.println("Çevre = " + (4*kenar));
kenar = int(input("Tarlanın 1 kenar uzunluğu="))
print("Çevre =", 4 * kenar)


# Bu Java kodunun Python'a çevrilmiş hali:

import sys

# Kullanıcıdan karenin bir kenar uzunluğunu alalım
print("Tarlanın 1 kenar uzunluğu=")
kenar = int(input())

# Karenin çevresini hesaplayalım
cevre = 4 * kenar

# Çevreyi ekrana yazdıralım
print("Çevre = " + str(cevre))

