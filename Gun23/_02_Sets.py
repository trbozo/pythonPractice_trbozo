# package Gun23;
#
# import java.util.HashSet;
#
# public class _02_Sets {
#     public static void main(String[] args) {
#
#         HashSet<Integer> hs1=new HashSet<>();
#
#         hs1.add(1);
#         hs1.add(2);
#         hs1.add(38);
#         hs1.add(22);
#         hs1.add(4);
#
#         System.out.println("hs1 = " + hs1);
#
#         //bakalım eklenecek mi
#         hs1.add(4); // eklemek istesenizde SET ler tekrar eklemez
#         hs1.add(2); // eklemek istesenizde SET ler tekrar eklemez
#
#         System.out.println("hs1 = " + hs1);
#
#     }
# }


# ##Bu Java kodu, HashSet kullanarak bir Set oluşturur ve içine eleman ekler. HashSet, tekrar eden elemanları kabul etmez; yani aynı elemanı Sete ikinci bir kez eklemeye çalışmak hiçbir etki yapmaz ve Setin içeriği değişmez.
#
# Python'da set kullanımı Java'daki HashSete çok benzerdir. Python'daki set de tekrar eden elemanları kabul etmez ve elemanlar sırasız bir şekilde saklanır. Aşağıda, Java'daki bu kodun Python'da bir karşılığı verilmiştir:
#

# Set oluşturma ve eleman ekleme
hs1 = {1, 2, 38, 22, 4}
print("hs1 =", hs1)

# Bakalım eklenecek mi
hs1.add(4)  # Set zaten '4' içerdiği için bu eleman tekrar eklenmez
hs1.add(2)  # Set zaten '2' içerdiği için bu eleman tekrar eklenmez

print("hs1 =", hs1)


