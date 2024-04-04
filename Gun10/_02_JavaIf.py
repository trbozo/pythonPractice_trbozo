# package Gun10;
#
# import java.util.Scanner;
#
# public class _02_JavaIf {
#     public static void main(String[] args) {
#         // Girilen bir öğrencinin notuna göre 50 ve 50 den büyükse
#         // ise geçtiniz, küçük ise kaldınız yazdırınız.
#
#         Scanner oku=new Scanner(System.in);
#         System.out.print("Öğrenci notu=");
#         int ogrNot= oku.nextInt();
#
#         if (ogrNot >= 50)
#             System.out.println("Geçtiniz, tebrikler");
#
#         if (ogrNot < 50)
#             System.out.println("Üzgünüz, kaldınız");
#     }
# }

ogr_not = int(input("Öğrenci notu="))

if ogr_not >= 50:
    print("Geçtiniz, tebrikler")
else:
    print("Üzgünüz, kaldınız")


#kullanıcıdan bir öğrencinin notunu alır ve bu not 50 veya üzeri ise "Geçtiniz, tebrikler", 50'den küçük ise "Üzgünüz, kaldınız" mesajını yazdırır. Python'da, kullanıcıdan veri almak için input() fonksiyonu kullanılır ve int() fonksiyonu ile bu veri tam sayıya dönüştürülür. Daha sonra if-else yapısı ile notun değerlendirilmesi gerçekleştirilir.