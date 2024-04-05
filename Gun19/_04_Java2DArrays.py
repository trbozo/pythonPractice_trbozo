# package Gun19;
#
# import java.util.Arrays;
#
# public class _04_Java2DArrays {
#     public static void main(String[] args) {
#
#         int[][]  tablo=new int[2][3];
#
#         int[][] tablo2= // farklı satır boyutları ancak bu tanımlama şekli ile oluşturulabilir.
#                 {
#                         {2,8},
#                         {22,33,44,5,6,7,8},
#                         {3,4,5,6,6,7}
#                 };
#
#         //tablo2[0]=new int[9];  // yada herhangi bir satırı yeniden istediğiniz boyutla verebilirsiniz.
#
#         for (int i = 0; i < tablo2.length; i++) {
#
#             for (int j = 0; j < tablo2[i].length; j++)
#                 System.out.print(tablo2[i][j]+"\t");
#
#             System.out.println();
#         }
#
#         System.out.println("0.satır = " + Arrays.toString(tablo2[0]));
#         System.out.println("1.satır = " + Arrays.toString(tablo2[1]));
#         System.out.println("2.satır = " + Arrays.toString(tablo2[2]));
#
#
#     }
# }


# 2x3'lük sabit boyutlu bir tablo tanımlama
tablo = [[0 for _ in range(3)] for _ in range(2)]

# Farklı satır boyutlarına sahip bir 2D liste (dizi) tanımlama
tablo2 = [
    [2, 8],
    [22, 33, 44, 5, 6, 7, 8],
    [3, 4, 5, 6, 6, 7]
]

# Herhangi bir satırı yeniden farklı bir boyutla tanımlama
# Python'da doğrudan yeni bir liste ataması yapılabilir, ancak özgün Java kodunda bu satır yorum içine alınmıştı.
# tablo2[0] = [0] * 9

# tablo2'deki tüm elemanları yazdırma
for i in range(len(tablo2)):
    for j in range(len(tablo2[i])):
        print(tablo2[i][j], end="\t")
    print()  # Her satırdan sonra bir alt satıra geç

# Her satırı ayrı ayrı yazdırma
print("0.satır =", tablo2[0])
print("1.satır =", tablo2[1])
print("2.satır =", tablo2[2])


#Java'daki 2 boyutlu dizilerin (2D arrays) işlevselliğini yansıtır.
# Python'da, listeler üzerinde iterasyon yapmak ve iç içe listeler (iki boyutlu diziler) oluşturmak için
# for döngüleri kullanılır. Farklı boyutlarda satırlar içeren bir 2D liste tanımlayabilir ve bu listenin elemanlarını
# ekrana yazdırabiliriz. Ayrıca, Python'da listelerin boyutları dinamik olduğundan, herhangi bir satırın boyutunu doğrudan
# değiştirebiliriz.
# Ancak, yukarıdaki kodda bu işlem yorum olarak bırakılmıştır çünkü Java kodundaki ilgili satır da yorum içine alınmıştı.