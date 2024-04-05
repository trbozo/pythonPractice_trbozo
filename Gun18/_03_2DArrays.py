# package Gun18;
#
# import java.util.Scanner;
#
# public class _03_2DArrays {
#     public static void main(String[] args) {
#         // 2 Boyutlu dizi (2D Arrays) nedir ?
#         int sayi=0;  // 1 tane sayı tutar
#
#         int[] dizi=new int[10]; // 10 tane sayı tutar, apartman dı
#
#         int[] ders1Notlar=new int[50];  // ayrı ayrı 50
#         int[] ders2Notlar=new int[50];  // ayrı ayrı 50
#         int[] ders3Notlar=new int[50];  // ayrı ayrı 50
#
#         // 3 tane 50 yi tek kalemde tek değişkende nasıl tanımlarım
#         int[][] tumDersNotlar=new int[3][50];  // 3 tane 50 , yukarıdaki ile aynı, site
#
#                    //[satır][sütun]
#         tumDersNotlar[0][0] = 80;  // 2 indexle eleman ulaşılır, bu ilk elemanı
#
#         System.out.println("tumDersNotlar = " + tumDersNotlar[0][0]);
#
#         Scanner oku=new Scanner(System.in);
#         tumDersNotlar[0][0]=oku.nextInt();
#
#     }
# }


# Tek boyutlu liste
ders1_notlar = [50] * 50  # 50 elemanlı, her biri 50 değerine sahip liste

# İki boyutlu liste
tum_ders_notlar = [[0 for _ in range(50)] for _ in range(3)]  # 3 ders için, her birinde 50 not tutan 2D liste

# Bir elemana değer atama
tum_ders_notlar[0][0] = 80  # İlk dersin ilk notuna değer atama

print("tumDersNotlar =", tum_ders_notlar[0][0])

# Kullanıcıdan değer alma ve bir elemana atama
sayi = int(input("Bir not giriniz: "))
tum_ders_notlar[0][0] = sayi



## bir öğrencinin birden fazla ders için notlarını tutacak şekilde iki boyutlu
# bir liste (2D array) tanımlar ve bu listeye değerler atar. İlk olarak, tum_ders_notlar adında
# 3 satır ve her satırda 50 sütundan oluşan bir liste tanımlanır. Daha sonra bu listenin ilk elemanına
# (ilk dersin ilk notuna) 80 değeri atanır ve ekrana yazdırılır. Sonrasında, kullanıcıdan alınan bir değer,
# bu listenin ilk elemanına atanır.

#Python'da, 2D diziler üzerinde işlem yapmak için genellikle iç içe for döngüleri kullanılır.
# Bu örnek, iki boyutlu dizilerin (listelerin) temel kullanımını göstermektedir.