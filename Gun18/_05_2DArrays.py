# package Gun18;
#
# import java.util.Arrays;
#
# public class _05_2DArrays {
#     public static void main(String[] args) {
#         int[][] tablo2 = {
#                 {5,6,7,34,5  },   //1.satır
#                 {56,7,89,34,6}    //2.satır
#         };
#
#         System.out.println(Arrays.toString(tablo2[0])); // 0.satırın tüm elemanları
#         System.out.println(Arrays.toString(tablo2[1])); // 1.satırın tüm elemanları
#         System.out.println(tablo2[0].length); // 0.satırın eleman sayısı
#         System.out.println(tablo2[1].length); // 1.satırın eleman sayısı
#         System.out.println(tablo2.length); // satır sayısı
#
#         System.out.println();
#
#         for (int satir = 0; satir < tablo2.length; satir++) {  //2 satır
#
#             for (int sutun = 0; sutun < tablo2[satir].length; sutun++)   // 5 sütun
#                 System.out.print( tablo2[satir][sutun]+"\t");
#
#             System.out.println();
#         }
#
#     }
# }


tablo2 = [
    [5, 6, 7, 34, 5],  # 1. satır
    [56, 7, 89, 34, 6]  # 2. satır
]

# 0. ve 1. satırın tüm elemanlarını yazdırma
print(tablo2[0])  # 0. satırın tüm elemanları
print(tablo2[1])  # 1. satırın tüm elemanları

# 0. ve 1. satırın eleman sayısını yazdırma
print(len(tablo2[0]))  # 0. satırın eleman sayısı
print(len(tablo2[1]))  # 1. satırın eleman sayısı

# Satır sayısını yazdırma
print(len(tablo2))  # Satır sayısı

print()

# Tüm elemanları yazdırma
for satir in tablo2:
    for sutun in satir:
        print(sutun, end="\t")
    print()


