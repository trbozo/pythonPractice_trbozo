# package Gun23;
#
# import java.util.HashSet;
#
# public class _05_Sets {
#     public static void main(String[] args) {
#         HashSet<Integer> hs= new HashSet<>();
#         hs.add(1);
#         hs.add(5);  // silinen eleman
#         hs.add(7);
#         hs.add(34);
#         hs.add(3);
#         hs.add(4);
#
#         System.out.println("hs.size() = " + hs.size());
#
#         hs.remove(5); // elemanın değerine göre siler, index yok
#         System.out.println("hs = " + hs);
#         System.out.println("hs.size() = " + hs.size());
#
#         if (hs.contains(7))
#             System.out.println("var");
#         else
#             System.out.println("yok");
#
#         hs.clear();
#         System.out.println("hs = " + hs);
#
#     }
# }


# HashSet oluşturma ve eleman ekleme
hs = {1, 5, 7, 34, 3, 4}
print("hs.size() =", len(hs))

# Elemanın değerine göre silme, index kullanımı yok
hs.remove(5)  # 5 değerine sahip elemanı siler
print("hs =", hs)
print("hs.size() =", len(hs))

# Set içinde eleman arama
if 7 in hs:
    print("var")
else:
    print("yok")

# Set'i temizleme
hs.clear()
print("hs =", hs)
