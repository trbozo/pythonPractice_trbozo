# package Gun18;
#
# public class _04_2DArrays {
#     public static void main(String[] args) {
#         int[] dizi=new int[10]; // 10 tane, elemanları boş dizi,  default 0
#         int[] dizi2={2,3,4,5,66,7,8,99,23,3}; // 10 tane , elemanları dolu bir dizi
#
#         int[][] tablo=new int[2][5]; // 2 satır lı , 5 sütunlu, 10 elemanlı
#
#         int[][] tablo2 = {
#                 {5,6,7,34,5  },   //1.satır
#                 {56,7,89,34,6}    //2.satır
#         };
#
#         //1.Yöntem
#         for (int i = 0; i < 5; i++)  // bu for ilk satırın tüm elemnalarını yazdırır
#             System.out.println( tablo2[0][i]);
#
#         for (int i = 0; i < 5; i++)  // bu for 2. satırın tüm elemnalarını yazdırır
#             System.out.println( tablo2[1][i]);
#
#         System.out.println("*****");
#         // 2.yöntem
#         for (int satir = 0; satir < 2; satir++) {  //2 satır
#
#             for (int sutun = 0; sutun < 5; sutun++)   // 5 sütun
#                 System.out.print( tablo2[satir][sutun]+"\t");
#
#             System.out.println();
#         }
#
#
#
#     }
# }


# Tek boyutlu diziler
dizi = [0] * 10  # 10 elemanlı, elemanları 0 olan bir dizi
dizi2 = [2, 3, 4, 5, 66, 7, 8, 99, 23, 3]  # Elemanları dolu bir dizi

# İki boyutlu dizi
tablo = [[0 for _ in range(5)] for _ in range(2)]  # 2 satır, 5 sütunlu 2D dizi, elemanları 0

tablo2 = [
    [5, 6, 7, 34, 5],   # 1. satır
    [56, 7, 89, 34, 6]  # 2. satır
]

# 1.Yöntem: Her satırı ayrı ayrı yazdırma
for i in range(5):  # Bu döngü ilk satırın tüm elemanlarını yazdırır
    print(tablo2[0][i])

for i in range(5):  # Bu döngü 2. satırın tüm elemanlarını yazdırır
    print(tablo2[1][i])

print("*****")
# 2.Yöntem: Tüm satırları yazdırma
for satir in range(2):  # 2 satır
    for sutun in range(5):  # 5 sütun
        print(tablo2[satir][sutun], end="\t")
    print()  # Her satırdan sonra yeni bir satıra geç


##Java'daki _04_2DArrays sınıfının işlevselliğine benzer şekilde çalışır. İki boyutlu dizilerin (listelerin)
# nasıl tanımlanacağını, elemanlarının nasıl atanacağını ve nasıl yazdırılacağını gösterir.
# Python'da, iç içe döngüler kullanarak 2D listeler üzerinde gezinme ve elemanlarını işleme işlemi yapılır.
# print() fonksiyonundaki end="\t" parametresi, aynı satırda elemanları tab ile ayırarak yazdırmak için kullanılır.