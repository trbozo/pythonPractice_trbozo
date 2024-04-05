# package Gun18;
#
# import java.util.Arrays;
#
# public class _02_Soru {
#     public static void main(String[] args) {
#         // 10 elemanlı bir diziyi random(10 dahil sayılarla) doldurduktan sonra,
#         // dizide kaç tek ve kaç çift olduğunu bulunuz
#
#         int[] dizi=new int[10];
#
#         for (int i = 0; i < dizi.length; i++)
#             dizi[i] = (int)(Math.random()*11);
#
#         int tekMiktar=0, ciftMiktar=0;
#
#         for (int i = 0; i < dizi.length; i++) {
#
#             if (dizi[i] % 2 == 0)
#                 ciftMiktar++;  //ciftMiktar = ciftMiktar + 1;
#             else
#                 tekMiktar++;  //tekMiktar = tekMiktar + 1;
#         }
#
#         System.out.println("dizi = " + Arrays.toString(dizi));
#         System.out.println("tekMiktar = " + tekMiktar);
#         System.out.println("ciftMiktar = " + ciftMiktar);
#
#     }
# }


import random

# 10 elemanlı bir dizi oluştur ve 0-10 arası rastgele sayılarla doldur
dizi = [random.randint(0, 10) for _ in range(10)]

tek_miktar = 0
cift_miktar = 0

# Dizideki her bir sayı için tek veya çift olduğunu kontrol et
for sayi in dizi:
    if sayi % 2 == 0:
        cift_miktar += 1
    else:
        tek_miktar += 1

print("dizi =", dizi)
print("tekMiktar =", tek_miktar)
print("ciftMiktar =", cift_miktar)


##Bu Python kodu, 10 elemanlı bir diziyi 0'dan 10'a kadar (dahil) rastgele sayılarla doldurur ve ardından dizide
# kaç tek ve kaç çift sayı olduğunu hesaplar. Java'da olduğu gibi, Python'da da random.randint(0, 10) fonksiyonu
# ile rastgele sayılar üretilir ve for döngüsü ile her bir elemanın tek veya çift olup olmadığı kontrol edilir.
# Son olarak, dizinin kendisi ve tek ile çift sayıların miktarları ekrana yazdırılır.