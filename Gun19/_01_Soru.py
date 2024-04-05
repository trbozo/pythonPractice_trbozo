# package Gun19;
#
# import java.util.Arrays;
#
# public class _01_Soru {
#     public static void main(String[] args) {
#         // 2 ye 5 lik bir tabloyu random 100 e kadar sayılarla doldurunuz
#         // bütün doldurma işlemi bittikten sonra
#         // kaç tane tek sayı olduğunu bulunuz.
#
#         int[][] tablo=new int[2][5];
#         // random sayılarla doldurma
#         for (int satir = 0; satir < tablo.length; satir++) {
#
#             for (int sutun = 0; sutun < tablo[satir].length; sutun++)
#                 tablo[satir][sutun] = (int) (Math.random() * 100); //10 kez çalıştı
#
#         }
#
#
#
#         int tekMiktar=0; // tek miktarını bulma
#         for (int satir = 0; satir < tablo.length; satir++) {
#
#             for (int sutun = 0; sutun < tablo[satir].length; sutun++)
#                  if (tablo[satir][sutun] %2 == 1)
#                      tekMiktar++;
#         }
#
#         System.out.println("tekMiktar = " + tekMiktar);
#     }
# }


import random

# 2x5'lik bir tablo oluşturma ve random sayılarla doldurma
tablo = [[random.randint(0, 99) for _ in range(5)] for _ in range(2)]

# Tek sayıların miktarını bulma
tek_miktar = sum(1 for satir in tablo for sayi in satir if sayi % 2 == 1)

print("tekMiktar =", tek_miktar)


#Bu kod, Python'da random.randint(0, 99) fonksiyonunu kullanarak her bir hücreye 0 ile 99 arasında rastgele
# bir tam sayı atar. Daha sonra, iç içe döngüler ve bir koşullu ifade (if sayi % 2 == 1) kullanarak, tablodaki
# tüm tek sayıların sayısını hesaplar. sum() fonksiyonu, bir generator expression ile birlikte kullanılarak,
# tek sayıların toplam sayısını verir.
# Bu, Java'daki for döngüleri ve if koşullarını kullanarak yapılan işlemin Python'daki daha sade bir karşılığıdır.