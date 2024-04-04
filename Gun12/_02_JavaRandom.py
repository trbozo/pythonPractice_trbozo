# package Gun12;
#
# import java.util.Scanner;
#
# public class _02_JavaRandom {
#     public static void main(String[] args) {
#         // Girilen bir sayıya kadar random sayı üreterek tahmin etmeye çalışnız
#         // kullanıcı bilirse tebrikler yazdırınız.
#         // mesala 5 girersem 5 e kadar sayı üretsin, ben tahmin etmeye çalışayım
#
#         Scanner oku=new Scanner(System.in);
#         System.out.print("Üretilecek sayı sınırı=");
#         int sinir=oku.nextInt();
#
#         int tutulanSayi= (int)(Math.random()*sinir);
#
#         System.out.print("Tahmininiz=");
#         int tahmin=oku.nextInt();
#
#         if (tutulanSayi == tahmin)
#             System.out.println("Tebrikelr bildiniz");
#         else
#             System.out.println("Bilemedin ki , bilemedin ki , "+tutulanSayi);
#     }
# }


import random

# Girilen bir sayıya kadar random sayı üreterek tahmin etmeye çalışın
# Kullanıcı bilirse "Tebrikler" yazdırınız.
# Örneğin, 5 girilirse 5'e kadar sayı üretsin, kullanıcı tahmin etmeye çalışsın.

sinir = int(input("Üretilecek sayı sınırı= "))
tutulan_sayi = random.randint(0, sinir)

tahmin = int(input("Tahmininiz= "))

if tutulan_sayi == tahmin:
    print("Tebrikler, bildiniz!")
else:
    print("Bilemedin ki, bilemedin ki,", tutulan_sayi)


#kullanıcının belirttiği sınıra kadar bir rastgele sayı tutar ve kullanıcıdan tahmin yapmasını ister. Ardından, kullanıcının tahmini ile tutulan sayıyı karşılaştırarak sonucu belirtir. Python'da, random modülünden random.randint(a, b) fonksiyonu ile belirtilen aralıkta bir rastgele tam sayı üretilebilir. Ayrıca, kullanıcıdan giriş almak için input() fonksiyonu kullanılır.