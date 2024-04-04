# package Gun16;
#
# public class _01_JavaNestedLoop {
#     public static void main(String[] args) {
#         // Aşağıdaki görünümü tek yıldız kullanarak yazdırınız.
#         //  *****
#         //  *****
#         //  *****
#         //  *****
#         //  *****
#
#         for (int j = 1; j <= 5; j++) {
#
#             //yukarıdaki döngü bu döngüyü 5 kez çalıştır
#             for (int i = 1; i <= 5; i++)
#                 System.out.print("*"); //25 kez çalışır
#
#             System.out.println();
#
#         }
#
#
#     }
# }



# Aşağıdaki görünümü tek yıldız kullanarak yazdırınız.
#  *****
#  *****
#  *****
#  *****
#  *****

for j in range(5):  # Dıştaki döngü, her satır için
    for i in range(5):  # İçteki döngü, her satırda yıldızları yazdırmak için
        print("*", end="")  # Yıldızı yazdır
    print()  # Bir sonraki satıra geç
