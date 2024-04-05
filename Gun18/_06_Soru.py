# package Gun18;
#
# public class _06_Soru {
#     public static void main(String[] args) {
#         // 2 ye 3 lük bir tabloyu random 100 e kadar sayılarla doldurunuz
#         // bütün doldurma işlemi bittikten sonra
#         // sonrasında yazdırınız
#
#         int[][] tablo=new int[2][3];  //2 ye 3 lük bir tablo
#
#         //tabloyu random 100 e kadar sayılarla doldurunuz
#         for (int i = 0; i < tablo.length; i++) {
#
#             for (int j = 0; j < tablo[i].length; j++)
#                 tablo[i][j]=(int)(Math.random()*100);
#
#         }
#
#
#         for (int satir = 0; satir < tablo.length; satir++) {
#
#             for (int sutun = 0; sutun < tablo[satir].length; sutun++)
#                 System.out.print(tablo[satir][sutun]+"\t");
#
#             System.out.println();
#         }
#
#
#
#
#     }
# }


import random

# 2'ye 3'lük bir tablo tanımlama
tablo = [[0 for _ in range(3)] for _ in range(2)]

# Tabloyu random 100'e kadar sayılarla doldurma
for i in range(len(tablo)):
    for j in range(len(tablo[i])):
        tablo[i][j] = random.randint(0, 99)  # 0 ile 99 arası rastgele sayı üretir

# Tabloyu yazdırma
for satir in tablo:
    for sutun in satir:
        print(sutun, end="\t")
    print()


#Bu Python kodu, 2x3 boyutunda bir dizi oluşturur ve bu diziyi 0 ile 99 arasında rastgele sayılarla doldurur.
# random.randint(0, 99) fonksiyonu, belirtilen aralıkta rastgele bir tam sayı üretir. Daha sonra iç içe döngüler
# kullanılarak dizi elemanları yazdırılır. print() fonksiyonunun end="\t" parametresi, aynı satırdaki elemanları
# tab boşluğu ile ayırarak yazdırmak için kullanılır.
# Bu, dizinin okunabilir bir şekilde konsola yazılmasını sağlar.