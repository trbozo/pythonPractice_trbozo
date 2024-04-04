# // Scanner oku=new Scanner(System.in);
# // System.out.print("Sayi1 = ");
# // int sayi1=oku.nextInt();
# // System.out.print("Sayi2 = ");
# // int sayi2=oku.nextInt();
# // int toplam=sayi1+sayi2;
# // System.out.println("Toplam = " + toplam);
sayi1 = int(input("Sayi1 = "))
sayi2 = int(input("Sayi2 = "))
toplam = sayi1 + sayi2
print("Toplam =", toplam)


# Bu Java kodunun Python'a çevrilmiş hali:

import sys

# Kullanıcıdan 2 tam sayı alalım
print("Sayi1 = ")
sayi1 = int(input())

print("Sayi2 = ")
sayi2 = int(input())

# Sayıların toplamını hesaplayalım
toplam = sayi1 + sayi2

# Toplamı ekrana yazdıralım
print("Toplam = " + str(toplam))  # 1. Yöntem

print("Toplam = " + str(sayi1 + sayi2))  # 2. Yöntem
